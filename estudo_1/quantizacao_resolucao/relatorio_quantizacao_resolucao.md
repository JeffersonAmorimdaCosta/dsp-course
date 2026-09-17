# Quantização e Resolução

---

# Resumo conceitual

## Quantização

Na conversão de um sinal analógico para uma representação digital, a amostragem discretiza o tempo, enquanto a quantização discretiza a amplitude. A quantização aproxima cada valor do sinal para um dos níveis disponíveis no sistema.

Como há uma quantidade finita de níveis, a amplitude quantizada normalmente não coincide exatamente com a amplitude original. A diferença entre esses valores constitui o erro de quantização.

## Número de bits e níveis

Cada bit possui dois estados possíveis. Assim, um sistema com $N$ bits consegue representar:

$$
L = 2^N
$$

níveis distintos.

Quanto maior for $N$, maior será a quantidade de níveis disponíveis.

## Resolução

Considerando uma faixa de tensão de $0$ até $V_{\mathrm{ref}}$, a resolução aproximada de um quantizador uniforme é:

$$
\Delta V = \frac{V_{\mathrm{ref}}}{2^N}
$$

Uma resolução menor significa que os níveis de amplitude estão mais próximos e, portanto, que pequenas variações do sinal podem ser representadas com maior precisão.

## Erro de quantização

O erro de quantização pode ser definido como:

$$
e_q(t) = x(t) - x_q(t)
$$

Para um quantizador uniforme ideal com arredondamento, o módulo do erro é limitado por:

$$
\left|e_q(t)\right| \leq \frac{\Delta V}{2}
$$

## Relação entre amostragem e quantização

A amostragem e a quantização são processos diferentes. A primeira determina os instantes em que o sinal é observado; a segunda determina os valores de amplitude permitidos.

| Processo | Discretização | Parâmetro |
| :---- | :---- | :---- |
| Amostragem | Tempo | Frequência de amostragem $f_s$ |
| Quantização | Amplitude | Número de bits $N$ |

Uma representação digital completa depende, portanto, da discretização temporal e da discretização da amplitude.

# Formulação matemática

## Número de níveis

O número de níveis disponíveis em um quantizador de $N$ bits é dado por:

$$
L = 2^N
$$

onde:

- $L$ é o número de níveis de quantização;
- $N$ é o número de bits utilizados pelo sistema.

## Resolução

Para uma faixa de entrada entre $0$ e $V_{\mathrm{ref}}$, a resolução do quantizador é aproximadamente:

$$
\Delta V = \frac{V_{\mathrm{ref}}}{2^N}
$$

onde:

- $\Delta V$ resolução do quantizador, ou seja, o intervalo entre níveis consecutivos;
- $V_{\mathrm{ref}}$ é a tensão de referência;
- $N$ é o número de bits.

## Quantização uniforme

A quantização uniforme pode ser representada por:

$$
x_q(t) =
\Delta V
\operatorname{round}
\left(
\frac{x(t)}{\Delta V}
\right)
$$

onde:

- $x(t)$ representa o sinal original, antes da quantização;
- $x_q(t)$ representa o sinal quantizado, ou seja, o sinal após a amplitude ter sido aproximada para os níveis disponíveis;
- $\operatorname{round}(\cdot)$ representa a operação de arredondamento para o nível inteiro mais próximo.

Na implementação, os valores quantizados são limitados à faixa permitida pelo conversor, evitando que valores fora do intervalo de representação sejam produzidos.

## Erro de quantização

O erro de quantização $e_q(t)$ é definido por:

$$
e_q(t) = x(t) - x_q(t)
$$

Para avaliar o erro médio da simulação, pode-se utilizar o erro RMS:

$$
e_{\mathrm{RMS}}
=
\sqrt{
\frac{1}{M}
\sum_{i=1}^{M}
e_q^2[i]
}
$$

onde:

- $e_{\mathrm{RMS}}$ é o valor eficaz do erro de quantização;
- $M$ é o número total de amostras;
- $e_q[i]$ é o erro associado à $i$-ésima amostra.

## Tendência com o aumento do número de bits

O comportamento da quantização com o aumento do número de bits pode ser resumido por:

$$
N \uparrow
\;\Rightarrow\;
L \uparrow
\;\Rightarrow\;
\Delta V \downarrow
\;\Rightarrow\;
\left|e_q\right| \downarrow
$$

Isso significa que, à medida que o número de bits aumenta, o número de níveis também aumenta, a distância entre os níveis diminui e o erro de quantização tende a diminuir.

