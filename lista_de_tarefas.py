# lista de tarefas

import os
import json


#Função que realiza a leitura da lista

def ler_tarefas(lista, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar_tarefas(lista, caminho_arquivo)

    return dados


#Função que salva as alterações na lista

def salvar_tarefas(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)


CAMINHO_ARQUIVO = 'LISTA_TAREFAS.json'
lista = ler_tarefas([], CAMINHO_ARQUIVO)
desfeitos = []

while True:
    entrada = input('insira uma opção: listar, desfazer, refazer, adicionar, limpar: ')
    print()

    if entrada == 'adicionar':
        novo_item = input('Insira uma tarefa: ')
        lista.append(novo_item)
        salvar_tarefas(lista, CAMINHO_ARQUIVO)

        print()
        print(f'{novo_item} foi adicionado a lista.')
        print()
        print('--TAREFAS--')
        print()
        for i in lista:
            print(i)

    elif entrada == 'listar':
        if lista:
            print()
            print('--TAREFAS--')
            print()
            for i in lista:
                print(i)
        else:
            print('Nada para listar')

    elif entrada == 'desfazer':
        if lista:
            item_removido = lista.pop()
            desfeitos.append(item_removido)
            salvar_tarefas(lista, CAMINHO_ARQUIVO)

            print(f'{item_removido} foi apagado.')
            print()
            for i in lista:
                print(i)
        else:
            print('Nada a desfazer!')

    elif entrada == 'refazer':
        if desfeitos:
            item_refazer = desfeitos.pop()
            lista.append(item_refazer)
            salvar_tarefas(lista, CAMINHO_ARQUIVO)

            print(f'{item_refazer} foi adicionado novamente.')
        else:
            print('Nada a refazer!')

    elif entrada == 'limpar':
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print('Comando desconhecido, verifique se foi digitado corretamente.')
        print()