# Relação entre Laplace e Transformada Z

---

# Resumo conceitual

O mapeamento exponencial associa modos contínuos amostrados aos modos discretos. O semiplano esquerdo é levado ao interior do círculo unitário.

---

# Formulação matemática

$$
z=e^{sT_s}=e^{\sigma T_s}e^{j\Omega T_s}.
$$

 Para $s=-2$ e $T_s=0{,}1$ s, $z=e^{-0{,}2}\approx0{,}81873$. O mapeamento de polos não define sozinho toda a função de transferência discretizada.

---

# Exemplo

Compare s = −2, +1 e −1 ± j4 com Ts = 0,05; 0,1; 0,5 s.

---

:::: {include} ./simulacao/simulacao_laplace_z.ipynb
::::

---

# Resultados

Polos com parte real negativa permanecem dentro do círculo e o polo +1 fica fora dele. Aumentar Ts reduz o raio dos polos estáveis e aumenta o ângulo de modos oscilatórios.

# Interpretação e Discussão

O ângulo discreto é periódico: frequências contínuas separadas por múltiplos de 2π/Ts coincidem. Métodos como retenção de ordem zero também definem numerador e ganho; não se deve discretizar um sistema apenas substituindo polos.

# Conclusões

Polos com parte real negativa permanecem dentro do círculo e o polo +1 fica fora dele. Aumentar Ts reduz o raio dos polos estáveis e aumenta o ângulo de modos oscilatórios.
