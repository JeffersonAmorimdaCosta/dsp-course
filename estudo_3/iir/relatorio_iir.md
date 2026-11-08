# Filtros IIR

---

# Resumo conceitual

Filtros IIR usam realimentação para produzir uma resposta ao impulso teoricamente infinita. Poucos coeficientes podem gerar memória longa, mas a estabilidade depende dos polos.

---

# Formulação matemática

$$
y[n]=0{,}8y[n-1]+0{,}2x[n],\quad H(z)=\frac{0{,}2}{1-0{,}8z^{-1}},\quad h[n]=0{,}2(0{,}8)^nu[n].
$$

 Há um polo em 0,8 e um zero em 0 ao escrever $H(z)=0{,}2z/(z-0{,}8)$.

---

# Exemplo

Analise o filtro recursivo de primeira ordem, com repouso inicial e fs = 1000 Hz.

---

:::: {include} ./simulacao/simulacao_iir.ipynb
::::

---

# Resultados

A resposta decai exponencialmente sem se tornar exatamente nula. O ganho em DC é 1, o polo está dentro do círculo e a fase é não linear.

# Interpretação e Discussão

A primeira ordem exige duas multiplicações por amostra na forma direta. A economia de coeficientes vem acompanhada de realimentação e maior atenção a arredondamento, saturação e estabilidade.

# Conclusões

A resposta decai exponencialmente sem se tornar exatamente nula. O ganho em DC é 1, o polo está dentro do círculo e a fase é não linear.
