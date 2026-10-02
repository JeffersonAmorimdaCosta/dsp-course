# Convolução Discreta

---

# Resumo Conceitual

A convolução discreta é uma operação fundamental no processamento digital de sinais e na análise de sistemas LTI (Lineares e Invariantes no Tempo). Ela permite determinar a saída de um sistema a partir do sinal de entrada e de sua resposta ao impulso.

Para um sistema LTI, a saída $y[n]$ é determinada pela convolução entre o sinal de entrada $x[n]$ e a resposta ao impulso $h[n]$:

$$
y[n] = x[n] \ast h[n]
$$

A operação de convolução combina as amostras de dois sinais de maneira sistemática. Para cada posição $n$, uma sequência é invertida, deslocada, multiplicada amostra a amostra pela outra sequência e, por fim, os produtos são somados.

A convolução pode ser compreendida a partir das seguintes operações:

1. inversão;
2. deslocamento;
3. multiplicação;
4. soma.

Essas operações são realizadas para cada posição da saída, produzindo uma nova sequência que representa a resposta do sistema à entrada aplicada.

A convolução é especialmente importante para sistemas LTI porque, conhecendo $h[n]$, é possível determinar a resposta do sistema para diferentes sinais de entrada sem precisar analisar novamente toda a estrutura interna do sistema.

---

# Formulação Matemática

## Definição da Convolução Discreta

A convolução discreta entre dois sinais $x[n]$ e $h[n]$ é definida por:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

em que:

* $y[n]$ é o sinal de saída;
* $x[k]$ é o sinal de entrada;
* $h[n-k]$ é a resposta ao impulso invertida e deslocada;
* $k$ é o índice utilizado na soma;
* $n$ representa a posição da amostra de saída;
* $\ast$ representa a operação de convolução.

A notação compacta é:

$$
y[n] = x[n] \ast h[n]
$$

## Interpretação da Expressão $h[n-k]$

O termo $h[n-k]$ representa uma sequência que passa por duas operações.

Primeiramente, ocorre a inversão temporal:

$$
h[-k]
$$

Em seguida, a sequência é deslocada de acordo com o valor de $n$:

$$
h[n-k]
$$

Depois desse deslocamento, cada amostra de $h[n-k]$ é multiplicada pela amostra correspondente de $x[k]$.

Finalmente, os produtos são somados:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

Assim, cada valor de $y[n]$ é obtido pela soma dos produtos entre as amostras das duas sequências.

## Comprimento da Saída

Quando duas sequências de comprimento finito são convoluídas, o comprimento da saída é dado por:

$$
N_y = N_x + N_h - 1
$$

em que:

* $N_x$ é o número de amostras de $x[n]$;
* $N_h$ é o número de amostras de $h[n]$;
* $N_y$ é o número de amostras da sequência resultante $y[n]$.

Essa relação permite determinar antecipadamente o número de amostras da saída.

## Relação com Sistemas LTI

Para um sistema LTI, a resposta ao impulso $h[n]$ caracteriza o comportamento do sistema.

Se a entrada for:

$$
x[n]
$$

a saída será:

$$
y[n]
=
x[n]\ast h[n]
$$

ou, de forma expandida:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

Portanto, a convolução estabelece diretamente a relação entre entrada, resposta ao impulso e saída de um sistema LTI.

---

# Exemplo

Considere as sequências:

$$
x[n] = \{1,2,1\}
$$

e:

$$
h[n] = \{1,1\}
$$

Considerando o primeiro elemento de cada sequência em $n=0$, temos:

$$
x[0]=1,\quad x[1]=2,\quad x[2]=1
$$

e:

$$
h[0]=1,\quad h[1]=1
$$

## Determinação do Comprimento da Saída

A sequência de entrada possui:

$$
N_x=3
$$

amostras, enquanto a resposta ao impulso possui:

$$
N_h=2
$$

amostras.

Portanto:

$$
N_y=N_x+N_h-1
$$

Substituindo:

$$
N_y=3+2-1=4
$$

Logo, a saída terá quatro amostras.

## Cálculo Manual da Convolução

A saída é calculada pela expressão:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

### Para $n=0$

Somente a primeira amostra de cada sequência contribui:

$$
y[0]=x[0]h[0]
$$

$$
y[0]=(1)(1)=1
$$

### Para $n=1$

Duas combinações são possíveis:

$$
y[1]=x[0]h[1]+x[1]h[0]
$$

Substituindo os valores:

$$
y[1]=(1)(1)+(2)(1)
$$

$$
y[1]=1+2=3
$$

### Para $n=2$

As combinações são:

$$
y[2]=x[1]h[1]+x[2]h[0]
$$

Substituindo:

$$
y[2]=(2)(1)+(1)(1)
$$

$$
y[2]=2+1=3
$$

### Para $n=3$

Apenas a última combinação permanece:

$$
y[3]=x[2]h[1]
$$

Portanto:

$$
y[3]=(1)(1)=1
$$

Assim, a saída completa é:

$$
y[n]=\{1,3,3,1\}
$$

## Tabela do Cálculo

| $n$ | $y[n]$ |
| :---: | :------: |
|   0   |     1    |
|   1   |     3    |
|   2   |     3    |
|   3   |     1    |

Portanto:

$$
\boxed{
y[n]=\{1,3,3,1\}
}
$$

O resultado mostra como cada amostra da saída é formada pela soma dos produtos entre as amostras sobrepostas das duas sequências.

---

:::: {include} ./simulacao/simulacao_convolucao_discreta.ipynb
::::

---

# Resultados

Para o primeiro experimento, foram utilizadas as sequências:

$$
x[n]=\{1,2,1\}
$$

e:

$$
h[n]=\{1,1\}
$$

