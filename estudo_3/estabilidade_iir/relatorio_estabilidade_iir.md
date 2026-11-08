# Estabilidade dos Filtros IIR

---

# Resumo conceitual

A estabilidade BIBO de um filtro causal racional exige todos os polos estritamente dentro do círculo unitário. A proximidade à borda aumenta o tempo de acomodação.

---

# Formulação matemática

$$
h[n]=p^nu[n],\qquad |p|<1\Rightarrow \sum_{n=0}^{\infty}|h[n]|=1/(1-|p|).
$$

 O tempo para atingir 1% da amplitude inicial é aproximadamente $\ln(0{,}01)/\ln|p|$ amostras.

---

# Exemplo

Compare p = 0,5; 0,9; 0,99 e 1,05 com entrada impulso.

---

:::: {include} ./simulacao/simulacao_estabilidade_iir.ipynb
::::

---

# Resultados

Os três primeiros casos são estáveis; 1,05 é instável. Para 0,99 são necessárias cerca de 459 amostras para atingir 1% da amplitude inicial.

# Interpretação e Discussão

Uma resposta lenta pode parecer constante em uma janela curta. A verificação analítica dos polos deve acompanhar a simulação; um polo em 1 não é estritamente estável BIBO.

# Conclusões

Os três primeiros casos são estáveis; 1,05 é instável. Para 0,99 são necessárias cerca de 459 amostras para atingir 1% da amplitude inicial.
