class Libro:
    def __init__(self, tit, aut, ed):
        self.titulo = tit
        self.autor = aut
        self.edicion = ed

    def __str__(self) -> str:
        return f"""Libro
Titulo: {self.titulo}
Autor: {self.autor}
Edicion: {self.edicion}"""

class Pila:
    def __init__(self):
        self.datos = []

    def apilar(self, dato):
        self.datos.append(dato)

    def desapilar(self):
        try:
            return self.datos.pop()
        except IndexError:
            raise ValueError("No se han ingresado libros.")
    
    def esVacia(self):
        return self.datos==[]
        
    


                