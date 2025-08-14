#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import socket
import netifaces
import nmap
from tabulate import tabulate

# Função para pegar IP local automaticamente
def get_local_ip():
    try:
        for iface in netifaces.interfaces():
            if netifaces.AF_INET in netifaces.ifaddresses(iface):
                ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
                if ip.startswith("192.") or ip.startswith("10.") or ip.startswith("172."):
                    return ip
    except:
        return "127.0.0.1"

# Função para descobrir dispositivos ativos via ping
def ping(ip):
    try:
        subprocess.check_output(["ping", "-c", "1", "-W", "1", ip], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# Identificação básica do dispositivo
def device_type(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0].lower()
        if "android" in hostname or "mobile" in hostname:
            return "Smartphone/Tablet"
        elif "camera" in hostname or "ipcam" in hostname:
            return "Câmera"
        elif "pc" in hostname or "laptop" in hostname:
            return "PC"
        else:
            return "Desconhecido"
    except:
        return "Desconhecido"

# Função para verificar portas abertas com nmap
def check_ports(ip):
    try:
        nm = nmap.PortScanner()
        scan = nm.scan(ip, arguments='-F')  # fast scan
        open_ports = []
        if 'tcp' in scan['scan'][ip]:
            for port in scan['scan'][ip]['tcp']:
                if scan['scan'][ip]['tcp'][port]['state'] == 'open':
                    open_ports.append(str(port))
        return ','.join(open_ports) if open_ports else "Nenhuma aberta"
    except:
        return "Erro Nmap"

# Função principal para escanear a rede
def scan_network():
    local_ip = get_local_ip()
    print(f"[INFO] Seu IP local detectado: {local_ip}")
    ip_base = '.'.join(local_ip.split('.')[:-1]) + '.'

    devices_list = []
    print("[INFO] Escaneando a rede (isso pode demorar alguns minutos)...")
    for i in range(1, 255):
        ip = ip_base + str(i)
        if ping(ip):
            devices_list.append({
                "IP": ip,
                "Hostname": socket.gethostbyaddr(ip)[0] if is_resolvable(ip) else "Desconhecido",
                "Tipo": device_type(ip),
                "Portas Abertas": check_ports(ip)
            })

    return devices_list

# Verifica se o hostname pode ser resolvido
def is_resolvable(ip):
    try:
        socket.gethostbyaddr(ip)
        return True
    except:
        return False

# Exibe resultado
def display(devices_list):
    print(tabulate(devices_list, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    devices = scan_network()
    display(devices)
