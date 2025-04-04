import json
import os

# Caminho da pasta onde estão os JSON
data_folder = "C:/Teste Minsaint/pacientes_data/data" 

# Pegando um dos arquivos JSON para inspecionar
example_file = os.listdir(data_folder)[0]  # Pega o primeiro arquivo da pasta
file_path = os.path.join(data_folder, example_file)

# Lendo o JSON
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Exibindo uma amostra dos dados
print(json.dumps(data, indent=4)[:1000])  # Mostra apenas os primeiros 1000 caracteres