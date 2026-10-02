# Mini Projeto Integrador — Parte 1

## 1. Objetivo e fenômeno escolhido

O projeto simula a aquisição e o processamento do deslocamento vibratório de uma máquina, integrando modelagem de sinais, amostragem, quantização, ruído, sistemas LTI e convolução. O objetivo é avaliar como cada etapa modifica a informação adquirida e o compromisso entre redução de ruído e preservação da vibração.

O fenômeno é representado por uma oscilação principal e uma terceira harmônica. Os valores foram escolhidos para fins didáticos e não representam uma máquina medida em laboratório.

## 2. Formulação matemática e parâmetros

O modelo é

$$
x(t)=A_1\cos(2\pi f_1t+\phi_1)+A_2\cos(2\pi f_2t+\phi_2).
$$

| Parâmetro | Valor | Significado |
| :--- | :--- | :--- |
| $A_1$ | 1 mm | Amplitude do deslocamento principal |
| $A_2$ | 0,25 mm | Amplitude da terceira harmônica |
| $f_1$ e $f_2$ | 5 Hz e 15 Hz | Frequências das oscilações |
| $\phi_1$ e $\phi_2$ | 0 e $\pi/4$ rad | Fases iniciais |
| Observação | 2 s | Duração do registro |
| $f_s$ | 200 Hz | Frequência de aquisição escolhida |
| $T_s=1/f_s$ | 5 ms | Intervalo entre amostras |
| Resoluções | 4 e 8 bits | 16 e 256 níveis de quantização |
| Faixa do conversor | −1,5 a +1,5 mm | Limites dos níveis representáveis |
| $\sigma$ | 0,15 mm | Desvio padrão do ruído gaussiano |
| $M$ | 5 amostras | Comprimento da média móvel |

A cadeia principal utiliza

$$
x(t)\ \longrightarrow\ x[n]=x(nT_s)\ \longrightarrow\ q_8[n]\ \longrightarrow\ x_r[n]=q_8[n]+r[n]\ \longrightarrow\ y[n]=(x_r*h)[n].
$$

O ramo de 4 bits permite comparar resoluções. A amostragem a 20 Hz é um segundo experimento para evidenciar aliasing. O ruído é adicionado ao sinal quantizado, seguindo a ordem das etapas do roteiro; uma aquisição física com ruído no sensor exigiria adicioná-lo antes do conversor.

## 3. Simulação e resultados

O notebook abaixo contém o código completo, os gráficos de todos os estágios e as respectivas interpretações. A semente do gerador de ruído é fixa, permitindo reproduzir as tabelas e os gráficos. A execução sequencial requer as dependências já utilizadas no projeto: NumPy, Matplotlib, pandas e Jupyter.

:::: {include} ./simulacao/simulacao_mini_projeto.ipynb
::::

### Síntese quantitativa do experimento

Os valores abaixo foram obtidos com a semente 42. Os erros da comparação entre entrada e saída usam a mesma região interior do registro e compensam o atraso de duas amostras da saída.

| Medida | Resultado |
| :--- | ---: |
| RMSE da entrada contaminada versus sinal ideal | 0,143093 mm |
| RMSE da saída alinhada versus sinal ideal | 0,077124 mm |
| RMSE da referência filtrada versus ideal (distorção) | 0,040420 mm |
| Desvio padrão do ruído na entrada | 0,142673 mm |
| Desvio padrão do ruído na saída, sem bordas | 0,063830 mm |
| Desvio padrão teórico do ruído filtrado | 0,067082 mm |

A redução do erro total é observada para esta realização de ruído e estes parâmetros. O erro da referência filtrada mostra que uma parcela da diferença permanece mesmo sem ruído, devido à atenuação das componentes úteis.

## 4. Discussão integradora

### 4.1 Como o fenômeno foi representado matematicamente?

O deslocamento foi modelado pela soma de dois cossenos de 5 e 15 Hz. As amplitudes determinam a contribuição de cada oscilação em milímetros, as frequências controlam a repetição temporal e as fases determinam a condição inicial. A harmônica modifica a forma de onda, permitindo observar se o processamento preserva apenas a oscilação principal ou também os detalhes.

### 4.2 Como a escolha de $f_s$ modificou a representação?

Com 200 Hz, a frequência máxima de 15 Hz fica abaixo de $f_s/2=100$ Hz e o modelo ideal atende à condição de Nyquist. Com 20 Hz, a componente de 15 Hz sofre aliasing e se confunde com uma oscilação de 5 Hz. Essa perda ocorre na aquisição e não pode ser corrigida pelo filtro posterior. A malha densa do gráfico apenas aproxima visualmente o sinal contínuo.

### 4.3 Qual foi o efeito da quantização?

A quantização substituiu os valores reais das amostras pelos níveis disponíveis no conversor. Isso produz um erro determinístico dependente dos valores de entrada. Sem saturação, o arredondamento limita seu módulo a $\Delta_N/2$. Não se pressupõe que esse erro seja branco ou independente do sinal.

