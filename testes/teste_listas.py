"""
Testes funcionais para ListaSequencial e ListaEncadeada.
Desafio 1 - Parte B
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from estruturas.lista_sequencial import Aluno, ListaSequencial
from estruturas.lista_encadeada import ListaEncadeada


def executar_testes_estrutura(cls_lista, nome_estrutura: str):
    print(f"=== Testando {nome_estrutura} ===")
    lista = cls_lista()

    # 1. Operacoes em estrutura vazia
    assert lista.tamanho() == 0, "Tamanho inicial deve ser 0"
    assert lista.listar() == [], "Listar em estrutura vazia deve retornar []"
    assert lista.buscar(101) is None, "Busca em estrutura vazia deve retornar None"
    assert lista.remover(101) is None, "Remocao em estrutura vazia deve retornar None"
    print("[OK] Operacoes em estrutura vazia")

    # 2. Insercao e remocao de unico elemento
    a1 = Aluno(101, "Ana")
    lista.inserir_inicio(a1)
    assert lista.tamanho() == 1
    assert lista.buscar(101) == a1
    removido = lista.remover(101)
    assert removido == a1
    assert lista.tamanho() == 0
    assert lista.listar() == []
    print("[OK] Insercao e remocao do unico elemento")

    # 3. Insercoes no inicio e no final
    lista.inserir_inicio(Aluno(102, "Bruno"))     # [Bruno(102)]
    lista.inserir_inicio(Aluno(101, "Ana"))       # [Ana(101), Bruno(102)]
    lista.inserir_final(Aluno(103, "Carla"))      # [Ana(101), Bruno(102), Carla(103)]
    lista.inserir_final(Aluno(104, "Diego"))      # [Ana(101), Bruno(102), Carla(103), Diego(104)]
    lista.inserir_final(Aluno(105, "Elisa"))    # [Ana(101), Bruno(102), Carla(103), Diego(104), Elisa(105)]

    assert lista.tamanho() == 5
    matriculas = [a.matricula for a in lista.listar()]
    assert matriculas == [101, 102, 103, 104, 105], f"Ordem incorreta: {matriculas}"
    print("[OK] Insercoes no inicio e no final")

    # 4. Busca existente e inexistente
    achado = lista.buscar(103)
    assert achado is not None and achado.nome == "Carla"
    assert lista.buscar(999) is None
    print("[OK] Busca de elemento existente e inexistente")

    # 5. Remocao do primeiro, intermediario, ultimo e inexistente
    rem_primeiro = lista.remover(101)
    assert rem_primeiro is not None and rem_primeiro.nome == "Ana"
    assert [a.matricula for a in lista.listar()] == [102, 103, 104, 105]

    rem_intermediario = lista.remover(103)
    assert rem_intermediario is not None and rem_intermediario.nome == "Carla"
    assert [a.matricula for a in lista.listar()] == [102, 104, 105]

    rem_ultimo = lista.remover(105)
    assert rem_ultimo is not None and rem_ultimo.nome == "Elisa"
    assert [a.matricula for a in lista.listar()] == [102, 104]
    assert lista.tamanho() == 2

    assert lista.remover(999) is None
    print("[OK] Remocao do primeiro, intermediario, ultimo e inexistente")

    # 6. Regra de matricula duplicada
    # 6a. Com verificar_duplicata=True (bloqueia com ValueError)
    try:
        lista.inserir_final(Aluno(102, "Bruno Clonado"), verificar_duplicata=True)
        assert False, "Deveria ter lancado ValueError para matricula duplicada"
    except ValueError:
        pass

    # 6b. Com verificar_duplicata=False (padrao: insere sem busca previa e opera na 1a ocorrencia)
    lista.inserir_final(Aluno(102, "Bruno Segundo"))
    assert lista.buscar(102).nome == "Bruno"
    removido_dup = lista.remover(102)
    assert removido_dup.nome == "Bruno"
    assert lista.buscar(102).nome == "Bruno Segundo"
    print("[OK] Regra de matricula duplicada validada\n")


if __name__ == "__main__":
    executar_testes_estrutura(ListaSequencial, "ListaSequencial")
    executar_testes_estrutura(ListaEncadeada, "ListaEncadeada")
    print("Todos os testes funcionais de listas passaram com sucesso!")
