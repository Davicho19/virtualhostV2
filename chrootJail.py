#!/usr/bin/env python
import os

os.system("clear")

print("ingrese el nombre de su grupo")
chroot=input()

print("ingrese el nombre del directorio")
ruta=input()



jail=open("/etc/ssh/sshd_config", "a+") 
jail.write("Match Group "+chroot+"\nChrootDirectory /var/www/"+ruta+"\n ForceCommand internal-sftp\nX11Forwarding no\nAllowTcpForwarding no")
jail.close()


print("reiniciando ssh")
os.system("sudo systemctl restart sshd")
