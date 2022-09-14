class ColaDePaciente:
    def __init__(self, nom, ape):
        self.nombres = nom
        self.apellidos = ape

    def __str__(self) -> str:
        return f"""Cliente
        Nombre: {self.nombres}
        Apellidos: {self.apellidos}"""

    def __init__(self):
        self.elementos = []

    def nuevoPaciente(self, elemento):
        self.elementos.append(elemento)
    
    def pacienteActual(self, elemento):
        try:
            return self.elementos.pop(0)
        except Exception as ex:
            print(str(ex))
    
    def estaVacia(self):
        return self.elementos == []

        
        
        

        

