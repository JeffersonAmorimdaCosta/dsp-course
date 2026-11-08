# Polos, Zeros e Estabilidade no Plano s

---

# Resumo conceitual

Para sistemas contínuos causais racionais próprios, polos de transferência no semiplano esquerdo garantem estabilidade BIBO. Polos complexos produzem modos oscilatórios.

---

# Formulação matemática

$$
H(s)=K\frac{\prod_i(s-z_i)}{\prod_k(s-p_k)},\qquad h_p(t)=e^{pt}u(t).
$$

 Um polo $p=\sigma+j\Omega$ produz envoltória $e^{\sigma t}$ e oscilação de frequência angular $\Omega$.

---

# Exemplo

Compare polos −1, −5, +1 e −1 ± j4. Inclua um zero em −2 no sistema oscilatório para observar sua influência na resposta.

---

:::: {include} ./simulacao/simulacao_plano_s.ipynb
::::

---

# Resultados

O polo −5 decai mais rápido que −1. O polo +1 cresce. O par complexo produz oscilação amortecida e o zero modifica a forma da resposta.

# Interpretação e Discussão

O critério se refere aos polos da função de transferência sem cancelamentos ocultos. Estabilidade interna exige analisar também os modos do modelo de estados.

# Conclusões

O polo −5 decai mais rápido que −1. O polo +1 cresce. O par complexo produz oscilação amortecida e o zero modifica a forma da resposta.
