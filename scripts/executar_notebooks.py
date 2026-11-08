"""Execute e salve os notebooks dos estudos 2 e 3 com o Python ativo."""
from pathlib import Path
import sys

import nbformat
from nbclient import NotebookClient
from jupyter_client import AsyncKernelManager


def main():
    raiz = Path(__file__).resolve().parents[1]
    caminhos = [Path(nome).resolve() for nome in sys.argv[1:]] if sys.argv[1:] else [
        caminho
        for estudo in (2, 3)
        for caminho in sorted((raiz / f'estudo_{estudo}').rglob('*.ipynb'))
    ]
    for caminho in caminhos:
        notebook = nbformat.read(caminho, as_version=4)
        gerente = AsyncKernelManager(kernel_name='python3')
        gerente.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
        cliente = NotebookClient(notebook, timeout=300, km=gerente)
        cliente.execute(cwd=str(caminho.parent), cleanup_kc=True)
        nbformat.write(notebook, caminho)
        print(f'OK {caminho.relative_to(raiz)}', flush=True)


if __name__ == '__main__':
    main()
