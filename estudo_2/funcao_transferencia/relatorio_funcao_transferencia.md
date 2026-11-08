# Função de Transferência Contínua

---

# Resumo conceitual

A função de transferência relaciona saída e entrada de um sistema LTI sob condições iniciais nulas. Ganho, constante de tempo, amortecimento e frequência natural controlam a resposta temporal.

---

# Formulação matemática

$$
H(s)=Y(s)/X(s),\quad H_1(s)=K/(\tau s+1),\quad H_2(s)=\omega_n^2/(s^2+2\zeta\omega_ns+\omega_n^2).
$$

 No primeiro caso, $\tau\dot y+y=Kx$ e a resposta ao degrau unitário é $K(1-e^{-t/\tau})u(t)$.

---

# Exemplo

Compare K = 1 e 2; τ = 0,2 e 1 s; ζ = 0,2, 0,7 e 1,2; ωn = 4 e 8 rad/s.

---

:::: {include} ./simulacao/simulacao_funcao_transferencia.ipynb
::::

---

# Resultados

O ganho determina o valor final da primeira ordem. Menor τ acelera a resposta. Baixo amortecimento provoca oscilação e sobressinal; maior ωn acelera a dinâmica.

# Interpretação e Discussão

A função de transferência não inclui a resposta livre produzida por condições iniciais não nulas. Comparar sistemas exige declarar tanto a entrada quanto as condições iniciais.

# Conclusões

O ganho determina o valor final da primeira ordem. Menor τ acelera a resposta. Baixo amortecimento provoca oscilação e sobressinal; maior ωn acelera a dinâmica.
