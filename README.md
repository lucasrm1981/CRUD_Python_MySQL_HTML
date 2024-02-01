<h2>Esse código Python <a href="https://github.com/lucasrm1981/CRUD_Python_MySQL_HTML/blob/main/main.py">main.py</a> cria uma aplicação simples de cadastro de alunos em um banco de dados MySQL, permitindo a criação de base de dados, tabela, inserção, visualização, atualização e exclusão de alunos.</h2>

**Importação de Bibliotecas:**
```
import mysql.connector
import random
```

<p>mysql.connector: Biblioteca para interagir com o banco de dados MySQL.<br/>
random: Biblioteca para gerar números randômicos.</p>

**Conexão com o Banco de Dados:**

```
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="db_python"
)
mycursor = mydb.cursor()
```
<p>Conecta ao banco de dados MySQL usando as credenciais fornecidas.</p>

**Função create_db:**

```
def create_db():
    # Cria uma nova conexão sem especificar um banco de dados
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123")
    try:
        mycursor = mydb.cursor()
        dataBase = "db_python"
        # Tenta criar um novo banco de dados
        mycursor.execute(f"CREATE DATABASE {dataBase}")
    except:
        print(f"\nBase de Dados {dataBase} já Existe!\n")
```
<p>Função para criar um banco de dados chamado "db_python" se não existir.<br/></p>

**Função create_table**
```
def create_table():
    try:
        # Tenta criar uma tabela chamada "students"
        mycursor.execute(f"CREATE TABLE  students("
                         "id_aluno INTEGER primary key auto_increment NOT NULL, "
                         "... outras colunas ...)")
    except:
        print(f"\nTabela students já Existe!\n")
```
<p>Função para criar uma tabela chamada "students" com várias colunas.</p>

**Função create_student:**

```
def create_student():
    # Coleta informações do usuário
    # Insere os dados na tabela students
```
<p>Função para inserir um novo aluno na tabela, gerando uma matrícula aleatória.</p>

**Função show_students:**
```
def show_students():
    # Permite a busca de alunos por diferentes campos
    # Imprime os resultados
```

<p>Função para mostrar os alunos cadastrados, permitindo busca por diferentes campos.</p>

**Função update_student:**

```
def update_student():
    # Permite a atualização de informações de um aluno
```

<p>Função para atualizar informações de um aluno específico.</p>

**Função delete_student:**

```
def delete_student():
    # Permite a exclusão de alunos com base em determinado campo
```

<p>Função para deletar alunos com base em determinado campo.</p>

**Loop Principal (Menu):**
```
opcao = str.lower(input("Deseja utilizar o sistema de Cadastro de Alunos? S ou N\n"))
while opcao == "s":
    # Apresenta um menu e realiza a ação escolhida pelo usuário
```
<p>Loop principal que apresenta um menu para o usuário e executa a função correspondente à escolha.</p>


<h2>Esse código em Python arquivo <a href="https://github.com/lucasrm1981/CRUD_Python_MySQL_HTML/blob/main/index.py">index.py </a>conecta a um banco de dados MySQL, recupera dados da tabela "students" e cria uma página HTML exibindo esses dados em forma de tabela. Em seguida, abre essa página HTML no navegador. Vamos explicar cada parte do código:</h2>


**Verificação da Conexão:**
```
if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")
```

<p>Verifica se a conexão foi estabelecida com sucesso e imprime uma mensagem correspondente.</p>

**Execução de Consulta SQL:**

```
select_employee = """SELECT * FROM students"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()
```
<p>Executa uma consulta SQL para selecionar todos os registros da tabela "students". O resultado é armazenado em uma lista chamada result.</p>

**Construção da Tabela HTML:**

```
p = []
tbl = "<tr><td>ID</td><td>Matricula</td><td>Nome</td><td>Sobrenome</td></tr>"
p.append(tbl)
for row in result:
    a = "<tr><td>%s</td>" % row[0]
    p.append(a)
    b = "<td>%s</td>" % row[1]
    p.append(b)
    c = "<td>%s</td>" % row[2]
    p.append(c)
    d = "<td>%s</td></tr>" % row[3]
    p.append(d)
```
<p>Constrói uma lista p contendo as linhas da tabela HTML com os dados recuperados do banco de dados.</p>

**Criação do Conteúdo HTML:**

```
contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=UTF-8"
http-equiv="content-type">
<title>Python Web Browser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
''' % (p)
```
<p>Cria o conteúdo HTML incorporando a lista p na tabela.</p>

**Gravação do Conteúdo HTML em um Arquivo:**

```
filename = '.venv/index.html'
def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()
main(contents, filename)
```
<p>Grava o conteúdo HTML no arquivo '.venv/index.html'.</p>

**Abertura do Arquivo no Navegador Web:**

```
webbrowser.open(filename)
```
<p>Abre o arquivo HTML recém-criado no navegador web padrão.</p>

**Fechamento da Conexão com o Banco de Dados:**

```if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")
```
<p>Fecha a conexão com o banco de dados se estiver aberta.</p
                                                              
**Em resumo, o código conecta-se a um banco de dados MySQL, recupera dados de uma tabela, cria uma página HTML com esses dados e a abre no navegador.**





