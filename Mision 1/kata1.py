print ("Bienvenido tripulante, ¿problemas con la conversión entre parsecs y años luz?")
respuesta_tripiulante = str(input("ingresa tu respuesta: "))
if respuesta_tripiulante == str("si"):
    print ("descuida el programa conversor universal LaunchX te ayudara... \n")
    numero_de_parsecs = int(input("por favor ingrese los parsec: "))
    añosLuz= 3.26156 * numero_de_parsecs
    print(numero_de_parsecs , " parsec es el equivalente a:" , añosLuz, "años luz." )
    print("fin de la comversion, suerte en tu viaje.")
    exit()
else:
    print("ok tripulante, si necesitas ayuda no dudes en acudir a Universal LaunchX, bye.")
    exit()
