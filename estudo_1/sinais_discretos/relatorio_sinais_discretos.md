# Sinais Contínuos e Discretos

---

# Resumo conceitual

Sinais são representações matemáticas de fenômenos físicos ou de informações que variam em função de uma ou mais variáveis independentes. Em Engenharia Elétrica, Eletrônica e áreas relacionadas, os sinais são utilizados para representar grandezas como tensão, corrente, temperatura, pressão, velocidade, áudio e outras informações provenientes de sistemas físicos. Uma das classificações fundamentais dos sinais está relacionada à natureza da variável independente, distinguindo-se entre **sinais contínuos** e **sinais discretos**.

Um **sinal contínuo** é definido para todos os valores de sua variável independente dentro de determinado intervalo. No caso de sinais no tempo, sua representação pode ser escrita como $x(t)$, em que $t$ representa o tempo. Assim, entre dois instantes quaisquer existe um número infinito de valores possíveis para o sinal. Uma tensão elétrica produzida por um sensor analógico, por exemplo, pode ser modelada como um sinal contínuo.

Já um **sinal discreto** é definido somente em instantes ou posições específicas. Quando a variável independente é o tempo, sua representação é normalmente indicada por $x[n]$, em que $n$ é um índice inteiro e **adimensional**. Dessa forma, o sinal possui uma sequência de amostras, não sendo necessário que esteja definido entre dois índices consecutivos. Um sinal obtido por meio da amostragem periódica de um sinal contínuo constitui um exemplo típico de sinal discreto; nesse caso, a relação entre o índice e o tempo físico é dada por $t = nT_s$, em que $T_s$ é o período de amostragem.

É importante distinguir a discretização **temporal** de **quantização de amplitude**. A discretização temporal consiste em representar um sinal apenas em determinados instantes, enquanto a quantização restringe os valores possíveis da amplitude a um conjunto finito de níveis. Um sinal pode, portanto, possuir tempo discreto e amplitude contínua, como ocorre em uma sequência ideal de amostras antes da conversão para valores digitais.

Outra classificação importante considera a periodicidade, a simetria e a energia ou potência do sinal. Um sinal periódico apresenta repetição de seu comportamento após determinado intervalo, enquanto um sinal aperiódico não apresenta essa repetição. Além disso, sinais podem ser classificados como determinísticos ou aleatórios, dependendo da possibilidade de determinar seu comportamento matemáticamente.

A distinção entre sinais contínuos e discretos é particularmente importante no processamento de sinais. Sistemas físicos frequentemente produzem sinais contínuos, enquanto computadores e microcontroladores realizam operações sobre sequências discretas de valores. Consequentemente, técnicas de amostragem, reconstrução, filtragem e transformação entre os domínios contínuo e discreto são fundamentais para estabelecer a comunicação entre fenômenos físicos e sistemas digitais.

Um aspecto central desse processo é a **frequência de amostragem**, que determina quantas amostras são obtidas por unidade de tempo. Para representar adequadamente determinados componentes de frequência de um sinal, a frequência de amostragem deve ser suficientemente elevada. Caso contrário, pode ocorrer **aliasing**, fenômeno no qual diferentes componentes espectrais podem produzir representações discretas indistinguíveis ou incorretas.

---

# Formulação matemática

Um sinal contínuo no tempo pode ser representado genericamente por

$$x(t), \qquad t\in\mathbb{R}$$

onde:

* $x(t)$ — amplitude do sinal;  
* $t$ — variável independente, geralmente o tempo, em segundos (s).

Para um sinal discreto, a representação é dada por

$$x[n], \qquad n\in\mathbb{Z}$$

onde:

* $x[n]$ — valor da $n$-ésima amostra do sinal;  
* $n$ — índice inteiro e adimensional da sequência. A associação a um instante físico só existe quando o sinal discreto provém de amostragem, caso em que $t = nT_s$.

## Amostragem

Considerando um sinal contínuo $x(t)$, sua amostragem periódica pode ser expressa por

$$x[n]=x(nT_s)$$

onde:

* $x[n]$ — sinal discreto obtido após a amostragem;  
* $x(t)$ — sinal contínuo original;  
* $n$ — índice inteiro da amostra;  
* $T_s$ — período de amostragem, em segundos (s).

A frequência de amostragem é definida como

$$f_s=\frac{1}{T_s}$$

onde:

