import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#try:
#    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
#        escritor = csv.writer(arquivo)
#        escritor.writerow(["Id", "Nome"])
#        escritor.writerow(["1", "Kaynan"])
#        escritor.writerow(["2", "Julia"])      
#except IOError as exc:
#    print(f"Erro ao criar arquivo: {exc}")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID: {row["Id"]}")
            print(f"Nome: {row["Nome"]}")
     
except Exception as exc:
    print(f"Erro ao ler arquivo: {exc}")