# Estabilidade no Plano z

---

# Resumo conceitual

Um sistema LTI discreto é estável BIBO quando sua resposta ao impulso é absolutamente somável. Para sistemas causais racionais, isso corresponde a polos estritamente dentro do círculo unitário.

---

# Formulação matemática

$$
\sum_n|h[n]|<\infty.\quad h[n]=a^nu[n]\Rightarrow\sum_{n=0}^{\infty}|a|^n=\frac{1}{1-|a|},\quad |a|<1.
$$

 Polos sobre o círculo unitário não satisfazem estabilidade BIBO em geral.

---

# Exemplo

Compare os polos do capítulo anterior, incluindo um caso instável, e confira a fórmula do impulso.

---

:::: {include} ./simulacao/simulacao_estabilidade_z.ipynb
::::

---

# Resultados

O polo 0,9 decai mais lentamente que 0,5 e a resposta de 1,1 cresce sem limite.

# Interpretação e Discussão

A análise de estabilidade não deve depender apenas de uma simulação curta. O critério analítico evita classificar um crescimento lento como estabilidade.

# Conclusões

O polo 0,9 decai mais lentamente que 0,5 e a resposta de 1,1 cresce sem limite.
