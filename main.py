import pyodbc

server = 'DESKTOP-B54DPF9\SQLEXPRESS'
database = 'python_sql'
username = 'sa'
password = '123456'

conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print("Conexão Bem Sucedida")

cursor = conexao.cursor()

#Inserindo Dados
id = 5
cliente = "Fernando"
produto = "Android"
data = "28/08/2021"
preco = 3000
quantidade = 1

comando = f"""INSERT INTO dbo.Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

#Executando uma procedure

comando = """\
EXEC clientes_c 4, 'Felipe', 'Iphone', '25/02/2021', 6000, 1
"""


cursor.execute(comando)
cursor.commit()
print(comando)

