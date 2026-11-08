---
title: Relatório Completo do Estudo 3
exports:
  - format: pdf
    template: templates/relatorio
    output: ../output/pdf/estudo_3.pdf
---

# Estudo 3 — Filtros Digitais: Análise, Projeto e Aplicações

**Instituição:** Instituto Federal da Paraíba — IFPB\
**Disciplina:** Processamento Digital de Sinais\
**Professor:** Moacy Pereira da Silva\
**Equipe:** Marcos Vinicius Belo da Silva e Jefferson Amorim da Costa

## Introdução

O estudo aplica os fundamentos dos estudos anteriores ao projeto de filtros FIR e IIR. Reúne os 14 tópicos do guia e um tratamento digital de sensor com validação quantitativa. Os resultados computacionais são reproduzíveis pelos notebooks incluídos. Os sinais dos projetos são sintéticos.

```{include} conceito_filtragem/relatorio_conceito_filtragem.md
```

```{include} resposta_frequencia/relatorio_resposta_frequencia.md
```

```{include} decibeis/relatorio_decibeis.md
```

```{include} fir/relatorio_fir.md
```

```{include} iir/relatorio_iir.md
```

```{include} comparacao_fir_iir/relatorio_comparacao_fir_iir.md
```

```{include} polos_zeros/relatorio_polos_zeros.md
```

```{include} estabilidade_iir/relatorio_estabilidade_iir.md
```

```{include} fase_atraso/relatorio_fase_atraso.md
```

```{include} atraso_grupo/relatorio_atraso_grupo.md
```

```{include} projeto_fir/relatorio_projeto_fir.md
```

```{include} projeto_iir/relatorio_projeto_iir.md
```

```{include} comparacao_metodos/relatorio_comparacao_metodos.md
```

```{include} aplicacao_filtros/relatorio_aplicacao_filtros.md
```

```{include} mini_projeto/relatorio_mini_projeto.md
```

## Conclusões da Parte 3

A filtragem exige especificações justificadas pelo sinal e verificação posterior. FIR oferece fase linear com maior comprimento; IIR oferece economia de ordem com atraso dependente da frequência. O mini projeto compara as mesmas tolerâncias e usa métricas de erro, SNR, ganho, rejeição e custo para justificar a escolha, sem omitir transientes e latência.

```{include} referencias/relatorio_referencias.md
```
