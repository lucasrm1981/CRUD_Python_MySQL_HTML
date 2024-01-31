import mysql.connector  ## Importação para conectar ao mysql
import random  ## Biblioteca para número randomico

## Conexão com a tabela criada
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python"
)
mycursor = mydb.cursor()


def create_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE db_python")


def create_table():
    mycursor.execute("CREATE TABLE students ("
                     "id_aluno INTEGER primary key auto_increment NOT NULL, "
                     "matricula VARCHAR(20), "
                     "nome VARCHAR(100), "
                     "sobrenome VARCHAR(100), "
                     "idade INTEGER,"
                     "email VARCHAR(255),"
                     "rf FLOAT,"  ## Renda percápita
                     "fil VARCHAR(255),"  ## Filiação
                     "cpf VARCHAR(14),"
                     "esc VARCHAR(20),"  ## Escolaridade
                     "enem_n INTEGER"  ## Nota do ENEM
                     ")")


def create_student():
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

    sql = (f"INSERT INTO students (nome, sobrenome,idade,email,rf,fil,cpf,esc,enem_n) "
           f"VALUES ('{nome}','{sobrenome}',{idade},'{email}',"
           f"{rf},'{fil}','{cpf}','{esc}',{enem_n})")

    mycursor.execute(sql)
    mydb.commit()

    last_id = mycursor.lastrowid  ## retorna o ultimo id
    matricula = str(random.randint(10000, 90000)) + "-" + str(last_id)
    cad_mat = f"UPDATE students SET matricula='{matricula}' WHERE id_aluno={last_id}"
    mycursor.execute(cad_mat)
    mydb.commit()

    print(mycursor.rowcount, "Registro Inserido.")  ## IMPRESSÃO DA QUANTIDADE DE LINHAS INSERIDAS


def show_students():
    campoBusca = input("Deseja procurar por qual campo? ou * para Visualizar Todos Alunos: \n")
    if campoBusca != "*":
        valorBusca = input("Digite o valor da Busca: \n")

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


def update_student():
    matricula = input("Digite a matrícula do Estudante que deseja alterar:\n ")
    nomeColuna = input("Deseja atualizar qual campo?\n")
    if nomeColuna == "matricula":
        print("Não é possível alterar a Matrícula")
        update_student()
    novoValor = input("Digite o novo valor do campo\n")

    query = f"UPDATE students SET {nomeColuna} = '{novoValor}' WHERE matricula= '{matricula}'"

    mycursor.execute(query)
    mydb.commit()
    if mycursor.rowcount > 0:
        print(mycursor.rowcount, "Registro(s) Atualizados.")
    else:
        print("Nenhum Resultado encontrado")


def delete_student():
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
while opcao == "s":
    menu = input("Escolha a opção desejada:\n"
                 "1. Criar Base de Dados\n"
                 "2. Criar tabela dos Alunos\n"
                 "3. Inserir Aluno\n"
                 "4. Deletar Aluno\n"
                 "5. Atualizar Informação\n"
                 "6. Listar Aluno(s)\n"
                 "7. Sair do Programa\n")
    match menu:
        case '1':
            create_db()
        case '2':
            create_table()
        case '3':
            create_student()
        case '4':
            delete_student()
        case '5':
            update_student()
        case '6':
            show_students()
        case '7':
            exit(0)
        case _:
            print("Opção não Encontrada escolha de 1 até 7 ")

    opcao = str.lower(input("Deseja utilizar o sistema de Cadastro de Alunos? S ou N\n"))