"""
Script principal de demonstracao pratica dos 3 desafios da AV1 de Estrutura de Dados.
"""
from estruturas.lista_sequencial import Aluno, ListaSequencial
from estruturas.lista_encadeada import ListaEncadeada
from estruturas.fila import Fila
from estruturas.pilha import Pilha
from testes.teste_listas import executar_testes_estrutura
from testes.teste_fila import executar_testes_fila
from testes.teste_pilha import executar_testes_pilha
from comparacao import executar_experimentos


def demonstrar_desafio_1():
    print("==========================================================================================")
    print("DEMONSTRACAO PRATICA - DESAFIO 1: ListaSequencial e ListaEncadeada")
    print("==========================================================================================")
    for cls, nome in [(ListaSequencial, "ListaSequencial"), (ListaEncadeada, "ListaEncadeada")]:
        lista = cls()
        lista.inserir_inicio(Aluno(202602, "Bruno"))
        lista.inserir_inicio(Aluno(202601, "Ana"))
        lista.inserir_final(Aluno(202603, "Carla"))
        print(f"\n[{nome}] Apos insercoes no inicio e final (tamanho={lista.tamanho()}):")
        print("  Registros:", lista.listar())
        print("  Busca matricula 202602:", lista.buscar(202602))
        print("  Busca matricula inexistente 999999:", lista.buscar(999999))
        print("  Removendo matricula 202602:", lista.remover(202602))
        print(f"  Registros restantes (tamanho={lista.tamanho()}):", lista.listar())
    print()


def main():
    demonstrar_desafio_1()
    executar_testes_estrutura(ListaSequencial, "ListaSequencial")
    executar_testes_estrutura(ListaEncadeada, "ListaEncadeada")
    executar_testes_fila()
    print()
    executar_testes_pilha()
    print()
    executar_experimentos()


if __name__ == "__main__":
    main()
