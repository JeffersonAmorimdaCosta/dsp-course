# Sequências Fundamentais

## 1. Resumo conceitual

Em Processamento Digital de Sinais (PDS), uma sequência é uma representação matemática de um sinal definido em instantes discretos. Diferentemente dos sinais de tempo contínuo, que são definidos para qualquer instante de tempo, uma sequência é representada por valores associados a índices inteiros, normalmente denotados por $n$.

As sequências fundamentais possuem grande importância na análise e na representação de sistemas discretos. Entre as principais estão o **impulso unitário**, o **degrau unitário**, a **sequência exponencial**, a **senoide discreta** e a **exponencial complexa**. Essas sequências podem ser utilizadas individualmente ou combinadas para representar sinais mais complexos.

O **impulso unitário** é uma das sequências mais importantes da análise de sistemas discretos. Ele apresenta valor unitário apenas no instante $n=0$ e valor nulo nos demais instantes. Uma de suas propriedades fundamentais permite representar qualquer sequência como uma soma ponderada de impulsos deslocados.

O **degrau unitário** apresenta valor igual a um a partir do instante $n=0$ e zero para índices negativos. Essa sequência está diretamente relacionada ao impulso unitário, uma vez que o impulso pode ser obtido pela diferença entre dois degraus consecutivos.

A **sequência exponencial** é caracterizada por valores que variam de acordo com uma potência da constante $a$. Dependendo do valor dessa constante, a sequência pode apresentar crescimento, decaimento, comportamento constante ou alternância de sinais.

A **senoide discreta** é uma sequência periódica que pode ser utilizada para representar oscilações em sistemas discretos. Seu comportamento é determinado principalmente pela amplitude, frequência angular e fase.

Por fim, a **exponencial complexa** constitui uma representação especialmente importante das senoides. Por meio da identidade de Euler, uma exponencial complexa pode ser escrita como uma combinação de uma senoide cossenoidal e uma senoide senoidal. Essa representação é fundamental para o estudo de ferramentas de análise espectral, como a Transformada de Fourier.

---

## 2. Formulação matemática

### 2.1 Impulso unitário

O impulso unitário discreto, também denominado **delta de Kronecker**, é definido por

$$
\delta[n] =
\begin{cases}
1, & n = 0,\\
0, & n \neq 0.
\end{cases}
$$

Portanto, o impulso possui apenas uma amostra diferente de zero. Essa amostra está localizada na posição $n=0$.

Uma propriedade fundamental do impulso é a propriedade de amostragem ou seleção:

$$
x[n] =
\sum_{k=-\infty}^{+\infty} x[k]\delta[n-k].
$$

Essa expressão mostra que uma sequência arbitrária $x[n]$ pode ser reconstruída a partir de impulsos deslocados.

Para compreender essa propriedade, considere um determinado valor de $n$. O termo

$$
\delta[n-k]
$$

será igual a 1 somente quando

$$
n-k=0,
$$

ou seja,

$$
k=n.
$$

Para todos os demais valores de $k$, o impulso será igual a zero. Consequentemente, na soma

$$
\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k],
$$

todos os termos são eliminados, exceto aquele correspondente a $k=n$. O resultado é, portanto,

$$
x[n]\delta[0]=x[n].
$$

Assim, uma sequência pode ser interpretada como uma soma de impulsos deslocados, em que cada impulso possui como coeficiente o valor da sequência no respectivo instante:

$$
x[n]
=
\cdots
+x[-1]\delta[n+1]
+x[0]\delta[n]
+x[1]\delta[n-1]
+\cdots.
$$

Essa propriedade é fundamental na análise de sistemas discretos, principalmente na definição da resposta ao impulso e na operação de convolução.

---

### 2.2 Degrau unitário

O degrau unitário discreto é definido por

$$
u[n] =
\begin{cases}
1, & n \geq 0,\\
0, & n < 0.
\end{cases}
$$

Dessa forma, a sequência apresenta valor zero para todos os índices negativos e valor unitário a partir de $n=0$.

O degrau unitário pode ser utilizado para representar sinais que passam a existir ou assumir determinado comportamento a partir de um instante específico.

Existe uma relação direta entre o degrau e o impulso:

$$
\delta[n] = u[n] - u[n-1].
$$

Para verificar essa relação, considere três situações.

Para $n<0$,

$$
u[n]=0
$$

e

$$
u[n-1]=0.
$$

Logo,

$$
u[n]-u[n-1]=0.
$$

Para $n=0$,

$$
u[0]=1
$$

e

$$
u[-1]=0.
$$

Assim,

$$
u[0]-u[-1]=1.
$$

Para $n>0$,

$$
u[n]=1
$$

e

$$
u[n-1]=1.
$$

Consequentemente,

$$
u[n]-u[n-1]=0.
$$

Portanto, a diferença entre dois degraus consecutivos produz exatamente um impulso unitário.

---

### 2.3 Sequência exponencial

Uma sequência exponencial real pode ser representada por