---

# Exemplo

## Sinal utilizado

Considere o sinal senoidal:

$$
x(t) = 0.5 + 0.5\sin(2\pi f_0t)
$$

O deslocamento de $0.5,\mathrm{V}$ garante que o sinal permaneça entre $0$ e $1,\mathrm{V}$. Para este exemplo, serão utilizados os parâmetros:

* $f_0 = 5,\mathrm{Hz}$;
* $V_{\mathrm{ref}} = 1,\mathrm{V}$;
* $0 \leq x(t) \leq 1,\mathrm{V}$;
* $N \in {3,4,8}$.

O objetivo é observar como o aumento do número de bits modifica a resolução e, consequentemente, a precisão da representação do sinal.

## Quantização de uma amostra

Para visualizar o processo de quantização, considere o instante:

$$
t = 0{,}02\,\mathrm{s}
$$

O valor do sinal nesse instante é:

$$
x(0{,}02)
=
0.5+0.5\sin(2\pi\cdot5\cdot0{,}02)
$$

Como:

$$
2\pi\cdot5\cdot0{,}02=0{,}2\pi
$$

e:

$$
\sin(0{,}2\pi)\approx0{,}5878
$$

obtém-se:

$$
x(0{,}02)
\approx
0{,}7939\,\mathrm{V}
$$

Esse valor será quantizado utilizando $3$, $4$ e $8$ bits.

### Caso de 3 bits

Para $N=3$:

$$
L=2^3=8
$$

e:

$$
\Delta V=\frac{1}{8}=0{,}125\,\mathrm{V}
$$

Aplicando a equação de quantização:

$$
x_q(t)
=
\Delta V
\operatorname{round}
\left(
\frac{x(t)}{\Delta V}
\right)
$$

temos:

$$
x_q(0{,}02)
=
0{,}125
\operatorname{round}
\left(
\frac{0{,}7939}{0{,}125}
\right)
$$

$$
x_q(0{,}02)
=
0{,}125
\operatorname{round}(6{,}3512)
$$

Portanto:

$$
x_q(0{,}02)
=
0{,}125\cdot6
=
0{,}750\,\mathrm{V}
$$

O erro de quantização é:

$$
e_q=x-x_q
$$

$$
e_q
=
0{,}7939-0{,}750
\approx
0{,}0439\,\mathrm{V}
$$

### Caso de 4 bits

Para $N=4$:

$$
L=2^4=16
$$

e:

$$
\Delta V
=
\frac{1}{16}
=
0{,}0625\,\mathrm{V}
$$

Assim:

$$
x_q(0{,}02)
=
0{,}0625
\operatorname{round}
\left(
\frac{0{,}7939}{0{,}0625}
\right)
$$

$$
x_q(0{,}02)
=
0{,}0625
\operatorname{round}(12{,}7024)
$$

Logo:

$$
x_q(0{,}02)
=
0{,}0625\cdot13
=
0{,}8125\,\mathrm{V}
$$

O erro é:

$$
e_q
=
0{,}7939-0{,}8125
\approx
-0{,}0186\,\mathrm{V}
$$

### Caso de 8 bits

Para $N=8$:

$$
L=2^8=256
$$

e:

$$
\Delta V
=
\frac{1}{256}
=
0{,}00390625\,\mathrm{V}
$$

Aplicando a quantização:

$$
x_q(0{,}02)
=
0{,}00390625
\operatorname{round}
\left(
\frac{0{,}7939}{0{,}00390625}
\right)
$$

$$
x_q(0{,}02)
=
0{,}00390625
\operatorname{round}(203{,}236)
$$

Portanto:

$$
x_q(0{,}02)
=
0{,}00390625\cdot203
$$

$$
x_q(0{,}02)
\approx
0{,}79297\,\mathrm{V}
$$

O erro é:

$$
e_q
=
0{,}7939-0{,}79297
\approx
0{,}00092\,\mathrm{V}
$$

### Comparação

| Bits | Níveis |                 Resolução |       Valor quantizado |                   Erro |
| ---: | -----: | ------------------------: | ---------------------: | ---------------------: |
|  $3$ |    $8$ |      $0{,}125,\mathrm{V}$ |   $0{,}750,\mathrm{V}$ |  $0{,}0439,\mathrm{V}$ |
|  $4$ |   $16$ |     $0{,}0625,\mathrm{V}$ |  $0{,}8125,\mathrm{V}$ | $-0{,}0186,\mathrm{V}$ |
|  $8$ |  $256$ | $0{,}00390625,\mathrm{V}$ | $0{,}79297,\mathrm{V}$ | $0{,}00092,\mathrm{V}$ |

