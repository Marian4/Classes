class retangulo(object):
  def __init__(self):
    self.base = 1
    self.altura = 2
  def MudarValorLados(self,novaBase,novaAltura):
    self.base = novaBase
    self.altura = novaAltura
  def RetornarValorLados(self):
    return self.base,self.altura
  def calcularArea(self):
    return self.base*self.altura
  def calcularPerimetro(self):
    return (self.base*2)+(self.altura*2)
base = eval(input("Informe a medida da base/largura do local:"))
altura = eval(input("Informe a medida da altura/comprimento do local:"))
basePiso = eval(input("Informe a medida da base/largura do piso:"))
alturaPiso = eval(input("Informe a medida da altura/comprimento do piso:"))
areaPiso = basePiso*alturaPiso
local = retangulo()
local.MudarValorLados(base,altura)
areaLocal = local.calcularArea()
QuantPisos = areaLocal/areaPiso
print("\nSão necessários %i pisos para o local."%QuantPisos)