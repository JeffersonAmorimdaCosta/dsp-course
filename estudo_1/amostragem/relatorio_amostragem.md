# Amostragem

---

## Resumo conceitual

A amostragem é o processo de medir um sinal contínuo em instantes de tempo regularmente espaçados. Em um sistema de aquisição, o sinal físico existe continuamente no tempo, mas o equipamento registra apenas determinados valores desse sinal. Esses valores são chamados de **amostras** e formam uma sequência discreta.

Fisicamente, portanto, a amostragem transforma uma grandeza que pode variar continuamente, como tensão elétrica, pressão ou posição, em uma sequência de valores que pode ser processada por um computador. Os instantes de aquisição são separados pelo período de amostragem $T_s$.

A frequência de amostragem $f_s$ indica quantas amostras são obtidas por segundo. Quanto maior for $f_s$, menor será o intervalo entre duas amostras e mais detalhada será a representação temporal do sinal.

Para que um sinal possa ser reconstruído adequadamente a partir de suas amostras, é necessário respeitar o **critério de Nyquist-Shannon**. Para um sinal cuja maior frequência é $f_{\max}$, utiliza-se, idealmente,

$$
f_s > 2f_{\max}.
$$

Quando essa condição é violada, pode ocorrer **aliasing**, isto é, uma distorção na representação da frequência.

---

## Formulação matemática

O processo de amostragem uniforme é representado por:

$$
x[n] = x(nT_s).
$$

Nessa expressão:

* $x(t)$ representa o sinal contínuo;
* $x[n]$ representa a sequência discreta obtida após a amostragem;
* $n$ é o índice inteiro da amostra;
* $T_s$ é o período de amostragem, medido em segundos.

A frequência de amostragem é dada por:

$$
f_s = \frac{1}{T_s}.
$$

A frequência $f_s$ é medida em hertz (Hz), ou seja, amostras por segundo. Dessa forma, $T_s$ e $f_s$ são grandezas inversamente proporcionais: aumentar $f_s$ significa diminuir $T_s$.

Os instantes nos quais as amostras são adquiridas são:

$$
t_n = nT_s.
$$

Para o sinal senoidal utilizado neste estudo, adotamos:

$$
x(t) = A\sin(2\pi f_0t + \varphi),
$$

onde:

* $A$ é a amplitude;
* $f_0$ é a frequência do sinal;
* $\varphi$ é a fase inicial;
* $t$ é o tempo.

Será utilizado:

$$
A = 1,\qquad f_0 = 5\,\text{Hz},\qquad \varphi = 0.
$$

Assim,

$$
x(t) = \sin(10\pi t).
$$

Como a maior frequência do sinal é $5\,\text{Hz}$, o limite de Nyquist é:

$$
2f_0 = 10\,\text{Hz}.
$$

---

## Exemplo

Considere o sinal contínuo

$$
x(t) = \sin(2\pi\cdot5t),
$$

observado durante $1$ segundo. Serão analisadas três frequências de amostragem: $20\,\text{Hz}$, $10\,\text{Hz}$ e $6\,\text{Hz}$.

### Frequência de amostragem de $20\,\text{Hz}$

Para $f_s = 20\,\text{Hz}$, temos:

$$
T_s = \frac{1}{20} = 0{,}0500\,\text{s}.
$$

Isso corresponde a aproximadamente $4{,}00$ amostras por ciclo.

**Situação:** adequada, pois

$$
f_s > 2f_0.
$$

### Frequência de amostragem de $10\,\text{Hz}$

Para $f_s = 10\,\text{Hz}$, temos:

$$
T_s = \frac{1}{10} = 0{,}1000\,\text{s}.
$$

Isso corresponde a aproximadamente $2{,}00$ amostras por ciclo.

**Situação:** limite de Nyquist, pois

$$
f_s = 2f_0.
$$

### Frequência de amostragem de $6\,\text{Hz}$

Para $f_s = 6\,\text{Hz}$, temos:

$$
T_s = \frac{1}{6} \approx 0{,}1667\,\text{s}.
$$

