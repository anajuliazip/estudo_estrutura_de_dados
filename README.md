# Atividade Prática de Estrutura de Dados (AV1)

- **Instituição:** Faculdade INBEC
- **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
- **Disciplina:** Estrutura de Dados
- **Professor:** Niltemberg Carvalho
- **Aluna:** Ana Júlia N. da Cruz
- **Turno:** Noite

---

## 1. Estrutura do Projeto e Instruções de Execução

```text
├── estruturas/
│   ├── __init__.py
│   ├── lista_sequencial.py
│   ├── lista_encadeada.py
│   ├── fila.py
│   └── pilha.py
├── testes/
│   ├── teste_listas.py
│   ├── teste_fila.py
│   └── teste_pilha.py
├── comparacao.py
├── main.py
└── README.md
```

### Como executar:
- **Demonstração completa (todos os testes e experimentos):**
  ```bash
  python3 main.py
  ```
- **Testes individuais:**
  ```bash
  python3 testes/teste_listas.py
  python3 testes/teste_fila.py
  python3 testes/teste_pilha.py
  ```
- **Experimentos de desempenho (Desafio 1 - Parte B):**
  ```bash
  python3 comparacao.py
  ```

---

## 2. Decisões de Projeto e Regras Documentadas

### Desafio 1: `ListaSequencial` e `ListaEncadeada`
Ambas as estruturas manipulam objetos `Aluno(matricula, nome)` e oferecem exatamente a mesma interface:
1. **Regra para matrícula duplicada:**
   - Por padrão (`verificar_duplicata=False`), `inserir_inicio` e `inserir_final` inserem o registro diretamente sem realizar busca linear prévia na estrutura, preservando a complexidade assintótica nativa de inserção ($O(1)$ no início da `ListaEncadeada` e $O(1)$ amortizado no final da `ListaSequencial`).
   - Caso `verificar_duplicata=True` seja passado na chamada de inserção e a matrícula já exista, é lançado um `ValueError`.
   - Se houver matrículas duplicadas armazenadas, `buscar(matricula)` e `remover(matricula)` operam sobre a **primeira ocorrência** encontrada a partir do início da lista.
2. **Regra para elemento inexistente e estrutura vazia:**
   - `buscar(matricula)` retorna `None` caso a matrícula não exista ou a estrutura esteja vazia.
   - `remover(matricula)` retorna o registro `Aluno` removido em caso de sucesso, ou `None` caso a matrícula não seja encontrada ou a estrutura esteja vazia.
3. **Referência ao último nó na `ListaEncadeada`:**
   - A `ListaEncadeada` mantém referência apenas para o primeiro nó (`self.inicio`) e um contador `self._tamanho`, sem ponteiro para o último nó (`fim`/`tail`). Assim, `inserir_final` percorre a cadeia de nós até o final ($O(n)$).

### Desafio 2: `Fila` (FIFO)
- Armazenamento interno em `list` do Python (`self._itens`).
- `enfileirar(aluno)` utiliza `append(aluno)` no final da lista ($O(1)$ amortizado).
- `desenfileirar()` utiliza `pop(0)` no início da lista ($O(n)$) e retorna `None` caso a fila esteja vazia.
- `primeiro()` retorna `self._itens[0]` ($O(1)$) ou `None` caso a fila esteja vazia.

### Desafio 3: `Pilha` (LIFO)
- Armazenamento interno em `list` do Python (`self._itens`), onde o topo corresponde ao último índice (`-1`).
- `empilhar(acao)` utiliza `append(acao)` ($O(1)$ amortizado).
- `desempilhar()` utiliza `pop()` ($O(1)$ amortizado) e retorna `None` se a pilha estiver vazia.
- `topo()` retorna `self._itens[-1]` ($O(1)$) ou `None` se a pilha estiver vazia.
- **Ordem documentada de `listar()`:** retorna as ações **do topo (ação mais recente) até a base (ação mais antiga)**.

---

## 3. Desafio 1 - Tabela de Desempenho (Parte B)

- **Unidade de tempo:** microssegundos ($\mu s$, onde $1\text{ }\mu s = 10^{-6}\text{ s}$).
- **Escopo medido:** **1 operação unitária** medida com `time.perf_counter()`, apresentando a **mediana de 7 repetições** (estado preparado e restaurado fora do intervalo medido).

