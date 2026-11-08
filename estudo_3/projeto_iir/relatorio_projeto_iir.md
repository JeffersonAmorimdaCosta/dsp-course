# Projeto de Filtros IIR

---

# Resumo conceitual

O projeto IIR aproxima especificações com famílias de funções racionais. Butterworth privilegia magnitude monotônica; Chebyshev I permite ripple na passagem; Chebyshev II permite ripple na rejeição; elíptico permite ripple nas duas bandas para obter transições mais seletivas.

---

# Formulação matemática

$$
H(z)=\frac{\sum_{k=0}^{M}b_kz^{-k}}{1+\sum_{k=1}^{N}a_kz^{-k}}.
$$

 Especificações: banda passante até $f_p$, rejeição a partir de $f_r$, perda máxima $A_p$ e atenuação mínima $A_r$.

---

# Exemplo

Compare Butterworth, Chebyshev I, Chebyshev II e elíptico para fs = 1000 Hz, fp = 80 Hz, fr = 150 Hz, Ap = 1 dB e Ar = 40 dB.

---

:::: {include} ./simulacao/simulacao_projeto_iir.ipynb
::::

---

# Resultados

As quatro famílias produzem respostas distintas para o mesmo conjunto de tolerâncias. A família elíptica tende a exigir menos coeficientes, com ripple e fase não linear.

# Interpretação e Discussão

A função de projeto calcula coeficientes para as especificações; cabe verificar bandas, polos e efeito temporal. Para ordens elevadas, seções de segunda ordem reduzem problemas numéricos da forma polinomial direta.

# Conclusões

As quatro famílias produzem respostas distintas para o mesmo conjunto de tolerâncias. A família elíptica tende a exigir menos coeficientes, com ripple e fase não linear.
