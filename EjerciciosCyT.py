#Hacer un programa que calcule tu salario y te pague 1.5 veces más por cada hora extra
#Asi:
#   Horas trabajadas: 45
#   Pago normal:      10
#   Pago total:       475.0

Ht= input('Ingrese la cantidad de horas trabajadas: ')
Pn=input ('Ingrese su pago habitual: ')

try:
    fHorast=float(Ht)
    fPagon=float(Pn)
except:
    print('Error, ingresa un numero')
    quit()

if fHorast>40:
    Pago= fHorast*fPagon + (fHorast-40.0)*(fPagon*0.5)
else:
    Pago=fHorast*fPagon

print('El pago es: ', Pago)