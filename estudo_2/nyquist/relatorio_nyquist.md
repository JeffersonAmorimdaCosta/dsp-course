# Teorema da Amostragem e Nyquist

---

# Resumo conceitual

A amostragem uniforme de um sinal limitado em banda permite reconstrução ideal quando as réplicas espectrais não se sobrepõem. O limite exato exige cuidado com fase e componentes na borda.

---

# Formulação matemática

$$
f_s>2f_{max},\qquad f_N=f_s/2.
$$

 A reconstrução ideal usa interpolação sinc e pressupõe um sinal limitado em banda e amostragem sem erros.

---

# Exemplo

Amostre uma senoide de 70 Hz a 500, 140 e 100 Hz. O caso de 140 Hz é o limite e deve ser comparado com uma senoide em quadratura.

---

:::: {include} ./simulacao/simulacao_nyquist.ipynb
::::

---

# Resultados

A 500 Hz o pico aparece em 70 Hz; a 100 Hz aparece em 30 Hz. A 140 Hz o cosseno alterna sinais, mas uma senoide de fase zero gera amostras praticamente nulas.

# Interpretação e Discussão

O limite de Nyquist não garante preservação de uma componente arbitrária exatamente na borda. Sistemas reais necessitam margem para a transição do filtro analógico antialiasing.

# Conclusões

A 500 Hz o pico aparece em 70 Hz; a 100 Hz aparece em 30 Hz. A 140 Hz o cosseno alterna sinais, mas uma senoide de fase zero gera amostras praticamente nulas.
