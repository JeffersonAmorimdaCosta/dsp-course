# Comparação de Métodos de Projeto

---

# Resumo conceitual

A comparação de métodos deve fixar as mesmas bandas e tolerâncias. Ordem menor, fase linear, atraso e robustez numérica são critérios complementares.

---

# Formulação matemática

$$
A_r=-\max_{f\ge f_r}20\log_{10}|H(f)|,\quad R_p=\max_{f\le f_p}G_{dB}-\min_{f\le f_p}G_{dB}.
$$

 A verificação usa grade de 32768 pontos; os extremos entre pontos podem diferir ligeiramente.

---

# Exemplo

Use fp = 80 Hz, fr = 150 Hz, fs = 1000 Hz, Ap = 1 dB e Ar = 40 dB; procure um comprimento FIR Hamming suficiente e compare quatro famílias IIR.

---

:::: {include} ./simulacao/simulacao_comparacao_metodos.ipynb
::::

---

# Resultados

A tabela calcula ordem, custo direto, ripple e atenuação obtidos. O FIR é selecionado por verificação explícita das bandas; os IIR são calculados para as mesmas tolerâncias.

# Interpretação e Discussão

Para um sensor com prioridade de baixo custo, um IIR é atraente. Se a preservação temporal for decisiva, a fase linear do FIR pode justificar mais coeficientes e atraso. A escolha final requer analisar também os sinais processados.

# Conclusões

A tabela calcula ordem, custo direto, ripple e atenuação obtidos. O FIR é selecionado por verificação explícita das bandas; os IIR são calculados para as mesmas tolerâncias.
