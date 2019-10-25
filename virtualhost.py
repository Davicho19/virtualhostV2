#!/usr/bin/env python
import os

os.system("clear")

print("Ingrese el nombre de su domino")
domain=input()


#print("Ingrese su direccion ip actual")
#addip=input()

#index="index.html"
directory="/var/www/"

print("su domino sera almacenado en el siguiente directorio /var/www")
os.system("sudo mkdir -p "+directory+"/"+domain)

print("Asignando permisos")
os.system("sudo chmod -R 755 "+directory+domain)

print("ajustando la landing page")



landing=open(directory+"/"+domain+"/index.html", "w")
landing.write("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Felicidades!</title><style>html{background-color: #508bc9;color: #fff;font-family: sans-serif, arial;}.container{width: 80%;margin: auto auto;}.inl{text-align: center;}.inl img{border-radius: 10px;}a{color: #f2d8ab;}</style></head><body><div class='container'><h1>Virtual Hosts creado exitosamente!</h1><br><br><h1>Let's celebrate!</h1><img src='http://i.imgur.com/vCbBhwy.gif' alt='Scene from Spider Man Movie (C) Spider Man Movie ..'></div></div></div></body></html>")
landing.close()



#virtual host
virtual=open("/etc/apache2/sites-available/"+domain+".conf", "w")
virtual.write("<VirtualHost *:80>\nServerAdmin localserver@localhost\nServerName "+domain+"\nServerAlias www."+domain+"\nDocumentRoot "+directory+domain+"\nErrorLog ${APACHE_LOG_DIR}/error.log\nCustomLog ${APACHE_LOG_DIR}/access.log combined\n</VirtualHost>")
virtual.close()

print("Agregando su pagina inicio")
os.system("sudo a2ensite "+domain+".conf")

print("Reiniciando apache2")
os.system("service apache2 reload")

os.system("clear")
print("tu domino ha sido creado satisfactoriamente")
#print(" Setting Up Local Host File ")
#if host_flag == 0:
#os.system("sudo sed -i -e 127.0.1.2   "+domain+"\' \"/etc/hosts\"")
#else:
#print " Skipped! "

#    print "\nSuccess! Please visit http://"+domain+"/ from any web browser\n\n"

#host_flag = 0

#host
os.system("nano /etc/hosts")
#add.write(addip +domain)
#add.close=() 

#print("configuracion hosts")
#os.system("sudo sed -i -e\n192.168.1.42" +domain+"\' \"/etc/hosts\"")
#print("\nSuccess! Please visit http://"+domain+"/ from any web browser\n\n")

