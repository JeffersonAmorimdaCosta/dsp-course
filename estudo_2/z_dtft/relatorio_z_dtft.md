# Relação entre Transformada Z e DTFT

---

# Resumo conceitual

A DTFT corresponde à avaliação da transformada Z sobre o círculo unitário quando esse círculo pertence à ROC. A distância aos polos e zeros ajuda a interpretar a magnitude.

---

# Formulação matemática

$$
H(e^{j\omega})=H(z)|_{z=e^{j\omega}},\qquad H(z)=\frac{1-z^{-1}}{1-0{,}8z^{-1}}.
$$

 O zero em z = 1 anula DC; a ROC causal $|z|>0{,}8$ inclui o círculo unitário.

---

# Exemplo

Analise b = [1, −1] e a = [1, −0,8] a fs = 1000 Hz. Compare a magnitude e o plano z.

---

:::: {include} ./simulacao/simulacao_z_dtft.ipynb
::::

---

# Resultados

A magnitude é zero em DC, e o plano z mostra o zero no ponto em que o círculo unitário cruza o eixo real positivo.

# Interpretação e Discussão

Não basta substituir formalmente z = eʲʷ: é necessário verificar a ROC. Um sistema causal instável pode ter uma expressão racional finita sobre parte do círculo sem possuir DTFT da resposta ao impulso.

# Conclusões

A magnitude é zero em DC, e o plano z mostra o zero no ponto em que o círculo unitário cruza o eixo real positivo.
