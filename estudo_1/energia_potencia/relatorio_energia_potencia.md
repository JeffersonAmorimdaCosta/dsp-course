# Energia e Potência

---

# Resumo conceitual

## Energia de um sinal discreto

A energia de um sinal discreto representa a soma das contribuições de todas as amostras da sequência. Para cada amostra, considera-se o módulo do valor ao quadrado, evitando que valores positivos e negativos se cancelem.

$$
E = \sum_{n=-\infty}^{\infty} |x[n]|^2
$$

Um sinal é classificado como sinal de energia quando sua energia é finita e maior que zero:

$$
0 < E < \infty
$$

Portanto, um sinal de energia possui uma quantidade total de energia limitada.

## Potência média de um sinal discreto

A potência média mede a quantidade média de energia por amostra ao considerar uma janela cada vez maior de amostras ao redor da origem.

$$
P =
\lim_{N \to \infty}
\frac{1}{2N+1}
\sum_{n=-N}^{N}
|x[n]|^2
$$

O limite considera uma quantidade crescente de amostras e permite determinar o valor médio da energia por amostra no longo prazo.

## Diferença entre sinais de energia e sinais de potência

A energia está relacionada à quantidade total acumulada do sinal, enquanto a potência média está relacionada à quantidade média de energia por amostra quando o sinal é analisado em uma janela cada vez maior.

| Característica | Sinal de energia | Sinal de potência |
| :--- | :--- | :--- |
| Energia total | Finita e maior que zero | Pode ser infinita |
| Potência média | Pode tender a zero | Finita e maior que zero |
| Critério principal | $0 < E < \infty$ | $0 < P < \infty$ |
| Interpretação | Energia total limitada | Energia média por amostra |

---

# Formulação matemática

## Energia

A energia de um sinal discreto é definida por:

$$
E = \sum_{n=-\infty}^{\infty} |x[n]|^2
$$

onde:

- $E$ é a energia total do sinal.
- $x[n]$ é o valor do sinal na amostra de índice $n$.
- $|x[n]|^2$ representa o módulo ao quadrado da amostra.
- $n$ representa o índice inteiro da sequência.

## Critério para sinal de energia

$$
0 < E < \infty
$$

Se a soma for finita e diferente de zero, o sinal pertence à classe dos sinais de energia.

## Potência média

A potência média é definida por:

$$
P =
\lim_{N \to \infty}
\frac{1}{2N+1}
\sum_{n=-N}^{N}
|x[n]|^2
$$

onde:

- $P$ é a potência média do sinal.
- $N$ define o limite da janela de observação.
- $2N+1$ é o número total de amostras consideradas entre $-N$ e $N$.
- $|x[n]|^2$ representa a contribuição energética de cada amostra.

## Critério para sinal de potência

$$
0 < P < \infty
$$

Um sinal é classificado como sinal de potência quando sua potência média é finita e diferente de zero.

## Classificação dos sinais

### Sinais de energia

Um sinal de energia apresenta energia total finita. Para esses sinais, a quantidade total obtida pela soma das contribuições das amostras permanece limitada.

### Sinais de potência

Um sinal de potência apresenta potência média finita e não nula. Esse tipo de classificação é especialmente associado à análise de sinais que permanecem ativos por períodos muito longos ou indefinidamente.

### Relação entre as classificações

As classificações são baseadas nas grandezas que permanecem finitas e não nulas. Em uma análise ideal, um sinal de energia possui energia finita, enquanto um sinal de potência possui potência média finita e não nula.

---

# Exemplos

## Sequência de duração finita

Considere a sequência finita:

$$
x[n] = \{1, 2, 1\}
$$

Considerando que os demais valores são zero, a energia pode ser calculada diretamente pela soma dos quadrados:

$$
E = 1^2 + 2^2 + 1^2 = 6
$$

Nesse caso, a energia é finita e diferente de zero. Portanto, a sequência satisfaz o critério de um sinal de energia.

## Sinal constante

Considere uma sequência constante não nula:

$$
x[n] = A
$$

Nesse caso, cada amostra possui magnitude constante. A soma da energia ao longo de infinitas amostras não permanece finita, enquanto a média dos valores de $|x[n]|^2$ permanece igual a $|A|^2$.

$$
P = |A|^2
$$

Assim, para $A \neq 0$, o sinal apresenta potência média finita e não nula.

---

:::: {include} ./simulacao/simulacao_energia_potencia.ipynb
::::

---

# Resultados

## Sinal de energia

Para o sinal finito utilizado na simulação, a energia é obtida pela soma dos quadrados das amplitudes. Como apenas um número finito de amostras é diferente de zero, o resultado é finito.

$$
E = \sum |x[n]|^2
$$

Esse comportamento caracteriza o sinal como sinal de energia.

## Sinal de potência

Para o sinal constante utilizado na simulação, a energia acumulada cresce com o número de amostras. Entretanto, ao dividir essa soma pela quantidade de amostras, a potência média permanece constante.

$$
P = |A|^2
$$

Para $A = 2$, o valor teórico da potência média é:

$$
P = 2^2 = 4
$$

## Comparação

| Grandeza | Sinal finito | Sinal constante |
| :--- | :--- | :--- |
| Energia | Finita | Não finita no intervalo infinito |
| Potência média | Tende a zero quando a janela cresce | Finita e não nula |
| Classificação | Sinal de energia | Sinal de potência |

---

# Discussão

## Energia

A energia considera a contribuição acumulada de todas as amostras do sinal. Quando essa soma é finita e diferente de zero, o sinal é classificado como sinal de energia.

## Potência

A potência média considera a energia média por amostra em uma janela que aumenta progressivamente. Para um sinal de potência, essa média tende a um valor finito e não nulo.

## Diferença fundamental

A principal diferença está na forma de análise. A energia busca determinar a quantidade total acumulada no sinal, enquanto a potência procura determinar a quantidade média associada ao sinal quando o intervalo de observação cresce.

Assim, sinais de duração finita e não nulos são exemplos naturais de sinais de energia, enquanto sinais que permanecem ativos indefinidamente podem apresentar potência média finita e não nula.