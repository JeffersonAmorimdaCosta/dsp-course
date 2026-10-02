# Convolução como Filtragem

---

# Resumo conceitual

Uma das principais aplicações da convolução em Processamento Digital de Sinais é a filtragem. Um filtro pode ser utilizado para modificar determinadas características de um sinal, como reduzir ruídos, suavizar variações rápidas ou destacar determinadas componentes do sinal.

Um exemplo simples é o filtro de média móvel. Nesse filtro, cada amostra da saída é calculada a partir da média de um conjunto de amostras consecutivas da entrada.

Para um filtro de média móvel com $M$ coeficientes, a resposta ao impulso é dada por

$$
h[n]
=
\frac{1}{M}
\{1,1,\ldots,1\}.
$$

Os $M$ coeficientes possuem o mesmo valor, igual a $1/M$. Dessa forma, a soma dos coeficientes é igual a 1.

Para $M=3$, por exemplo,

$$
h[n]
=
\frac{1}{3}
\{1,1,1\}.
$$

Quando esse filtro é aplicado a um sinal $x[n]$, a saída é obtida pela convolução entre o sinal de entrada e a resposta ao impulso:

$$
y[n]
=
x[n] \ast h[n].
$$

Como o filtro é causal, a saída em um determinado instante depende apenas da amostra atual e de amostras anteriores. Para $M=3$, temos

$$
y[n]
=
\frac{x[n]+x[n-1]+x[n-2]}{3}.
$$

Portanto, cada amostra da saída representa a média entre a amostra atual e as duas amostras anteriores.

O filtro de média móvel é um exemplo de filtro FIR (Finite Impulse Response), pois sua resposta ao impulso possui duração finita. Neste caso, existem apenas $M$ coeficientes diferentes de zero.

Quanto maior o valor de $M$, maior será a quantidade de amostras utilizada no cálculo da média. Isso tende a produzir uma suavização mais intensa, mas também pode alterar mais significativamente as características temporais do sinal, como transições rápidas e picos.

---

# Formulação matemática

## Filtro de média móvel

Um filtro de média móvel com $M$ coeficientes pode ser representado por

$$
h[n]
=
\frac{1}{M}
\sum_{k=0}^{M-1}
\delta[n-k].
$$

Essa expressão representa uma resposta ao impulso formada por $M$ amostras com valor $1/M$.

A saída do sistema é obtida pela convolução:

$$
y[n]
=
x[n] \ast h[n].
$$

Pela definição da convolução discreta,

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k].
$$

Substituindo a resposta ao impulso do filtro de média móvel, obtém-se

$$
y[n]
=
\frac{1}{M}
\sum_{k=0}^{M-1}
x[n-k].
$$

Portanto, a expressão geral do filtro de média móvel causal é

$$
\boxed{
y[n]
=
\frac{1}{M}
\sum_{k=0}^{M-1}
x[n-k]
}
$$

onde:

* $y[n]$ é a saída filtrada;
* $x[n]$ é o sinal de entrada;
* $M$ é o número de coeficientes do filtro;
* $k$ é o índice utilizado na soma;
* $h[n]$ é a resposta ao impulso do filtro.

### Caso $M=3$

Para três coeficientes,

$$
h[n]
=
\frac{1}{3}
\{1,1,1\}.
$$

A saída é

$$
y[n]
=
\frac{1}{3}
\left(
x[n]+x[n-1]+x[n-2]
\right).
$$

Nesse caso, cada saída é calculada utilizando três amostras da entrada.

### Caso $M=5$

Para $M=5$,

$$
h[n]
=
\frac{1}{5}
\{1,1,1,1,1\},
$$

e

$$
y[n]
=
\frac{1}{5}
\left(
x[n]+x[n-1]+x[n-2]+x[n-3]+x[n-4]
\right).
$$

Agora, cada amostra da saída utiliza cinco amostras da entrada.

### Caso $M=10$

Para $M=10$,

