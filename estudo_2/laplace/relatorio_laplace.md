# Transformada de Laplace

---

# Resumo conceitual

A transformada de Laplace representa sinais contínuos por exponenciais complexas. A parte real de s controla crescimento ou decaimento e a parte imaginária descreve oscilação.

---

# Formulação matemática

$$
X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}\,dt,\quad s=\sigma+j\Omega.
$$

 Para $e^{-at}u(t)$, $X(s)=1/(s+a)$ e $\operatorname{Re}s>-a$. Para $e^{-at}\sin(bt)u(t)$, $X(s)=b/((s+a)^2+b^2)$, na mesma ROC.

---

# Exemplo

Analise e⁻²ᵗu(t) e e⁻ᵗsen(4t)u(t). A primeira integral é ∫₀∞e⁻⁽ˢ⁺²⁾ᵗdt = 1/(s+2); a segunda decorre da decomposição do seno em duas exponenciais.

---

:::: {include} ./simulacao/simulacao_laplace.ipynb
::::

---

# Resultados

A primeira sequência decai sem oscilar, com constante de tempo 0,5 s. A segunda oscila a 4 rad/s sob envoltória de constante de tempo 1 s.

# Interpretação e Discussão

Os polos explicam simultaneamente velocidade de decaimento e oscilação. A expressão racional precisa da ROC para determinar o sinal bilateral; as hipóteses causais são explicitadas nos exemplos.

# Conclusões

A primeira sequência decai sem oscilar, com constante de tempo 0,5 s. A segunda oscila a 4 rad/s sob envoltória de constante de tempo 1 s.
