# Fase e Atraso

---

# Resumo conceitual

A fase descreve o deslocamento angular aplicado a cada componente. Uma fase linear impõe um atraso comum; fase não linear pode alterar a forma de sinais compostos mesmo quando as amplitudes são preservadas.

---

# Formulação matemática

$$
\phi(\omega)=-\omega n_0+\phi_0,\qquad b_k=b_{M-k}\Rightarrow n_0=M/2.
$$

 Em regiões sem zeros, um FIR simétrico apresenta fase linear por trechos, podendo existir saltos de π.

---

# Exemplo

Compare o FIR simétrico de ordem 50 e o IIR Butterworth de ordem 4 a fs = 1000 Hz.

---

:::: {include} ./simulacao/simulacao_fase_atraso.ipynb
::::

---

# Resultados

O FIR possui inclinação de fase correspondente a 25 amostras de atraso; o IIR tem inclinação variável.

# Interpretação e Discussão

Não se interpreta fase em nulos de magnitude. Em sinais de pulso ou formas de onda com várias componentes, atrasos diferentes por frequência podem modificar o formato temporal.

# Conclusões

O FIR possui inclinação de fase correspondente a 25 amostras de atraso; o IIR tem inclinação variável.
