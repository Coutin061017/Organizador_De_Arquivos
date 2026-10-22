# Organizador de Arquivos por Extensão

Automação simples em Python que organiza arquivos em subpastas com base nas suas extensões. Por exemplo, arquivos `.pdf` vão para uma pasta `pdf`, e arquivos `.png` vão para `png`.

## Como funciona

O script `Script.py`:

1. Localiza a pasta `Documents/downloads_teste` dentro do diretório do usuário.
2. Lista os arquivos presentes diretamente nessa pasta.
3. Cria subpastas com o nome de cada extensão, caso ainda não existam.
4. **Move** os arquivos para as subpastas correspondentes.
5. Exibe um resumo com o total por tipo.

## Tecnologias

- Python 3
- `os` — caminhos e diretórios
- `shutil` — movimentação de arquivos
- `collections.Counter` — contagem por extensão

Não requer instalação de bibliotecas externas.

## Como executar

```powershell
git clone https://github.com/Coutin061017/Organizador_De_Arquivos.git
cd Organizador_De_Arquivos
python Script.py
```

**Antes de executar:** crie uma pasta `downloads_teste` dentro de `Documents` do seu usuário e coloque nela apenas arquivos descartáveis para teste. O script usa esse caminho fixo e **move os arquivos originais**, não apenas gera uma prévia. No Windows com OneDrive ou Documents redirecionado, verifique se o caminho configurado em `Script.py` corresponde à pasta real.

## Exemplo

Antes:

```text
downloads_teste/
├── arquivo.pdf
├── foto.png
└── relatorio.xlsx
```

Depois:

```text
downloads_teste/
├── pdf/
│   └── arquivo.pdf
├── png/
│   └── foto.png
└── xlsx/
    └── relatorio.xlsx
```

## Possíveis melhorias futuras

Permitir selecionar a pasta na execução, tratar colisões de nomes e acrescentar um modo de simulação sem mover arquivos.

**Autor:** [André Coutinho](https://github.com/Coutin061017)
