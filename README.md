# Processamento Digital de Sinais

Este site agrega os estudos, topicos, simulacoes e relatorios produzidos na disciplina de Processamento Digital de Sinais.

## Estudos

```{list-table}
:header-rows: 1

* - Estudo
  - Topicos
  - PDF
* - [Estudo 1 - Sinais discretos](estudo_1/index.md)
  - [Sinais continuos e discretos](estudo_1/sinais_discretos/relatorio_sinais_discretos.md)
  - [Baixar PDF](pdfs/estudo_1.pdf)
```

## Como adicionar um novo estudo

1. Crie uma pasta `estudo_N/`.
2. Crie `estudo_N/index.md` com a apresentacao do estudo.
3. Crie `estudo_N/relatorio_estudo_N.md` incluindo todos os topicos que devem entrar no PDF.
4. Crie uma pasta para cada topico dentro do estudo.
5. Adicione os topicos no `toc` do `myst.yml`.
6. Adicione um comando de geracao do PDF do estudo no workflow de deploy.
