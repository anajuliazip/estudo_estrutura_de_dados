"""
Implementacao de Lista Sequencial utilizando list do Python.
Desafio 1 - Parte A
"""

class Aluno:
    """Representa o registro de um aluno com matricula e nome."""
    def __init__(self, matricula: int, nome: str):
        self.matricula = matricula
        self.nome = nome

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.matricula == other.matricula and self.nome == other.nome
        return False

    def __repr__(self):
        return f"Aluno(matricula={self.matricula}, nome='{self.nome}')"


class ListaSequencial:
    """
    Lista sequencial baseada em list do Python.

    Regras adotadas (identicas a ListaEncadeada):
    1. Matricula duplicada:
       - Por padrao (verificar_duplicata=False), as insercoes nao realizam busca linear
         previa para preservar a complexidade nativa de insercao da estrutura.
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
        self._dados = []

    def inserir_inicio(self, aluno: Aluno, verificar_duplicata: bool = False) -> None:
        """Insere um registro no inicio da lista sequencial. Complexidade: O(n)."""
        if verificar_duplicata and self.buscar(aluno.matricula) is not None:
            raise ValueError(f"Matricula {aluno.matricula} ja cadastrada.")
        self._dados.insert(0, aluno)

    def inserir_final(self, aluno: Aluno, verificar_duplicata: bool = False) -> None:
        """Insere um registro no final da lista sequencial. Complexidade: O(1) amortizado."""
        if verificar_duplicata and self.buscar(aluno.matricula) is not None:
            raise ValueError(f"Matricula {aluno.matricula} ja cadastrada.")
        self._dados.append(aluno)

    def buscar(self, matricula: int):
        """Localiza e retorna o primeiro registro correspondente a matricula, ou None. Complexidade: O(n)."""
        for aluno in self._dados:
            if aluno.matricula == matricula:
                return aluno
        return None

    def remover(self, matricula: int):
        """Remove e retorna o registro identificado pela matricula, ou None se inexistente. Complexidade: O(n)."""
        for i, aluno in enumerate(self._dados):
            if aluno.matricula == matricula:
                return self._dados.pop(i)
        return None

    def listar(self) -> list:
        """Retorna uma copia dos registros na ordem de armazenamento. Complexidade: O(n)."""
        return list(self._dados)

    def tamanho(self) -> int:
        """Retorna a quantidade de registros armazenados. Complexidade: O(1)."""
        return len(self._dados)
