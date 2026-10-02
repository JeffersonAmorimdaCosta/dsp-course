# Processamento Digital de Sinais

Repositório dos estudos, relatórios e simulações da disciplina de Processamento Digital de Sinais do IFPB. O conteúdo é organizado como um livro digital com Jupyter Book e MyST, e as simulações são desenvolvidas em Python.

Para consultar o conteúdo, acesse a [apresentação do Estudo 1](estudo_1/README.md) ou o [índice dos tópicos](estudo_1/index.md).

## Organização do projeto

```text
README.md                         Instruções do repositório
myst.yml                          Configuração e navegação do livro
requirements.txt                  Dependências Python
estudo_1/
├── README.md                     Apresentação do estudo
├── index.md                      Índice dos capítulos
├── relatorio_estudo_1.md          Relatório completo para exportação
├── <topico>/
│   ├── relatorio_<topico>.md      Texto do capítulo
│   └── simulacao/                Notebooks e resultados
└── referencias/                  Referências bibliográficas
.github/workflows/deploy.yml      Geração do site e do PDF
```

## Preparar o ambiente

Execute os comandos na raiz do repositório. O workflow utiliza Python 3.10 e Node.js 24, com npm disponível. A exportação para PDF também requer LaTeX, incluindo XeLaTeX e latexmk.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Para abrir e executar as simulações:

```bash
jupyter notebook
```

Abra o notebook do tópico desejado e execute as células na ordem, desde o início. Salve as saídas para que os gráficos e as tabelas apareçam nos capítulos que incluem o notebook.

## Gerar o livro e o relatório

Para gerar o site HTML:

```bash
jupyter-book build --html --ci
```

O site gerado fica em `_build/html/`. Para exportar o relatório completo do Estudo 1:

```bash
jupyter-book build estudo_1/relatorio_estudo_1.md --pdf --force --ci --output _build/exports/estudo_1.pdf
```

O workflow de publicação executa essas etapas a cada envio para a branch `main`, copia o PDF para a pasta `pdfs/` do site e publica o resultado no GitHub Pages. O link de download presente no estudo aponta para esse PDF publicado.

## Adicionar um novo tópico ou estudo

1. Para um novo estudo, crie `estudo_N/README.md`, `estudo_N/index.md` e `estudo_N/relatorio_estudo_N.md`.
2. Organize cada tópico em uma pasta própria, com o relatório em Markdown e os notebooks em `simulacao/`.
3. Apresente a fundamentação, as equações, os parâmetros, o código, os resultados e sua interpretação. Identifique os eixos e as unidades dos gráficos.
4. Inclua o notebook no capítulo com a diretiva MyST abaixo, ajustando o nome do arquivo.
5. Atualize o índice do estudo e o `project.toc` do `myst.yml`.
6. Inclua o capítulo no relatório completo. Para um novo estudo com PDF, acrescente as etapas de exportação e cópia ao workflow.
7. Execute os notebooks, confira os links relativos e gere o livro para revisar o resultado.

Exemplo de inclusão de uma simulação no capítulo:

````markdown
:::: {include} ./simulacao/simulacao_topico.ipynb
::::
````

Exemplo de inclusão de um capítulo no relatório completo:

````markdown
```{include} topico/relatorio_topico.md
```
````

Os caminhos das inclusões são relativos ao arquivo Markdown que as contém. As referências bibliográficas devem identificar as fontes consultadas e, para materiais on-line, informar o link e a data de acesso.