* $f_s$ — frequência de amostragem, em hertz (Hz);  
* $T_s$ — período de amostragem, em segundos (s).

Portanto, quanto menor for o intervalo entre duas amostras consecutivas, maior será a frequência de amostragem.

## Relação com a frequência do sinal

Para um sinal senoidal contínuo,

$$x(t)=A\cos(2\pi f_0 t+\varphi)$$

onde:

* $A$ — amplitude do sinal;  
* $f_0$ — frequência do sinal, em hertz (Hz);  
* $t$ — tempo, em segundos (s);  
* $\varphi$ — fase inicial, em radianos (rad).

O período do sinal é dado por $T_0 = 1/f_0$.

Após a amostragem, obtém-se

$$x[n]=A\cos(2\pi f_0 nT_s+\varphi)$$

Como $f_s = 1/T_s$, a expressão também pode ser escrita como

$$x[n]=A\cos\left(2\pi\frac{f_0}{f_s}n+\varphi\right)$$

Essa equação demonstra que o comportamento do sinal discreto depende da razão entre a frequência do sinal $f_0$ e a frequência de amostragem $f_s$.

## Teorema da amostragem

Para evitar a ocorrência de aliasing na representação de um sinal limitado em banda, a frequência de amostragem deve satisfazer a condição

$$f_s>2f_{\max}$$

onde:

* $f_s$ — frequência de amostragem;  
* $f_{\max}$ — maior frequência presente no sinal.

O valor $2f_{\max}$ corresponde à **taxa de Nyquist** (frequência mínima de amostragem para reconstrução ideal), enquanto a **frequência de Nyquist** associada a uma dada taxa de amostragem é definida por $f_N = f_s/2$. A condição acima é conhecida como critério de Nyquist-Shannon. Em situações ideais de banda estritamente limitada, a igualdade $f_s = 2f_{\max}$ ainda permite reconstrução; em sistemas reais, adota-se a desigualdade estrita por robustez.

Quando essa condição não é atendida, componentes de frequência podem ser representadas incorretamente no domínio discreto. Por esse motivo, sistemas reais de aquisição geralmente utilizam filtros passa-baixas antes da conversão analógico-digital, reduzindo as componentes acima da faixa desejada.

---

# Exemplo

Considere um sinal senoidal contínuo com frequência de $1\,\text{kHz}$, que será convertido para uma sequência discreta por meio de um sistema de aquisição de dados.

**Dados de entrada:**

* Amplitude: $A=2\,\text{V}$;  
* Frequência do sinal: $f_0=1\,\text{kHz}$;  
* Fase inicial: $\varphi=0$;  
* Frequência de amostragem: $f_s=8\,\text{kHz}$.

**Hipóteses ou condições consideradas:**

* O sinal é senoidal e periódico;  
* A amplitude é tratada como variável contínua (sem quantização), de modo que o sinal discreto resultante possui tempo discreto e amplitude contínua;  
* A amostragem ocorre em intervalos regulares;  
* Não são considerados efeitos de ruído ou quantização;  
* A maior frequência presente no sinal é $1\,\text{kHz}$.

**Procedimento de cálculo:**

Inicialmente, determina-se o período de amostragem. Em seguida, verifica-se se a frequência de amostragem atende ao critério de Nyquist. Finalmente, utiliza-se a relação entre o sinal contínuo e suas amostras para determinar alguns valores da sequência discreta.

### Desenvolvimento

O sinal contínuo pode ser descrito por

$$x(t)=2\cos(2\pi\cdot1000\,t)$$

A frequência de amostragem é

$$f_s=8000\,\text{Hz}$$

Portanto, o período de amostragem é

$$T_s=\frac{1}{f_s}=\frac{1}{8000}=0{,}000125\,\text{s}=125\,\mu\text{s}$$

Assim, uma nova amostra é obtida a cada $125\,\mu\text{s}$.

O sinal discreto é obtido substituindo $t=nT_s$ na expressão do sinal contínuo:

$$x[n]=2\cos(2\pi\cdot1000\,nT_s)$$

Substituindo $T_s=1/8000$:

$$x[n]=2\cos\left(2\pi\cdot1000\cdot\frac{n}{8000}\right)=2\cos\left(\frac{\pi}{4}n\right)$$

Algumas amostras podem ser calculadas diretamente:

$$x[0]=2\cos(0)=2\,\text{V}$$

