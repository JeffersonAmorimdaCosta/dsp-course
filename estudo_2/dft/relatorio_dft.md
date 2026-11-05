# Transformada Discreta de Fourier (DFT)

---

# Resumo conceitual

A Transformada Discreta de Fourier (DFT, do inglês *Discrete Fourier Transform*) é uma ferramenta matemática utilizada no Processamento Digital de Sinais para analisar o conteúdo em frequência de sequências discretas e finitas. Sua principal função é transformar um sinal representado no domínio do tempo em uma representação no domínio da frequência, permitindo identificar quais componentes de frequência estão presentes e suas respectivas contribuições.

Na prática computacional, os sinais digitais são armazenados como sequências finitas de amostras. Dessa forma, a DFT permite analisar essas sequências por meio de um conjunto de coeficientes complexos que representam a contribuição de diferentes frequências para a composição do sinal.

A DFT transforma uma sequência contendo $N$ amostras em $N$ coeficientes espectrais. Cada coeficiente $X[k]$ está associado a uma frequência específica e contém informações sobre a magnitude e a fase dessa componente.

A magnitude indica a intensidade de cada componente de frequência, enquanto a fase representa seu deslocamento angular em relação à referência utilizada na representação do sinal.

A Transformada Discreta de Fourier é amplamente utilizada em aplicações como análise espectral, processamento de áudio, telecomunicações, processamento de imagens, identificação de frequências e análise de vibrações.

Além disso, a DFT possui uma versão inversa, denominada IDFT (*Inverse Discrete Fourier Transform*), que permite reconstruir a sequência original a partir dos coeficientes espectrais.

---

# Formulação matemática

## Transformada Discreta de Fourier

A Transformada Discreta de Fourier de uma sequência $x[n]$, contendo $N$ amostras, é definida por:

$$
X[k]=\sum_{n=0}^{N-1}x[n]e^{-j\frac{2\pi}{N}kn}
$$

Para:

$$
k=0,1,2,\ldots,N-1
$$

Em que:

* $X[k]$: coeficiente complexo da DFT associado ao índice de frequência $k$;
* $x[n]$: sequência original no domínio do tempo;
* $N$: número total de amostras;
* $n$: índice das amostras no domínio do tempo;
* $k$: índice correspondente aos coeficientes espectrais;
* $j$: unidade imaginária, sendo $j^2=-1$.

O termo exponencial complexo pode ser desenvolvido utilizando a relação de Euler:

$$
e^{-j\theta}=\cos(\theta)-j\sin(\theta)
$$

Assim, a DFT realiza a comparação entre o sinal original e diferentes componentes exponenciais complexas, determinando a contribuição de cada frequência presente na sequência.

## Transformada Discreta de Fourier inversa

A reconstrução do sinal original é realizada por meio da Transformada Discreta de Fourier inversa:

$$
x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j\frac{2\pi}{N}kn}
$$

Essa expressão demonstra que é possível recuperar a sequência original a partir dos coeficientes calculados pela DFT.

## Magnitude e fase

Como os coeficientes da DFT são números complexos, cada um pode ser representado por uma parte real e uma parte imaginária:

$$
X[k]=\operatorname{Re}\{X[k]\}+j\operatorname{Im}\{X[k]\}
$$

A magnitude do espectro é calculada por:

$$
|X[k]|=\sqrt{\operatorname{Re}\{X[k]\}^2+ \operatorname{Im}\{X[k]\}^2}
$$

Já a fase é determinada por:

$$
\phi[k]=\operatorname{atan2} \left(\operatorname{Im}\{X[k]\}, \operatorname{Re}\{X[k]\}\right)
$$

A magnitude permite identificar a intensidade das componentes de frequência, enquanto a fase fornece informações sobre o deslocamento angular de cada componente.

## Relação entre os índices da DFT e as frequências

A frequência associada a cada índice $k$ é determinada por:

$$
f_k=\frac{k f_s}{N}
$$

Em que:

* $f_k$: frequência correspondente ao índice $k$, em hertz;
* $f_s$: frequência de amostragem, em hertz;
* $N$: número de amostras.

A resolução em frequência da DFT é dada por:

