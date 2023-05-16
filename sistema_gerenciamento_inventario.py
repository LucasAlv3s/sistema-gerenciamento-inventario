class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class SistemaGerenciamentoInventario:
    def __init__(self):
        self.inventario = []

    def adicionar_produto(self, nome, quantidade):
        produto = Produto(nome, quantidade)
        self.inventario.append(produto)
        print("Produto adicionado com sucesso!")

    def exibir_inventario(self):
        if not self.inventario:
            print("O inventário está vazio.")
        else:
            print("Inventário:")
            for produto in self.inventario:
                print(f"Nome: {produto.nome}, Quantidade: {produto.quantidade}")

# Exemplo de uso
sistema = SistemaGerenciamentoInventario()

# Adicionar produtos
sistema.adicionar_produto("Camiseta", 10)
sistema.adicionar_produto("Calça", 5)
sistema.adicionar_produto("Meias", 15)

# Exibir inventário
sistema.exibir_inventario()
