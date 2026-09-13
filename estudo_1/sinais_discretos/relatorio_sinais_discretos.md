# Sinais Contínuos e Discretos

---

# Resumo conceitual

Sinais são representações matemáticas de fenômenos físicos ou de informações que variam em função de uma ou mais variáveis independentes. Em Engenharia Elétrica, Eletrônica e áreas relacionadas, os sinais são utilizados para representar grandezas como tensão, corrente, temperatura, pressão, velocidade, áudio e outras informações provenientes de sistemas físicos. Uma das classificações fundamentais dos sinais está relacionada à natureza da variável independente, distinguindo-se entre **sinais contínuos** e **sinais discretos**.

Um **sinal contínuo** é definido para todos os valores de sua variável independente dentro de determinado intervalo. No caso de sinais no tempo, sua representação pode ser escrita como x(t)x(t), em que tt representa o tempo. Assim, entre dois instantes quaisquer existe um número infinito de valores possíveis para o sinal. Uma tensão elétrica produzida por um sensor analógico, por exemplo, pode ser modelada como um sinal contínuo.

Já um **sinal discreto** é definido somente em instantes ou posições específicas. Quando a variável independente é o tempo, sua representação é normalmente indicada por $x[n]$, em que $n$ é um índice inteiro. Dessa forma, o sinal possui uma sequência de amostras, não sendo necessário que esteja definido entre dois índices consecutivos. Um sinal obtido por meio da amostragem periódica de um sinal contínuo constitui um exemplo típico de sinal discreto.

É importante distinguir a discretização **temporal** de **quantização de amplitude**. A discretização temporal consiste em representar um sinal apenas em determinados instantes, enquanto a quantização restringe os valores possíveis da amplitude a um conjunto finito de níveis. Um sinal pode, portanto, possuir tempo discreto e amplitude contínua, como ocorre em uma sequência ideal de amostras antes da conversão para valores digitais.

Outra classificação importante considera a periodicidade, a simetria e a energia ou potência do sinal. Um sinal periódico apresenta repetição de seu comportamento após determinado intervalo, enquanto um sinal aperiódico não apresenta essa repetição. Além disso, sinais podem ser classificados como determinísticos ou aleatórios, dependendo da possibilidade de determinar seu comportamento matematicamente.

A distinção entre sinais contínuos e discretos é particularmente importante no processamento de sinais. Sistemas físicos frequentemente produzem sinais contínuos, enquanto computadores e microcontroladores realizam operações sobre sequências discretas de valores. Consequentemente, técnicas de amostragem, reconstrução, filtragem e transformação entre os domínios contínuo e discreto são fundamentais para estabelecer a comunicação entre fenômenos físicos e sistemas digitais.

Um aspecto central desse processo é a **frequência de amostragem**, que determina quantas amostras são obtidas por unidade de tempo. Para representar adequadamente determinados componentes de frequência de um sinal, a frequência de amostragem deve ser suficientemente elevada. Caso contrário, pode ocorrer **aliasing**, fenômeno no qual diferentes componentes espectrais podem produzir representações discretas indistinguíveis ou incorretas.

---

# Formulação matemática

Um sinal contínuo no tempo pode ser representado genericamente por

$$x(t), \qquad t\in\mathbb{R}$$

onde:

* x(t)x(t) — amplitude do sinal;  
* tt — variável independente, geralmente o tempo, em segundos (s).

Para um sinal discreto, a representação é dada por

$$x[n], \qquad n\in\mathbb{Z}$$

onde:

* $x[n]$ — valor da $n$-ésima amostra do sinal;  
* nn — índice inteiro da sequência;  
* $n$ — não representa necessariamente uma unidade física de tempo, mas pode estar associado ao instante $t=nT_s$.

## Amostragem

Considerando um sinal contínuo x(t)x(t), sua amostragem periódica pode ser expressa por

$$x[n]=x(nT_s)$$

onde:

* $x[n]$ — sinal discreto obtido após a amostragem;  
* x(t)x(t) — sinal contínuo original;  
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

$$x(t)=A\cos(2\pi f t+\phi)$$

