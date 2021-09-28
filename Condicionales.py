#Elif---------------------------------------------------------

x=3
if x<2:
    print('Small')
elif x<10:
    print('Medium')
else:
    print('large')
print('All donde')

#Try & except ---------------------------------------------------

saludo= 'Hola Bob'
try:
    isaludo= int(saludo)            #try/except se utiliza para encapsular codigo con potencial fallo
except:
    isaludo= -1
print('Primero', isaludo)


saludo='123'
try:
    isaludo= int(saludo)
except:
    isaludo= -1
print('Segundo', isaludo)

#Ejemplo--------------------------------------------------

ingreso=input('Ingresa un numero: ')
try:
    valor= int(ingreso)
except:
    valor= -1

if valor>0:
    print('Buen trabajo')
else:
    print('No es un numero')

