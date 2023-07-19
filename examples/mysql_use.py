import pymysql
from utils.uuid_manager import UUIDManager

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'uuid_test'

# Conectar ao banco de dados
conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = conn.cursor()

# Criar a tabela 'usuarios'
create_table_query = """
CREATE TABLE IF NOT EXISTS usuarios (
    id BINARY(36) PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100)
)
"""
cursor.execute(create_table_query)

def insert_usuario(nome, email, senha):
    # Gerar um UUID
    user_id = UUIDManager.generate_uuid()
    print(user_id)

    # Inserir o usuário na tabela 'usuarios'
    insert_query = "INSERT INTO usuarios (id, nome, email, senha) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (user_id, nome, email, senha))
    conn.commit()

try:
    # Exemplo de inserção de um novo usuário
    insert_usuario("João da Silva", "joao@example.com", "senha123")
    print("Usuário inserido com sucesso!")

except pymysql.Error as e:
    print("Erro ao inserir o usuário:", e)

finally:
    # Fechar a conexão com o banco de dados
    conn.close()
