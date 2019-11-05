#!/usr/bin/env python
import os


os.system("sudo clear")

#crear un usuario

print("Ingrese el nombre del usurio que guste")
user=input()
os.system("sudo adduser "+user) 

#crear un grupo
os.system("sudo clear")
print("ingrese un nombre de grupo")
group=input()
os.system("sudo addgroup "+group)

userm=group+" "+user
os.system("sudo usermod -G "+userm)
print("El usuario se agrego al grupo satisfactoriamente")

owner=user+":"+group
var="/var/www/"
os.system("sudo clear")
print("Ahora ingrese el nombre del directorio que quiere cambiar de dueño")
directory=input()
os.system("sudo chown "+owner+" "+var+directory)

