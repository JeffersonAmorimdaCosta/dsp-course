# Frequência e Exponenciais Complexas

---

# Resumo conceitual

Os sinais oscilatórios podem ser representados por funções senoidais e exponenciais complexas, que são ferramentas fundamentais no Processamento Digital de Sinais. Uma senoide discreta é caracterizada por três parâmetros principais: amplitude, frequência angular e fase. A amplitude determina o valor máximo da oscilação, a frequência angular indica a rapidez com que o sinal varia ao longo das amostras e a fase representa o deslocamento inicial da senoide.

A relação entre senoides e exponenciais complexas é estabelecida pela relação de Euler, que permite expressar funções trigonométricas utilizando números complexos. Essa representação facilita operações matemáticas e a análise de sinais, especialmente no estudo das transformadas de Fourier.

Uma exponencial complexa pode ser interpretada como um sinal cuja parte real corresponde a um cosseno e cuja parte imaginária corresponde a um seno. Dessa forma, as duas componentes podem ser analisadas separadamente para compreender o comportamento do sinal no plano complexo.

---

# Formulação matemática

## Representação de uma senoide discreta

Uma senoide discreta pode ser representada por:

$$
x[n] = A\cos(\omega_0 n+\phi)
$$

Em que:

* $x[n]$: valor do sinal na amostra $n$;
* $A$: amplitude do sinal;
* $\omega_0$: frequência angular em radianos por amostra;
* $n$: índice da amostra;
* $\phi$: fase inicial, em radianos.

A amplitude determina a intensidade da oscilação. A frequência angular controla a variação do sinal entre as amostras, enquanto a fase modifica a posição inicial da senoide no eixo horizontal.

A frequência angular está relacionada à frequência em ciclos por amostra pela expressão:

$$
\omega_0 = 2\pi f
$$

Quando a frequência é expressa em hertz e existe uma frequência de amostragem $f_s$, a relação é:

$$
\omega_0 = 2\pi\frac{f}{f_s}
$$

## Relação de Euler

A relação de Euler estabelece uma conexão entre as funções trigonométricas e as exponenciais complexas:

$$
e^{j\theta}=\cos(\theta)+j\sin(\theta)
$$

Em que:

* $e$: número de Euler;
* $j$: unidade imaginária, com $j^2=-1$;
* $\theta$: ângulo em radianos;
* $\cos(\theta)$: parte real;
* $\sin(\theta)$: parte imaginária.

Aplicando essa relação a uma frequência angular discreta:

$$
e^{j\omega_0 n}=
\cos(\omega_0 n)+j\sin(\omega_0 n)
$$

Assim, uma exponencial complexa reúne duas componentes oscilatórias: uma real e outra imaginária.

## Representação de cosseno e seno por exponenciais complexas

A partir da relação de Euler, podemos obter as expressões:

$$
\cos(\omega_0 n)=
\frac{1}{2}
\left(
e^{j\omega_0 n}+e^{-j\omega_0 n}
\right)
$$

E:

$$
\sin(\omega_0 n)=
\frac{1}{2j}
\left(
e^{j\omega_0 n}-e^{-j\omega_0 n}
\right)
$$

Portanto, uma senoide pode ser representada pela combinação de duas exponenciais complexas com frequências angulares opostas.

## Representação complexa de uma senoide com amplitude e fase

Considerando uma senoide com amplitude $A$ e fase inicial $\phi$, sua representação complexa pode ser escrita como:

$$
z[n]=A e^{j(\omega_0 n+\phi)}
$$

Aplicando a relação de Euler:

$$
z[n]=A\cos(\omega_0 n+\phi)
+jA\sin(\omega_0 n+\phi)
$$

Consequentemente:

$$
\operatorname{Re}\{z[n]\}
=A\cos(\omega_0 n+\phi)
$$

$$
\operatorname{Im}\{z[n]\}
=A\sin(\omega_0 n+\phi)
$$

A parte real corresponde à senoide cossenoidal, enquanto a parte imaginária corresponde à senoide senoidal.

---

# Exemplo

Considere o seguinte sinal discreto:

$$
x[n]=2\cos\left(\frac{\pi}{4}n+\frac{\pi}{6}\right)
$$

Nesse exemplo, os parâmetros são:

* Amplitude: $A=2$;
* Frequência angular: $\omega_0=\frac{\pi}{4}$ rad/amostra;
* Fase inicial: $\phi=\frac{\pi}{6}$ rad.

Para a amostra $n=0$, temos:

$$
x[0]=2\cos\left(\frac{\pi}{4}\cdot 0+
\frac{\pi}{6}\right)
$$

$$
x[0]=2\cos\left(\frac{\pi}{6}\right)
$$

