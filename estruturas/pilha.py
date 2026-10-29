"""
Implementacao da classe Pilha com armazenamento interno em list, respeitando LIFO.
Desafio 3 - Historico de acoes com pilha
"""

class Pilha:
    """
    Estrutura de dados Pilha (LIFO - Last In, First Out) utilizando list do Python.
    Regra para estrutura vazia:
    - desempilhar() e topo() retornam None quando a pilha esta vazia.
    Ordem documentada de listar():
    - Retorna as acoes do topo (acao mais recente) ate a base (acao mais antiga).
    """

    def __init__(self):
        self._itens = []

    def empilhar(self, acao: str) -> None:
        """Adiciona uma acao ao topo da pilha. Complexidade: O(1) amortizado."""
        self._itens.append(acao)

    def desempilhar(self):
        """Remove e retorna a ultima acao empilhada (topo), ou None se vazia. Complexidade: O(1) amortizado."""
        if self.esta_vazia():
            return None
        return self._itens.pop()

    def topo(self):
        """Consulta a ultima acao sem remove-la, ou None se vazia. Complexidade: O(1)."""
        if self.esta_vazia():
            return None
        return self._itens[-1]

    def tamanho(self) -> int:
        """Retorna a quantidade de acoes na pilha. Complexidade: O(1)."""
        return len(self._itens)

    def esta_vazia(self) -> bool:
        """Retorna True se a pilha estiver vazia, False caso contrario. Complexidade: O(1)."""
        return len(self._itens) == 0

    def listar(self) -> list:
        """
        Retorna as acoes na ordem documentada pela equipe:
        do topo (mais recente) para a base (mais antiga).
        Complexidade: O(n).
        """
        return list(reversed(self._itens))