$$x[1]=2\cos\left(\frac{\pi}{4}\right)\approx 1{,}414\,\text{V}$$

$$x[2]=2\cos\left(\frac{\pi}{2}\right)=0\,\text{V}$$

$$x[3]=2\cos\left(\frac{3\pi}{4}\right)\approx -1{,}414\,\text{V}$$

$$x[4]=2\cos(\pi)=-2\,\text{V}$$

Dessa maneira, os primeiros valores da sequência são aproximadamente

$$x[n]=\{2;\;1{,}414;\;0;\;-1{,}414;\;-2;\;-1{,}414;\;0;\;1{,}414;\;2;\ldots\}$$

Também é possível verificar a condição de Nyquist:

$$f_s>2f_{\max}\;\Rightarrow\;8000>2(1000)\;\Rightarrow\;8000>2000$$

Portanto, a frequência de amostragem utilizada é suficientemente elevada para representar a componente de $1\,\text{kHz}$ sem violar o critério de Nyquist.

### Resultado do exemplo

O sinal contínuo de $1\,\text{kHz}$ foi convertido em uma sequência discreta utilizando uma frequência de amostragem de $8\,\text{kHz}$. O período entre amostras obtido foi de $125\,\mu\text{s}$, resultando na sequência

$$x[n]=2\cos\left(\frac{\pi}{4}n\right)$$

A frequência de amostragem corresponde a oito vezes a frequência do sinal, proporcionando quatro amostras por meio ciclo e oito amostras por período completo. Além disso, a condição $f_s>2f_{\max}$ foi satisfeita, indicando que, sob as hipóteses consideradas, a amostragem atende ao critério de Nyquist e permite representar adequadamente o sinal de $1\,\text{kHz}$ no domínio discreto.

---

:::: {include} ./simulacao/sinais_simulacao.ipynb
::::

## Resultados

Os resultados apresentados nesta seção correspondem à simulação computacional do sinal senoidal definido na seção de exemplo. Foram considerados amplitude de $2\,\text{V}$, frequência de $1\,\text{kHz}$, fase inicial nula e frequência de amostragem de $8\,\text{kHz}$.

A simulação foi utilizada para representar simultaneamente o sinal contínuo e suas respectivas amostras, permitindo verificar computacionalmente as relações estabelecidas na formulação matemática.

## Resultados numéricos

Os principais parâmetros utilizados na simulação e os resultados obtidos são apresentados na Tabela 1.

**Tabela 1 — Parâmetros da simulação**

| Parâmetro                          |    Valor | Unidade |
| :--------------------------------- | -------: | :------ |
| Amplitude $A$                      |        2 | V       |
| Frequência do sinal $f_0$          |     1000 | Hz      |
| Fase inicial $\varphi$             |        0 | rad     |
| Frequência de amostragem $f_s$     |     8000 | Hz      |
| Período do sinal $T_0$             |    0,001 | s       |
| Período de amostragem $T_s$        | 0,000125 | s       |
| Taxa de Nyquist $2f_0$             |     2000 | Hz      |
| Frequência de Nyquist $f_s/2$      |     4000 | Hz      |

A partir da relação

$$T_0 = \frac{1}{f_0}$$

obtém-se um período de

$$T_0 = \frac{1}{1000} = 0{,}001\,\text{s} = 1\,\text{ms}.$$

Da mesma forma, o período de amostragem é determinado por

$$T_s = \frac{1}{f_s} = \frac{1}{8000} = 0{,}000125\,\text{s} = 125\,\mu\text{s}.$$

A sequência discreta obtida para o sinal pode ser expressa por

$$x[n] = 2\cos\left(\frac{\pi}{4}n\right).$$

Os primeiros valores calculados analiticamente são apresentados na Tabela 2.

**Tabela 2 — Primeiras amostras da sequência $x[n]$**

| $n$ | $t = nT_s$ | $x[n]$ |
| --: | ---------: | -----: |
|   0 |       0 µs | 2,000 V |
|   1 |     125 µs | 1,414 V |
|   2 |     250 µs | 0,000 V |
|   3 |     375 µs | $-1{,}414$ V |
|   4 |     500 µs | $-2{,}000$ V |
|   5 |     625 µs | $-1{,}414$ V |
|   6 |     750 µs | 0,000 V |
|   7 |     875 µs | 1,414 V |
|   8 |    1000 µs | 2,000 V |

