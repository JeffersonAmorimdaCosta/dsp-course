# Mini Projeto Integrador — Análise Multidomínio de um Sensor

---

# Resumo conceitual

O projeto investiga como a amostragem e a dinâmica de um sensor industrial alteram a identificação de duas componentes de vibração. O sinal é inteiramente sintético e permite conhecer a referência exata.

---

# Formulação matemática

$$
x(t)=\cos(2\pi10t)+0{,}5\cos(2\pi70t+\pi/4),\quad H(s)=\frac{1}{0{,}02s+1}.
$$

 Com retenção de ordem zero e $T_s=1/500$ s, $p=e^{-50T_s}$ e $H_d(z)=(1-p)z^{-1}/(1-pz^{-1})$. A equação é $y[n]=py[n-1]+(1-p)x[n-1]$.

---

# Exemplo

Observe 2 s a 500 Hz (Δf = 0,5 Hz), compare a aquisição a 100 Hz e estude um registro de 0,73 s para provocar vazamento. O modelo do sensor é um passa-baixas de primeira ordem com τ = 20 ms.

---

:::: {include} ./simulacao/simulacao_mini_projeto.ipynb
::::

---

# Resultados

O espectro identifica 10 e 70 Hz com amplitudes 1 e 0,5 e fases 0 e π/4. A aquisição a 100 Hz desloca 70 para 30 Hz. O polo do sensor é −50 s⁻¹, mapeado em 0,90484, e os ganhos contínuos são aproximadamente 0,623 e 0,113 nas duas frequências.

# Interpretação e Discussão

O tempo mostra a composição e os transientes, enquanto a frequência separa as componentes. A dinâmica do sensor reduz principalmente 70 Hz, mesmo com aquisição adequada. A discretização ZOH é exata para entradas constantes entre amostras; por isso sua saída pode diferir da resposta à entrada contínua senoidal. Hann e Hamming reduzem os lóbulos laterais do registro não coerente, à custa de largura do lóbulo principal. O modelo é estável nos dois planos e a observação de polos não substitui a análise de ganho e banda útil.

# Conclusões

O espectro identifica 10 e 70 Hz com amplitudes 1 e 0,5 e fases 0 e π/4. A aquisição a 100 Hz desloca 70 para 30 Hz. O polo do sensor é −50 s⁻¹, mapeado em 0,90484, e os ganhos contínuos são aproximadamente 0,623 e 0,113 nas duas frequências.
