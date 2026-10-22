# Organizador de Arquivos por Extensão

Automação simples em Python que organiza arquivos em subpastas com base nas suas extensões. Por exemplo, arquivos `.pdf` vão para uma pasta `pdf`, e arquivos `.png` vão para `png`.

## Como funciona

O script `Script.py`:

1. Localiza a pasta `Documents/downloads_teste` dentro do diretório do usuário.
2. Lista os arquivos presentes diretamente nessa pasta.
3. Cria subpastas por extensão.
4. **Move** os arquivos sem sobrescrever nomes repetidos.
5. Arquivos sem extensão são colocados em `sem_extensao`.
6. Exibe o total por extensão e quantos conflitos foram ignorados.

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

**Antes de executar:** crie uma pasta `downloads_teste` dentro de `Documents` do seu usuário e coloque nela apenas arquivos descartáveis para teste. Por padrão, **move os arquivos originais**, mas você pode testar antes com `--simular`. No Windows com OneDrive ou Documents redirecionado, verifique se o caminho configurado em `Script.py` corresponde à pasta real.

## Modos de execução

Simular sem mover arquivos:

```powershell
python Script.py --simular
```

Selecionar outra pasta para simulação:

```powershell
python Script.py --pasta "C:\\Users\\SeuUsuario\\Downloads" --simular
```

Para mover arquivos dessa pasta, execute o comando sem `--simular`. Arquivos com nomes já existentes no destino são ignorados, não sobrescritos.

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

## Próximas melhorias

Adicionar interface gráfica e um registro de histórico das movimentações.

**Autor:** [André Coutinho](https://github.com/Coutin061017)
