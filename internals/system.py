import os

gasto = None
lucro = None
lucro_final = []
gasto_total = []

lucro_bruto = None    

def mostrar_estoque(estoq):
    for item, info in estoq.items():
        print(f"{item}: quantidade: {info["quantidade"]} preço: {info["preço"]}")
        print("----------------------------------------------------")

def vender_produto(estoq: dict[str, int], produto: str, quantidade: int):
    if produto in estoq:
        if estoq[produto]["quantidade"] >= quantidade:
            estoq[produto]["quantidade"] -= quantidade

def adicionar_produto(estoq, produto, quantidade):
    if produto in estoq:
        estoq[produto]["quantidade"] += quantidade

def especification(estoq, produto):
    if produto in estoq:
        return estoq[produto]["quantidade"]
    
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        