$$
h[n]
=
\frac{1}{10}
\{1,1,1,1,1,1,1,1,1,1\},
$$

resultando em

$$
y[n]
=
\frac{1}{10}
\sum_{k=0}^{9}x[n-k].
$$

Nesse caso, dez amostras consecutivas são utilizadas para calcular cada valor da saída.

## Relação entre $M$ e a suavização

O parâmetro $M$ controla a quantidade de amostras consideradas no cálculo da média.

Quando $M$ aumenta, a média é calculada sobre uma quantidade maior de amostras. Como consequência, variações rápidas tendem a ser reduzidas com maior intensidade.

Entretanto, um valor elevado de $M$ também pode fazer com que mudanças rápidas do sinal sejam representadas com menor intensidade ou apareçam mais suavizadas.

Assim, existe um compromisso entre:

* redução do ruído;
* preservação das variações rápidas;
* suavização do sinal;
* resposta temporal do filtro.

---

# Exemplo

Considere o sinal discreto

$$
x[n]
=
\{2,4,6,4,2\}
$$

e um filtro de média móvel com $M=3$:

$$
h[n]
=
\frac{1}{3}
\{1,1,1\}.
$$

Considerando que o primeiro elemento das sequências está associado a $n=0$, a saída pode ser calculada pela convolução

$$
y[n]
=
x[n]\ast h[n].
$$

A saída possui comprimento

$$
N_y=N_x+N_h-1.
$$

Como $N_x=5$ e $N_h=3$,

$$
N_y=5+3-1=7.
$$

A convolução resulta em

$$
y[n]
=
\left\{
\frac{2}{3},
2,
4,
\frac{14}{3},
4,
2,
\frac{2}{3}
\right\}.
$$

Entretanto, em uma implementação de média móvel causal aplicada continuamente ao sinal, normalmente considera-se a disponibilidade das amostras anteriores e uma condição inicial para as primeiras posições. Nesse caso, podemos utilizar zeros antes do início do sinal.

Assim, para $M=3$:

### $n=0$

$$
y[0]
=
\frac{x[0]+x[-1]+x[-2]}{3}
$$

Considerando $x[-1]=x[-2]=0$,

$$
y[0]
=
\frac{2+0+0}{3}
=
\frac{2}{3}.
$$

### $n=1$

$$
y[1]
=
\frac{x[1]+x[0]+x[-1]}{3}
$$

$$
y[1]
=
\frac{4+2+0}{3}
=
2.
$$

### $n=2$

$$
y[2]
=
\frac{x[2]+x[1]+x[0]}{3}
$$

$$
y[2]
=
\frac{6+4+2}{3}
=
4.
$$

### $n=3$

$$
y[3]
=
\frac{x[3]+x[2]+x[1]}{3}
$$

$$
y[3]
=
\frac{4+6+4}{3}
=
\frac{14}{3}.
$$

### $n=4$

$$
y[4]
=
\frac{x[4]+x[3]+x[2]}{3}
$$

$$
y[4]
=
\frac{2+4+6}{3}
=
4.
$$

O resultado mostra que a média móvel reduz variações bruscas, pois cada amostra da saída é influenciada por várias amostras da entrada.

---

:::: {include} ./simulacao/simulacao_convolucao_filtragem.ipynb
::::

---

# Resultados

A simulação considera três filtros de média móvel, com $M=3$, $M=5$ e $M=10$.

As respostas ao impulso são:

Para $M=3$,

$$
h_3[n]
=
\frac{1}{3}
\{1,1,1\}.
$$

Para $M=5$,

$$
h_5[n]
=
\frac{1}{5}
\{1,1,1,1,1\}.
$$

Para $M=10$,

$$
h_{10}[n]
=
\frac{1}{10}
\{1,1,1,1,1,1,1,1,1,1\}.
$$

Em todos os casos, a soma dos coeficientes é igual a 1:

$$
\sum_k h[k]=1.
$$

Essa característica faz com que o filtro preserve aproximadamente o nível médio ou componente contínua do sinal.

