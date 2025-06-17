import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = os.getenv("AWS_BUCKET_NAME")
region = os.getenv("AWS_REGION")

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client(
        's3',
        region_name=region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Upload realizado com sucesso: {object_name}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except NoCredentialsError:
        print("Credenciais não encontradas.")
    except Exception as e:
        print(f"Erro: {e}")

# Debug: verificar se as variáveis carregaram corretamente
print("AWS_BUCKET_NAME:", bucket_name)

# Caminho do arquivo para subir
#file_path = "C:/Users/Fernando/Desktop/Projetos/Tech_Challenge_AWS/16-06-25.xlsx"
#upload_file(file_path, bucket_name)
