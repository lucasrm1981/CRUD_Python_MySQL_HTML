<h2>Esse código cria uma aplicação simples de cadastro de alunos em um banco de dados MySQL, permitindo a criação de base de dados, tabela, inserção, visualização, atualização e exclusão de alunos.</h2>

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
Função create_student:

python
Copy code
def create_student():
    # Coleta informações do usuário
    # Insere os dados na tabela students
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

