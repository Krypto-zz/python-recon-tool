from IPnetwork.network import target_ip
from scanerPort.scanner import run_scanner, run_scanner_network
from utils.export_data import report_export
from ipaddress import ip_network
while True:
    print("============ MENU ==============")
    print("1. Escanear puertos por IP")
    print("2. Detectar IPs activas")
    print("3. Salir")
    print("================================")
    option_user = int(input("Ingresa una opcion: "))
    match option_user:
        case 3:
            print("Hasta luego...")
            break
        case 1:
            print("********************")
            print("1. Escanear una IP")
            print("2. Escanear una RED")
            print("3. Salir")
            print("********************")
            option = int(input("Ingresa una opcion: "))
            match option:
                case 3:
                    print("Volviendo...")
                case 1:
                    report = run_scanner()
                    option_report = input("¿Deseas exportar a JSON? (S/N)")
                    if option_report.upper().strip() == "S":
                        report_export(report)
                case 2:
                    try:
                        Ip = input("Ingresa la direccion de red:")
                        IpNet = ip_network(Ip, strict=False)
                        reports = run_scanner_network(IpNet)
                        option_report = input("¿Deseas exportar a JSON? (S/N)")
                        if option_report.upper().strip() == "S":
                            report_export(reports)
                    except:
                        print("Direccion de red no valida")
        case 2:
            report = target_ip()
            if report is not None: 
                option_report = input("¿Deseas exportar a JSON? (S/N)")
                if option_report.upper().strip() == "S":
                    report_export(report)