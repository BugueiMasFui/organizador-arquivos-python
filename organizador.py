import os
import shutil

# Caminho da pasta que você quer organizar
caminho = "C:/Users/dougf/Downloads"

# Tipos de arquivos
tipos = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Pedes": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Documentos": [".docx", ".txt"]
}

for arquivo in os.listdir(caminho):
    arquivo_path = os.path.join(caminho, arquivo)

    if os.path.isfile(arquivo_path):
        for pasta, extensoes in tipos.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                pasta_destino = os.path.join(caminho, pasta)

                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                shutil.move(arquivo_path, os.path.join(pasta_destino, arquivo))
                break