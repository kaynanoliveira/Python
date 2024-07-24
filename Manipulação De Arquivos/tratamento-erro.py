from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)

except PermissionError as exc:
    print(f'Não foi possivel abrir o arquivo: {exc}')

except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

except Exception as exc:
    print(f"Algum problema ocorru ao tentar abrir o arquivo: {exc}")



# try:
#   arquivo = open(ROOT_PATH / "novo-diretorio")
# except PermissionError as exc:
#    print(f'Não foi possivel abrir o arquivo: {exc}')
