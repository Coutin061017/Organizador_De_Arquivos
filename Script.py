import os
import shutil
from collections import Counter

pasta = os.path.join(os.path.expanduser("~"), "Documents", "downloads_teste")

arquivos = os.listdir(pasta)

contador = Counter()


for arquivo in arquivos:

    caminho_arquivo = os.path.join(pasta, arquivo)

    
    if os.path.isfile(caminho_arquivo):

        
        extensao = os.path.splitext(arquivo)[1].lower()

        
        tipo = extensao.replace(".", "")

        
        subpasta = os.path.join(pasta, tipo)
        os.makedirs(subpasta, exist_ok=True)

        
        destino = os.path.join(subpasta, arquivo)
        shutil.move(caminho_arquivo, destino)

        
        contador[tipo] += 1


print("\nArquivos organizados:")

for tipo, quantidade in contador.items():
    print(f"{tipo}: {quantidade} arquivo(s)")
