# Resposta em Frequência

---

# Resumo conceitual

A resposta em frequência especifica o ganho e a fase aplicados a cada senoide. A banda passante conserva componentes dentro de tolerâncias, e a banda de rejeição as atenua.

---

# Formulação matemática

$$
H(z)=\frac{1/3(1+z^{-1}+z^{-2})}{1},\quad h[n]=\tfrac13\{1,1,1\},\quad H(e^{j\omega})=\tfrac13(1+2\cos\omega)e^{-j\omega}.
$$

 Ripple é a variação de ganho na banda; seletividade descreve a rapidez da transição. A frequência de corte precisa de uma convenção, frequentemente −3 dB.

---

# Exemplo

Analise a média móvel de três amostras a fs = 1000 Hz. Identifique ganho em DC, primeiro nulo e fase.

---

:::: {include} ./simulacao/simulacao_resposta_frequencia.ipynb
::::

---

# Resultados

O ganho em DC é 1 e o primeiro nulo ocorre em 333,33 Hz. A fase é linear por trechos, com saltos de π associados a mudanças de sinal da parcela real.

# Interpretação e Discussão

Um passa-baixas real não possui uma única fronteira perfeita: a transição separa as bandas especificadas. O nulo de uma média móvel não é a mesma coisa que sua frequência de corte.

# Conclusões

O ganho em DC é 1 e o primeiro nulo ocorre em 333,33 Hz. A fase é linear por trechos, com saltos de π associados a mudanças de sinal da parcela real.
