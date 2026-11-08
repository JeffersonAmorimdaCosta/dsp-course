# Resolução Espectral

---

# Resumo conceitual

A duração de observação limita a separação de frequências próximas. O preenchimento com zeros aumenta a densidade do gráfico, mas não acrescenta informação ao registro.

---

# Formulação matemática

$$
\Delta f=\frac{f_s}{N}=\frac{1}{T_{obs}}.
$$

 Aqui $T_{obs}=N/f_s$ é a duração do registro. A resolução efetiva depende também da largura do lóbulo principal da janela.

---

# Exemplo

Use fs = 1024 Hz, frequências de 100 e 108 Hz e N = 64, 256 e 1024. Compare ainda N = 64 preenchido com zeros até 1024.

---

:::: {include} ./simulacao/simulacao_resolucao_espectral.ipynb
::::

---

# Resultados

Os espaçamentos são 16, 4 e 1 Hz. O registro de 1024 amostras separa claramente as componentes de 100 e 108 Hz.

# Interpretação e Discussão

O registro curto não oferece a mesma separação mesmo após o preenchimento com zeros. Aumentar N melhora a resolução somente quando aumenta o tempo efetivamente observado.

# Conclusões

Os espaçamentos são 16, 4 e 1 Hz. O registro de 1024 amostras separa claramente as componentes de 100 e 108 Hz.
