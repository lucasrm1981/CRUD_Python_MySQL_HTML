import mysql.connector ## Importação para conectar ao mysql
import random

def create_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE db_python")

def create_tables():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="db_python"
    )
## Nome da base criada
    mytable = mydb.cursor()
    mytable .execute("CREATE TABLE students ("
                     "id_aluno INTEGER primary key auto_increment NOT NULL, "
                     "matricula INTEGER, "
                     "nome VARCHAR(100), "
                     "sobrenome VARCHAR(100), "
                     "idade INTEGER,"
                     "email VARCHAR(255),"
                     "rf FLOAT," ## Renda percápita
                     "fil VARCHAR(255)," ## Filiação
                     "cpf VARCHAR(14),"
                     "esc VARCHAR(20)," ## Escolaridade
                     "enem_n INTEGER" ## Nota do ENEM
                     ")")

def create_students():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="db_python"
    )

    mycursor = mydb.cursor()

    matricula = random.randint(10000, 90000)
    nome = input("Digite seu Nome: ")
    sobrenome = input("Digite seu Sobrenome: ")
    idade = int(input("Digite sua Idade: "))
    email = input("Digite seu e-mail: ")
    rf = float(input("Digite su Renda Familiar: R$ "))
    fil = input("Digite sua Filiação: ")
    cpf = input("Digite seu CPF: ")
    esc = input("Digite sua escolaridade: ")
    if idade >= 16:
        enem_n = input("Digite sua nota do ENEM")
    else:
        enem_n = 0

    sql = (f"INSERT INTO students (matricula,nome, sobrenome,idade,email,rf,fil,cpf,esc,enem_n) "
           f"VALUES ({matricula}, '{nome}','{sobrenome}',{idade},'{email}',"
           f"{rf},'{fil}','{cpf}','{esc}',{enem_n})")

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Registro Inserido.")  ## IMPRESSÃO DA QUANTIDADE DE LINHAS INSERIDAS

def show_students():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="db_python"
    )

    mycursor = mydb.cursor()
    campoBusca = input("Deseja procurar por qual campo? ou * para Visualizar Todos Alunos")
    valorBusca = input("Digite o valor da Busca")
    ## LIKE %TEXTO ignora a parte inicial e completa com o valor digitado
    ## TEXTO% ignora a parte final
    if campoBusca == "*":
        query = "SELECT * FROM students"
    else:
        query = f"SELECT * FROM students WHERE {campoBusca} LIKE '%{valorBusca}%'"

    mycursor.execute(query)

    myresult = mycursor.fetchall()
    ## Imprime como uma Lista Linha a Linha
    for x in myresult:
        print(x)

def delete_student():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="db_python")

    mycursor = mydb.cursor()
    campoBusca = input("Deseja procurar por qual campo para Deletar?")
    valorBusca = input("Digite o valor da Busca")
    ## LIKE %TEXTO ignora a parte inicial e completa com o valor digitado
    ## TEXTO% ignora a parte final
    query = f"DELETE FROM students WHERE {campoBusca} LIKE '%{valorBusca}%'"
    mycursor.execute(query)
    mydb.commit()
    if mycursor.rowcount > 0:
        print(mycursor.rowcount, "Registro(s) Apagado.")
    else:
        print("Nenhum Resultado encontrado")

opcao = str.lower(input("Deseja utilizar o sistema de Cadastro de Alunos? S ou N\n"))
while opcao=="s":
    menu = input("Escolha a opção desejada:\n"
                 "1. Criar Base de Dados\n"
                 "2. Criar tabela dos Alunos\n"
                 "3. Inserir Aluno\n"
                 "4. Deletar Aluno\n"
                 "5. Listar Alunos\n"
                 "6. Sair do Programa\n")
    match menu:
        case '1':
            create_db()
        case '2':
            create_tables()
        case '3':
            create_students()
        case '4':
            delete_student()
        case '5':
            show_students()
        case '6':
            exit(0)
        case _:
            print("Opção não Encontrada escolha de 1 até 5 ")

    opcao = str.lower(input("Deseja utilizar o sistema de Cadastro de Alunos? S ou N\n"))