$$
x[n]=a^n,
$$

em que $a$ é uma constante real e $n$ representa o índice discreto da sequência.

O comportamento da sequência depende diretamente do valor de $a$.

Para

$$
a>1,
$$

a sequência apresenta crescimento exponencial à medida que $n$ aumenta. Por exemplo,

$$
x[n]=2^n.
$$

Nesse caso, os valores para índices crescentes são

$$
\ldots,\frac{1}{4},\frac{1}{2},1,2,4,8,16,\ldots
$$

Para

$$
0<a<1,
$$

a sequência apresenta decaimento exponencial. Por exemplo,

$$
x[n]=\left(\frac{1}{2}\right)^n.
$$

Nesse caso, para índices crescentes, os valores são

$$
\ldots,4,2,1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\ldots
$$

Para

$$
a=1,
$$

tem-se

$$
x[n]=1^n=1,
$$

resultando em uma sequência constante.

Para

$$
-1<a<0,
$$

a sequência apresenta decaimento de amplitude acompanhado por alternância de sinal.

Para

$$
a=-1,
$$

obtém-se

$$
x[n]=(-1)^n,
$$

que alterna entre $1$ e $-1$.

Já para

$$
a<-1,
$$

a amplitude cresce enquanto o sinal alterna entre valores positivos e negativos.

Portanto, o módulo de $a$ determina principalmente o crescimento ou decaimento da amplitude, enquanto o seu sinal determina a presença ou ausência de alternância de sinal.

---

### 2.4 Senoide discreta

Uma senoide discreta pode ser representada por

$$
x[n]=A\cos(\omega_0 n+\phi),
$$

em que:

* $A$ é a amplitude da sequência;
* $\omega_0$ é a frequência angular discreta, expressa em radianos por amostra;
* $n$ é o índice discreto;
* $\phi$ é a fase inicial, expressa em radianos.

A amplitude determina o valor máximo que a sequência pode atingir. A frequência angular controla a velocidade de oscilação da sequência ao longo dos índices. A fase determina o deslocamento da senoide em relação à origem.

A frequência angular está relacionada à frequência ordinária $f$ pela relação

$$
\omega_0=2\pi f,
$$

quando $f$ é expressa em ciclos por amostra.

Uma característica importante das senoides discretas é que frequências angulares que diferem por múltiplos inteiros de $2\pi$ produzem a mesma sequência:

$$
\omega_0
\quad\text{e}\quad
\omega_0+2\pi k,
$$

onde $k$ é um número inteiro.

Isso ocorre porque

$$
\cos[(\omega_0+2\pi k)n+\phi]
=
\cos(\omega_0 n+\phi+2\pi kn).
$$

Como $n$ e $k$ são inteiros, $2\pi kn$ corresponde a um número inteiro de períodos da função cosseno.

---

### 2.5 Exponencial complexa

A identidade de Euler estabelece a relação

$$
e^{j\theta}=\cos(\theta)+j\sin(\theta),
$$

em que $j$ representa a unidade imaginária,

$$
j^2=-1.
$$

Aplicando essa identidade a uma frequência angular $\omega$, obtém-se

$$
e^{j\omega n}
=
\cos(\omega n)+j\sin(\omega n).
$$

Essa equação mostra que uma exponencial complexa é composta por duas partes: uma componente real correspondente ao cosseno e uma componente imaginária correspondente ao seno.

A partir dessa relação, uma senoide cossenoidal pode ser obtida considerando a parte real da exponencial complexa:

$$
\cos(\omega n)=\operatorname{Re}\{e^{j\omega n}\}.
$$

Da mesma forma,

$$
\sin(\omega n)=\operatorname{Im}\{e^{j\omega n}\}.
$$

A representação complexa é particularmente útil porque permite tratar senoides por meio de operações algébricas com exponenciais. Essa propriedade simplifica significativamente a análise matemática de sistemas discretos e constitui uma das bases para o estudo da Transformada de Fourier.

Também é possível representar uma senoide real utilizando duas exponenciais complexas. Pela fórmula de Euler,

$$
\cos(\omega n)
=
\frac{e^{j\omega n}+e^{-j\omega n}}{2},
$$

enquanto

$$
\sin(\omega n)
=
\frac{e^{j\omega n}-e^{-j\omega n}}{2j}.
$$

Assim, as senoides reais podem ser interpretadas como combinações de exponenciais complexas com frequências de sinais opostos.

---

## 3. Exemplo

Para demonstrar o comportamento das principais sequências fundamentais, considere os índices

$$
n=-3,-2,-1,0,1,2,3.
$$

### 3.1 Exemplo: impulso unitário

Para o impulso unitário,

$$
x[n]=\delta[n],
$$

os valores são:

|         $n$ | -3 | -2 | -1 |  0 |  1 |  2 |  3 |
| ----------: | -: | -: | -: | -: | -: | -: | -: |
| $\delta[n]$ |  0 |  0 |  0 |  1 |  0 |  0 |  0 |

