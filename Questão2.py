class quadrado(object):

  def __init__(self):

    self.lado = 1

  def MudarTamanhoLado(self,novoValor):

    self.lado = novoValor

  def RetornarValorLado(self):

    return self.lado

  def CalcularArea(self):

    return self.lado*self.lado