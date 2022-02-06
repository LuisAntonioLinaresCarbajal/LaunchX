
#Ejercicio - Escribir declaraciones if, else, y elif
print("Saludos tripulante este programa te ayudara a calcular si un asteoride se acerca a velocidades peligrosas")
asteroide = int(input("por favor ingresa la velocidad del asteroide: "))
if asteroide > 25:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print('¡Sigue con tu día!, la velocidad no es peligrosa.')