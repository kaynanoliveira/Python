import os 
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# Cria um diretório 
os.mkdir(ROOT_PATH / 'novo-diretorio')

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Renomear arquivo
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "renomeado.txt")

# Remover um arquivo
os.remove(ROOT_PATH / "renomeado.txt")

# Mover um arquivo
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio", ROOT_PATH / "novo.txt")