onde:

* $A$ — amplitude do sinal;  
* $f$ — frequência do sinal, em hertz (Hz);  
* $t$ — tempo, em segundos (s);  
* $\phi$ — fase inicial, em radianos (rad).

Após a amostragem, obtém-se

$$x[n]=A\cos(2\pi f nT_s+\phi)$$

Como fs=1/Tsf\_s=1/T\_s, a expressão também pode ser escrita como

$$x[n]=A\cos\left(2\pi\frac{f}{f_s}n+\phi\right)$$

Essa equação demonstra que o comportamento do sinal discreto depende da razão entre a frequência do sinal $f$ e a frequência de amostragem $f_s$.

## Teorema da amostragem

Para evitar a ocorrência de aliasing na representação de um sinal limitado em banda, a frequência de amostragem deve satisfazer a condição

$$f_s>2f_{\max}$$

onde:

* $f_s$ — frequência de amostragem;  
* $f_{\max}$ — maior frequência presente no sinal.

O valor $2f_{\max}$ corresponde à chamada **frequência de Nyquist**, sendo a condição acima conhecida como critério de Nyquist-Shannon.

Quando essa condição não é atendida, componentes de frequência podem ser representadas incorretamente no domínio discreto. Por esse motivo, sistemas reais de aquisição geralmente utilizam filtros passa-baixas antes da conversão analógico-digital, reduzindo as componentes acima da faixa desejada.

---

# Exemplo

Considere um sinal senoidal contínuo com frequência de $1\,\text{kHz}$, que será convertido para uma sequência discreta por meio de um sistema de aquisição de dados.

**Dados de entrada:**

* Amplitude: $A=2\,\text{V}$;  
* Frequência do sinal: $f=1\,\text{kHz}$;  
* Fase inicial: $\phi=0$;  
* Frequência de amostragem: $f_s=8\,\text{kHz}$.

**Hipóteses ou condições consideradas:**

* O sinal é senoidal e periódico;  
* A amplitude é considerada contínua;  
* A amostragem ocorre em intervalos regulares;  
* Não são considerados efeitos de ruído ou quantização;  
* A maior frequência presente no sinal é $1\,\text{kHz}$.

**Procedimento de cálculo:**

Inicialmente, determina-se o período de amostragem. Em seguida, verifica-se se a frequência de amostragem atende ao critério de Nyquist. Finalmente, utiliza-se a relação entre o sinal contínuo e suas amostras para determinar alguns valores da sequência discreta.

### Desenvolvimento

O sinal contínuo pode ser descrito por

$$x(t)=2\cos(2\pi1000t)$$

A frequência de amostragem é

$$f_s=8000\,\text{Hz}$$

Portanto, o período de amostragem é

$$T_s=\frac{1}{f_s}$$

$$T_s=\frac{1}{8000}$$

$$T_s=0,000125\,\text{s}$$

ou

$$T_s=125\,\mu\text{s}$$

Assim, uma nova amostra é obtida a cada $125\,\mu\text{s}$.

O sinal discreto é obtido substituindo $t=nT_s$ na expressão do sinal contínuo:

$$x[n]=2\cos(2\pi1000nT_s)$$

Substituindo $T_s=1/8000$:

$$x[n]=2\cos\left(2\pi1000\frac{n}{8000}\right)$$

Logo,

$$x[n]=2\cos\left(\frac{\pi}{4}n\right)$$

Algumas amostras podem ser calculadas diretamente:

$$x[0]=2\cos(0)=2\,\text{V}$$

$$x[1]=2\cos\left(\frac{\pi}{4}\right)\approx1,414\,\text{V}$$

$$x[2]=2\cos\left(\frac{\pi}{2}\right)=0\,\text{V}$$

$$x[3]=2\cos\left(\frac{3\pi}{4}\right)\approx-1,414\,\text{V}$$

$$x[4]=2\cos(\pi)=-2\,\text{V}$$

Dessa maneira, os primeiros valores da sequência são aproximadamente

$$x[n]=\{2,\;1,414,\;0,\;-1,414,\;-2,\;-1,414,\;0,\;1,414,\;2,\ldots\}$$