A função `np.convolve()` produziu:

$$
y[n]=\{1,3,3,1\}
$$

O resultado computacional coincide com o cálculo realizado manualmente.

A comparação pode ser apresentada pela tabela:

| $n$ | $x[n]$ | $h[n]$ | $y[n]$ |
| :---: | :------: | :------: | :------: |
|   0   |     1    |     1    |     1    |
|   1   |     2    |     1    |     3    |
|   2   |     1    |     0    |     3    |
|   3   |     0    |     0    |     1    |

O comprimento da saída também confirma a relação:

$$
N_y=N_x+N_h-1
$$

resultando em:

$$
N_y=3+2-1=4
$$

Portanto, a convolução produz quatro amostras na saída.

## Resultado com Alteração da Resposta ao Impulso

No segundo experimento, foi utilizada:

$$
h_2[n]=\{1,2\}
$$

mantendo:

$$
x[n]=\{1,2,1\}
$$

A nova convolução é:

$$
y_2[n]
=
x[n]\ast h_2[n]
$$

Realizando o cálculo:

$$
y_2[0]=(1)(1)=1
$$

$$
y_2[1]=(1)(2)+(2)(1)=4
$$

$$
y_2[2]=(2)(2)+(1)(1)=5
$$

$$
y_2[3]=(1)(2)=2
$$

Assim:

$$
y_2[n]=\{1,4,5,2\}
$$

A comparação entre as duas respostas é:

| $n$ | $y[n]$ com $h[n]=\{1,1\}$ | $y_2[n]$ com $h_2[n]=\{1,2\}$ |
| :---: | :---------------------------: | :-------------------------------: |
|   0   |               1               |                 1                 |
|   1   |               3               |                 4                 |
|   2   |               3               |                 5                 |
|   3   |               1               |                 2                 |

Os gráficos permitem visualizar tanto os sinais utilizados na convolução quanto a diferença entre as duas saídas.

---

# Discussão

## Interpretação da Convolução

A convolução pode ser interpretada como um processo de sobreposição entre duas sequências.

Para cada valor de $n$, a sequência $h[n-k]$ é invertida e deslocada. Em seguida, suas amostras são multiplicadas pelas amostras correspondentes de $x[k]$. A soma desses produtos determina o valor de $y[n]$.

Assim:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

representa matematicamente o processo de combinação entre os dois sinais.

## Comparação entre o Cálculo Manual e Computacional

O cálculo manual resultou em:

$$
y[n]=\{1,3,3,1\}
$$

A implementação computacional utilizando `np.convolve()` produziu o mesmo resultado:

$$
y[n]=\{1,3,3,1\}
$$

Isso confirma que a implementação computacional está de acordo com a definição matemática da convolução discreta.

A utilização de uma função pronta facilita a realização dos cálculos para sequências maiores, reduzindo a possibilidade de erros durante operações repetitivas.

## Efeito da Alteração de $h[n]$

No primeiro experimento:

$$
h[n]=\{1,1\}
$$

e a saída foi:

$$
y[n]=\{1,3,3,1\}
$$

Após modificar a resposta ao impulso para:

$$
h_2[n]=\{1,2\}
$$

a saída passou a ser:

$$
y_2[n]=\{1,4,5,2\}
$$

A mudança demonstra que a resposta ao impulso determina diretamente como o sistema transforma o sinal de entrada.

A segunda amostra de $h[n]$ foi aumentada de $1$ para $2$. Como essa amostra participa das combinações durante a convolução, os valores correspondentes da saída também foram modificados.

Esse comportamento é fundamental na análise de sistemas LTI: diferentes respostas ao impulso representam diferentes comportamentos de sistema.

## Comprimento da Saída

Nos dois experimentos, a entrada possui três amostras e a resposta ao impulso possui duas:

$$
N_x=3
$$

e:

$$
N_h=2
$$

Portanto:

$$
N_y=3+2-1=4
$$

A alteração dos valores de $h[n]$ modificou as amplitudes da saída, mas não alterou sua quantidade de amostras, pois os comprimentos das sequências permaneceram os mesmos.

## Relação com Sistemas LTI

A convolução é uma ferramenta fundamental para sistemas LTI porque permite determinar a saída de um sistema a partir de duas informações:

* o sinal de entrada $x[n]$;
* a resposta ao impulso $h[n]$.

A relação:

$$
y[n]=x[n]\ast h[n]
$$

resume essa característica.

Dessa forma, uma vez conhecida a resposta ao impulso de um sistema LTI, é possível calcular sua resposta para diferentes sinais de entrada utilizando a convolução discreta.

---

# Conclusões

O estudo da convolução discreta permitiu compreender como dois sinais podem ser combinados para produzir uma sequência de saída.

Foi apresentada a definição matemática:

$$
y[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k]
$$

e foram identificadas as principais operações envolvidas no processo: inversão, deslocamento, multiplicação e soma.

No exemplo analisado, a convolução entre:

$$
x[n]=\{1,2,1\}
$$

e:

$$
h[n]=\{1,1\}
$$

produziu:

$$
y[n]=\{1,3,3,1\}
$$

O cálculo manual e a implementação utilizando `np.convolve()` apresentaram o mesmo resultado, confirmando a correspondência entre a formulação matemática e a implementação computacional.

A alteração da resposta ao impulso para:

$$
h_2[n]=\{1,2\}
$$

produziu uma nova saída:

$$
y_2[n]=\{1,4,5,2\}
$$

demonstrando que mudanças em $h[n]$ modificam diretamente a resposta do sistema.

Assim, a convolução discreta constitui uma ferramenta fundamental para analisar sistemas LTI, permitindo relacionar de forma direta o sinal de entrada, a resposta ao impulso e o sinal de saída.
