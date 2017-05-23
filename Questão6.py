import time

class TV(object):

  def __init__(self):

    self.canais = [3,5,7,9,11,13,14,18]

    self.volumeMaximo = 100

    self.volumeMinimo = 0

class controle(object):

  def __init__(self,televisor):

    self.canal = 3

    self.volume = 10

    self.televisor = televisor

  def aumentarVolume(self):

    if self.volume+1 <= self.televisor.volumeMaximo:

      self.volume += 1

      print("                      volume:",self.volume)

    else:

      print("                      volume:",self.volume)

  def abaixarVolume(self):

    if self.volume-1 >= self.televisor.volumeMinimo:

      self.volume -= 1

      print("                      volume:",self.volume)

    else:

      print("                      volume:",self.volume)

  def proximoCanal(self):

    if self.canal == 69:

      self.canal = 1

      print("                    (%i)Sem sinal."%self.canal)

    elif self.canal+1 in self.televisor.canais:

      self.canal += 1

      print("             (Você está assistindo o canal %i)"%self.canal)

    else:

      self.canal += 1

      print("                    (%i)Sem sinal."%self.canal)

  def anteriorCanal(self):

    if self.canal == 1:

      self.canal = 69

      print("                    (%i)Sem sinal."%self.canal)

    elif self.canal-1 in self.televisor.canais:

      self.canal -= 1

      print("              (Você está assistindo o canal %i)"%self.canal)

    else:

      self.canal -= 1

      print("                    (%i)Sem sinal."%self.canal)

def tvi():

  print("-----------------------------------------------------------")

  print()

  print()

  print()

def tvf():

  print()

  print()

  print()

  print("-----------------------------------------------------------")

  print("                            ||                         ")

  print("                       ------------                   \n")

televisor = TV()

controle = controle(televisor)

botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

while botoes != 1:

  tvi()

  print("")

  tvf()

  botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

if botoes == 1:

  tvi()

  print("                   A TV FOI LIGADA :)")

  tvf()

  botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

  while botoes != 1:

    if botoes > 5 or botoes < 1:

      tvi()

      print("                   ?????????????????")

      tvf()

      botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

    elif botoes == 2:

      tvi()

      controle.aumentarVolume()

      tvf()

      botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

    elif botoes == 3:

      tvi()

      controle.abaixarVolume()

      tvf()

      botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

    elif botoes == 4:

      tvi()

      controle.proximoCanal()

      tvf()

      botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

    elif botoes == 5:

      tvi()

      controle.anteriorCanal()

      tvf()

      botoes = eval(input("(1)LIGAR/DESLIGAR (2)AUMENTAR VOLUME (3)ABAIXAR VOLUME (4)PRÓXIMO CANAL (5)CANAL ANTERIOR."))

tvi()

print("                      DESLIGANDO...")

tvf()

time.sleep(2)

tvi()

print("")

tvf()   