Observa-se que somente a amostra correspondente a $n=0$ possui valor igual a 1.

---

### 3.2 Exemplo: propriedade de seleção do impulso

Considere a sequência

$$
x[n]=\{2,4,6,8,10\},
$$

associada aos índices

$$
n=-2,-1,0,1,2.
$$

A representação por impulsos deslocados pode ser escrita como

$$
x[n]
=
2\delta[n+2]
+4\delta[n+1]
+6\delta[n]
+8\delta[n-1]
+10\delta[n-2].
$$

Por exemplo, para $n=1$,

$$
x[1]
=
2\delta[3]
+4\delta[2]
+6\delta[1]
+8\delta[0]
+10\delta[-1].
$$

Como

$$
\delta[0]=1
$$

e os demais impulsos são iguais a zero,

$$
x[1]=8.
$$

Dessa maneira, a combinação de impulsos deslocados reproduz exatamente os valores da sequência original.

---

### 3.3 Exemplo: degrau unitário

Para

$$
x[n]=u[n],
$$

considerando os índices de $-3$ a $3$, obtém-se:

|    $n$ | -3 | -2 | -1 |  0 |  1 |  2 |  3 |
| -----: | -: | -: | -: | -: | -: | -: | -: |
| $u[n]$ |  0 |  0 |  0 |  1 |  1 |  1 |  1 |

Agora, aplicando

$$
\delta[n]=u[n]-u[n-1],
$$

obtém-se:

|         $n$ | -3 | -2 | -1 |  0 |  1 |  2 |  3 |
| ----------: | -: | -: | -: | -: | -: | -: | -: |
|      $u[n]$ |  0 |  0 |  0 |  1 |  1 |  1 |  1 |
|    $u[n-1]$ |  0 |  0 |  0 |  0 |  1 |  1 |  1 |
| $\delta[n]$ |  0 |  0 |  0 |  1 |  0 |  0 |  0 |

O resultado confirma matematicamente a relação entre as duas sequências.

---

### 3.4 Exemplo: sequência exponencial

Considere

$$
x[n]=\left(\frac{1}{2}\right)^n.
$$

Para alguns índices, temos:

|    $n$ | -3 | -2 | -1 |  0 |   1 |    2 |     3 |
| -----: | -: | -: | -: | -: | --: | ---: | ----: |
| $x[n]$ |  8 |  4 |  2 |  1 | 0,5 | 0,25 | 0,125 |

Observa-se que, à medida que $n$ aumenta, os valores da sequência diminuem. Isso ocorre porque a base está entre 0 e 1:

$$
0<\frac{1}{2}<1.
$$

Se fosse utilizada a sequência

$$
x[n]=2^n,
$$

ocorreria o comportamento contrário para índices crescentes, caracterizado pelo crescimento exponencial.

---

### 3.5 Exemplo: senoide discreta

Considere uma senoide com

$$
A=2,
$$

$$
\omega_0=\frac{\pi}{2},
$$

e

$$
\phi=0.
$$

A sequência é dada por

$$
x[n]=2\cos\left(\frac{\pi}{2}n\right).
$$

Calculando alguns valores:

|    $n$ |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
| -----: | -: | -: | -: | -: | -: | -: | -: | -: |
| $x[n]$ |  2 |  0 | -2 |  0 |  2 |  0 | -2 |  0 |

A sequência é periódica, pois os valores se repetem a cada quatro amostras. Portanto, seu período fundamental é

$$
N_0=4.
$$

Esse exemplo mostra que a frequência angular determina diretamente a quantidade de amostras necessárias para que o padrão da senoide se repita.

---

### 3.6 Exemplo: exponencial complexa

Considere

$$
x[n]=e^{j\frac{\pi}{2}n}.
$$

Aplicando a identidade de Euler,

$$
x[n]
=
\cos\left(\frac{\pi}{2}n\right)
+
j\sin\left(\frac{\pi}{2}n\right).
$$

Para alguns valores de $n$:

| $n$ | $x[n]$ |
| --: | :----- |
|   0 | $1$    |
|   1 | $j$    |
|   2 | $-1$   |
|   3 | $-j$   |
|   4 | $1$    |

A sequência percorre sucessivamente os pontos

$$
1,\quad j,\quad -1,\quad -j
$$

no plano complexo, retornando a $1$ após quatro amostras.

A parte real dessa sequência é

$$
\operatorname{Re}\{x[n]\}
=
\cos\left(\frac{\pi}{2}n\right),
$$

enquanto a parte imaginária é

$$
\operatorname{Im}\{x[n]\}
=
\sin\left(\frac{\pi}{2}n\right).
$$

Esse exemplo demonstra de maneira direta a relação entre a exponencial complexa e as senoides. A possibilidade de representar sinais oscilatórios dessa maneira torna a exponencial complexa uma ferramenta essencial para a análise de sinais e sistemas discretos, especialmente no desenvolvimento da Transformada de Fourier.
