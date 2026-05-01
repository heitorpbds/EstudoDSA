# Lab 5 - Analytics Engineering - Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados
# Python - Pipeline de Criação do Banco de Dados

# Import
import psycopg2

# Função para executar script SQL
def dsa_executa_script_sql(filename):
    
    print(f"[DEBUG] Procurando arquivo: {filename}")
    
    # Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
    try:
        print("[DEBUG] Conectando ao PostgreSQL...")
        conn = psycopg2.connect(
            dbname="dsadb",
            user="dsa",
            password="dsa1010",
            host="localhost",
            port="5559"
        )
        print("[DEBUG] Conexão estabelecida com sucesso")
    except Exception as e:
        print(f"[ERRO] Falha na conexão: {e}")
        return

    # Abre um cursor para realizar operações no banco de dados
    cur = conn.cursor()

    # Lê o conteúdo do arquivo SQL
    try:
        with open(filename, 'r') as file:
            sql_script = file.read()
        print(f"[DEBUG] Arquivo SQL lido: {len(sql_script)} caracteres")
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {filename}")
        conn.close()
        return

    try:
        # Executa o script SQL
        print("[DEBUG] Executando script SQL...")
        cur.execute(sql_script)

        # Confirma as mudanças no banco de dados
        conn.commit()  
        print("\nScript executado com sucesso!\n")
    except Exception as e:
        # Reverte as mudanças em caso de erro
        conn.rollback()  
        print(f"[ERRO] Erro ao executar o script: {e}")
    finally:
        # Fecha a comunicação com o banco de dados
        cur.close()
        conn.close()

# Executa o script SQL
print("\nExecutando o script SQL para criar o banco de dados...\n")
dsa_executa_script_sql('Lab5-01-Database.sql')
