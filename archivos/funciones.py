#!/umesr/bin/python
# coding: utf-8

def imprimir_mensaje():
        """Esta función sólo imprime un mensaje en pantalla.
        """
        print("Hola! Simplemente vine a imprimir esto")
        print("Chau")

def saludo(nombre, apellido):
        """Recibe el nombre y apellido de una persona e imprime un saludo
        personalizado.
        """
        print("Bienvenido {} {}".format(nombre, apellido))

def saludo2(nombre, apellido, mensaje="Bienvenido"):
        """Recibe el nombre y apellido de una persona e imprime un saludo 
        personalizado.
        Puede recibir un tercer argumento de texto que es lo que ante-
        cede al nombre y al apellido de la persona.
        """
        print(mensaje+" "+nombre+" "+apellido)

def saludo3(nombre, *args, **kwargs):
        """Imprime en pantalla el segundo argumento de texto recibido y
        el nombre a continuación.
        En la línea siguiente imprime el tercer argumento recibido.
        Y para terminar imprime el mensaje pasado como despedida.
        """
        print(args[0]+" "+nombre)
        print(args[1])
        print(kwargs['despedida'])

def incrementar(valor):
        """Incrementa el valor recibido y lo imprime en pantalla.
        Es importante destacar que no devuelve este valor.
        Modifica el argumento por valor.
        """
        valor = valor + 1
        print(valor)

def agregar(valor, lista):
        """Agrega el valor a la lista pasada.
        Es importante destacar que no devuelve ningún valor.
        Modifica el argumento por referencia.
        """
        lista.append(valor)

## Para consultar el docstring escribimos el nombre de la función se-
## guido de un . y __doc__ dentro de un print. Por ejemplo:
print(imprimir_mensaje.__doc__)

print("Usando la función imprimir_mensaje():")
imprimir_mensaje()
print("-"*50)

print("Usando la función saludo():")
name = "Leo"
lastname = "Colombo Viña"
saludo(name, lastname)
print("-"*50)

print("Usando la función saludo2() con el argumento por defecto:")
saludo2(name, lastname)
print("Usando la función saludo2() sin el argumento por defecto:")
saludo2(name, lastname, mensaje="Hola!")
print("-"*50)

print("Usando la función saludo3():")
saludo3(name, "Bienvenido", "Es un buen día para aprender Python!", 
        despedida="Python no resulta tan difícil, no?")
print("-"*50)

print("Usando la función incrementar():")
x = 1
print("x vale {}".format(x))
print("Ejecutamos incrementar...")
incrementar(x)
print("x vale {}".format(x))
print("-"*50)


print("Usando la función agregar():")
lista = [1, 2, 3, 4, 5]
valor = 6
print("La lista es: {}".format(lista))
print("El valor a agregar es: {}".format(valor))
agregar(valor, lista)
print("Ahora la lista es: {}".format(lista))
print("-"*50)

