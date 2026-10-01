# Sistemas Discretos

---

# Resumo Conceitual

Um sistema discreto é uma formulação matemática ou computacional que processa uma sequência de entrada $x[n]$ para gerar uma sequência de saída $y[n]$. Essa transformação é denotada como:

$$
y[n] = T\{x[n]\}
$$

Para compreender profundamente a dinâmica desses sistemas, avaliamos cinco propriedades essenciais:

## Memória

Classifica o sistema quanto à sua dependência de informações passadas ou futuras. Se a saída no instante $n$ depende exclusivamente da entrada no mesmo instante $n$, o sistema é sem memória (ou estático). Se depende de valores defasados (atrasos) ou antecipados (avanços), possui memória (ou é dinâmico).

## Causalidade

Determina a viabilidade física de implementação em tempo real. Um sistema é causal se a saída $y[n_0]$ depender apenas de amostras presentes e passadas $x[k]$, onde $k \leq n_0$. Sistemas que exigem informações futuras, isto é, $k > n_0$, são não causais.

## Linearidade (Superposição)

Um sistema é linear se obedece rigorosamente ao princípio da superposição, que engloba os axiomas de aditividade e homogeneidade (escalonamento). A resposta a uma combinação linear de entradas deve ser equivalente à combinação linear das saídas individuais.

## Invariância no Tempo

O sistema é invariante no tempo se suas características dinâmicas não se alteram ao longo do tempo. Um deslocamento temporal na entrada $x[n-n_0]$ resulta em um deslocamento idêntico na saída $y[n-n_0]$, sem alterar o perfil do sinal.

## Estabilidade BIBO (Bounded-Input, Bounded-Output)

Avalia a limitação e segurança operacional do sistema. Um sistema é BIBO estável se qualquer entrada limitada em amplitude produzir uma saída também limitada.

## A Importância dos Sistemas LTI

Quando um sistema atende simultaneamente aos critérios de Linearidade e Invariância no Tempo (LTI), ele pode ser completamente caracterizado por uma única resposta fundamental: a sua resposta ao impulso:

$$
h[n] = T\{\delta[n]\}
$$

Para qualquer entrada arbitrária $x[n]$, a saída é obtida através da operação matemática de convolução discreta:

$$
y[n] = x[n] * h[n]
$$

ou, equivalentemente,

$$
y[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]
$$

---

# Formulação Matemática e Provas Formais

Para analisar analiticamente um operador $T{\cdot}$, aplicam-se as seguintes condições formais:

## Memória

Verifica-se se existe dependência temporal para $n \neq n_0$. Se:

$$
y[n_0] = f(x[n_0])
$$

o sistema é sem memória.

## Causalidade

Avalia-se o suporte temporal. Se $y[n_0]$ depende de $x[k]$ para algum $k > n_0$, o sistema é não causal.

## Linearidade

Sejam $x_1[n] \rightarrow y_1[n]$ e $x_2[n] \rightarrow y_2[n]$. O sistema é linear se, e somente se:

$$
T\{a \cdot x_1[n] + b \cdot x_2[n]\}
=
a \cdot T\{x_1[n]\}
+
b \cdot T\{x_2[n]\}
$$

ou:

$$
T\{a \cdot x_1[n] + b \cdot x_2[n]\}
=
a \cdot y_1[n] + b \cdot y_2[n],
\quad \forall a,b \in \mathbb{C}
$$

## Invariância no Tempo

1. Define-se a resposta a uma entrada atrasada:

$$
y_d[n] = T\{x[n-n_0]\}
$$

2. Atrasar a saída original $y[n]$ em $n_0$:

$$
y[n-n_0]
$$

3. O sistema é invariante no tempo se, e somente se:

$$
y_d[n] = y[n-n_0],
\quad \forall n_0 \in \mathbb{Z}
$$

## Estabilidade BIBO

Se a entrada for limitada tal que:

$$
|x[n]| \leq B_x < \infty,
\quad \forall n
$$

o sistema é BIBO estável se existir uma constante finita $B_y$ tal que:

$$
|y[n]| \leq B_y < \infty,
\quad \forall n
$$

Para sistemas LTI, a estabilidade BIBO é equivalente à somabilidade absoluta da resposta ao impulso:

$$
\sum_{k=-\infty}^{\infty} |h[k]| < \infty
$$

---

# Exemplos e Investigação Analítica

