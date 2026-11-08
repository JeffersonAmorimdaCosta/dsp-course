# Polos, Zeros e Resposta em Frequência

---

# Resumo conceitual

A magnitude depende das distâncias do círculo unitário aos zeros e polos. Um zero sobre esse círculo produz um nulo; um polo próximo produz uma região de maior ganho e memória longa.

---

# Formulação matemática

$$
|H(e^{j\omega})|=|K|\frac{\prod_i|e^{j\omega}-z_i|}{\prod_k|e^{j\omega}-p_k|}.
$$

 Para um rejeita-faixa em $\omega_0$, o numerador pode ser $1-2\cos\omega_0z^{-1}+z^{-2}$; polos com raio r controlam a largura.

---

# Exemplo

Construa filtros com zeros em e±ʲ⁰˒⁴π e polos no mesmo ângulo com raios 0,5 e 0,95. Normalize o ganho em DC.

---

:::: {include} ./simulacao/simulacao_polos_zeros.ipynb
::::

---

# Resultados

O nulo ocorre em 200 Hz. Com raio 0,95, a rejeição fica mais estreita e a resposta ao impulso demora mais para decair.

# Interpretação e Discussão

A geometria ajuda a prever a forma do espectro, mas o ganho K precisa ser considerado para comparar amplitudes absolutas. Polos muito próximos do círculo também aumentam a sensibilidade à precisão dos coeficientes.

# Conclusões

O nulo ocorre em 200 Hz. Com raio 0,95, a rejeição fica mais estreita e a resposta ao impulso demora mais para decair.
