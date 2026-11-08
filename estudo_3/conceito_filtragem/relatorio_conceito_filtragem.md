# Conceito de Filtragem Digital

---

# Resumo conceitual

Filtrar é modificar seletivamente componentes de um sinal. Passa-baixas suaviza sensores, passa-altas remove deriva, passa-faixa seleciona uma banda de vibração e rejeita-faixa remove interferência localizada.

---

# Formulação matemática

$$
y[n]=x[n]*h[n],\qquad Y(e^{j\omega})=X(e^{j\omega})H(e^{j\omega}).
$$

 Um filtro ideal tem magnitude 1 na banda preservada e 0 na banda removida; transições abruptas exigem resposta ao impulso infinita e, em geral, não causal.

---

# Exemplo

Represente os quatro tipos ideais a fs = 1000 Hz, com limites de 100 e 200 Hz.

---

:::: {include} ./simulacao/simulacao_conceito_filtragem.ipynb
::::

---

# Resultados

As quatro máscaras mostram as bandas preservadas e rejeitadas. A resposta ideal estabelece um objetivo de projeto, sem fornecer uma implementação causal finita.

# Interpretação e Discussão

Filtros realizáveis têm transição, ripple, atraso e atenuação finita. A seleção depende da faixa que contém informação útil e daquela que contém interferência.

# Conclusões

As quatro máscaras mostram as bandas preservadas e rejeitadas. A resposta ideal estabelece um objetivo de projeto, sem fornecer uma implementação causal finita.
