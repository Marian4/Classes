class contaCorrente(object):

  def __init__(self,numeroConta,nomeCorrentista,saldo=0):

    self.numeroConta = numeroConta

    self.nomeCorrentista = nomeCorrentista

    self.saldo = saldo

  def alterarNome(self,novoNome):

    self.nomeCorrentista = novoNome

  def depósito(self,valor):

    self.saldo += valor

    print("Depósito Concluído.\nSaldo atual:%.2f"%self.saldo)

  def saque(self,valor):

    if self.saldo >= valor:

      self.saldo -= valor

      print("Saque realizado.\nSaldo atual:%.2f"%self.saldo)

    else:

      print("O saque não poderá ser feito pois o saldo é insuficiente.\nSaldo atual:%.2f"%self.saldo)