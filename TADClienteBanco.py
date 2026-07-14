class ClienteBanco:
    def __init__(self, nome, conta, preferencial=False):
        self.nome = nome
        self.conta = conta
        self.preferencial = preferencial


class FilaClientes:
    def __init__(self):
        self.comuns = []
        self.preferenciais = []

    def adicionar_cliente(self, cliente):
        if cliente.preferencial == True:
            self.preferenciais.append(cliente)
        else:
            self.comuns.append(cliente)

    def atender_clientes(self):
        contador = 0

        while len(self.comuns) > 0 or len(self.preferenciais) > 0:

            if (contador < 2 and len(self.comuns) > 0) or len(self.preferenciais) == 0:
                cliente = self.comuns.pop(0)

                print(f"Chamando Cliente Comum: {cliente.nome}")
                contador += 1

            elif len(self.preferenciais) > 0:
                cliente = self.preferenciais.pop(0)

                print(f"Chamando Cliente Preferencial: {cliente.nome}")
                contador = 0



fila = FilaClientes()


fila.adicionar_cliente(ClienteBanco("José Henrique", 1001))
fila.adicionar_cliente(ClienteBanco("Ellen Mayara", 1002))
fila.adicionar_cliente(ClienteBanco("Paulo Guilherme", 1003))
fila.adicionar_cliente(ClienteBanco("Ingridy Luzia", 1004))
fila.adicionar_cliente(ClienteBanco("Nicole Lucena", 1005))
fila.adicionar_cliente(ClienteBanco("Carlos Eduardo", 1006))

fila.adicionar_cliente(ClienteBanco("Italo Berg", 2001, True))
fila.adicionar_cliente(ClienteBanco("Luciano Alexandre", 2002, True))
fila.adicionar_cliente(ClienteBanco("Ricardo Kleber", 2003, True))


fila.atender_clientes()