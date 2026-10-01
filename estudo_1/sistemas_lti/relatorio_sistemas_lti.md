# Sistemas LTI

---

# Resumo Conceitual

Sistemas Lineares e Invariantes no Tempo, conhecidos como sistemas LTI (Linear Time-Invariant), constituem uma das classes mais importantes de sistemas estudados em engenharia e processamento digital de sinais.

A importância dos sistemas LTI está relacionada ao fato de que suas propriedades permitem determinar a resposta do sistema a sinais complexos a partir de uma única informação fundamental: sua resposta ao impulso.

Um sistema discreto pode ser representado genericamente por:

$$
y[n] = T\{x[n]\}
$$

em que $x[n]$ é o sinal de entrada, $y[n]$ é o sinal de saída e $T\{\cdot\}$ representa a transformação realizada pelo sistema.

Para que um sistema seja classificado como LTI, ele deve satisfazer simultaneamente duas propriedades:

* linearidade;
* invariância no tempo.

## Linearidade

Um sistema é linear quando obedece ao princípio da superposição. Isso significa que a resposta do sistema a uma combinação de entradas é igual à mesma combinação das respostas individuais.

Matematicamente:

$$
T\{a x_1[n] + b x_2[n]\}
=
aT\{x_1[n]\}
+
bT\{x_2[n]\}
$$

para quaisquer sinais $x_1[n]$ e $x_2[n]$ e quaisquer escalares $a$ e $b$.

A linearidade envolve duas propriedades:

### Aditividade

Se:

$$
T\{x_1[n]\} = y_1[n]
$$

e:

$$
T\{x_2[n]\} = y_2[n]
$$

então:

$$
T\{x_1[n]+x_2[n]\}
=
y_1[n]+y_2[n]
$$

### Homogeneidade

Para um escalar $a$:

$$
T\{a x[n]\}
=
aT\{x[n]\}
$$

Quando aditividade e homogeneidade são satisfeitas, o sistema é linear.

## Invariância no Tempo

Um sistema é invariante no tempo quando um deslocamento aplicado ao sinal de entrada produz o mesmo deslocamento na saída, sem alterar a resposta do sistema.

Se:

$$
T\{x[n]\}=y[n]
$$

então, para uma entrada deslocada:

$$
x_d[n]=x[n-n_0]
$$

o sistema será invariante no tempo se:

$$
T\{x[n-n_0]\}
=
y[n-n_0]
$$

para qualquer deslocamento $n_0$.

Essa propriedade significa que o comportamento do sistema não depende do instante em que o sinal é aplicado.

## Resposta ao Impulso

O impulso unitário discreto, representado por $\delta[n]$, é definido por:

$$
\delta[n] =
\begin{cases}
1, & n=0 \\
0, & n\neq0
\end{cases}
$$

Quando esse impulso é aplicado à entrada de um sistema, a saída obtida é denominada resposta ao impulso.

Para um sistema $T$:

$$
x[n]=\delta[n]
$$

a saída correspondente é:

$$
h[n]=T\{\delta[n]\}
$$

em que $h[n]$ representa a resposta ao impulso do sistema.

A resposta ao impulso é particularmente importante para sistemas LTI porque contém informações suficientes para determinar a resposta do sistema a qualquer entrada.

## Impulsos Deslocados

Uma sequência discreta pode ser representada como uma combinação de impulsos unitários deslocados.

Uma amostra $x[k]$ pode ser associada ao impulso deslocado:

$$
x[k]\delta[n-k]
$$

Assim, um sinal arbitrário pode ser representado por:

$$
x[n]
=
\sum_{k=-\infty}^{\infty}
x[k]\delta[n-k]
$$

Essa representação é conhecida como decomposição do sinal em impulsos deslocados.

## Caracterização de um Sistema LTI

Para um sistema LTI, cada impulso deslocado da entrada produz uma versão deslocada da resposta ao impulso.

Como:

$$
T\{\delta[n]\}=h[n]
$$

pela invariância no tempo:

$$
T\{\delta[n-k]\}
=
h[n-k]
$$

Pela linearidade:

$$
T\{x[k]\delta[n-k]\}
=
x[k]h[n-k]
$$

Portanto, aplicando o sistema à representação do sinal:

$$
x[n]
=
\sum_{k=-\infty}^{\infty}
x[k]\delta[n-k]
$$

obtém-se:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

Essa expressão corresponde à convolução discreta.

Dessa forma, um sistema LTI pode ser completamente caracterizado por sua resposta ao impulso.

---

# Formulação Matemática

