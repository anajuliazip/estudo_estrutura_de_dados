"""
Implementacao da classe Fila com armazenamento interno em list, respeitando FIFO.
Desafio 2 - Fila de atendimento
"""

class Fila:
    """
    Estrutura de dados Fila (FIFO - First In, First Out) utilizando list do Python.
    Regra para estrutura vazia:
    - desenfileirar() e primeiro() retornam None quando a fila esta vazia.
    """

    def __init__(self):
        self._itens = []

    def enfileirar(self, aluno: str) -> None:
        """Adiciona um aluno ao final da fila. Complexidade: O(1) amortizado."""
        self._itens.append(aluno)

    def desenfileirar(self):
        """Remove e retorna o primeiro aluno da fila, ou None se estiver vazia. Complexidade: O(n)."""
        if self.esta_vazia():
            return None
        return self._itens.pop(0)

    def primeiro(self):
        """Consulta o primeiro aluno sem remove-lo, ou None se estiver vazia. Complexidade: O(1)."""
        if self.esta_vazia():
            return None
        return self._itens[0]

    def tamanho(self) -> int:
        """Retorna a quantidade de alunos na fila. Complexidade: O(1)."""
        return len(self._itens)

    def esta_vazia(self) -> bool:
        """Retorna True se a fila estiver vazia, False caso contrario. Complexidade: O(1)."""
        return len(self._itens) == 0

    def listar(self) -> list:
        """Retorna os alunos na ordem de atendimento (do primeiro ao ultimo). Complexidade: O(n)."""
        return list(self._itens)
