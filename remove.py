#declarando librerías
import os
os.system("adb devices > .device.txt")
f = open(".device.txt", "r")
linea = f.readlines()[1]
if len(linea) > 26:
    print("\n **Por favor asegúrece de usar USB como Transferir Archivos**\n Saliendo...")
    
elif len(linea) > 7 and len(linea) < 26:
    print("\nDispositivo conectado con éxito :)")
    print("\n Dispositivo:\t" + linea )
else:
    print("\n**Asegúrece de conectar el teléfono a la PC y tener la depuración activa**\nSaliendo...")

f.close()
