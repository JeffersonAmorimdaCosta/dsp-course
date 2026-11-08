# Frequência Normalizada

---

# Resumo conceitual

A frequência discreta mede ciclos ou radianos por amostra. A conversão para hertz requer conhecer a taxa de amostragem.

---

# Formulação matemática

$$
f_n=f/f_s,\qquad \omega=2\pi f_n,\qquad f=\omega f_s/(2\pi).
$$

 Frequências separadas por $2\pi$ rad/amostra geram a mesma exponencial complexa discreta.

---

# Exemplo

Compare (f, fs) = (50, 1000), (100, 1000) e (50, 500), em hertz.

---

:::: {include} ./simulacao/simulacao_frequencia_normalizada.ipynb
::::

---

# Resultados

As frequências angulares são 0,1π, 0,2π e 0,2π rad/amostra. Os dois últimos sinais coincidem.

# Interpretação e Discussão

Uma sequência não determina sua frequência física sem fs. Metade da taxa de amostragem corresponde a π rad/amostra e a 0,5 ciclo/amostra.

# Conclusões

As frequências angulares são 0,1π, 0,2π e 0,2π rad/amostra. Os dois últimos sinais coincidem.
