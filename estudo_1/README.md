---
title: Apresentação do Estudo 1
---

# Estudo 1 — Fundamentos de Sinais e Sistemas Discretos

**Instituição:** Instituto Federal da Paraíba — IFPB  
**Disciplina:** Processamento Digital de Sinais  
**Professor:** Moacy Pereira da Silva  
**Equipe:** Marcos Vinicius Belo da Silva e Jefferson Amorim da Costa

Este estudo apresenta os fundamentos da representação, aquisição e processamento de sinais discretos. O material combina explicações conceituais, formulação matemática, exemplos e simulações em Python, conectando as equações ao comportamento observado nos gráficos.

## Objetivos

Ao longo do estudo, buscamos compreender como um sinal contínuo é representado por amostras, como a quantização limita a precisão das amplitudes e como as operações com sequências permitem analisar sistemas discretos. O estudo também desenvolve a relação entre resposta ao impulso, convolução e filtragem por sistemas lineares e invariantes no tempo (LTI).

## Percurso do estudo

O conteúdo segue três etapas:

1. **Representação e aquisição:** sinais contínuos e discretos, amostragem, quantização e resolução.
2. **Análise de sinais e sistemas:** sequências fundamentais, operações com sinais, energia e potência, propriedades de sistemas discretos e sistemas LTI.
3. **Processamento e integração:** convolução discreta, filtragem e aplicação dos conceitos em um mini projeto.

O [índice dos tópicos](index.md) reúne os capítulos e as [referências bibliográficas](referencias/relatorio_referencias.md) oferecem fontes para aprofundamento. Os notebooks incluídos nos capítulos apresentam o código, os parâmetros escolhidos e os resultados das simulações.

## Mini projeto integrador

O [mini projeto](mini_projeto/relatorio_mini_projeto.md) simula uma cadeia de aquisição e processamento da vibração de uma máquina. A aplicação gera um sinal composto, realiza a amostragem, compara resoluções de quantização, adiciona ruído e aplica um filtro de média móvel por convolução.

A comparação entre os estágios permite avaliar a precisão da aquisição e o compromisso entre redução do ruído, atraso e preservação das componentes do sinal.

## Relatório completo

O [relatório consolidado](relatorio_estudo_1.md) reúne os capítulos, o mini projeto, as conclusões e as referências em um único documento.

[Baixar o PDF do Estudo 1](../pdfs/estudo_1.pdf)

O PDF é disponibilizado no site após a publicação. Para executar as simulações ou gerar o livro localmente, consulte as [instruções do repositório](../README.md).
