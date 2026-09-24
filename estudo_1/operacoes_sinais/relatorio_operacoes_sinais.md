# Operações com Sinais

---

# Resumo conceitual

## Sinais discretos

Um sinal discreto é representado por uma sequência de valores definida em índices inteiros. A sequência pode ser escrita como $x[n]$, em que $n$ identifica a posição de cada amostra.

As operações com sinais discretos podem modificar a posição das amostras, seus valores de amplitude ou combinar diferentes sequências.

## Principais operações

| Operação | Tipo | Expressão |
| :--- | :--- | :--- |
| Atraso | Temporal | $x[n-n_0]$ |
| Avanço | Temporal | $x[n+n_0]$ |
| Inversão temporal | Temporal | $x[-n]$ |
| Escalonamento | Amplitude | $Ax[n]$ |
| Soma | Combinação | $x_1[n]+x_2[n]$ |

# Formulacão Matemática

## Atraso

Um atraso desloca a sequência para a direita. Para $n_0$ amostras:

$$
y[n] = x[n-n_0]
$$

Neste estudo, $n_0=2$:

$$
y[n] = x[n-2]
$$

Os valores permanecem iguais, somente suas posições no eixo $n$ são alteradas.

## Avanço

Um avanço desloca a sequência para a esquerda:

$$
y[n] = x[n+n_0]
$$

Para duas amostras:

$$
y[n] = x[n+2]
$$

Novamente, as amplitudes permanecem iguais, mas os índices são deslocados.

## Inversão temporal

A inversão temporal substitui $n$ por $-n$:

$$
y[n] = x[-n]
$$

Uma amostra localizada em $n=k$ passa para $n=-k$. Graficamente, a sequência é refletida em relação ao eixo $n=0$.

## Escalonamento de amplitude

$$
y[n] = Ax[n]
$$

## Amplificação

Para $A=2$:

$$
y[n] = 2x[n]
$$

Cada amplitude é multiplicada por dois, enquanto os índices permanecem inalterados.

## Inversão de amplitude

Para $A=-1$:

$$
y[n] = -x[n]
$$

Os índices permanecem iguais, mas os valores positivos tornam-se negativos e vice-versa.

## Soma de sinais

A soma combina duas sequências amostra a amostra:

$$
y[n] = x_1[n] + x_2[n]
$$

Embora a soma não esteja entre as seis transformações principais da simulação, ela é uma operação fundamental sobre sinais discretos.

# Exemplo

## Sequência escolhida

Para tornar as transformações visualmente claras, será utilizada uma sequência finita definida entre $n=-4$ e $n=4$:

$$
x[n] = \{1,2,3,2,1,0,-1,-2,-1\}
$$

| $n$ | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $x[n]$ | 1 | 2 | 3 | 2 | 1 | 0 | −1 | −2 | −1 |

## Transformações

- $x[n]$ – sinal original.
- $x[n-2]$ – atraso de 2 amostras.
- $x[n+2]$ – avanço de 2 amostras.
- $x[-n]$ – inversão temporal.
- $2x[n]$ – amplificação por fator 2.
- $-x[n]$ – inversão de amplitude.

---

:::: {include} ./simulacao/simulacao_operacoes_sinais.ipynb
::::

---

# Resultados

## Sinal original

O sinal original representa a sequência de referência. Nenhuma alteração é aplicada aos índices ou às amplitudes.

## Atraso $x[n-2]$

A sequência é deslocada duas posições para a direita. Os valores permanecem inalterados.

$$
k \rightarrow k+2
$$

## Avanço $x[n+2]$

A sequência é deslocada duas posições para a esquerda. Os valores permanecem inalterados.

$$
k \rightarrow k-2
$$

## Inversão $x[-n]$

A posição de cada amostra é refletida em torno de $n=0$. Os valores das amostras não são alterados.

## Amplificação $2x[n]$

Cada amplitude é multiplicada por dois. A posição das amostras permanece igual.

## Inversão $-x[n]$

Cada amplitude troca de sinal. O módulo dos valores permanece igual e os índices não sofrem alteração.

## Resumo dos efeitos

| Operação | Índices | Amplitudes | Efeito |
| :--- | :--- | :--- | :--- |
| $x[n]$ | Inalterados | Inalteradas | Referência |
| $x[n-2]$ | $n \rightarrow n+2$ | Inalteradas | Atraso |
| $x[n+2]$ | $n \rightarrow n-2$ | Inalteradas | Avanço |
| $x[-n]$ | $n \rightarrow -n$ | Inalteradas | Reflexão temporal |
| $2x[n]$ | Inalterados | $\times 2$ | Amplificação |
| $-x[n]$ | Inalterados | $\times(-1)$ | Inversão vertical |

# Discussão

## Operações temporais

Os deslocamentos modificam apenas a posição das amostras no eixo $n$. A forma e os valores da sequência permanecem os mesmos. Já a inversão temporal reflete a sequência em relação a $n=0$.

## Operações de amplitude

O escalonamento atua diretamente nos valores da sequência. Em $2x[n]$, todas as amplitudes são dobradas. Em $-x[n]$, todas as amplitudes são invertidas em relação ao eixo horizontal.

## Importância

Essas operações são fundamentais em processamento digital de sinais e aparecem em análise de sequências, filtros digitais, sistemas de comunicação, áudio e diversas aplicações de engenharia.