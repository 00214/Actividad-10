from particula import Particula

# Administrador de Particulas

class Particulas:
    def __init__(self):
        self.__particulas = [] # Lista
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    
    def __str__(self):
        return "".join(
            str(particula) + "\n" for particula in self.__particulas
        )