| Tamanho ($N$) | Operação | Posição / Alvo | `ListaSequencial` ($\mu s$) | `ListaEncadeada` ($\mu s$) |
| :--- | :--- | :--- | ---: | ---: |
| **100** | `inserir_inicio` | Início (pos 0) | 0,552 | 0,913 |
| **100** | `inserir_final` | Final (pos 100) | 0,404 | 7,515 |
| **100** | `buscar` | Início (`mat=1`) | 0,374 | 0,389 |
| **100** | `buscar` | Meio (`mat=50`) | 3,023 | 5,710 |
| **100** | `buscar` | Final (`mat=100`) | 5,594 | 11,233 |
| **100** | `buscar` | Inexistente (`mat=-1`) | 5,527 | 11,372 |
| **100** | `remover` | Início (`mat=1`) | 1,069 | 0,930 |
| **100** | `remover` | Meio (`mat=50`) | 4,578 | 7,116 |
| **100** | `remover` | Final (`mat=100`) | 8,190 | 12,805 |
| **1.000** | `inserir_inicio` | Início (pos 0) | 1,846 | 1,177 |
| **1.000** | `inserir_final` | Final (pos 1000) | 0,921 | 66,900 |
| **1.000** | `buscar` | Início (`mat=1`) | 0,423 | 0,428 |
| **1.000** | `buscar` | Meio (`mat=500`) | 28,644 | 56,960 |
| **1.000** | `buscar` | Final (`mat=1000`) | 56,181 | 114,778 |
| **1.000** | `buscar` | Inexistente (`mat=-1`) | 54,745 | 118,035 |
| **1.000** | `remover` | Início (`mat=1`) | 4,051 | 1,916 |
| **1.000** | `remover` | Meio (`mat=500`) | 45,779 | 62,410 |
| **1.000** | `remover` | Final (`mat=1000`) | 94,090 | 124,820 |
| **5.000** | `inserir_inicio` | Início (pos 0) | 8,301 | 2,578 |
| **5.000** | `inserir_final` | Final (pos 5000) | 2,985 | 389,775 |
| **5.000** | `buscar` | Início (`mat=1`) | 0,393 | 0,403 |
| **5.000** | `buscar` | Meio (`mat=2500`) | 148,349 | 294,654 |
| **5.000** | `buscar` | Final (`mat=5000`) | 312,486 | 626,621 |
| **5.000** | `buscar` | Inexistente (`mat=-1`) | 306,184 | 619,846 |
| **5.000** | `remover` | Início (`mat=1`) | 11,776 | 3,347 |
| **5.000** | `remover` | Meio (`mat=2500`) | 278,683 | 348,696 |
| **5.000** | `remover` | Final (`mat=5000`) | 534,469 | 748,421 |

---

## 4. Respostas às Questões de Análise

### Desafio 1 - Parte C (Análise dos Resultados)

1. **Qual estrutura apresentou melhor desempenho na inserção no início? Explique.**
   - A **`ListaEncadeada`** apresenta melhor escalabilidade e desempenho à medida que $N$ cresce ($1,177\text{ }\mu s$ contra $1,846\text{ }\mu s$ em $N=1.000$, e $2,578\text{ }\mu s$ contra $8,301\text{ }\mu s$ em $N=5.000$). Isso ocorre porque na lista encadeada a inserção no início é $O(1)$: basta instanciar um novo `No` e apontar `novo_no.proximo = self.inicio`. Já na `ListaSequencial`, `list.insert(0, aluno)` tem complexidade $O(n)$, exigindo o deslocamento (*shift*) de todos os $n$ elementos subsequentes na memória. Em $N=100$, a `ListaSequencial` parece ligeiramente mais rápida ($0,552\text{ }\mu s$ vs $0,913\text{ }\mu s$) apenas porque o deslocamento de 100 ponteiros em C (`memmove`) tem constante multiplicativa menor do que a alocação de um objeto Python `No`, mas o custo $O(n)$ torna-se evidente conforme $N$ aumenta.