$$
x[0]=\sqrt{3}\approx 1{,}732
$$

A representação complexa correspondente é:

$$
z[n]=2e^{j\left(\frac{\pi}{4}n+\frac{\pi}{6}\right)}
$$

Sua parte real representa o sinal original, enquanto a parte imaginária representa a componente senoidal associada.

Esse exemplo demonstra que a exponencial complexa permite representar simultaneamente duas componentes oscilatórias, mantendo as informações de amplitude, frequência e fase.

---

:::: {include} ./simulacao/simulacao_frequencia_exponencial_complexa.ipynb
::::

---

# Resultados gráficos

A execução da simulação produz cinco conjuntos de representações gráficas, permitindo observar diferentes características dos sinais.

## Senoides com diferentes frequências

O primeiro conjunto apresenta três senoides com frequências angulares de $\frac{\pi}{8}$, $\frac{\pi}{4}$ e $\frac{\pi}{2}$ radianos por amostra.

Espera-se observar que o aumento da frequência angular provoca mais oscilações em uma mesma quantidade de amostras. A senoide de menor frequência apresenta variações mais lentas, enquanto a de maior frequência apresenta oscilações mais rápidas.

## Influência da fase

O segundo gráfico apresenta senoides com a mesma amplitude e frequência, mas com fases iniciais diferentes: $0$, $\frac{\pi}{4}$ e $\frac{\pi}{2}$.

As curvas mantêm a mesma amplitude e o mesmo padrão de oscilação, porém apresentam deslocamentos entre si. Isso demonstra que a fase modifica a posição inicial do sinal sem alterar sua frequência ou amplitude.

## Influência da amplitude

O terceiro gráfico compara sinais com amplitudes de $0{,}5$, $1{,}0$ e $2{,}0$.

Observa-se que o aumento da amplitude amplia os valores máximos e mínimos da senoide. Apesar dessa alteração, a frequência e a fase permanecem constantes.

## Partes real e imaginária

O quarto conjunto apresenta separadamente a parte real e a parte imaginária da exponencial complexa.

A parte real possui comportamento de cosseno, enquanto a parte imaginária possui comportamento de seno. Ambas apresentam a mesma frequência angular, mas possuem uma diferença de fase de $\frac{\pi}{2}$.

## Representação no plano complexo

O último gráfico apresenta os valores da exponencial complexa no plano formado pelos eixos real e imaginário.

Como a amplitude utilizada é igual a 1, os pontos pertencem à circunferência unitária. Conforme o índice das amostras aumenta, os pontos percorrem essa circunferência, representando a evolução da fase da exponencial complexa.

---

# Interpretação

Os resultados demonstram que amplitude, frequência e fase são parâmetros independentes que determinam características específicas de uma senoide discreta.

A amplitude controla a intensidade da oscilação, enquanto a frequência angular determina a rapidez com que ocorrem as variações entre as amostras. A fase, por sua vez, estabelece o deslocamento inicial do sinal, sem modificar sua amplitude ou frequência.

A representação por exponenciais complexas permite reunir as componentes cossenoidal e senoidal em uma única expressão matemática. A parte real reproduz o comportamento do cosseno, enquanto a parte imaginária representa o seno.

A visualização no plano complexo também evidencia que uma exponencial complexa de amplitude constante percorre uma circunferência de raio igual à amplitude. O ângulo associado a cada amostra corresponde à fase instantânea do sinal.

Dessa maneira, a simulação confirma as relações matemáticas apresentadas e demonstra como a representação complexa facilita a análise de sinais oscilatórios.

---

# Discussão crítica

A representação de sinais por exponenciais complexas é uma ferramenta importante no Processamento Digital de Sinais, pois simplifica operações matemáticas e estabelece a base para técnicas de análise no domínio da frequência, como as Transformadas de Fourier.

A utilização das partes real e imaginária permite compreender que uma exponencial complexa não representa apenas uma operação matemática abstrata, mas uma forma compacta de descrever duas componentes oscilatórias relacionadas.

Entretanto, é importante considerar que, em sinais discretos, frequências angulares separadas por múltiplos de $2\pi$ produzem as mesmas sequências exponenciais. Além disso, uma senoide discreta somente será periódica quando a razão entre sua frequência angular e $2\pi$ for racional.

Outro aspecto importante é que a análise realizada considera sinais ideais, sem a presença de ruídos ou outras interferências. Em aplicações reais, esses fatores podem modificar os sinais observados e exigir técnicas adicionais de processamento.

Portanto, o estudo das frequências e exponenciais complexas fornece uma base matemática essencial para compreender as próximas etapas da análise espectral, especialmente o desenvolvimento das Transformadas de Fourier, que utilizam exponenciais complexas para representar e analisar sinais em diferentes frequências.