### 4.4 Como o número de bits afetou o resultado?

O aumento de 4 para 8 bits elevou o número de níveis de 16 para 256 e reduziu o passo de 0,2 mm para aproximadamente 0,011765 mm. Os gráficos e a tabela de erros mostram a aproximação mais precisa com 8 bits. Maior resolução aumenta a precisão de amplitude, mas não resolve aliasing nem elimina perturbações adicionadas depois da quantização.

### 4.5 Qual foi o efeito do ruído?

O ruído de média zero introduziu irregularidades rápidas sobre o registro. Foi escolhido um modelo gaussiano independente com desvio padrão de 0,15 mm para representar perturbações aleatórias idealizadas. Uma realização finita não tem média exatamente zero, e a amplitude instantânea não é limitada pelo desvio padrão.

### 4.6 Qual é a resposta ao impulso?

A resposta é $h[n]=1/5$ para $n=0,1,2,3,4$ e zero nos demais índices. Sua soma é 1, preservando a componente constante em regime permanente. A saída é a média da amostra atual e das quatro anteriores.

### 4.7 Por que o sistema é LTI?

Se $\mathcal{T}\{x\}=x*h$, então $\mathcal{T}\{a x_1+b x_2\}=a(x_1*h)+b(x_2*h)$, o que demonstra linearidade. Para uma entrada deslocada $x[n-n_0]$, a saída é $y[n-n_0]$, porque a resposta ao impulso é fixa, demonstrando invariância no tempo. Essas propriedades pertencem ao filtro; a cadeia completa com quantização não é linear.

### 4.8 Qual foi o efeito da convolução?

A convolução aplicou a média móvel ao registro, suavizando variações e introduzindo atraso de duas amostras, equivalente a 10 ms. O modo completo conserva a cauda da resposta, produzindo 404 amostras de saída. A extensão por zeros gera transientes nas bordas; por isso, eles são excluídos das métricas principais.

### 4.9 O sistema reduziu as variações do ruído?

Para ruído independente com variância $\sigma^2$, a média de cinco amostras tem variância $\sigma^2/5$, logo seu desvio padrão esperado é aproximadamente 0,0671 mm. A tabela compara esse valor com o desvio padrão observado da parcela de ruído filtrada. As janelas sobrepostas tornam as amostras do ruído de saída correlacionadas. O erro total também depende de quantização e distorção do sinal, não apenas do ruído.

### 4.10 Houve alteração significativa do sinal de interesse?

A resposta em frequência é

$$
H(e^{j\omega})=\frac{1}{M}\sum_{k=0}^{M-1}e^{-j\omega k}.
$$

Com $M=5$ e $f_s=200$ Hz, o ganho em 5 Hz é aproximadamente 0,9755, enquanto em 15 Hz é aproximadamente 0,7915. A componente principal é pouco atenuada, mas a harmônica perde cerca de 20,85% da amplitude. Essa alteração é relevante se a harmônica for usada no diagnóstico da máquina. A escolha de $M=5$ oferece uma redução de ruído com pequeno atraso, mas não preserva integralmente o conteúdo útil.

### 4.11 Quais limitações foram observadas?

O modelo não contempla mudanças de velocidade, transientes mecânicos, não linearidades, resposta do sensor, jitter ou ruído colorido. Não há filtro analógico anti-aliasing, e a faixa do conversor foi escolhida para evitar saturação do sinal ideal. O ruído posterior ao ADC é uma simplificação didática. As bordas dependem da extensão por zeros, e as métricas usam a referência ideal conhecida, geralmente indisponível em uma medição real.

### 4.12 Como o modelo poderia ser melhorado?

Uma evolução incluiria dados de um acelerômetro real, com unidades e calibração apropriadas, ruído antes da quantização e um filtro anti-aliasing antes do ADC. Seria possível variar o número de bits, a taxa e o comprimento do filtro, comparar vários registros de ruído e projetar um filtro FIR com limites explícitos de atenuação na banda de interesse. A análise espectral permitiria verificar a preservação das componentes de vibração.

## 5. Conclusões

O projeto evidencia que cada etapa atua sobre uma característica diferente do sinal. A amostragem define a informação temporal disponível, a quantização limita a precisão de amplitude e o ruído perturba as medições. A convolução com uma média móvel reduz as variações aleatórias, mas também introduz atraso e atenua parte do sinal útil. A avaliação deve considerar conjuntamente erro, preservação das componentes, transientes e requisitos físicos da aplicação.

## 6. Referências

- Oppenheim, A. V.; Schafer, R. W. *Discrete-Time Signal Processing*. 3ª edição. Pearson, 2010.
- Lathi, B. P. *Linear Systems and Signals*. 2ª edição. Oxford University Press, 2005.
- Roteiro da Parte 1 da disciplina Processamento Digital de Sinais, IFPB: Mini Projeto Integrador e orientações de apresentação gráfica.