O exemplo evidencia o efeito do aumento da resolução. Para o mesmo valor original de aproximadamente $0{,}7939,\mathrm{V}$, a quantização com $3$ bits produz uma aproximação de $0{,}750,\mathrm{V}$, enquanto a utilização de $8$ bits resulta em aproximadamente $0{,}79297,\mathrm{V}$.

Portanto, quanto maior o número de bits, menor é o espaçamento entre os níveis de quantização e, nesse exemplo, menor é o erro entre o valor original e o valor quantizado.



---

:::: {include} ./simulacao/simulacao_quantizacao_resolucao.ipynb
::::

---

# Resultados

## Resultado visual

Com $3$ bits, os degraus do sinal quantizado são grandes e facilmente identificáveis. Com $4$ bits, os níveis ficam mais próximos. Com $8$ bits, a curva quantizada apresenta degraus muito menores e visualmente se aproxima do sinal original.

## Resultado numérico

| Bits | Níveis | Resolução (V) | Erro máximo ideal (V) | Erro RMS aproximado |
| :---- | :---- | :---- | :---- | :---- |
| $3$ | $8$ | $0{,}125000$ | $0{,}062500$ | $\approx 0{,}036$ |
| $4$ | $16$ | $0{,}062500$ | $0{,}031250$ | $\approx 0{,}018$ |
| $8$ | $256$ | $0{,}003906$ | $0{,}001953$ | $\approx 0{,}0011$ |

Os valores do erro RMS podem variar ligeiramente conforme os pontos utilizados na simulação. O limite teórico do erro máximo é determinado por:

$$
\left|e_q\right|_{\max}
=
\frac{\Delta V}{2}
$$

## Comparação

Ao passar de $3$ para $8$ bits, a quantidade de níveis aumenta de $8$ para $256$, enquanto a resolução diminui de $0{,}125\,\mathrm{V}$ para aproximadamente $0{,}003906\,\mathrm{V}$.

A razão entre as quantidades de níveis é:

$$
\frac{256}{8} = 32
$$

Dessa forma, o quantizador de $8$ bits possui $32$ vezes mais níveis que o quantizador de $3$ bits e permite uma representação muito mais detalhada da amplitude do sinal.

# Discussão

## Influência do número de bits

Cada bit adicional dobra a quantidade de níveis. Isso pode ser demonstrado pela relação:

$$
L = 2^N
$$

Mantendo $V_{\mathrm{ref}}$ constante, o aumento de um bit reduz aproximadamente pela metade o intervalo entre níveis:

$$
\Delta V = \frac{V_{\mathrm{ref}}}{2^N}
$$

Portanto, o aumento da resolução não ocorre de forma linear em relação ao número de bits.

## Influência da resolução

A resolução define o tamanho dos degraus de amplitude. Quanto menor for $\Delta V$, menor será a variação necessária para que o sistema disponha de um novo nível de representação.

Assim, aumentar $N$ resulta em:

$$
N \uparrow
\Rightarrow
\Delta V \downarrow
$$

Consequentemente, a representação da amplitude torna-se mais detalhada.

## Erro de quantização

O erro ocorre porque valores intermediários entre dois níveis precisam ser aproximados. Em um quantizador uniforme ideal, o erro máximo em módulo é aproximadamente:

$$
\left|e_q\right|_{\max}
=
\frac{\Delta V}{2}
$$

Portanto, aumentar o número de bits reduz $\Delta V$ e, consequentemente, reduz o limite máximo do erro de quantização.

## Comparação entre $3$, $4$ e $8$ bits

- **$3$ bits:** $8$ níveis, maior intervalo entre níveis e maior erro de quantização.
- **$4$ bits:** $16$ níveis, intervalo intermediário entre níveis e menor erro.
- **$8$ bits:** $256$ níveis, menor intervalo entre níveis e erro significativamente menor.

## Limitações

A simulação considera um quantizador uniforme ideal. Conversores reais podem apresentar erros de offset, ganho, não linearidade, ruído e outras limitações.

Além disso, quantização e aliasing são fenômenos diferentes. A quantização está relacionada à discretização da amplitude, enquanto o aliasing está associado à discretização temporal e à escolha inadequada da frequência de amostragem.

Assim, uma representação digital adequada depende tanto de uma frequência de amostragem compatível com as frequências presentes no sinal quanto de uma resolução de amplitude suficiente para representar as variações desejadas.