Observa-se que são obtidas oito amostras por período do sinal, uma vez que

$$\frac{f_s}{f_0} = \frac{8000}{1000} = 8.$$

## Resultados gráficos

A Figura 1 apresenta a representação simultânea do sinal contínuo e das amostras obtidas durante a simulação computacional.

**Figura 1 — Representação do sinal contínuo e do sinal amostrado**

::::{figure} ./simulacao/grafico_sinal.png
:name: fig-sinal-continuo-amostrado
:alt: Sinal contínuo e sinal amostrado
:align: center

Sinal contínuo e respectivas amostras obtidas durante a simulação computacional. A linha vertical tracejada marca o período do sinal $T_0$.
::::

**Fonte:** Elaborado pelo autor.

O gráfico permite observar que as amostras estão posicionadas sobre a curva do sinal contínuo nos respectivos instantes de amostragem. A utilização de uma frequência de amostragem de $8\,\text{kHz}$ proporciona oito amostras para cada período do sinal de $1\,\text{kHz}$, permitindo visualizar adequadamente sua variação temporal.

## Comparação dos resultados

A comparação entre os resultados analíticos e computacionais permite verificar a consistência da implementação realizada. A expressão analítica utilizada para determinar as amostras foi

$$x[n] = 2\cos\left(\frac{\pi}{4}n\right).$$

Na simulação, os mesmos instantes de amostragem foram utilizados para avaliar numericamente a função do sinal. Consequentemente, os valores obtidos computacionalmente coincidem, considerando a precisão numérica da representação em ponto flutuante, com os valores determinados analiticamente.

**Tabela 3 — Comparação entre resultados analítico e computacional**

| Método        | $x[0]$ | $x[1]$ | $x[2]$ |
| :------------ | -----: | -----: | -----: |
| Analítico     | 2,000 V | 1,414 V | 0,000 V |
| Computacional | 2,000 V | 1,414 V | 0,000 V |
| Diferença     | 0 V | $\approx 0$ V | 0 V |

A pequena diferença eventualmente observada em determinados valores decorre da representação numérica utilizada pelo computador para operações com números reais e funções trigonométricas, não caracterizando uma discrepância significativa entre os modelos.

# Discussão

Os resultados obtidos na simulação apresentam comportamento coerente com o modelo matemático desenvolvido. O sinal contínuo apresentou comportamento senoidal com amplitude de $2\,\text{V}$ e frequência de $1\,\text{kHz}$, enquanto o conjunto de amostras reproduziu os valores do sinal nos instantes definidos pelo período de amostragem de $125\,\mu\text{s}$.

A frequência de amostragem utilizada foi de $8\,\text{kHz}$, enquanto a maior frequência presente no sinal é de $1\,\text{kHz}$. Portanto,

$$f_s = 8000\,\text{Hz} > 2(1000\,\text{Hz}) = 2000\,\text{Hz}.$$

A condição estabelecida pelo critério de Nyquist foi, portanto, satisfeita. Dessa forma, não houve violação da condição mínima de amostragem para a frequência considerada, e as amostras apresentaram uma representação adequada do comportamento do sinal contínuo.

Outro aspecto observado é a relação entre as frequências do sinal e de amostragem. Como $f_s/f_0 = 8$, são obtidas oito amostras em cada período do sinal. Essa quantidade permite visualizar claramente a evolução da senoide no domínio discreto e identificar os valores correspondentes aos seus máximos, mínimos e cruzamentos com o eixo temporal.

A correspondência entre os resultados analíticos e computacionais também confirma a correta implementação da expressão matemática no ambiente de simulação. As amostras calculadas pela função computacional apresentaram os mesmos valores previstos pela expressão analítica, dentro da precisão numérica utilizada.

Como limitação da simulação, destaca-se que o modelo considera um sinal senoidal ideal e não incorpora efeitos presentes em sistemas reais, como ruído, distorções, limitações do circuito de aquisição e quantização da amplitude. Dessa forma, os resultados representam uma situação idealizada destinada à verificação dos fundamentos de amostragem de sinais.

Os resultados obtidos demonstram, portanto, a relação entre as representações contínua e discreta de um sinal e evidenciam a influência da frequência de amostragem sobre sua representação. A simulação confirma computacionalmente os resultados obtidos por meio da formulação matemática e permite visualizar de forma direta o processo de amostragem de um sinal contínuo.