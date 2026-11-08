---
title: Relatório Completo do Estudo 2
exports:
  - format: pdf
    template: templates/relatorio
    output: ../output/pdf/estudo_2.pdf
---

# Estudo 2 — Análise de Sinais e Sistemas nos Domínios da Frequência e da Transformada

**Instituição:** Instituto Federal da Paraíba — IFPB\
**Disciplina:** Processamento Digital de Sinais\
**Professor:** Moacy Pereira da Silva\
**Equipe:** Marcos Vinicius Belo da Silva e Jefferson Amorim da Costa

## Introdução

Fourier, Laplace e Z conectam tempo, frequência e planos complexos. O estudo reúne os 18 tópicos do guia e uma aplicação de sensor industrial. Os resultados computacionais são reproduzíveis pelos notebooks incluídos. Os sinais dos projetos são sintéticos.

```{include} frequencia_exponencial_complexa/relatorio_frequencia_exponencial_complexa.md
```

```{include} dtft/relatorio_dtft.md
```

```{include} dft/relatorio_dft.md
```

```{include} fft/relatorio_fft.md
```

```{include} resolucao_espectral/relatorio_resolucao_espectral.md
```

```{include} frequencia_normalizada/relatorio_frequencia_normalizada.md
```

```{include} nyquist/relatorio_nyquist.md
```

```{include} aliasing/relatorio_aliasing.md
```

```{include} janelamento/relatorio_janelamento.md
```

```{include} laplace/relatorio_laplace.md
```

```{include} funcao_transferencia/relatorio_funcao_transferencia.md
```

```{include} plano_s/relatorio_plano_s.md
```

```{include} transformada_z/relatorio_transformada_z.md
```

```{include} regiao_convergencia/relatorio_regiao_convergencia.md
```

```{include} transferencia_discreta/relatorio_transferencia_discreta.md
```

```{include} estabilidade_z/relatorio_estabilidade_z.md
```

```{include} z_dtft/relatorio_z_dtft.md
```

```{include} laplace_z/relatorio_laplace_z.md
```

```{include} mini_projeto/relatorio_mini_projeto.md
```

## Conclusões da Parte 2

A análise espectral distingue componentes sobrepostas no tempo, mas depende da duração do registro, da janela e da taxa de amostragem. Laplace e Z explicam a dinâmica e a estabilidade, sempre com as hipóteses de causalidade e convergência. O projeto do sensor evidencia que aquisição correta não elimina as limitações de banda do sistema.

```{include} referencias/relatorio_referencias.md
```
