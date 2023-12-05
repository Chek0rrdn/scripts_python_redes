#/usr/bin/env python3

import argparse
import socket
import signal
import sys

from concurrent.futures import ThreadPoolExecutor
from termcolor import colored



open_socket = []

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa", 'red'))
    
    for socket in open_socket:
        socket.close()
    
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler) # Ctrl+C


def get_arguments():
    parser = argparse.ArgumentParser(description='Escáner de Puertos')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Host a escanear (Ex. 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Rango de puertos a escanear (EX. -p 1-2000)")
    options = parser.parse_args()

    return options.target, options.port


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    open_socket.append(s)

    return s


def port_scanner(port: int, host):
    s = create_socket()

    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()


def scan_ports(ports, target):
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)


def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    
    elif ',':
        return map(int, ports_str.split(','))
    
    else:
        return (int(ports_str),)


def main():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)



if __name__ == '__main__':
    main()