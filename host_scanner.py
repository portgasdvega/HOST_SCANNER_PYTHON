import subprocess as sp
from datetime import datetime

time=datetime.now()

sp.run("clear", shell=True)
ip = str(input("Ingrese la IP: "))
escaneo=sp.run(f"nmap -sn {ip}", shell=True, capture_output=True)
salida=escaneo.stdout.decode()

resultados=[]

for linea in salida.splitlines():
    if "Nmap scan report for" in linea:
        ip_salida=linea.split()[-1]
        resultado=f"Hay un host con la IP: {ip_salida}"
        print(resultado)
        resultados.append(resultado)
    elif "Host is up" in linea:
        host=f"El host {ip_salida} esta en (up)"
        print(host)
        resultados.append(host)

pregunta = input("Deseas guardar esta informacion(y/n)?: ")

while True:
    if pregunta.lower()=="y":
        archivo = input("Como deseas nombrar el archivo(.txt): ")
        with open(archivo, "w") as f:
            f.write(f"El escaneo se realizo: {time} \n")
            for texto in resultados:
                f.write(texto + "\n")
        break
    elif pregunta.lower()=="n":
        print("Ok")
        break
    else:
        print("Error")
