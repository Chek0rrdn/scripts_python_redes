# Herramientas de Escaneo en Python

Este repositorio contiene dos herramientas escritas en Python para realizar escaneo de puertos y descubrimiento de hosts activos en una red mediante ICMP.

## Escáner de Puertos

### Uso

```bash
python3 escaner_de_puertos.py -t <host_objetivo> -p <rango_de_puertos>
```

- `<host_objetivo>`: Especifica la dirección IP del host a escanear.
- `<rango_de_puertos>`: Especifica el rango de puertos a escanear, por ejemplo, "1-2000".

### Funcionalidades
- Escaneo de puertos en paralelo utilizando ThreadPoolExecutor.
- Manejo de interrupciones (Ctrl+C) para una salida limpia.
- Soporte para escanear rangos de puertos y puertos individuales.


## Descubrimiento de Hosts Activos

### Uso

```bash
python3 descubrimiento_de_hosts.py -t <host_o_rango>
```

- `<host_o_rango>`: Especifica la dirección IP o rango de IP a escanear, por ejemplo, "192.168.1.1" o "192.168.1.1-200".

### Funcionalidades

- Descubrimiento de hosts activos en una red utilizando ICMP.
- Manejo de interrupciones (Ctrl+C) para una salida limpia.
- Soporte para rangos de IP y direcciones IP individuales.


## Funcionalidades

- Descubrimiento de hosts activos en una red utilizando ICMP.
- Manejo de interrupciones (Ctrl+C) para una salida limpia.
- Soporte para rangos de IP y direcciones IP individuales.

```bash
pip install -r requirements.txt
```