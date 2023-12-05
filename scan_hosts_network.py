import argparse
import re
import signal
import subprocess
import sys

from concurrent.futures import ThreadPoolExecutor
from termcolor import colored


def def_handler(sig, frame):
    print(colored(f"\n Saliendo del programa...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para descubrir hosts activos en unan red con ICMP")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")

    args = parser.parse_args()

    return args.target


def parse_target(target_str: str):
    #192.168.1.1-254
    target_str_splitted = target_str.split('.') #["192", "168", "1", "1-100"]
    first_three_octets = '.'.join(target_str_splitted[:3]) #192.168.1

    if re.match(r'^\d+$', str(len(target_str_splitted))) and len(target_str_splitted)==4:
        if re.search('-', target_str_splitted[3]):
            start, end = target_str_splitted[3].split('-')
            return [f"{first_three_octets}.{i}" for i in range(int(start), int(end)+1) if i < 255]
        else:
            return [target_str]
    else:
        print(colored("\n El formato de la IP o el rango de IP es invalido \n", 'red'))


def host_discovery(target: list):
    
    try:
        ping = subprocess.run(['ping', '-c', '1', target], timeout=2, stdout=subprocess.DEVNULL)

        if ping.returncode == 0:
            print(colored(f"\t[i] La IP {target} está activa", 'green'))
        
    except subprocess.TimeoutExpired: pass



def main():
    target_str = get_arguments()
    targets = parse_target(target_str)

    print(f"\n Hosts activos en la red: \n")

    max_threads = 50
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discovery, targets)


if __name__ == __name__:
    main()