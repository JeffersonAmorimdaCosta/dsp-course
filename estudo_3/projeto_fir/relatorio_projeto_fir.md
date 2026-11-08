# Projeto de Filtros FIR

---

# Resumo conceitual

O método de janelas aproxima uma resposta ideal infinita por coeficientes finitos. A janela controla os lóbulos laterais e o comprimento controla a largura da transição.

---

# Formulação matemática

$$
h_d[n]=2\frac{f_c}{f_s}\operatorname{sinc}\left(2\frac{f_c}{f_s}(n-M/2)\right),\quad h[n]=h_d[n]w[n].
$$

 Aqui sinc usa $\sin(\pi x)/(\pi x)$; a ordem é M e existem M+1 coeficientes.

---

# Exemplo

Projete passa-baixas de 100 Hz a fs = 1000 Hz, compare ordens 30 e 60 e janelas retangular, Hann, Hamming e Blackman.

---

:::: {include} ./simulacao/simulacao_projeto_fir.ipynb
::::

---

# Resultados

O comprimento maior estreita a transição. Janelas suaves reduzem lóbulos laterais em relação à retangular; os coeficientes são simétricos e somam aproximadamente 1.

# Interpretação e Discussão

A frequência fornecida a firwin indica meia amplitude aproximadamente, não meia potência. A validação deve medir a banda passante e a rejeição em uma grade densa, em vez de assumir atendimento com base apenas na janela.

# Conclusões

O comprimento maior estreita a transição. Janelas suaves reduzem lóbulos laterais em relação à retangular; os coeficientes são simétricos e somam aproximadamente 1.