Análise rigorosa das propriedades para cinco sistemas fundamentais.

## Sistema A: $y[n] = 2x[n]$ (Amplificador Ideal)

### Memória

A saída em $n$ depende exclusivamente de $x[n]$. Sem memória.

### Causalidade

Depende apenas da amostra presente $x[n]$. Causal.

### Linearidade

$$
\begin{aligned}
T\{a x_1[n] + b x_2[n]\}
&= 2(a x_1[n] + b x_2[n]) \\
&= a(2x_1[n]) + b(2x_2[n]) \\
&= a y_1[n] + b y_2[n]
\end{aligned}
$$

Portanto, o sistema é linear.

### Invariância

Entrada atrasada:

$$
y_d[n] = 2x[n-n_0]
$$

Saída atrasada:

$$
y[n-n_0] = 2x[n-n_0]
$$

Como:

$$
y_d[n] = y[n-n_0]
$$

o sistema é invariante no tempo.

### Estabilidade BIBO

Dado:

$$
|x[n]| \leq B_x
$$

temos:

$$
|y[n]| = 2|x[n]| \leq 2B_x
$$

Definindo:

$$
B_y = 2B_x < \infty
$$

o sistema é BIBO estável.

## Sistema B: $y[n] = x[n] + x[n-1]$ (Filtro Média/FIR)

### Memória

Avalia o estado passado $x[n-1]$. Portanto, possui memória.

### Causalidade

Depende do instante presente ($n$) e passado ($n-1$). Não acessa o futuro. Portanto, é causal.

### Linearidade

$$
\begin{aligned}
T\{a x_1[n] + b x_2[n]\}
&= [a x_1[n] + b x_2[n]]
+ [a x_1[n-1] + b x_2[n-1]] \\
&= a(x_1[n] + x_1[n-1])
+ b(x_2[n] + x_2[n-1]) \\
&= a y_1[n] + b y_2[n]
\end{aligned}
$$

Portanto, o sistema é linear.

### Invariância

Entrada atrasada:

$$
y_d[n]
=
x[n-n_0] + x[(n-n_0)-1]
$$

Simplificando:

$$
y_d[n]
=
x[n-n_0] + x[n-n_0-1]
$$

Saída atrasada:

$$
y[n-n_0]
=
x[n-n_0] + x[n-n_0-1]
$$

Como:

$$
y_d[n] = y[n-n_0]
$$

o sistema é invariante no tempo.

### Estabilidade BIBO

Pela desigualdade triangular:

$$
|y[n]|
\leq
|x[n]| + |x[n-1]|
$$

Como:

$$
|x[n]| \leq B_x
$$

temos:

$$
|y[n]| \leq B_x + B_x = 2B_x < \infty
$$

Portanto, o sistema é BIBO estável.

## Sistema C: $y[n] = x^2[n]$ (Operador Quadrático)

### Memória

Avalia apenas $x[n]$ no ponto atual. Portanto, é sem memória.

### Causalidade

Não requer amostras futuras. Portanto, é causal.

### Linearidade

Testando a homogeneidade com um escalar $a \neq 1$:

$$
T\{a x[n]\}
=
(ax[n])^2
=
a^2x^2[n]
$$

Enquanto:

$$
aT\{x[n]\}
=
ax^2[n]
$$

Como:

$$
a^2x^2[n] \neq ax^2[n]
$$

em geral, o sistema viola a propriedade de homogeneidade. Portanto, é não linear.

### Invariância

Entrada atrasada:

$$
y_d[n]
=
(x[n-n_0])^2
$$

Saída atrasada:

$$
y[n-n_0]
=
(x[n-n_0])^2
$$

Como:

$$
y_d[n] = y[n-n_0]
$$

o sistema é invariante no tempo.

### Estabilidade BIBO

Dado:

$$
|x[n]| \leq B_x
$$

temos:

$$
|y[n]|
=
|x[n]|^2
\leq
B_x^2
$$

Definindo:

$$
B_y = B_x^2 < \infty
$$

o sistema é BIBO estável.

## Sistema D: $y[n] = x[n+1]$ (Avanço Temporal)

### Memória

O índice temporal difere de $n$. Portanto, o sistema possui memória.

### Causalidade

Para calcular $y[0]$, o sistema necessita de $x[1]$, que é uma amostra futura. Portanto, é não causal.

### Linearidade

