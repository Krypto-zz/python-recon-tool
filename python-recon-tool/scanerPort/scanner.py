import socket
from concurrent.futures import ThreadPoolExecutor
from ipaddress import ip_address, ip_network
from icmplib import multiping

def run_scanner_network(IpNet):
    report_scanner_net = []
    list_ips = [str(ip) for ip in IpNet]
    host_live = multiping(list_ips, count=1, timeout=1, interval=2)
    list_ips_live = []
    for ip in host_live:
        if ip.is_alive:
            list_ips_live.append(ip.address)


    for ip in list_ips_live:
        ip_target = ip_address(ip)
        ports = range(1,1025)
        print(f"--- Iniciando escaneo a {ip_target} ---")
        
        with ThreadPoolExecutor(max_workers= 100) as executor:
            responses = executor.map(lambda p: check_port(ip_target, p), ports)
        found_ports = 0
        ports_ip = []
        for port, status in responses:
            if status == 0:
                print(f"[+] Puerto Abierto: {port}")
                ports_ip.append(port)
                found_ports += 1
        print(f"\n----- Puertos encontrados {found_ports} -----")
        report_scanner_net.append({
            "target":ip,
            "open ports": ports_ip
            })
    
    return report_scanner_net

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    
    status = sock.connect_ex((str(ip), port))
    sock.close()
    return port, status

def run_scanner():
    ip_input = input("- Ingresa una IP: ")
    try:
        ip_target = ip_address(ip_input)
        ports = range(1,1025)
        
        print(f"--- Iniciando escaneo a {ip_target} ---")
        
        with ThreadPoolExecutor(max_workers= 100) as executor:
            responses = executor.map(lambda p: check_port(ip_target, p), ports)
            
        ports_ip = []
        found_ports = 0

        for port, status in responses:
            if status == 0:
                print(f"[+] Puerto Abierto: {port}")
                ports_ip.append(port)
                found_ports += 1
        
        report_ip = {
            "Target":ip_input,
            "Open Ports":ports_ip
            }
        
        print(f"\n----- Puertos encontrados {found_ports} -----")
        return report_ip
    
    except Exception as e:
        print(f"ERROR: {e}")

