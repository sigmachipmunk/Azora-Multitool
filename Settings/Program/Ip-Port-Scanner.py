

from Config.Util import *
from Config.Config import *
try:
   import socket
   import concurrent.futures
except Exception as e:
   ErrorModule(e)
   
Title("Ip Port Scanner")

try:
    def port_scanner(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }

        def scan_port(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = identify_protocol(ip, port)
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Port: {white}{port}{red} Status: {white}Open{red} Protocol: {white}{protocol}{red}")
                sock.close()
            except:
                pass

        def identify_protocol(ip, port):
            try:
                if port in port_protocol_map:
                    return port_protocol_map[port]
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    sock.connect((ip, port))
                    
                    sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
                    response = sock.recv(100).decode('utf-8')
                    if "HTTP" in response:
                        return "HTTP"
                    
                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "FTP" in response:
                        return "FTP"
                    
                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "SSH" in response:
                        return "SSH"

                    return "Unknown"
            except:
                return "Unknown"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(scan_port, ip, port): port for port in range(1, 65535 + 1)}
        concurrent.futures.wait(results)
    
    Slow(scan_banner)
    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..")
    port_scanner(ip)
    Continue()
    Reset()
except Exception as e:
    Error(e)
