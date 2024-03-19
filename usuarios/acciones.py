import usuarios.usuarios as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        nombre = input("Cual es tu nombre: ")
        apellidos = input("Cual son tus apellidos: ")
        email = input("Cual es tu correo: ")
        password= input("Cual es tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password )
        registro = usuario.registrar()

        if registro[0] >= 1 :
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print(f"\nError al registrar {registro[1].nombre}")

    def login(self):
        print("\nOk!! Vamos a loguearte en el sistema...")
        try:
            email = input("Cual es tu correo: ")
            password= input("Cual es tu contraseña: ")

            usuario = modelo.Usuario("" ,"" , email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]} ")
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!! intentalo más tarde")

    def proximasAcciones(self, usuario):
        print('''\nAcciones disponibles:
              - Crear nota (crear)
              - Mostrar notas (mostrar)
              - Borrar notas (borrar)
              - Salir (salir)''')
        
        accion = input('Que quieres hacer?:   ')
        hazEl = notas.acciones.Acciones()

        if accion == 'crear':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion =="mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion =="borrar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion =="salir":
            print(f"{usuario[1]}, hasta pronto!!")
            exit()
