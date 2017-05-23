class pessoa(object):
  def __init__(self,nome,peso,idade,altura):
    self.nome = nome
    self.peso = peso
    self.idade = idade
    self.altura = altura
  def envelhecer(self):
    self.idade += 1 
  def engordar(self):
    self.peso += 1 
  def emagrecer(self):
    self.peso -= 1 
  def crescer(self):
    self.altura += 0.05