## Condição de Linearidade

Considere:

$$
y_1[n]=T\{x_1[n]\}
$$

e:

$$
y_2[n]=T\{x_2[n]\}
$$

O sistema é linear quando:

$$
T\{a x_1[n]+b x_2[n]\}
=
a y_1[n]+b y_2[n]
$$

para quaisquer escalares $a$ e $b$.

## Condição de Invariância no Tempo

Se:

$$
T\{x[n]\}=y[n]
$$

então, para um deslocamento $n_0$, o sistema é invariante no tempo quando:

$$
T\{x[n-n_0]\}
=
y[n-n_0]
$$

para todo $n_0$.

## Resposta ao Impulso

Aplicando o impulso unitário à entrada:

$$
x[n]=\delta[n]
$$

a saída é:

$$
h[n]=T\{\delta[n]\}
$$

O termo $h[n]$ representa a resposta do sistema ao impulso unitário.

## Representação de um Sinal por Impulsos

Qualquer sequência $x[n]$ pode ser representada por:

$$
x[n]
=
\sum_{k=-\infty}^{\infty}
x[k]\delta[n-k]
$$

Nessa expressão:

* $x[n]$ é o sinal original;
* $x[k]$ é o valor da sequência no instante $k$;
* $\delta[n-k]$ é um impulso deslocado para o instante $k$;
* $k$ é o índice utilizado para percorrer todas as amostras do sinal.

## Convolução Discreta

Para um sistema LTI, substituindo a decomposição por impulsos na relação de entrada e saída:

$$
y[n]
=
T\left\{
\sum_{k=-\infty}^{\infty}
x[k]\delta[n-k]
\right\}
$$

Pela linearidade:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]T\{\delta[n-k]\}
$$

Como o sistema é invariante no tempo:

$$
T\{\delta[n-k]\}
=
h[n-k]
$$

Portanto:

$$
\boxed{
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
}
$$

Essa operação é denominada convolução discreta e pode ser representada por:

$$
y[n]=x[n]\ast h[n]
$$

em que:

* $x[n]$ é o sinal de entrada;
* $h[n]$ é a resposta ao impulso;
* $y[n]$ é o sinal de saída;
* $\ast$ representa a operação de convolução.

---

# Exemplo

Considere um sistema LTI cuja resposta ao impulso seja:

$$
h[n]
=
\delta[n]
+
\delta[n-1]
$$

Considere também a entrada:

$$
x[n]
=
\delta[n]
+
2\delta[n-1]
+
\delta[n-2]
$$

O objetivo é determinar a saída $y[n]$.

## Representação da Entrada

A entrada possui três amostras não nulas:

$$
x[0]=1
$$

$$
x[1]=2
$$

e:

$$
x[2]=1
$$

Portanto:

$$
x[n]
=
\delta[n]
+
2\delta[n-1]
+
\delta[n-2]
$$

## Cálculo pela Convolução

Como o sistema é LTI:

$$
y[n]=x[n]\ast h[n]
$$

Substituindo as expressões de $x[n]$ e $h[n]$:

$$
y[n]
=
\left(
\delta[n]
+
2\delta[n-1]
+
\delta[n-2]
\right)
\ast
\left(
\delta[n]
+
\delta[n-1]
\right)
$$

Utilizando a propriedade de convolução dos impulsos:

$$
\delta[n-k]\ast\delta[n-m]
=
\delta[n-(k+m)]
$$

obtém-se:

$$
y[n]
=
\delta[n]
+
3\delta[n-1]
+
3\delta[n-2]
+
\delta[n-3]
$$

Assim, os valores da saída são:

| $n$ | $x[n]$ | $h[n]$ | $y[n]$ |
| :---: | :------: | :------: | :------: |
|   0   |     1    |     1    |     1    |
|   1   |     2    |     1    |     3    |
|   2   |     1    |     0    |     3    |
|   3   |     0    |     0    |     1    |

Portanto:

$$
y[0]=1
$$

$$
y[1]=3
$$

$$
y[2]=3
$$

e:

$$
y[3]=1
$$

O exemplo demonstra que a resposta do sistema pode ser determinada diretamente a partir da entrada e da resposta ao impulso, sem a necessidade de conhecer novamente toda a transformação interna do sistema.

## Interpretação

A resposta ao impulso:

$$
h[n]=\delta[n]+\delta[n-1]
$$

faz com que cada amostra da entrada contribua para duas posições consecutivas da saída.

Por exemplo, a amostra:

$$
x[1]=2
$$

