# Mini Projeto Integrador — Tratamento Digital de um Sensor

---

# Resumo conceitual

O problema é reduzir uma interferência de 200 Hz em um sensor preservando a componente útil de 40 Hz. A origem dos dados é um modelo matemático com ruído pseudoaleatório reproduzível, sem uso de medições reais.

---

# Formulação matemática

$$
x_{ref}[n]=\cos(2\pi40n/1000),\quad x[n]=x_{ref}[n]+0{,}6\cos(2\pi200n/1000)+r[n].
$$

 Define-se $f_p=80$ Hz, $f_r=150$ Hz, perda máxima de 1 dB e rejeição mínima de 40 dB. As métricas são $MSE=N^{-1}\sum_n(y[n]-x_{ref}[n])^2$, $SNR=10\log_{10}(\sum x_{ref}^2/\sum(y-x_{ref})^2)$ e ganho na componente de interesse.

---

# Exemplo

O sinal dura 4 s a fs = 1000 Hz (Δf = 0,25 Hz), com ruído gaussiano de desvio 0,1 e semente 42. A banda passante até 80 Hz inclui 40 Hz com margem. A rejeição começa antes de 200 Hz, permitindo transição de 70 Hz. Compare FIR Hamming de comprimento ímpar escolhido por validação com IIR Butterworth de ordem calculada.

---

:::: {include} ./simulacao/simulacao_mini_projeto.ipynb
::::

---

# Resultados

A tabela gerada registra as ordens efetivas, coeficientes, custo direto, atenuação, ripple, limites de atraso de grupo, ganho em 40 Hz, ganho em 200 Hz, MSE e SNR. As duas soluções são verificadas por assertions para a mesma especificação. Os gráficos mostram impulso, polos e zeros, magnitude, fase, atraso e sinais antes e depois da filtragem.


Os valores abaixo foram obtidos na execução com semente 42. Os custos referem-se à forma direta geral, sem explorar simetria; a execução IIR usa quatro seções de segunda ordem, com aproximadamente 20 multiplicações e 16 somas por amostra e 20 coeficientes não triviais armazenados.

| Grandeza | FIR Hamming | IIR Butterworth |
|---|---:|---:|
| Ordem | 44 | 8 |
| Coeficientes na forma direta, sem a₀ | 45 | 17 |
| Multiplicações por amostra, forma direta | 45 | 17 |
| Somas por amostra, forma direta | 44 | 16 |
| Rejeição mínima a partir de 150 Hz | 43,33 dB | 41,76 dB |
| Ripple até 80 Hz | 0,078 dB | 0,998 dB |
| Atraso de grupo na passagem | 22 amostras | 9,17 a 17,23 amostras |
| Alinhamento usado na métrica | 22 amostras | 9 amostras |
| Ganho de amplitude em 40 Hz | 0,99906 | 0,999998 |
| Ganho em 200 Hz | −63,00 dB | −66,41 dB |
| MSE sem alinhar | 0,27232 | 1,72478 |
| MSE alinhado | 0,002253 | 0,008750 |
| SNR alinhada | 23,47 dB | 17,57 dB |
| Fase linear | Sim | Não |
| Estabilidade causal | Estável | Estável |

A entrada apresenta MSE de 0,18871 e SNR de 4,23 dB. As duas soluções melhoram a SNR alinhada e atendem às bandas especificadas. O FIR produz menor erro alinhado, enquanto o IIR exige menos operações e menor atraso na região de 40 Hz. A rejeição de 200 Hz é superior à rejeição mínima de banda, pois esta considera o pior ponto a partir de 150 Hz.

# Interpretação e Discussão

O FIR tem coeficientes simétricos e atraso constante, enquanto o Butterworth causal tem menor ordem e atraso variável. A interferência de 200 Hz é atenuada segundo os ganhos medidos e o ganho de 40 Hz quantifica a preservação. MSE e SNR são calculados após excluir 500 amostras de transiente e alinhar a componente útil; também se informa o MSE sem alinhamento para não esconder a latência. O alinhamento do IIR usa fase em 40 Hz arredondada para amostras inteiras: é adequado à referência monofrequencial, mas não corrige a distorção de fase de um sinal de banda larga. Para este sensor com informação concentrada em 40 Hz, a escolha é o IIR por menor custo e latência; para pulsos cuja forma importa, o FIR merece preferência. A avaliação usa precisão de ponto flutuante, ruído estacionário e uma grade espectral finita; hardware com quantização dos coeficientes e sinais não estacionários exige nova validação.

# Conclusões

As soluções FIR de ordem 44 e Butterworth de ordem 8 atendem à perda máxima de 1 dB e à rejeição mínima de 40 dB. A SNR aumenta de 4,23 dB para 23,47 dB no FIR e 17,57 dB no IIR após o alinhamento descrito. A escolha do IIR prioriza custo e latência; a escolha do FIR prioriza fase linear e o menor erro obtido neste experimento. Nenhuma dessas conclusões dispensa a validação para outro sinal ou implementação numérica.
