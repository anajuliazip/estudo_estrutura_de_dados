"""
Implementacao de Lista Simplesmente Encadeada utilizando nos com referencia para o proximo no.
Desafio 1 - Parte A
"""

from estruturas.lista_sequencial import Aluno


class No:
    """No da lista simplesmente encadeada."""
    def __init__(self, aluno: Aluno):
        self.aluno = aluno
        self.proximo = None


class ListaEncadeada:
    """
    Lista simplesmente encadeada baseada em nos (sem uso de list para o encadeamento interno).
    Nao mantem referencia para o ultimo no (cauda/tail), apenas para o primeiro no (inicio/head)
    e contador de tamanho.

    Regras adotadas (identicas a ListaSequencial):
    1. Matricula duplicada:
       - Por padrao (verificar_duplicata=False), as insercoes nao realizam busca linear
         previa para preservar a complexidade nativa de insercao O(1) no inicio.
       - Se verificar_duplicata=True for informado na insercao e a matricula ja existir,
         um ValueError e lancado.
       - Caso haja matriculas duplicadas armazenadas, buscar(matricula) e remover(matricula)
         atuam sobre a primeira ocorrencia a partir do inicio da lista.
    2. Elemento inexistente:
       - buscar(matricula) retorna None quando a matricula nao e encontrada ou a lista esta vazia.
       - remover(matricula) retorna None quando a matricula nao e encontrada ou a lista esta vazia
         (e retorna o objeto Aluno removido quando a remocao ocorre com sucesso).
    """

    def __init__(self):
        self.inicio = None
        self._tamanho = 0

    def inserir_inicio(self, aluno: Aluno, verificar_duplicata: bool = False) -> None:
        """Insere um registro no inicio da lista encadeada. Complexidade: O(1)."""
        if verificar_duplicata and self.buscar(aluno.matricula) is not None:
            raise ValueError(f"Matricula {aluno.matricula} ja cadastrada.")
        novo_no = No(aluno)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
        self._tamanho += 1

    def inserir_final(self, aluno: Aluno, verificar_duplicata: bool = False) -> None:
        """
        Insere um registro no final da lista encadeada.
        Como nao ha referencia direta para o ultimo no, percorre a lista ate o fim.
        Complexidade: O(n).
        """
        if verificar_duplicata and self.buscar(aluno.matricula) is not None:
            raise ValueError(f"Matricula {aluno.matricula} ja cadastrada.")
        novo_no = No(aluno)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self._tamanho += 1

    def buscar(self, matricula: int):
        """Localiza e retorna o registro correspondente a matricula, ou None. Complexidade: O(n)."""
        atual = self.inicio
        while atual is not None:
            if atual.aluno.matricula == matricula:
                return atual.aluno
            atual = atual.proximo
        return None

    def remover(self, matricula: int):
        """Remove e retorna o registro identificado pela matricula, ou None se inexistente. Complexidade: O(n)."""
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.aluno.matricula == matricula:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return atual.aluno
            anterior = atual
            atual = atual.proximo
        return None

    def listar(self) -> list:
        """Retorna uma lista com os registros percorridos na ordem de armazenamento. Complexidade: O(n)."""
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.aluno)
            atual = atual.proximo
        return resultado

    def tamanho(self) -> int:
        """Retorna a quantidade de registros armazenados. Complexidade: O(1)."""
        return self._tamanho
