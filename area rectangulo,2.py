class Rectangulo:
    def __init__(self, base, altura):
        self.__base=base
        self.__altura=altura
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def set_base(self, nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else:
            print("Base no válida")
    def set_altura(self, nueva_altura):
        if nueva_altura > 0:
            self.__altura = nueva_altura
        else:
            print("Altura no válida")
    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)
rectangulo = Rectangulo(5, 3)

area_redondeada = round(rectangulo.calcular_area(), 2)
perimetro_redondeado = round(rectangulo.calcular_perimetro(), 2)

print("Área del rectángulo:", area_redondeada)
print("Perímetro del rectángulo:", perimetro_redondeado)
