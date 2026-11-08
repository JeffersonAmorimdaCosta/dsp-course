# Aliasing

---

# Resumo conceitual

Aliasing é a ambiguidade entre frequências que produzem as mesmas amostras. Uma vez sobrepostas, essas contribuições não podem ser separadas apenas por filtragem digital posterior.

---

# Formulação matemática

$$
f_a=\left|((f_0+f_s/2)\bmod f_s)-f_s/2\right|.
$$

 Para cossenos reais, $\cos(2\pi70n/100)=\cos(2\pi30n/100)$.

---

# Exemplo

Compare um cosseno de 70 Hz com outro de 30 Hz, ambos amostrados a 100 Hz.

---

:::: {include} ./simulacao/simulacao_aliasing.ipynb
::::

---

# Resultados

As sequências coincidem dentro da precisão numérica e o espectro apresenta pico em 30 Hz.

# Interpretação e Discussão

Em sensores de vibração, aliasing pode ser interpretado como uma oscilação mecânica inexistente. A prevenção exige filtrar antes da aquisição e escolher fs com margem para a banda do sinal.

# Conclusões

As sequências coincidem dentro da precisão numérica e o espectro apresenta pico em 30 Hz.
