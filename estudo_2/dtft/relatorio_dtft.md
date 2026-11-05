# Transformada de Fourier em Tempo Discreto (DTFT)

---

# Resumo conceitual

A Transformada de Fourier em Tempo Discreto (DTFT) é uma ferramenta matemática utilizada para analisar o conteúdo em frequência de sinais discretos. Enquanto a representação no domínio do tempo mostra como os valores de uma sequência variam em função do índice das amostras, a DTFT permite observar quais frequências estão presentes no sinal e como elas contribuem para sua composição.

A DTFT transforma uma sequência discreta $x[n]$ em uma representação no domínio da frequência angular, identificada por $X(e^{j\omega})$. Essa representação é, em geral, uma função complexa e periódica em relação à frequência angular, com período de $2\pi$.

A análise espectral normalmente utiliza duas grandezas: o espectro de magnitude e o espectro de fase. A magnitude indica a intensidade das componentes presentes em cada frequência, enquanto a fase representa o deslocamento angular dessas componentes.

Dessa forma, a DTFT permite compreender características de um sinal que nem sempre são facilmente identificadas apenas pela observação de sua sequência no domínio do tempo, sendo fundamental para o estudo de filtragem, análise espectral e processamento digital de sinais.

---

# Formulação matemática

## Definição da DTFT

A Transformada de Fourier em Tempo Discreto de uma sequência $x[n]$ é definida por:

$$
X(e^{j\omega})=
\sum_{n=-\infty}^{+\infty}
x[n]e^{-j\omega n}
$$

Em que:

* $X(e^{j\omega})$: representação do sinal no domínio da frequência;

* $x[n]$: sequência discreta original;

* $n$: índice da amostra;

* $\omega$: frequência angular, em radianos por amostra;

* $j$: unidade imaginária;

* $e^{-j\omega n}$: exponencial complexa utilizada na transformação.

A expressão realiza uma combinação das amostras do sinal com exponenciais complexas de diferentes frequências. O resultado permite identificar a contribuição de cada frequência para a composição do sinal.

## Transformada inversa

A recuperação da sequência original a partir de sua representação espectral é realizada pela Transformada Inversa de Fourier em Tempo Discreto:

$$
x[n]=\frac{1}{2\pi}
\int_{-\pi}^{\pi}
X(e^{j\omega})e^{j\omega n}\,d\omega
$$

Essa expressão demonstra que é possível reconstruir o sinal discreto a partir de seu espectro, considerando um período completo da representação em frequência.

## Espectro de magnitude

Como a DTFT apresenta valores complexos, sua magnitude é calculada pelo módulo da representação:

$$
|X(e^{j\omega})|=
\sqrt{
\operatorname{Re}\{X(e^{j\omega})\}^{2}
+
\operatorname{Im}\{X(e^{j\omega})\}^{2}
}
$$

A magnitude representa a intensidade das componentes espectrais em cada frequência angular.

## Espectro de fase

A fase é determinada pelo argumento do número complexo:

$$
\angle X(e^{j\omega})=
\operatorname{atan2}
\left(
\operatorname{Im}\{X(e^{j\omega})\},
\operatorname{Re}\{X(e^{j\omega})\}
\right)
$$

A função $\operatorname{atan2}$ permite determinar o ângulo considerando os sinais das partes real e imaginária, identificando corretamente o quadrante.

## Periodicidade da DTFT

A DTFT apresenta periodicidade de $2\pi$ radianos por amostra:

$$
X(e^{j(\omega+2\pi)})=
X(e^{j\omega})
$$

Isso significa que o espectro se repete a cada intervalo de $2\pi$, sendo comum representar a DTFT no intervalo de $-\pi$ a $\pi$.

---

# Exemplo

Para compreender a aplicação da DTFT, considere a seguinte sequência discreta:

$$
x[n]=
\begin{cases}
1, & 0\leq n\leq 3\\
0, & \text{caso contrário}
\end{cases}
$$

A sequência possui quatro amostras iguais a 1:

$$
x[n]=[1,1,1,1]
$$

Aplicando a definição da DTFT:

$$
X(e^{j\omega})=
\sum_{n=0}^{3}e^{-j\omega n}
$$

Expandindo o somatório:

$$
X(e^{j\omega})=
1+e^{-j\omega}+e^{-j2\omega}+e^{-j3\omega}
$$

Essa expressão pode ser simplificada utilizando a soma de uma progressão geométrica:

$$
X(e^{j\omega})=
\frac{1-e^{-j4\omega}}
{1-e^{-j\omega}}
$$

Para os pontos em que o denominador não é nulo, essa expressão pode ser reescrita como:

$$
X(e^{j\omega})=
e^{-j\frac{3\omega}{2}}
\frac{\sin(2\omega)}
{\sin(\omega/2)}
$$

Em frequências nas quais o denominador se anula, a expressão original deve ser utilizada por continuidade.

A magnitude é:

$$
|X(e^{j\omega})|=
\left|
\frac{\sin(2\omega)}
{\sin(\omega/2)}
\right|
$$

A fase, quando a magnitude é diferente de zero, é determinada pelo argumento da expressão complexa.

No caso de $\omega=0$, todas as exponenciais são iguais a 1. Portanto:

$$
X(e^{j0})=1+1+1+1=4
$$