O sinal contaminado apresenta variações rápidas causadas pelo ruído. Após a aplicação da média móvel, essas variações são reduzidas.

Para $M=3$, a filtragem utiliza poucas amostras. Dessa forma, ocorre uma suavização moderada, mas uma parte significativa das variações rápidas do sinal ainda é preservada.

Para $M=5$, a janela utilizada é maior e a suavização se torna mais evidente. O ruído é reduzido de forma mais intensa, mas as variações rápidas começam a ser modificadas.

Para $M=10$, dez amostras são utilizadas para cada cálculo da média. O resultado tende a apresentar uma curva mais suave, com redução mais significativa das variações rápidas.

A tabela produzida pela simulação apresenta o erro RMS entre o sinal original e cada sinal filtrado. O erro RMS pode ser calculado por

$$
e_{\mathrm{RMS}}
=
\sqrt{
\frac{1}{N}
\sum_{n=0}^{N-1}
\left(x[n]-y[n]\right)^2
}.
$$

Esse valor fornece uma medida numérica da diferença entre o sinal original e o sinal após a filtragem.

---

# Discussão

A convolução permite interpretar a filtragem como uma combinação ponderada de amostras do sinal de entrada. No filtro de média móvel, todos os coeficientes possuem o mesmo peso. Assim, cada amostra da saída é calculada como uma média das amostras presentes na janela.

O parâmetro $M$ controla diretamente o tamanho dessa janela.

Para $M=3$, somente três amostras são utilizadas. O filtro apresenta menor suavização e tende a preservar melhor as variações rápidas do sinal.

Para $M=5$, a janela é maior e o efeito de suavização aumenta. O ruído é reduzido de maneira mais evidente, mas algumas mudanças rápidas do sinal também podem ser atenuadas.

Para $M=10$, a janela é ainda maior. O filtro produz uma saída mais suave, porém as características temporais do sinal são modificadas de forma mais significativa.

Esse comportamento evidencia um compromisso importante da filtragem por média móvel:

$$
\boxed{
\text{maior }M
\quad\Longrightarrow\quad
\text{maior suavização}
}
$$

mas também

$$
\boxed{
\text{maior }M
\quad\Longrightarrow\quad
\text{maior alteração das variações rápidas}
}
$$

Portanto, não existe um único valor de $M$ que seja adequado para qualquer situação. A escolha depende das características do sinal e do objetivo da filtragem.

Outro aspecto importante é que o filtro de média móvel é um filtro FIR. Sua resposta ao impulso possui duração finita, com exatamente $M$ coeficientes diferentes de zero.

Além disso, aumentar $M$ não significa simplesmente "melhorar" a filtragem. Embora o ruído possa ser reduzido de forma mais intensa, informações importantes associadas a mudanças rápidas podem ser suavizadas ou atenuadas.

A análise dos gráficos permite observar esse compromisso de forma visual: valores menores de $M$ produzem uma saída mais próxima do sinal original, enquanto valores maiores produzem uma saída mais suave.

---

# Conclusões

A convolução possui uma aplicação fundamental na filtragem de sinais. Por meio dela, é possível combinar um sinal de entrada com a resposta ao impulso de um sistema para obter a saída.

Neste estudo, foi analisado o filtro de média móvel, definido por

$$
h[n]
=
\frac{1}{M}
\{1,1,\ldots,1\}.
$$

Foram investigados os valores $M=3$, $M=5$ e $M=10$, permitindo observar como o tamanho da janela influencia o comportamento do filtro.

Os resultados mostram que o aumento de $M$ produz maior suavização do sinal e maior redução das variações rápidas. Em contrapartida, valores maiores também modificam mais intensamente as características temporais do sinal.

Dessa forma, a escolha de $M$ representa um compromisso entre redução de ruído e preservação das características do sinal. Esse comportamento demonstra, na prática, como a convolução pode ser utilizada como uma ferramenta de filtragem em sistemas de processamento digital de sinais.
