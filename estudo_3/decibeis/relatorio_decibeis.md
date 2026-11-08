# Magnitude em Decibéis

---

# Resumo conceitual

A escala em decibéis expressa razões de forma logarítmica e facilita comparar ganhos muito diferentes. Relações de amplitude usam fator 20; razões de potência usam fator 10.

---

# Formulação matemática

$$
G_{dB}=20\log_{10}|H|,\quad |H|=10^{G_{dB}/20}.
$$

 Sob a mesma impedância, a potência é proporcional ao quadrado da amplitude.

---

# Exemplo

Converta 0, −3, −20 e −40 dB e represente a mesma média móvel em escala linear e logarítmica.

---

:::: {include} ./simulacao/simulacao_decibeis.ipynb
::::

---

# Resultados

As razões de amplitude são 1; 0,70795; 0,1 e 0,01. −3 dB corresponde aproximadamente à metade da potência.

# Interpretação e Discussão

Ganho negativo em dB significa atenuação, e não amplitude negativa. Nulos exatos corresponderiam a −∞ dB; o código aplica um piso apenas para permitir sua representação gráfica.

# Conclusões

As razões de amplitude são 1; 0,70795; 0,1 e 0,01. −3 dB corresponde aproximadamente à metade da potência.