$$
\begin{aligned}
T\{a x_1[n] + b x_2[n]\}
&=
a x_1[n+1] + b x_2[n+1] \\
&=
a y_1[n] + b y_2[n]
\end{aligned}
$$

Portanto, o sistema é linear.

### Invariância

Entrada atrasada:

$$
y_d[n]
=
x[(n-n_0)+1]
=
x[n-n_0+1]
$$

Saída atrasada:

$$
y[n-n_0]
=
x[(n-n_0)+1]
=
x[n-n_0+1]
$$

Como:

$$
y_d[n] = y[n-n_0]
$$

o sistema é invariante no tempo.

### Estabilidade BIBO

Temos:

$$
|y[n]|
=
|x[n+1]|
\leq
B_x
<
\infty
$$

Portanto, o sistema é BIBO estável.

## Sistema E: $y[n] = n \cdot x[n]$ (Modulador Rampa)

### Memória

O sinal $x[n]$ é avaliado estritamente no instante $n$. O termo $n$ é apenas um coeficiente multiplicativo variante no tempo. Portanto, o sistema é sem memória.

### Causalidade

A saída em $n$ depende unicamente de $x[n]$. Portanto, é causal.

### Linearidade

$$
\begin{aligned}
T\{a x_1[n] + b x_2[n]\}
&=
n(a x_1[n] + b x_2[n]) \\
&=
a(nx_1[n]) + b(nx_2[n]) \\
&=
a y_1[n] + b y_2[n]
\end{aligned}
$$

Portanto, o sistema é linear.

### Invariância

Entrada atrasada:

$$
y_d[n]
=
n \cdot x[n-n_0]
$$

Saída atrasada:

$$
y[n-n_0]
=
(n-n_0)x[n-n_0]
$$

Como, em geral:

$$
y_d[n] \neq y[n-n_0]
$$

devido ao fator $n \neq n-n_0$, o sistema é variante no tempo.

### Estabilidade BIBO

Considere uma entrada limitada:

$$
x[n] = u[n]
$$

onde $u[n]$ é o degrau unitário e:

$$
B_x = 1
$$

Para $n \geq 0$, a saída será:

$$
y[n] = n
$$

Conforme:

$$
n \rightarrow \infty
$$

temos:

$$
y[n] \rightarrow \infty
$$

Portanto, não existe uma constante finita $B_y$ que limite a saída. O sistema é BIBO instável.

---

:::: {include} ./simulacao/simulacao_sistemas_discretos.ipynb
::::

---

# Resultados

A simulação foi realizada considerando o vetor de tempo discreto \(n \in [-2,7]\) e a sequência de entrada definida como um pulso unitário no intervalo \(0 \leq n \leq 5\). A partir dessa entrada, foram calculadas as respostas dos cinco sistemas analisados.

A tabela a seguir apresenta os valores numéricos obtidos para a entrada e para cada sistema:

| \(n\) | Entrada \(x[n]\) | A: \(2x[n]\) | B: \(x[n]+x[n-1]\) | C: \(x^2[n]\) | D: \(x[n+1]\) | E: \(n \cdot x[n]\) |
| :---- | :--------------- | :----------- | :----------------- | :------------ | :------------ | :------------------ |
| -2    | 0.0              | 0.0          | 0.0                | 0.0           | 0.0           | 0.0                 |
| -1    | 0.0              | 0.0          | 0.0                | 0.0           | 1.0           | 0.0                 |
| 0     | 1.0              | 2.0          | 1.0                | 1.0           | 1.0           | 0.0                 |
| 1     | 1.0              | 2.0          | 2.0                | 1.0           | 1.0           | 1.0                 |
| 2     | 1.0              | 2.0          | 2.0                | 1.0           | 1.0           | 2.0                 |
| 3     | 1.0              | 2.0          | 2.0                | 1.0           | 1.0           | 3.0                 |
| 4     | 1.0              | 2.0          | 2.0                | 1.0           | 1.0           | 4.0                 |
| 5     | 1.0              | 2.0          | 2.0                | 1.0           | 0.0           | 5.0                 |
| 6     | 0.0              | 0.0          | 1.0                | 0.0           | 0.0           | 0.0                 |
| 7     | 0.0              | 0.0          | 0.0                | 0.0           | 0.0           | 0.0                 |

