# Comparação FIR e IIR

---

# Resumo conceitual

FIR e IIR podem cumprir objetivos espectrais semelhantes com compromissos diferentes de ordem, fase e custo. A escolha depende também da latência e da precisão numérica.

---

# Formulação matemática

$$
H_{FIR}(z)=\sum_{k=0}^{50}b_kz^{-k},\qquad H_{IIR}(z)=B(z)/A(z).
$$

 Um FIR simétrico de 51 coeficientes tem atraso de 25 amostras. Na forma direta, o custo aproximado é $N_b+N_a-1$ multiplicações por amostra, com $a_0=1$ não multiplicado.

---

# Exemplo

Compare um FIR Hamming de 51 coeficientes com um Butterworth IIR de ordem 4, ambos passa-baixas com parâmetro de corte de 100 Hz e fs = 1000 Hz.

---

:::: {include} ./simulacao/simulacao_comparacao_fir_iir.ipynb
::::

---

# Resultados

O FIR tem ordem 50 e 51 multiplicações por amostra na implementação direta; o IIR tem ordem 4 e 9. O FIR apresenta atraso constante na banda e o IIR apresenta atraso dependente da frequência.

# Interpretação e Discussão

A comparação é ilustrativa: o parâmetro de corte em firwin corresponde aproximadamente a −6 dB e em Butterworth a −3 dB. Igualar esse parâmetro não iguala as especificações; o mini projeto compara soluções verificadas contra as mesmas bandas e tolerâncias.

# Conclusões

O FIR tem ordem 50 e 51 multiplicações por amostra na implementação direta; o IIR tem ordem 4 e 9. O FIR apresenta atraso constante na banda e o IIR apresenta atraso dependente da frequência.
