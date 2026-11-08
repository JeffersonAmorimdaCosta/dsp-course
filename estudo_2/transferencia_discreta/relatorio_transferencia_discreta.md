# Função de Transferência Discreta

---

# Resumo conceitual

Sob repouso inicial, a função de transferência discreta relaciona entrada e saída no domínio Z. O denominador descreve a realimentação e seus polos determinam os modos naturais.

---

# Formulação matemática

$$
y[n]=ay[n-1]+x[n]\Rightarrow H(z)=\frac{Y(z)}{X(z)}=\frac{1}{1-az^{-1}},\quad h[n]=a^nu[n].
$$

 A ROC causal é $|z|>|a|$.

---

# Exemplo

Simule o sistema do guia com a = 0,8 e compare polos 0,5, 0,9, 1,1 e −0,8, com entrada impulso e memória inicialmente nula.

---

:::: {include} ./simulacao/simulacao_transferencia_discreta.ipynb
::::

---

# Resultados

Os polos positivos menores que 1 produzem decaimento; −0,8 produz alternância de sinais e 1,1 produz crescimento.

# Interpretação e Discussão

Polos mais próximos do círculo unitário prolongam a memória. Um polo negativo estável não é instável por oscilar: o que importa é o módulo.

# Conclusões

Os polos positivos menores que 1 produzem decaimento; −0,8 produz alternância de sinais e 1,1 produz crescimento.