Os resultados numéricos confirmam os comportamentos previstos pelas formulações matemáticas dos sistemas. O Sistema A produz uma amplificação constante da entrada, enquanto o Sistema B apresenta uma contribuição adicional associada ao atraso. O Sistema C mantém os valores da sequência utilizada na simulação, devido às características particulares do sinal de entrada. O Sistema D antecipa temporalmente a sequência, enquanto o Sistema E apresenta um ganho que varia de acordo com o índice discreto \(n\).

Os gráficos obtidos na simulação permitem visualizar esses comportamentos de forma complementar aos valores apresentados na tabela.

# Discussão

## Memória no Sistema B

O Sistema B é definido por:

$$
y[n] = x[n] + x[n-1]
$$

A presença do termo \(x[n-1]\) faz com que a saída dependa não apenas da amostra atual da entrada, mas também de uma amostra anterior. Portanto, o sistema possui memória.

Esse comportamento também explica a permanência de uma contribuição na saída quando a entrada já passou a zero. O sistema mantém, por meio do atraso, a influência da amostra anterior durante um instante adicional. Essa característica é comum em sistemas de processamento digital de sinais, especialmente em filtros que utilizam amostras anteriores da entrada.

## Causalidade no Sistema D

O Sistema D é definido por:

$$
y[n] = x[n+1]
$$

Nesse caso, a saída no instante \(n\) depende de uma amostra futura da entrada. Portanto, o sistema é não causal.

Essa característica impede sua implementação direta em aplicações de tempo real nas quais as amostras futuras ainda não estão disponíveis. Entretanto, a operação pode ser realizada em processamento off-line, quando toda a sequência de entrada já está armazenada, como ocorre em determinadas aplicações de análise de sinais, imagens e dados históricos.

## Não linearidade no Sistema C

O Sistema C é definido por:

$$
y[n] = x^2[n]
$$

A operação de elevação ao quadrado caracteriza uma transformação não linear. Na simulação realizada, os valores da entrada pertencem ao conjunto \(\{0,1\}\), fazendo com que a operação produza os mesmos valores:

$$
0^2 = 0
$$

e

$$
1^2 = 1.
$$

Por isso, apesar de o sistema ser não linear, essa característica não produz uma alteração numérica evidente para a sequência específica utilizada.

Para sinais com amplitudes diferentes de \(0\) e \(1\), entretanto, a operação modifica a forma do sinal. Além disso, quando aplicada a sinais com componentes senoidais, a operação de elevação ao quadrado pode produzir novas componentes espectrais, incluindo componentes harmônicas.

## Invariância temporal e estabilidade no Sistema E

O Sistema E é definido por:

$$
y[n] = n \cdot x[n]
$$

Nesse sistema, o valor da saída depende explicitamente do índice \(n\). Isso significa que o ganho aplicado à entrada varia ao longo do tempo discreto.

Essa dependência faz com que o sistema não seja invariante no tempo. Além disso, considerando uma entrada limitada que permaneça diferente de zero para valores crescentes de \(n\), o fator \(n\) pode fazer com que a saída cresça sem limite. Dessa forma, o sistema não satisfaz a condição de estabilidade BIBO.

O exemplo demonstra que as propriedades de linearidade, causalidade, memória, invariância no tempo e estabilidade BIBO são características distintas. Um sistema pode satisfazer algumas dessas propriedades e não satisfazer outras, sendo necessário analisar cada propriedade individualmente.

# Conclusões

A análise dos cinco sistemas permitiu verificar, por meio da formulação matemática e da simulação computacional, como diferentes operações modificam uma sequência discreta.

O Sistema A demonstrou uma alteração de amplitude sem introduzir dependência temporal adicional. O Sistema B evidenciou o efeito da memória por utilizar uma amostra anterior da entrada. O Sistema C mostrou o comportamento de uma transformação não linear, embora seus efeitos tenham sido pouco perceptíveis devido aos valores específicos da sequência utilizada. O Sistema D demonstrou a relação entre deslocamento temporal e causalidade, enquanto o Sistema E evidenciou a influência de um ganho dependente do índice ($n$), afetando a invariância temporal e a estabilidade BIBO.

Dessa forma, os resultados da simulação estão de acordo com as propriedades determinadas pela análise matemática dos sistemas. A combinação entre a análise teórica, os valores numéricos e a representação gráfica permite compreender de maneira mais clara o comportamento de sistemas discretos e a importância de avaliar suas propriedades individualmente.
    