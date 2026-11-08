# Transformada Rápida de Fourier (FFT)

---

# Resumo conceitual

A FFT é uma família de algoritmos eficientes para calcular a DFT. O resultado matemático é o mesmo da soma direta; a diferença está na quantidade de operações.

---

# Formulação matemática

$$
X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}.
$$

 A soma direta exige ordem $N^2$ de operações; algoritmos FFT adequados exigem ordem $N\log_2N$. O erro comparado é $\max_k|X_{direta}[k]-X_{FFT}[k]|$.

---

# Exemplo

Compare N = 32, 64, 128 e 256 para uma senoide de 5 ciclos por registro. Os tempos são medianas de cinco execuções e dependem da máquina.

---

:::: {include} ./simulacao/simulacao_fft.ipynb
::::

---

# Resultados

A tabela apresenta o erro numérico e os tempos medidos. As duas implementações produzem coeficientes equivalentes dentro da tolerância de 10⁻⁹.

# Interpretação e Discussão

A FFT reduz o custo de calcular o mesmo espectro. Para registros pequenos, overhead e implementação em Python afetam a comparação; os tempos medidos não isolam apenas a complexidade assintótica.

# Conclusões

A tabela apresenta o erro numérico e os tempos medidos. As duas implementações produzem coeficientes equivalentes dentro da tolerância de 10⁻⁹.
