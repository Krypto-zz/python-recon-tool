# Network & Port Scanner (Multi-threaded)
Esta es una herramienta modular que ayuda al reconocimiento de red desarrollada en Python.
este software permite descubrir hosts activos en una red mediante ICMP (ping) y realizar escaneos de puertos TCP (1-1024) utilizando multiples hilos para mayor rendimiento.
Ademas permite exportar los resultados en un formato **JSON**  con marcas de tiempo unicas para evitar que se sobreescriba

## Arquitectura del proyecto
Este proyecto sigue un diseño limpio y desacoplado, separando la logica de red, el motor de escaneo y las utilidades de persistencia:
```text
NETWORK-SCANNER/
├── IPnetwork/           Módulo de descubrimiento de hosts actua con => (ICMP)
│   ├── __init__.py
│   └── network.py
├── scanerPort/          Motor de escaneo de puertos TCP con Multi-Threading
│   ├── __init__.py
│   └── scanner.py
├── utils/               Funciones de soporte (Traducción y exportación)
│   ├── __init__.py
│   └── export_data.py
├── reports/             Carpeta de destino para los reportes JSON
├── main.py              Orquestador del menú interactivo (CLI)
└── README.md
```
# Caracteristicas Principales
## Descubrimiento de red flexible: Soporta el analisis de subredes completas, asi como la deteccion de un host
## Escaneo de Puertos de Alto Rendimiento: Este programa utiliza 100 hilos concurrrentes reduciendo el tiempo de escaneo a segundos
## Reportes automatizados: Exportacion limpia de datos de red (IPs vivas en una red, RRT, lista de puertos abiertos) usando archivos JSON con formato fecha y hora

# Tecnologías Utilizadas
## - Python 3.X

## - Socket (Conexiones TCP de bajo nivel)

## - Concurrent.Futures (Gestión de múltiples hilos en paralelo)

## - Icmplib (Inyección de paquetes ICMP)

## - Ipaddress (Validación técnica de direccionamiento IPv4)

## - JSON & Datetime (Persistencia y formateo de reportes)

## Instalacion y Requerimientos:
Este programa utiliza una libreria externa **icmplib** para el manejo avanzado de paquetes ICMP

# Clona el repositorio
```text
git clone https://github.com/Krypto-zz/python-recon-tool.git
```
# Instala las dependencias:
```text
pip install icmplib
```
## IMPORTANTE: el programa debe ejecutarse con privilegios de administrador debido a que el descubrimiento de red envia paquetes ICMP reales

# Disclairmer

Esta herramienta fue creada exclusivamente con fines educativos y para ser usada en auditoria etica, el uso de este software contra objetivos sin autorizacion previa es ilegal.
No me hago responsable del mal uso de esta herramienta

# Desarrollado por Miguel Sebastian Mendoza Choquehuanca
