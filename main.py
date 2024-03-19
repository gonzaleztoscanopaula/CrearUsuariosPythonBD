#Proyecto python mysql:
#abrir asistente
#login o registro
#si elegimos registro creara un usuario en la db
#si elegimos lelogin identifica el usuario y nos preguntara
#crear notas, mostrar notas, borrarlas

from usuarios import acciones

print('''
Acciones disponibles:
      -registro
      -login
''')

hazEl = acciones.Acciones()

accion = input('Que quieres hacer?')

if accion =='registro':
    hazEl.registro()

elif accion == 'login':
    hazEl.login()