produz uma contribuição igual a $2$ em $y[1]$ e outra contribuição igual a $2$ em $y[2]$.

A saída final é formada pela soma de todas essas contribuições.


---

:::: {include} ./simulacao/simulacao_sistemas_lti.ipynb
::::

---

# Resultados

A aplicação da convolução entre a entrada $x[n]$ e a resposta ao impulso $h[n]$ produz a sequência:

$$
y[n]
=
\delta[n]
+
3\delta[n-1]
+
3\delta[n-2]
+
\delta[n-3]
$$

Os valores numéricos obtidos são:

| $n$ | $x[n]$ | $h[n]$ | $y[n]$ |
| :---: | :------: | :------: | :------: |
|   0   |     1    |     1    |     1    |
|   1   |     2    |     1    |     3    |
|   2   |     1    |     0    |     3    |
|   3   |     0    |     0    |     1    |

A saída apresenta quatro amostras não nulas, com amplitudes:

$$
1,\quad 3,\quad 3,\quad 1
$$

O resultado computacional obtido pela função `np.convolve()` deve coincidir com o resultado calculado analiticamente.

Os gráficos da simulação permitem observar separadamente a entrada, a resposta ao impulso e a saída produzida pela convolução.

A entrada possui três amostras não nulas, enquanto a resposta ao impulso possui duas. Como consequência da convolução, a saída possui quatro amostras não nulas.

---

# Discussão

## Relação entre Linearidade e Invariância no Tempo

O exemplo utiliza um sistema LTI, portanto a resposta a qualquer combinação de sinais pode ser determinada a partir da resposta ao impulso.

A linearidade permite decompor uma entrada complexa em componentes mais simples e calcular a resposta de cada componente separadamente.

Já a invariância no tempo permite determinar a resposta a um impulso deslocado a partir de uma simples versão deslocada de $h[n]$:

$$
T\{\delta[n-k]\}
=
h[n-k]
$$

Essas duas propriedades são fundamentais para a caracterização do sistema.

## Importância da Resposta ao Impulso

A resposta ao impulso funciona como uma descrição característica do comportamento de um sistema LTI.

Ao conhecer:

$$
h[n]
$$

é possível determinar a saída para qualquer entrada $x[n]$ por meio da convolução:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

Isso elimina a necessidade de determinar individualmente a resposta do sistema para cada novo sinal de entrada.

## Decomposição em Impulsos

A representação:

$$
x[n]
=
\sum_{k=-\infty}^{\infty}
x[k]\delta[n-k]
$$

mostra que qualquer sequência discreta pode ser interpretada como uma soma de impulsos deslocados e ponderados pelas respectivas amplitudes.

Para um sistema LTI, cada um desses impulsos produz uma resposta correspondente:

$$
x[k]\delta[n-k]
\rightarrow
x[k]h[n-k]
$$

A saída total é obtida pela soma dessas respostas:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

Essa é justamente a operação de convolução.

## Interpretação do Resultado da Simulação

Os valores obtidos na simulação confirmam o resultado analítico.

A saída:

$$
y[n]=[1,3,3,1]
$$

surge da sobreposição das versões deslocadas da resposta ao impulso produzidas por cada amostra da entrada.

Assim, a simulação demonstra de forma prática como a resposta ao impulso pode ser utilizada para caracterizar o comportamento de um sistema LTI.

## Importância dos Sistemas LTI

Os sistemas LTI possuem grande importância porque permitem transformar um problema de análise de sistemas em uma operação de convolução.

A partir de uma única característica, $h[n]$, é possível determinar a resposta do sistema para diferentes entradas. Essa propriedade torna os sistemas LTI uma ferramenta fundamental no estudo de filtros digitais, processamento de áudio, imagens, telecomunicações e diversas outras aplicações de processamento de sinais.

---

# Conclusões

O estudo dos sistemas LTI permitiu compreender a relação entre linearidade, invariância no tempo e resposta ao impulso.

Foi demonstrado que um sistema LTI pode ser caracterizado por sua resposta ao impulso $h[n]$. A representação de uma sequência como uma soma de impulsos deslocados, combinada com as propriedades de linearidade e invariância no tempo, conduz naturalmente à expressão da convolução discreta:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

O exemplo analisado mostrou que a saída pode ser obtida pela combinação das versões deslocadas e ponderadas da resposta ao impulso. A simulação computacional confirmou os resultados obtidos analiticamente.

Dessa forma, a resposta ao impulso fornece uma representação compacta e completa do comportamento de um sistema LTI, permitindo determinar sua resposta para diferentes sinais de entrada por meio da convolução discreta.