Isso significa que a magnitude do espectro na frequência zero é igual a 4, indicando uma componente contínua associada à soma das amostras da sequência.

Os zeros do espectro ocorrem em:

$$
\omega=\frac{k\pi}{2}
$$

para $k$ inteiro, exceto nos pontos equivalentes a múltiplos de $2\pi$, nos quais a expressão apresenta o valor 4.

Esse exemplo demonstra como uma sequência simples no domínio do tempo pode ser representada por uma função complexa no domínio da frequência.

---

:::: {include} ./simulacao/simulacao_dtft.ipynb
::::

---

# Resultados gráficos

A execução da simulação produz cinco representações que permitem analisar o comportamento da sequência e de sua transformada.

## Sequência no domínio do tempo

O primeiro gráfico apresenta as quatro amostras da sequência, todas com amplitude igual a 1.

A representação permite identificar diretamente a quantidade de amostras e seus respectivos valores. Entretanto, não apresenta de forma explícita a distribuição das componentes em frequência.

## Espectro de magnitude

O segundo gráfico apresenta a magnitude da DTFT em função da frequência angular.

Espera-se observar o maior valor de magnitude na frequência zero, com amplitude igual a 4. Também são identificados zeros espectrais em $-\pi/2$ e $\pi/2$, dentro do intervalo apresentado.

Esses pontos indicam frequências nas quais as contribuições das amostras se cancelam na soma das exponenciais complexas.

## Espectro de fase

O terceiro gráfico apresenta a fase da DTFT.

A fase permite observar o comportamento angular das componentes complexas em cada frequência. Como a fase é indefinida quando a magnitude é zero, esses pontos são omitidos da representação para evitar interpretações incorretas.

Além disso, podem ocorrer mudanças de fase de aproximadamente $\pi$ radianos quando o espectro real muda de sinal.

## Periodicidade da DTFT

O quarto gráfico apresenta o espectro em um intervalo maior de frequência, permitindo observar sua repetição.

A periodicidade de $2\pi$ radianos por amostra é uma característica fundamental da DTFT. Portanto, os padrões observados entre $-\pi$ e $\pi$ voltam a aparecer nos intervalos seguintes.

## Valores numéricos

O último trecho do código apresenta informações numéricas sobre a sequência e sua transformada, incluindo a maior magnitude e o valor da DTFT na frequência zero.

Esses valores permitem verificar numericamente os resultados apresentados nos gráficos e comparar a simulação com a formulação matemática.

---

# Interpretação

A comparação entre os domínios do tempo e da frequência demonstra que cada representação fornece informações diferentes sobre o mesmo sinal.

No domínio do tempo, é possível observar a quantidade de amostras, seus valores e a organização da sequência. No domínio da frequência, a DTFT permite identificar como essas amostras contribuem para a composição espectral do sinal.

Para a sequência escolhida, o valor máximo da magnitude ocorre na frequência zero, sendo igual a 4. Isso acontece porque todas as amostras possuem o mesmo valor e, nessa frequência, as exponenciais complexas da transformação são iguais a 1.

Os zeros espectrais em $-\pi/2$ e $\pi/2$ indicam frequências nas quais as contribuições das amostras se anulam. Esse comportamento evidencia a utilidade da análise espectral para identificar características que não são imediatamente perceptíveis na representação temporal.

A fase complementa a análise da magnitude, fornecendo informações sobre o comportamento angular das componentes complexas. Entretanto, nos pontos em que a magnitude é nula, a fase não possui significado definido.

Por fim, a representação em um intervalo maior confirma a periodicidade da DTFT, demonstrando que seu espectro se repete a cada $2\pi$ radianos por amostra.

---

# Discussão crítica

A Transformada de Fourier em Tempo Discreto é uma ferramenta essencial para compreender a composição em frequência de sinais discretos. Sua principal vantagem está na possibilidade de analisar separadamente as componentes espectrais por meio da magnitude e da fase, facilitando a identificação de frequências predominantes e características importantes do sinal.

Entretanto, a DTFT apresenta algumas limitações práticas. Embora sua definição matemática considere uma soma infinita, a simulação computacional geralmente trabalha com sequências finitas ou com sequências que permitem o cálculo da transformação. Além disso, a representação numérica utiliza uma quantidade limitada de pontos de frequência, de modo que a resolução visual depende da densidade da grade utilizada.

Outro aspecto importante é que a DTFT não deve ser confundida com a DFT ou a FFT. A DTFT representa o espectro como uma função contínua da frequência angular, enquanto a DFT fornece um conjunto finito de amostras desse espectro. A FFT, por sua vez, é um algoritmo eficiente para calcular a DFT.

No exemplo desenvolvido, a sequência possui apenas quatro amostras, o que facilita a análise matemática e computacional. Entretanto, sinais reais podem apresentar maior duração, ruídos, variações de amplitude e componentes de frequência sobrepostas, exigindo métodos de análise mais elaborados.

Portanto, o estudo da DTFT estabelece uma base importante para compreender a análise espectral e os métodos computacionais de processamento de sinais. A capacidade de observar magnitude, fase e periodicidade no domínio da frequência será fundamental para os próximos tópicos, especialmente aqueles relacionados à DFT, FFT e resolução espectral.