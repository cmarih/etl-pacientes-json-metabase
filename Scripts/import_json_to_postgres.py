import json
import os
import psycopg2

# Configuração da conexão com PostgreSQL
conn = psycopg2.connect(
    dbname="pacientes_db",
    user="postgres",
    password="cmarih",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Caminho da pasta onde estão os JSONs
data_folder = "C:/Teste Minsaint/pacientes_data/data"

# Função para extrair dados do JSON
def process_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for entry in data["entry"]:
        resource = entry["resource"]
        resource_type = resource["resourceType"]

        if resource_type == "Patient":
            patient_id = resource["id"]
            name = resource.get("name", [{}])[0].get("text", "Desconhecido")
            gender = resource.get("gender", "Desconhecido")
            birth_date = resource.get("birthDate", None)

            cur.execute(
                "INSERT INTO patients (id, name, gender, birth_date) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                (patient_id, name, gender, birth_date)
            )

        elif resource_type == "Condition":
            condition_id = resource["id"]
            patient_id = resource["subject"]["reference"].split("/")[-1].replace("urn:uuid:", "")  # Pegando o ID do paciente
            condition_name = resource["code"]["text"]
            diagnosis_date = resource.get("recordedDate", None)

            cur.execute(
                "INSERT INTO conditions (id, patient_id, condition_name, diagnosis_date) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                (condition_id, patient_id, condition_name, diagnosis_date)
            )

        elif resource_type == "MedicationRequest":
            medication_id = resource["id"]
            patient_id = resource["subject"]["reference"].split("/")[-1].replace("urn:uuid:", "")  # Pegando o ID do paciente
            medication_name = resource["medicationCodeableConcept"]["text"]
            prescription_date = resource.get("authoredOn", None)

            cur.execute(
                "INSERT INTO medications (id, patient_id, medication_name, prescription_date) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                (medication_id, patient_id, medication_name, prescription_date)
            )

# Processando todos os arquivos JSON na pasta
for json_file in os.listdir(data_folder):
    file_path = os.path.join(data_folder, json_file)
    process_json_file(file_path)

# Commitando e fechando conexão
conn.commit()
cur.close()
conn.close()

print("Dados importados com sucesso!")
