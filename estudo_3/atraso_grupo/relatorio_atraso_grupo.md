# Atraso de Grupo

---

# Resumo conceitual

O atraso de grupo mede a inclinação negativa da fase e descreve o atraso de envoltórias estreitas em frequência. Sua constância na banda útil é relevante para preservar formas de onda.

---

# Formulação matemática

$$
\tau_g(\omega)=-\frac{d\phi}{d\omega},\qquad t_g=\tau_g/f_s.
$$

 A derivada em radianos por amostra resulta em amostras; dividir por fs fornece segundos.

---

# Exemplo

Compare os atrasos do FIR de 51 coeficientes e do IIR de ordem 4. Observe apenas a banda passante e exclua nulos da interpretação.

---

:::: {include} ./simulacao/simulacao_atraso_grupo.ipynb
::::

---

# Resultados

O FIR tem atraso de 25 amostras, equivalente a 25 ms a 1000 Hz. O atraso do IIR varia com a frequência.

# Interpretação e Discussão

O atraso de grupo não deve ser usado em regiões onde a magnitude é praticamente nula. Filtros de baixa latência podem justificar fase não linear, enquanto aquisição de pulsos pode exigir maior uniformidade de atraso.

# Conclusões

O FIR tem atraso de 25 amostras, equivalente a 25 ms a 1000 Hz. O atraso do IIR varia com a frequência.
