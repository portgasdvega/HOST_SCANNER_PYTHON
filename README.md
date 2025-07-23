
# Herramienta de Escaneo de Hosts - `host_scanner.py`

Este script permite detectar dispositivos activos en una red local usando `nmap` desde Python. Analiza la salida, identifica las IPs disponibles y permite guardar los resultados con sello de tiempo.

---

## Características

- Escaneo de red utilizando `nmap -sn`
- Procesamiento automático de IPs detectadas
- Asociación de cada host con su estado (`up`)
- Opción para guardar los resultados en un archivo `.txt`
- Registro de fecha y hora del escaneo

---

## Requisitos

- Python 3.7+
- `nmap` instalado y accesible desde la terminal
- Sistema operativo Linux (preferentemente)

---

## Uso

Ejecuta el script desde tu terminal:

```bash
python3 host_scanner.py
````

Y cuando te lo pida, ingresa el rango IP, por ejemplo:

```
Ingrese la IP: 192.168.20.0/24
```
---

## Ejemplo de salida guardada

```
El escaneo se hizo: 2025-07-21 20:53:10.308157 
Hay un host con la IP: 192.168.20.1
El host 192.168.20.1 esta en up
```

## Autor

Emiliano Martínez Vega