2. **Qual apresentou melhor desempenho na busca por matrícula?**
   - A **`ListaSequencial`** apresentou aproximadamente o dobro da velocidade da `ListaEncadeada` nas buscas no meio, no final e de elementos inexistentes (por exemplo, em $N=5.000$ no final: $312,486\text{ }\mu s$ na sequencial contra $626,621\text{ }\mu s$ na encadeada). Embora ambas possuam a mesma complexidade assintótica teórica de $O(n)$ (busca linear), a `ListaSequencial` percorre um vetor contíguo de ponteiros em C com excelente localidade espacial de cache da CPU, enquanto a `ListaEncadeada` realiza saltos de ponteiros (`atual = atual.proximo`) desreferenciando atributos em objetos Python dispersos no *heap*.

3. **Como o aumento da quantidade de alunos afetou os resultados?**
   - Operações $O(1)$ (como `inserir_inicio` e `buscar` no início na `ListaEncadeada`, e `inserir_final` na `ListaSequencial`) mantiveram tempos praticamente constantes na casa de poucos microssegundos independentemente de $N$ variar de $100$ para $5.000$.
   - Operações $O(n)$ (`buscar` no meio/fim, `remover` no meio/fim, `inserir_final` na `ListaEncadeada` sem ponteiro de cauda e `inserir_inicio` na `ListaSequencial`) cresceram de forma linearmente proporcional a $N$: ao multiplicar $N$ por 10 (de $100$ para $1.000$) e depois por 5 (de $1.000$ para $5.000$), os tempos de busca e inserção ao final na lista encadeada aumentaram na mesma proporção (~10x e ~5x).

4. **Qual é a complexidade Big O das operações nas implementações desenvolvidas?**
   - **`inserir_inicio(aluno)`:** $O(n)$ na `ListaSequencial` (deslocamento de $n$ elementos); $O(1)$ na `ListaEncadeada` (atualização direta de ponteiro `inicio`).
   - **`inserir_final(aluno)`:** $O(1)$ amortizado na `ListaSequencial` (`list.append`); $O(n)$ na `ListaEncadeada` implementada sem referência ao último nó (percorre os $n$ nós até o fim). *(Caso a `ListaEncadeada` mantivesse referência `self.fim` para o último nó, `inserir_final` passaria a ser $O(1)$).*
   - **`buscar(matricula)`:** $O(1)$ no melhor caso (primeiro elemento) e $O(n)$ no caso médio e pior caso em ambas as estruturas.
   - **`remover(matricula)`:** Composta por duas etapas: busca + remoção física.
     - Na `ListaSequencial`: no início, a busca é $O(1)$, mas a remoção `pop(0)` desloca $n-1$ elementos ($O(n)$); no final, a busca percorre $n$ elementos ($O(n)$) e a remoção `pop()` é $O(1)$; logo, é **$O(n)$ em todos os cenários**.
     - Na `ListaEncadeada`: no início, tanto a localização quanto o ajuste `self.inicio = atual.proximo` são **$O(1)$**; no meio e no final, a remoção do ponteiro em si é $O(1)$, mas a busca prévia até o nó exige percorrer a lista, resultando em **$O(n)$** no caso médio/pior caso.
   - **`listar()`:** $O(n)$ em ambas as estruturas.
   - **`tamanho()`:** $O(1)$ em ambas (`len(self._dados)` na sequencial e atributo `self._tamanho` na encadeada).

5. **Em quais situações uma lista encadeada seria mais adequada que uma lista sequencial?**
   - Quando há alta frequência de inserções e remoções no início da estrutura (ou em posições já referenciadas por ponteiros/iteradores), onde a lista encadeada opera em tempo constante $O(1)$ estrito sem deslocamento de memória.
   - Na implementação de filas (com ponteiros `inicio` e `fim`) e pilhas dinâmicas sem necessidade de realocação de blocos contíguos.
   - Em ambientes ou linguagens de mais baixo nível onde a memória está fragmentada ou o custo de realocação/cópia de grandes vetores contíguos (picos de latência no redimensionamento) precisa ser evitado.

---

### Desafio 2 - Questões para Análise (Fila FIFO)

1. **Por que uma fila é adequada para esse problema?**
   - Porque o setor acadêmico atende os estudantes por ordem de chegada, exigindo justiça temporal (*fairness*): o primeiro estudante que entrou na fila deve ser o primeiro a ser atendido, o que corresponde exatamente à disciplina FIFO (*First In, First Out*).

