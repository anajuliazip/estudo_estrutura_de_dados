"""
Experimentos de desempenho comparando ListaSequencial e ListaEncadeada.
Desafio 1 - Parte B
"""
import time
import statistics
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from estruturas.lista_sequencial import Aluno, ListaSequencial
from estruturas.lista_encadeada import ListaEncadeada

REPETICOES = 7  # Ao menos cinco repeticoes (usamos 7 para mediana estavel)
TAMANHOS = [100, 1000, 5000]


def preparar_estruturas(n: int):
    """Cria e popula ListaSequencial e ListaEncadeada com os mesmos n alunos (matriculas 1..n)."""
    seq = ListaSequencial()
    enc = ListaEncadeada()
    alunos = [Aluno(i, f"Aluno_{i}") for i in range(1, n + 1)]
    for a in alunos:
        seq.inserir_final(a)
    for a in reversed(alunos):
        enc.inserir_inicio(a)
    return seq, enc


def medir_inserir_inicio(n: int):
    tempos_seq = []
    tempos_enc = []
    novo_aluno = Aluno(0, "Novo_Inicio")

    for _ in range(REPETICOES):
        seq, enc = preparar_estruturas(n)

        t0 = time.perf_counter()
        seq.inserir_inicio(novo_aluno)
        t1 = time.perf_counter()
        tempos_seq.append((t1 - t0) * 1e6)

        t0 = time.perf_counter()
        enc.inserir_inicio(novo_aluno)
        t1 = time.perf_counter()
        tempos_enc.append((t1 - t0) * 1e6)

    return statistics.median(tempos_seq), statistics.median(tempos_enc)


def medir_inserir_final(n: int):
    tempos_seq = []
    tempos_enc = []
    novo_aluno = Aluno(n + 1, "Novo_Final")

    for _ in range(REPETICOES):
        seq, enc = preparar_estruturas(n)

        t0 = time.perf_counter()
        seq.inserir_final(novo_aluno)
        t1 = time.perf_counter()
        tempos_seq.append((t1 - t0) * 1e6)

        t0 = time.perf_counter()
        enc.inserir_final(novo_aluno)
        t1 = time.perf_counter()
        tempos_enc.append((t1 - t0) * 1e6)

    return statistics.median(tempos_seq), statistics.median(tempos_enc)


def medir_buscar(n: int, matricula_alvo: int):
    seq, enc = preparar_estruturas(n)
    tempos_seq = []
    tempos_enc = []

    for _ in range(REPETICOES):
        t0 = time.perf_counter()
        seq.buscar(matricula_alvo)
        t1 = time.perf_counter()
        tempos_seq.append((t1 - t0) * 1e6)

        t0 = time.perf_counter()
        enc.buscar(matricula_alvo)
        t1 = time.perf_counter()
        tempos_enc.append((t1 - t0) * 1e6)

    return statistics.median(tempos_seq), statistics.median(tempos_enc)


def medir_remover(n: int, matricula_alvo: int):
    tempos_seq = []
    tempos_enc = []

    for _ in range(REPETICOES):
        seq, enc = preparar_estruturas(n)

        t0 = time.perf_counter()
        seq.remover(matricula_alvo)
        t1 = time.perf_counter()
        tempos_seq.append((t1 - t0) * 1e6)

        t0 = time.perf_counter()
        enc.remover(matricula_alvo)
        t1 = time.perf_counter()
        tempos_enc.append((t1 - t0) * 1e6)

    return statistics.median(tempos_seq), statistics.median(tempos_enc)


def executar_experimentos():
    print("==========================================================================================")
    print("EXPERIMENTOS DE DESEMPENHO: ListaSequencial vs ListaEncadeada")
    print(f"Unidade de tempo: microssegundos (us) | Escopo: 1 operacao unitaria | Mediana de {REPETICOES} repeticoes")
    print("==========================================================================================")
    print(f"{'Tamanho':<8} | {'Operacao':<16} | {'Posicao / Alvo':<22} | {'Sequencial (us)':>16} | {'Encadeada (us)':>15}")
    print("-" * 90)

    resultados = []
    for n in TAMANHOS:
        meio = n // 2
        casos = [
            ("inserir_inicio", "Inicio (pos 0)", medir_inserir_inicio(n)),
            ("inserir_final", f"Final (pos {n})", medir_inserir_final(n)),
            ("buscar", "Inicio (mat=1)", medir_buscar(n, 1)),
            ("buscar", f"Meio (mat={meio})", medir_buscar(n, meio)),
            ("buscar", f"Final (mat={n})", medir_buscar(n, n)),
            ("buscar", "Inexistente (mat=-1)", medir_buscar(n, -1)),
            ("remover", "Inicio (mat=1)", medir_remover(n, 1)),
            ("remover", f"Meio (mat={meio})", medir_remover(n, meio)),
            ("remover", f"Final (mat={n})", medir_remover(n, n)),
        ]
        for op, alvo, (t_seq, t_enc) in casos:
            resultados.append((n, op, alvo, t_seq, t_enc))
            print(f"{n:<8} | {op:<16} | {alvo:<22} | {t_seq:>16.3f} | {t_enc:>15.3f}")
        print("-" * 90)
    return resultados


if __name__ == "__main__":
    executar_experimentos()
