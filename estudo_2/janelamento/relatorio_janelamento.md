# Janelamento e Vazamento Espectral

---

# Resumo conceitual

O recorte temporal multiplica o sinal por uma janela e espalha sua representação espectral. Janelas suaves reduzem lóbulos laterais, mas alargam o lóbulo principal.

---

# Formulação matemática

$$
x_w[n]=x[n]w[n],\qquad X_w(e^{j\omega})=\frac{1}{2\pi}(X*W)(e^{j\omega}).
$$

 Para uma senoide isolada longe de DC e Nyquist, a amplitude unilateral é estimada por $2|X_w[k]|/\sum_n w[n]$.

---

# Exemplo

Use 256 amostras a 1024 Hz de uma senoide de 100,5 Hz e compare retangular, Hann, Hamming e Blackman. O preenchimento com zeros serve apenas para visualizar os lóbulos.

---

:::: {include} ./simulacao/simulacao_janelamento.ipynb
::::

---

# Resultados

A janela retangular tem lóbulo principal estreito e lóbulos laterais elevados. Hann e Hamming reduzem os lóbulos laterais; Blackman amplia mais o lóbulo principal.

# Interpretação e Discussão

O ganho coerente deve ser compensado para comparar amplitudes. Componentes próximas podem se fundir após o janelamento; menor vazamento não significa automaticamente maior capacidade de separação.

# Conclusões

A janela retangular tem lóbulo principal estreito e lóbulos laterais elevados. Hann e Hamming reduzem os lóbulos laterais; Blackman amplia mais o lóbulo principal.
