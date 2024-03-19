
import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print( f"{usuario[1]} !! vamos a crear una nueva nota..")

        titulo = input("introduce el titulo de tu nota:  ")
        descripcion = input("Mete el contenido de tu nota: ")


        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"No se ha guardado la nota, lo siento{usuario[1]}")





    def mostrar(self, usuario):
        print(f"{usuario[1]}!! vamos a mostrar tus notas..")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("****************************")
            print(nota[2])
            print(nota[3])
            print("****************************")


    def borrar(self, usuario):
        print(f"Okey {usuario[1]}!! Vamos a borrar notas")

        titulo =  input("Introduce el titulo de la nota a borrar:  ")

        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Perfecto has borrado la nota: {nota.titulo}")
        else:
            print(f"No se ha borrado la nota, lo siento...")