"""
Testes obrigatorios para a classe Pilha (LIFO).
Desafio 3 - Historico de acoes com pilha
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from estruturas.pilha import Pilha


def executar_testes_pilha():
    print("=== Testando Historico de Acoes com Pilha (LIFO) ===")
    pilha = Pilha()

    # Estado inicial
    assert pilha.esta_vazia() is True
    assert pilha.tamanho() == 0

    # 1. Empilhe, nesta ordem: Criar documento, Inserir texto, Alterar titulo e Excluir paragrafo
    acoes = ["Criar documento", "Inserir texto", "Alterar título", "Excluir parágrafo"]
    for acao in acoes:
        pilha.empilhar(acao)
    assert pilha.tamanho() == 4
    assert pilha.esta_vazia() is False
    print("[OK] Empilhamento inicial (do topo para a base):", pilha.listar())

    # 2. Consulte topo(): deve retornar Excluir paragrafo sem alterar o tamanho
    assert pilha.topo() == "Excluir parágrafo"
    assert pilha.tamanho() == 4
    print(f"[OK] Consulta topo(): '{pilha.topo()}' (tamanho mantido em {pilha.tamanho()})")

    # 3. Desempilhe duas vezes: Excluir paragrafo e Alterar titulo, respectivamente
    des1 = pilha.desempilhar()
    des2 = pilha.desempilhar()
    assert des1 == "Excluir parágrafo"
    assert des2 == "Alterar título"
    print(f"[OK] Desempilhados: '{des1}', '{des2}'")

    # 4. Verifique que o novo topo e Inserir texto e que restam duas acoes
    assert pilha.topo() == "Inserir texto"
    assert pilha.tamanho() == 2
    assert pilha.listar() == ["Inserir texto", "Criar documento"]
    print(f"[OK] Novo topo: '{pilha.topo()}' | Acoes restantes ({pilha.tamanho()}): {pilha.listar()}")

    # 5. Esvazie a pilha e teste desempilhar() e topo() na estrutura vazia
    assert pilha.desempilhar() == "Inserir texto"
    assert pilha.desempilhar() == "Criar documento"

    assert pilha.esta_vazia() is True
    assert pilha.tamanho() == 0
    assert pilha.topo() is None
    assert pilha.desempilhar() is None
    print("[OK] Pilha esvaziada: esta_vazia()=True, tamanho()=0, topo()=None, desempilhar()=None\n")
    print("Todos os testes obrigatorios da Pilha passaram com sucesso!")


if __name__ == "__main__":
    executar_testes_pilha()
