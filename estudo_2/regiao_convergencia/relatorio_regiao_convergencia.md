# Região de Convergência (ROC)

---

# Resumo conceitual

A ROC faz parte da definição da transformada Z. A mesma expressão racional pode representar uma sequência causal ou anticausal, conforme a região escolhida.

---

# Formulação matemática

$$
\frac{1}{1-az^{-1}}\leftrightarrow a^nu[n],\ |z|>|a|;\qquad \frac{1}{1-az^{-1}}\leftrightarrow-a^nu[-n-1],\ |z|<|a|.
$$

 A estabilidade exige que a ROC inclua o círculo unitário.

---

# Exemplo

Para a = 0,8, a sequência causal é estável; a anticausal cresce para n negativo e sua ROC não contém |z| = 1.

---

:::: {include} ./simulacao/simulacao_regiao_convergencia.ipynb
::::

---

# Resultados

As duas sequências têm a mesma forma racional, mas suportes temporais e comportamentos de estabilidade diferentes.

# Interpretação e Discussão

Um gráfico com número finito de termos não prova convergência. A prova decorre da série geométrica: |a/z| < 1 para o caso causal e |z/a| < 1 para o anticausal.

# Conclusões

As duas sequências têm a mesma forma racional, mas suportes temporais e comportamentos de estabilidade diferentes.
