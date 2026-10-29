"""
Testes obrigatorios para a classe Fila (FIFO).
Desafio 2 - Fila de atendimento
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from estruturas.fila import Fila


def executar_testes_fila():
    print("=== Testando Fila de Atendimento (FIFO) ===")
    fila = Fila()

    # Estado inicial
    assert fila.esta_vazia() is True
    assert fila.tamanho() == 0

    # 1. Enfileire Ana, Bruno, Carla e Diego, nesta ordem
    for nome in ["Ana", "Bruno", "Carla", "Diego"]:
        fila.enfileirar(nome)
    assert fila.listar() == ["Ana", "Bruno", "Carla", "Diego"]
    assert fila.tamanho() == 4
    assert fila.esta_vazia() is False
    print("[OK] Enfileiramento inicial:", fila.listar())

    # 2. Consulte primeiro(): deve retornar Ana sem alterar o tamanho
    assert fila.primeiro() == "Ana"
    assert fila.tamanho() == 4
    print(f"[OK] Consulta primeiro(): '{fila.primeiro()}' (tamanho mantido em {fila.tamanho()})")

    # 3. Desenfileire duas vezes: retornos devem ser Ana e Bruno. Proximo deve ser Carla
    atendido1 = fila.desenfileirar()
    atendido2 = fila.desenfileirar()
    assert atendido1 == "Ana"
    assert atendido2 == "Bruno"
    assert fila.primeiro() == "Carla"
    assert fila.tamanho() == 2
    print(f"[OK] Desenfileirados: '{atendido1}', '{atendido2}' | Proximo da fila: '{fila.primeiro()}'")

    # 4. Enfileire Elisa. A ordem restante deve ser Carla, Diego e Elisa
    fila.enfileirar("Elisa")
    assert fila.listar() == ["Carla", "Diego", "Elisa"]
    assert fila.tamanho() == 3
    print("[OK] Apos enfileirar Elisa, ordem restante:", fila.listar())

    # 5. Esvazie a fila e teste desenfileirar() e primeiro() na estrutura vazia
    assert fila.desenfileirar() == "Carla"
    assert fila.desenfileirar() == "Diego"
    assert fila.desenfileirar() == "Elisa"

    assert fila.esta_vazia() is True
    assert fila.tamanho() == 0
    assert fila.primeiro() is None
    assert fila.desenfileirar() is None
    print("[OK] Fila esvaziada: esta_vazia()=True, tamanho()=0, primeiro()=None, desenfileirar()=None\n")
    print("Todos os testes obrigatorios da Fila passaram com sucesso!")


if __name__ == "__main__":
    executar_testes_fila()
