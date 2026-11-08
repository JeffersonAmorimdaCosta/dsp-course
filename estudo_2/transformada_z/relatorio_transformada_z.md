# Transformada Z

---

# Resumo conceitual

A transformada Z estende a análise de Fourier para além do círculo unitário. Ela converte atrasos e equações de diferenças em relações algébricas.

---

# Formulação matemática

$$
X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n},\quad z=re^{j\omega}.
$$

 Pares elementares: $\delta[n]\leftrightarrow1$; $u[n]\leftrightarrow1/(1-z^{-1})$, $|z|>1$; $a^nu[n]\leftrightarrow1/(1-az^{-1})$, $|z|>|a|$.

---

# Exemplo

Use a = 0,8 e compare a soma finita de 100 termos com a fórmula analítica em z = 1,2eʲʷ.

---

:::: {include} ./simulacao/simulacao_transformada_z.ipynb
::::

---

# Resultados

A soma truncada aproxima a expressão racional porque |a/z| < 1 em todos os pontos avaliados.

# Interpretação e Discussão

A convergência depende do raio r. Um valor finito calculado pela expressão racional fora da ROC é uma continuação algébrica e não prova convergência da série.

# Conclusões

A soma truncada aproxima a expressão racional porque |a/z| < 1 em todos os pontos avaliados.
