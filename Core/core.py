from internals import system
from Core.models.produtos import estoque
import os

Estoque = estoque()

estoque_final = Estoque.estoque

lucro_local = 0
gasto_local = 0

def main():

    global estoque_final
    global lucro_local
    global gasto_local

    print("--------SELECIONE AS ALTERNATIVAS ABAIXO---------")

    print("1: Ver estoque. \n2: Vender produto \n3: Comprar produto \n4: Sair e calcular lucro")

    print("\n-------------------------------------------------")

    escolha = input("Escolha uma alternativa: ")

    print("----------------------------------------------------")

    match escolha:
        case "1": 
            system.limpar_terminal()
            system.mostrar_estoque(Estoque.estoque)
        case "2": 
            system.limpar_terminal()
            produto = input("Digite o produto que deseja vender: ")
            quantidade = int(input("Digite a quantidade que deseja vender: "))
            estoque_final = Estoque.estoque
            system.vender_produto(Estoque.estoque, produto, quantidade)
            print(f"Novo estoque é: {system.especification(Estoque.estoque, produto)}")
            lucro_local += quantidade * Estoque.estoque[produto]["preço"]
        case "3":
            system.limpar_terminal()
            produto = input("Digite o produto que deseja comprar: ")
            quantidade = int(input("Digite a quantidade que deseja comprar: "))
            system.adicionar_produto(Estoque.estoque, produto, quantidade)
            estoque_final = Estoque.estoque
            print(f"Novo estoque de {produto} é: {system.especification(Estoque.estoque, produto)}")
            gasto_local -= quantidade * Estoque.estoque[produto]["preço"]
        case "4":
            if gasto_local + lucro_local > 0:
                system.limpar_terminal()
                print(f"Lucro bruto obtido foi de {gasto_local + lucro_local} reais")
                return True and gasto_local + lucro_local
            elif gasto_local + lucro_local < 0:
                system.limpar_terminal()
                print(f"Prejuizo de hoje foi de: {gasto_local + lucro_local} reais")
                return True and gasto_local + lucro_local
            elif gasto_local + lucro_local == 0:
                system.limpar_terminal()
                print("Não há gastos ou prejuízos nas vendas e compras de hoje")
                return True