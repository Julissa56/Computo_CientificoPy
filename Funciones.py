#Funcion-------------------------------------------------------------
def print_lyrics():
    print('I´m bullet proof')
    print('Nothing to lose')

x=5
print('Hello')

print('Yo')
print_lyrics()
x=x+2
print(x)

#Funcion con return---------------------------------------------------
def greet(lang):
    if lang=='es':
        return 'Hola'
    if lang=='fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
print(greet('fr'), 'Sally')
print(greet('es'), 'Matt')
#--------------------------------
def addtwo(a,b):
    added=a+b
    return added

x=addtwo(3, 5)
print(x)