Isso corresponde a aproximadamente $1{,}20$ amostras por ciclo.

**Situação:** insuficiente, pois

$$
f_s < 2f_0.
$$

Com $f_s = 20\,\text{Hz}$, são obtidas quatro amostras por período do sinal. A quantidade de pontos é suficiente para representar sua oscilação com boa resolução.

Com $f_s = 10\,\text{Hz}$, existem duas amostras por período, correspondendo ao limite teórico de Nyquist. Esse caso é crítico e, na prática, costuma-se trabalhar com uma margem acima desse limite.

Com $f_s = 6\,\text{Hz}$, são obtidas apenas $1{,}2$ amostras por período. A taxa é menor que duas vezes a frequência do sinal e ocorre subamostragem, podendo produzir **aliasing**.

---

## Simulação computacional

A simulação abaixo gera numericamente o sinal senoidal e calcula suas amostras para três valores diferentes de frequência de amostragem. O sinal contínuo é representado por uma malha temporal muito densa, enquanto os valores discretos são obtidos pela equação

$$
x[n] = x(nT_s).
$$

:::: {include} ./simulacao/simulacao_amostragem.ipynb
::::

---

## Resultados

Os resultados numéricos esperados para as três condições podem ser resumidos na tabela a seguir.

| $f_s$ (Hz) | $T_s$ (s) | Amostras/ciclo | Relação com Nyquist | Resultado                |
| :----------: | :---------: | :------------: | :-----------------: | :----------------------- |
|      20      |    0,0500   |      4,00      |    $f_s > 2f_0$   | Boa representação        |
|      10      |    0,1000   |      2,00      |    $f_s = 2f_0$   | Limite teórico           |
|       6      |    0,1667   |      1,20      |    $f_s < 2f_0$   | Subamostragem / aliasing |

A comparação mostra que a redução da frequência de amostragem aumenta o espaçamento entre as amostras. Consequentemente, menos informações sobre a evolução temporal do sinal ficam disponíveis na sequência discreta.

Para $f_s = 20\,\text{Hz}$, a sequência possui quatro pontos por ciclo. Para $f_s = 10\,\text{Hz}$, possui dois pontos por ciclo. Para $f_s = 6\,\text{Hz}$, há apenas $1{,}2$ pontos por ciclo, o que não é suficiente para distinguir corretamente a oscilação de $5\,\text{Hz}$.

---

## Discussão

A simulação demonstra que $T_s$ e $f_s$ possuem uma relação inversamente proporcional. Quando a frequência de amostragem passa de $20\,\text{Hz}$ para $10\,\text{Hz}$, o período de amostragem aumenta de $0{,}05\,\text{s}$ para $0{,}10\,\text{s}$. Ao utilizar $6\,\text{Hz}$, o período aumenta para aproximadamente $0{,}1667\,\text{s}$.

Essa mudança interfere diretamente na representação discreta. Uma frequência de amostragem elevada fornece mais pontos para descrever cada ciclo do sinal. Com uma frequência menor, os pontos ficam mais afastados e podem deixar de representar corretamente as variações do sinal.

No caso de $f_s = 20\,\text{Hz}$, a condição de Nyquist é satisfeita, pois:

$$
20 > 2\cdot5.
$$

A representação discreta contém informação suficiente para preservar a frequência do sinal, considerando um sistema ideal.

No caso de $f_s = 10\,\text{Hz}$, temos exatamente:

$$
f_s = 2f_0.
$$

Esse é o limite de Nyquist e constitui uma situação crítica. Em aplicações reais, recomenda-se utilizar uma taxa maior que esse limite e aplicar um **filtro anti-aliasing** antes da conversão analógico-digital.

No caso de $f_s = 6\,\text{Hz}$, a condição de Nyquist não é satisfeita. Como consequência, ocorre subamostragem e a sequência discreta pode apresentar uma frequência aparente diferente da frequência original. Esse fenômeno é denominado **aliasing** e representa uma perda de informação que não pode ser corrigida simplesmente após a amostragem.
