"""Organiza arquivos por extensão sem sobrescrever arquivos existentes."""

import argparse
import shutil
from collections import Counter
from pathlib import Path

PASTA_PADRAO = Path.home() / "Documents" / "downloads_teste"


def organizar(pasta: Path, simular: bool = False):
    """Move arquivos de uma pasta para subpastas de extensão; ignora conflitos."""
    if not pasta.is_dir():
        raise FileNotFoundError(f"Pasta não encontrada: {pasta}")

    contador = Counter()
    conflitos = 0

    for origem in sorted(pasta.iterdir()):
        if not origem.is_file():
            continue

        tipo = origem.suffix.lower().lstrip(".") or "sem_extensao"
        subpasta = pasta / tipo
        destino = subpasta / origem.name

        if destino.exists():
            print(f"Ignorado (arquivo já existe): {destino}")
            conflitos += 1
            continue

        if not simular:
            subpasta.mkdir(exist_ok=True)
            shutil.move(str(origem), str(destino))
        print(f"{'[SIMULAÇÃO] ' if simular else ''}{origem.name} -> {tipo}/")
        contador[tipo] += 1

    print("\nResumo por extensão:")
    for tipo, quantidade in sorted(contador.items()):
        print(f"{tipo}: {quantidade} arquivo(s)")
    print(f"Conflitos ignorados: {conflitos}")
    return contador, conflitos


def main():
    parser = argparse.ArgumentParser(description="Organiza arquivos em subpastas por extensão.")
    parser.add_argument("--pasta", type=Path, default=PASTA_PADRAO, help="Pasta a organizar")
    parser.add_argument("--simular", action="store_true", help="Mostra as mudanças sem mover arquivos")
    args = parser.parse_args()
    try:
        organizar(args.pasta.expanduser(), args.simular)
    except (OSError, shutil.Error) as erro:
        parser.exit(1, f"Erro: {erro}\n")


if __name__ == "__main__":
    main()