$$
\Delta f=\frac{f_s}{N}
$$

Portanto, quanto maior o número de amostras para uma mesma frequência de amostragem, menor será o espaçamento entre os pontos do espectro, proporcionando maior resolução em frequência.

Para sinais reais, o espectro apresenta simetria conjugada. Por esse motivo, é comum utilizar apenas a primeira metade do espectro, correspondente às frequências positivas, para facilitar a interpretação dos resultados.

---

# Exemplo

Considere um sinal discreto formado pela soma de duas senoides com frequências diferentes:

$$
x[n]=A_1\cos(\omega_1n)+A_2\cos(\omega_2n)
$$

Para o exemplo, serão utilizados os seguintes parâmetros:

* Amplitude da primeira senoide: $A_1=1{,}0$;
* Amplitude da segunda senoide: $A_2=0{,}5$;
* Primeira frequência: $f_1=10\,\text{Hz}$;
* Segunda frequência: $f_2=30\,\text{Hz}$;
* Frequência de amostragem: $f_s=256\,\text{Hz}$;
* Número de amostras: $N=256$.

Considerando que a frequência angular discreta é calculada por:

$$
\omega=\frac{2\pi f}{f_s}
$$

As frequências angulares das duas componentes serão:

$$
\omega_1=\frac{2\pi\cdot10}{256}
$$

$$
\omega_2=\frac{2\pi\cdot30}{256}
$$

Assim, o sinal utilizado será:

$$
x[n]=\cos\left(\frac{20\pi}{256}n\right) +0{,}5\cos\left(\frac{60\pi}{256}n\right)
$$

Aplicando a DFT a essa sequência, espera-se identificar duas componentes principais no espectro de magnitude, localizadas em 10 Hz e 30 Hz.

Como a primeira componente possui amplitude igual a $1{,}0$ e a segunda possui amplitude igual a $0{,}5$, espera-se que o primeiro pico apresente o dobro da magnitude do segundo no espectro unilateral corretamente normalizado.

Além disso, como as duas senoides foram definidas sem deslocamento de fase, suas fases iniciais são iguais a zero.

---

:::: {include} ./simulacao/simulacao_dft.ipynb
::::

---

# Resultados gráficos

A execução da simulação permite obter quatro representações gráficas distintas, cada uma responsável por apresentar uma característica específica do processamento realizado.

## Sinal no domínio do tempo

O primeiro gráfico apresenta o sinal resultante da soma das duas senoides, juntamente com suas componentes individuais.

É possível observar que o sinal resultante apresenta um comportamento oscilatório formado pela combinação das frequências de 10 Hz e 30 Hz.

A componente de 10 Hz possui amplitude maior, enquanto a componente de 30 Hz apresenta amplitude correspondente à metade da primeira.

## Espectro de magnitude

O segundo gráfico apresenta a magnitude dos coeficientes da DFT em função da frequência.

Espera-se observar dois picos principais:

* 10 Hz, com magnitude igual a $1{,}0$;
* 30 Hz, com magnitude igual a $0{,}5$.

Esses picos representam as duas componentes utilizadas na geração do sinal. A ausência de componentes significativas em outras frequências demonstra que, para essa configuração, a DFT identifica corretamente as frequências presentes no sinal.

## Espectro de fase

O terceiro gráfico apresenta a fase dos coeficientes espectrais em função da frequência.

Como as duas senoides foram geradas sem deslocamento de fase, os coeficientes correspondentes às frequências de 10 Hz e 30 Hz apresentam fase inicial igual a zero grau.

É importante observar que os coeficientes com magnitude nula ou muito próxima de zero podem apresentar valores de fase sem significado físico relevante, pois a fase de um componente inexistente não possui interpretação útil.

## Reconstrução do sinal

O quarto gráfico compara o sinal original com aquele reconstruído por meio da DFT inversa.

Espera-se que as duas curvas apresentem sobreposição praticamente perfeita, demonstrando que a transformação preserva as informações necessárias para reconstruir a sequência original.

---

# Interpretação

Os resultados obtidos demonstram a capacidade da Transformada Discreta de Fourier de identificar as componentes de frequência presentes em um sinal discreto.

