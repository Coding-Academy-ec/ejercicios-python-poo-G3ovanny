class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return f"Conduciendo el {self.marca} {self.modelo}"

