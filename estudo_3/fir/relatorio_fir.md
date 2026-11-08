# Filtros FIR

---

# Resumo conceitual

Filtros FIR possuem resposta ao impulso finita e podem ser implementados por uma soma de entradas atrasadas. Coeficientes finitos garantem estabilidade BIBO; simetria permite fase linear.

---

# Formulação matemática

$$
y[n]=\sum_{k=0}^{M-1}b_kx[n-k],\quad H(z)=\sum_{k=0}^{M-1}b_kz^{-k}.
$$

 Na média móvel $b_k=1/M$, a ordem é $M-1$, o atraso é $(M-1)/2$ amostras e o primeiro nulo ocorre em $f_s/M$.

---

# Exemplo

Compare M = 3, 5 e 10. Observe os coeficientes, polos na origem e zeros sobre o círculo unitário, exceto z = 1.

---

:::: {include} ./simulacao/simulacao_fir.ipynb
::::

---

# Resultados

Os primeiros nulos são 333,33; 200 e 100 Hz. Os atrasos são 1; 2 e 4,5 amostras. A soma dos coeficientes é 1 em todos os casos.

# Interpretação e Discussão

O comprimento maior estreita o lóbulo principal, mas a média móvel tem rejeição limitada nos lóbulos laterais. Os polos na origem aparecem ao escrever H como uma razão de polinômios em z; eles representam atrasos e não instabilidade.

# Conclusões

Os primeiros nulos são 333,33; 200 e 100 Hz. Os atrasos são 1; 2 e 4,5 amostras. A soma dos coeficientes é 1 em todos os casos.
