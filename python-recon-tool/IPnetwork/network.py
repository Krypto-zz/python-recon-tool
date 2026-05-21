from icmplib import ping, multiping
from ipaddress import ip_address, ip_network

def discovery_network(ip):
    ips_network = [str(ip) for ip in ip.hosts()]
    host_live = multiping(ips_network, count = 1, timeout = 2, interval = 1)
    hosts_alive = []
    for h in host_live:
        if h.is_alive:
            hosts_alive.append({
                "Live IP": h.address,
                "RTT": h.avg_rtt
                })
            print(f"Host activo. {h.address}, con un promedio en envio de {h.avg_rtt} con {h.packets_sent} paquetes enviados")
    return hosts_alive

def discovery_host(ip):
    ip_str = str(ip)
    host_objetivo =ping(ip_str, count=2, timeout=2, interval=1)
    
    if host_objetivo.is_alive:
        print(f"[+] Host Live: {host_objetivo.address} | RTT: {host_objetivo.avg_rtt}ms | Sent: {host_objetivo.packets_sent}")
        
        host_live = {
            "Live IP":host_objetivo.address,
            "RTT":host_objetivo.avg_rtt
            }

        return host_live
    else:
        print("sin respuesta")

def target_ip():
    ip_obje = input("Ingresa una IP o una Direccion de Red: ")
    try:
        if "/" in ip_obje:
            ip_valida = ip_network(ip_obje, strict= False)
            report = discovery_network(ip_valida)
            return report
        else:
            ip_valida = ip_address(ip_obje)
            report = discovery_host(ip_valida)
            return report
    except Exception as e:
        print(f"Ingresa una IP valida o una RED valida, ERROR: {e}")


