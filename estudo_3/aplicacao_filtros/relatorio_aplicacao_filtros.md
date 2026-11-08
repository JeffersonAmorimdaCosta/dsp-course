# Aplicação de Filtros a Sinais

---

# Resumo conceitual

A análise espectral deve preceder o projeto: identificar sinal útil e interferência permite justificar o tipo e as bandas do filtro. A aplicação causal também introduz transientes e atraso.

---

# Formulação matemática

$$
x[n]=\cos(2\pi40n/f_s)+0{,}6\cos(2\pi200n/f_s)+r[n],\quad Y=XH.
$$

 O objetivo é preservar 40 Hz e reduzir 200 Hz, com ruído gaussiano de desvio padrão 0,1.

---

# Exemplo

Gere 4 s a 1000 Hz com semente 42 e aplique um FIR Hamming de 61 coeficientes com parâmetro de corte de 115 Hz.

---

:::: {include} ./simulacao/simulacao_aplicacao_filtros.ipynb
::::

---

# Resultados

O espectro mostra preservação de 40 Hz e forte redução de 200 Hz. O sinal temporal filtrado aparece deslocado por 30 amostras.

# Interpretação e Discussão

O atraso não deve ser confundido com erro de amplitude. Para medir erro em relação à referência, é necessário alinhar os sinais e excluir o transiente; o mini projeto apresenta esse procedimento para FIR e IIR.

# Conclusões

O espectro mostra preservação de 40 Hz e forte redução de 200 Hz. O sinal temporal filtrado aparece deslocado por 30 amostras.