No domínio do tempo, o sinal apresenta uma forma de onda resultante da combinação de duas senoides. Entretanto, apenas pela observação temporal, pode ser mais difícil determinar com precisão quais frequências compõem o sinal.

No domínio da frequência, essa identificação torna-se mais simples, pois cada componente aparece representada por um pico na posição correspondente à sua frequência.

Para a simulação realizada, a frequência de amostragem foi de 256 Hz e foram utilizadas 256 amostras. Dessa forma, a resolução em frequência é:

$$
\Delta f=\frac{f_s}{N}
$$

$$
\Delta f=\frac{256}{256}=1\,\text{Hz}
$$

Isso significa que os coeficientes espectrais estão separados por intervalos de 1 Hz.

As frequências utilizadas na geração do sinal, 10 Hz e 30 Hz, coincidem exatamente com índices da DFT, facilitando sua identificação no espectro.

Os resultados esperados podem ser organizados na seguinte tabela:

| Componente | Frequência | Amplitude esperada | Fase inicial |
|---|---:|---:|---:|
| Primeira senoide | 10 Hz | $1{,}0$ | 0° |
| Segunda senoide | 30 Hz | $0{,}5$ | 0° |

A magnitude do primeiro pico é duas vezes maior que a do segundo, reproduzindo a proporção entre as amplitudes utilizadas na geração do sinal.

Outro resultado importante é a reconstrução da sequência por meio da DFT inversa. Como a transformação preserva as informações de magnitude e fase dos coeficientes, a sequência original pode ser recuperada com erro numérico muito pequeno, decorrente apenas da precisão computacional.

Portanto, a simulação confirma a relação entre os componentes utilizados na geração do sinal e os picos observados no espectro de magnitude.

---

# Discussão crítica

A Transformada Discreta de Fourier é uma ferramenta fundamental para a análise de sinais digitais, pois permite identificar componentes de frequência que nem sempre são facilmente reconhecidas pela observação direta do sinal no domínio do tempo.

Uma de suas principais vantagens é a possibilidade de decompor matematicamente uma sequência em componentes espectrais, fornecendo informações sobre frequência, magnitude e fase. Além disso, a utilização da FFT torna o cálculo computacionalmente eficiente, permitindo analisar sequências com grandes quantidades de amostras.

Entretanto, a aplicação da DFT apresenta algumas limitações que precisam ser consideradas.

A primeira está relacionada à resolução em frequência, que depende diretamente da quantidade de amostras e da frequência de amostragem. Quando a resolução é insuficiente, componentes de frequência próximas podem apresentar dificuldade de distinção.

Outra limitação está relacionada ao fenômeno de vazamento espectral (*spectral leakage*), que ocorre quando o sinal analisado não apresenta um número inteiro de ciclos dentro do intervalo observado. Nessa situação, a energia de uma componente pode se distribuir entre diferentes pontos do espectro, dificultando a identificação precisa de sua frequência e magnitude.

Além disso, a frequência de amostragem deve respeitar o critério de Nyquist, evitando que componentes acima da metade da frequência de amostragem sejam representadas incorretamente no espectro.

Na simulação apresentada, essas dificuldades foram minimizadas pela escolha de frequências que coincidem exatamente com os pontos da DFT, utilizando uma quantidade de amostras e uma frequência de amostragem que proporcionam resolução de 1 Hz.

Apesar disso, em aplicações reais, os sinais podem apresentar ruídos, variações de amplitude, frequências não inteiras em relação à resolução espectral e componentes simultâneas. Nesses casos, podem ser necessárias técnicas complementares, como a aplicação de janelas, o aumento do número de amostras e métodos de estimação espectral.

Conclui-se que a DFT é essencial para a análise de sinais no domínio da frequência, permitindo identificar e quantificar suas componentes espectrais. A simulação demonstrou que os picos encontrados correspondem às frequências utilizadas na geração do sinal e que a aplicação da transformada inversa permite recuperar a sequência original. Dessa maneira, a atividade evidencia a relação entre a representação temporal e espectral de um sinal, demonstrando a importância da DFT no Processamento Digital de Sinais.