2. **O que diferencia uma fila de uma pilha?**
   - A política de acesso e remoção dos elementos: a **Fila** segue o princípio **FIFO** (*First In, First Out*), em que as inserções ocorrem em uma extremidade (final/cauda) e as remoções na extremidade oposta (início/frente). Já a **Pilha** segue o princípio **LIFO** (*Last In, First Out*), em que tanto as inserções (`empilhar`) quanto as remoções (`desempilhar`) ocorrem na mesma extremidade (o topo).

3. **Qual é a complexidade das operações de inserção e remoção na sua implementação?**
   - `enfileirar(aluno)` (`self._itens.append(aluno)`): **$O(1)$ amortizado**.
   - `desenfileirar()` (`self._itens.pop(0)`): **$O(n)$**, pois remover o elemento do índice `0` de um `list` obriga o Python a deslocar todos os $n-1$ elementos restantes uma posição para a esquerda.
   - `primeiro()`, `tamanho()` e `esta_vazia()`: **$O(1)$**.

4. **Qual é a consequência de utilizar `pop(0)` em uma lista Python com muitos elementos?**
   - Como `list` em Python é implementada internamente como um vetor dinâmico contíguo de ponteiros, executar `pop(0)` exige mover $n - 1$ referências na memória a cada remoção ($O(n)$). Para filas com milhares ou milhões de elementos, processar $n$ desenfileiramentos seguidos resulta em custo quadrático $O(n^2)$, degradando severamente o desempenho. Em produção, para grandes volumes, utiliza-se uma lista encadeada com ponteiros `inicio`/`fim` ou `collections.deque`, onde `popleft()` tem custo $O(1)$.

---

### Desafio 3 - Questões para Análise (Pilha LIFO)

1. **Por que uma pilha é adequada para armazenar ações recentes?**
   - Porque em sistemas de histórico de ações (como o recurso *Desfazer / Undo*), a ação que precisa ser revertida ou consultada primeiro é sempre a última que o usuário executou, seguindo naturalmente a ordem cronológica inversa garantida pelo princípio **LIFO** (*Last In, First Out*).

2. **Qual ação será removida primeiro e por quê?**
   - No cenário de teste obrigatório, a ação removida primeiro é **"Excluir parágrafo"**, porque foi a última ação empilhada e, portanto, encontra-se no **topo** da pilha. Pela regra LIFO, o último elemento a entrar é obrigatoriamente o primeiro a sair.

3. **Qual é a complexidade de empilhar e desempilhar na implementação com `list`? Diferencie custo amortizado quando pertinente.**
   - Ambas as operações — `empilhar(acao)` via `append()` e `desempilhar()` via `pop()` no final da lista — possuem complexidade **$O(1)$ amortizado** (e $O(1)$ no caso comum).
   - **Diferenciação do custo amortizado:** Internamente, o `list` do Python aloca um array dinâmico com capacidade maior que o número atual de elementos (*over-allocation*). Na maioria das chamadas de `append()`, há espaço livre no final do array e a inserção ocorre em tempo constante estrito $O(1)$ sem deslocar nenhum elemento. Ocasionalmente, quando a capacidade do array se esgota, o Python aloca um bloco maior e copia as referências existentes, o que custa $O(n)$ naquele único passo; porém, como o crescimento da capacidade é geométrico, esse custo diluído (amortizado) ao longo de uma sequência de $n$ operações resulta em **$O(1)$ amortizado** por operação.

4. **Em quais outras aplicações computacionais uma pilha pode ser utilizada?**
   - **Pilha de chamadas de execução (*Call Stack*):** controle de chamadas de funções, variáveis locais e endereços de retorno em linguagens de programação e recursão.
   - **Navegadores Web:** histórico do botão "Voltar" (*Back*) entre páginas visitadas.
   - **Compiladores e Interpretadores:** validação de balanceamento de parênteses/chaves/colchetes, avaliação de expressões aritméticas (notação pós-fixa / Polonesa Reversa) e análise sintática (*parsing*).
   - **Algoritmos em Grafos e Árvores:** Busca em Profundidade (*Depth-First Search - DFS*) e travessias iterativas em árvores (pré-ordem, em-ordem e pós-ordem).