Também é possível verificar a condição de Nyquist:

$$f_s>2f_{\max}$$

Como

$$8000>2(1000)$$

tem-se

$$8000>2000$$

Portanto, a frequência de amostragem utilizada é suficientemente elevada para representar a componente de $1\,\text{kHz}$ sem violar o critério de Nyquist.

### 3.2 Resultado do exemplo

O sinal contínuo de $1\,\text{kHz}$ foi convertido em uma sequência discreta utilizando uma frequência de amostragem de $8\,\text{kHz}$. O período entre amostras obtido foi de $125\,\mu\text{s}$, resultando na sequência

$$x[n]=2\cos\left(\frac{\pi}{4}n\right)$$

A frequência de amostragem corresponde a oito vezes a frequência do sinal, proporcionando quatro amostras por meio ciclo e oito amostras por período completo. Além disso, a condição $f_s>2f_{\max}$ foi satisfeita, indicando que, sob as hipóteses consideradas, a amostragem atende ao critério de Nyquist e permite representar adequadamente o sinal de $1\,\text{kHz}$ no domínio discreto.

---

# Simulação

Implementar computacionalmente o exemplo desenvolvido na seção anterior, utilizando **GNU Octave ou Python**.

A implementação deve reproduzir, de forma computacional, as etapas matemáticas apresentadas anteriormente, permitindo verificar os resultados obtidos e, quando pertinente, analisar o comportamento do sistema para diferentes condições de entrada.

### Metodologia computacional

Descrever brevemente a metodologia empregada na implementação, incluindo:

* linguagem e ambiente utilizados;  
* bibliotecas ou pacotes empregados;  
* parâmetros de entrada;  
* método de cálculo ou algoritmo utilizado;  
* condições iniciais e demais configurações relevantes.

### Implementação

Apresentar o código-fonte utilizado na simulação.

**Código da simulação:**

### Execução da simulação

Descrever as condições utilizadas para a execução e indicar quais dados foram obtidos como saída.

---

# Resultados

Apresentar os resultados obtidos a partir da simulação computacional e, quando aplicável, do exemplo analítico.

Os resultados devem ser apresentados de maneira objetiva e organizada, utilizando recursos como:

* gráficos;  
* tabelas;  
* valores numéricos;  
* curvas características;  
* comparações entre resultados analíticos e computacionais.

### Resultados numéricos

| Parâmetro | Valor | Unidade |
| ----- | ----- | ----- |
| \[Parâmetro 1\] | \[valor\] | \[unidade\] |
| \[Parâmetro 2\] | \[valor\] | \[unidade\] |
| \[Resultado\] | \[valor\] | \[unidade\] |

### Resultados gráficos

**Figura 1 — \[Título descritivo do gráfico\]**

\[Inserir gráfico\]

**Fonte:** Elaborado pelo autor.

### Comparação dos resultados

Quando pertinente, comparar os resultados obtidos analiticamente com aqueles produzidos pela simulação computacional.

| Método | Resultado | Diferença |
| ----- | ----- | ----- |
| Analítico | \[valor\] | — |
| Computacional | \[valor\] | \[valor/%\] |

---

# Discussão

Interpretar os resultados obtidos, relacionando-os aos conceitos apresentados no **Resumo conceitual** e à **Formulação matemática**.

A discussão deve analisar o comportamento observado na simulação e verificar sua coerência com o modelo teórico desenvolvido. Devem ser identificadas, quando aplicável, as relações entre as variáveis, os efeitos da variação dos parâmetros e eventuais diferenças entre os resultados analíticos e computacionais.

Também podem ser discutidos:

* comportamento esperado e comportamento observado;  
* influência dos principais parâmetros;  
* possíveis fontes de erro ou discrepância;  
* limitações do modelo ou da simulação;  
* validade das hipóteses adotadas;  
* relação entre os resultados e a teoria estudada;  
* possíveis aplicações práticas dos resultados.

Ao final, apresentar uma síntese das principais conclusões obtidas a partir da análise realizada.
