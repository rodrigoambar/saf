import PySimpleGUI as sg
import psycopg2 as bd

# Estabelecendo a conexão
conn = bd.connect(
    host="localhost",
    port="5432",
    database='BD_SAF_1.11',
    user="postgres",
    password="123456"
)

# Criando o Cursor
cursor = conn.cursor()


# conn.commit() comando usado para mandar as informaçoes para o banco de dados

# definindo o cadastro do aluno

# função do cadastro de alunos
def cadastro_aluno(cadastro, cursor):
    comando1 = "INSERT INTO aluno(ra_aluno, nome_aluno, CPF_aluno, email_aluno, telefone_aluno, data_nasc_aluno, end_aluno, muni_aluno, UF_aluno, Cep_aluno, status_aluno, genero)" \
               + " VALUES (" + str(cadastro['ra_aluno']) + ",\'" + cadastro['nome_aluno'] + "\', " + "\'" + cadastro[
                   'CPF_aluno'] + "\', \'" + cadastro['email_aluno'] + "\', \'" + cadastro['telefone_aluno'] + "\', " \
               + "\'" + cadastro['data_nasc_aluno'] + "\', " + "\'" + cadastro['end_aluno'] + "\', \'" + cadastro[
                   'muni_aluno'] + "\', \'" + cadastro['UF_aluno'] + "\', \'" \
               + cadastro['Cep_aluno'] + "\', \'" + cadastro['status_aluno'] + "\', \'" + cadastro[
                   'genero'] + "\'" + ")"
    cursor.execute(comando1)
    conn.commit()


# criação da interface gráfica

layout_a = [
    [sg.Text(" Cadastro de aluno: ")],
    [sg.Text("Coloque o registro acadêmico do aluno: "), sg.InputText(key='ra_aluno')],
    [sg.Text(" Coloque  o nome completo do aluno: "), sg.InputText(key='nome_aluno')],
    [sg.Text("Coloque o CPF do aluno: "), sg.InputText(key='CPF_aluno')],
    [sg.Text("Coloque o email do aluno: "), sg.InputText(key='email_aluno')],
    [sg.Text("Coloque o número de telefone do aluno: "), sg.InputText(key='telefone_aluno')],
    [sg.Text("Coloque a data de nascimento do aluno: "), sg.InputText(key='data_nasc_aluno')],
    [sg.Text("Coloque o endereço do aluno: "), sg.InputText(key='end_aluno')],
    [sg.Text("Coloque o município do aluno:  "), sg.InputText(key='muni_aluno')],
    [sg.Text("Coloque a UF do aluno: "), sg.InputText(key='UF_aluno')],
    [sg.Text("Coloque o CEP do aluno: "), sg.InputText(key='Cep_aluno')],
    [sg.Text("Coloque o status do aluno: "), sg.InputText(key='status_aluno')],
    [sg.Text("Coloque o gênero do aluno:  (F/M) "), sg.InputText(key='genero'),
     sg.Button("Salvar dados cadastrais")]
]
janela_a = sg.Window("Cadastro de alunos", layout_a)
while True:
    evento, valores = janela_a.read()
    if evento == "Salvar dados cadastrais":
        cadastro_aluno(valores, cursor)
    if evento == sg.WIN_CLOSED:
        break
janela_a.close()


# definindo o cadastro do professor

def cadastro_professor(cadastro_prof, cursor):
    comando2 = "INSERT INTO professor(reg_professor, nome_professor, cpf_professor)" \
               + "VALUES(" + str(cadastro_prof['reg_professor']) + ", \'" + cadastro_prof['nome_professor'] + "\', \'" + \
               cadastro_prof['cpf_professor'] + "\'" + ")"
    cursor.execute(comando2)
    conn.commit()


layout_b = [
    [sg.Text("Coloque o cadastro do professor: "), sg.InputText(key='reg_professor')],
    [sg.Text("Coloque o nome do professor: "), sg.InputText(key='nome_professor')],
    [sg.Text("Coloque o CPF do professor: "), sg.InputText(key='cpf_professor')],
    [sg.Button("Salvar dados cadastrais")]
]
janela_b = sg.Window("Cadastro de professor", layout_b)
while True:
    evento, valores = janela_b.read()
    if evento == "Salvar dados cadastrais":
        cadastro_professor(valores, cursor)
    if evento == sg.WIN_CLOSED:
        break
janela_b.close()


def cadastro_turm(cadastro_turma, cursor):
    comando3 = "INSERT INTO turma(cod_turma, cod_curso, turno_turma, nome_turma)" \
               + "VALUES(" + str(cadastro_turma['cod_turma']) + ", " + str(cadastro_turma['cod_curso']) + ", \'" + \
               cadastro_turma['turno_turma'] + "\', \'" + cadastro_turma['nome_turma'] + "\')"
    cursor.execute(comando3)
    conn.commit()


layout_c = [
    [sg.Text("Coloque o código da turma:"), sg.InputText(key='cod_turma')],
    [sg.Text(" Coloque o código do curso:"), sg.InputText(key='cod_curso')],
    [sg.Text("Coloque o turno da turma: "), sg.InputText(key='turno_turma')],
    [sg.Text("Coloque o nome da turma:"), sg.InputText(key='nome_turma'),
        sg.Button("Salvar dados cadastrais")]
]
janela_c = sg.Window("Cadastro de turmas", layout_c)
while True:
    evento, valor = janela_c.read()
    if evento == "Salvar dados cadastrais":
        cadastro_turm(valor, cursor)
        conn.commit()
    if evento == sg.WIN_CLOSED:
        break
janela_c.close()


# funçao matricula:
def matricular(cadastro_mat, cursor):
    comando4 = "INSERT INTO matricula(nr_matricula, cod_curso, dt_matricula, ra_aluno)" \
               + "VALUES(" + str(cadastro_mat['nr_matricula']) + ", " + str(cadastro_mat['cod_curso']) + ",\'" + \
               cadastro_mat['dt_matricula'] + "\', " + str(cadastro_mat['ra_aluno']) + ")"
    cursor.execute(comando4)
    conn.commit()


layout_d = [
    [sg.Text("Coloque o número da matrícula:"), sg.InputText(key='nr_matricula')],
    [sg.Text(" Coloque o código do curso:"), sg.InputText(key='cod_curso')],
    [sg.Text("Coloque a data da matrícula: "), sg.InputText(key='dt_matricula')],
    [sg.Text("Coloque o registro acadêmico(ra) do aluno:"), sg.InputText(key='ra_aluno'),
        sg.Button("Salvar dados cadastrais")]
]
janela_d = sg.Window("Matrícula do aluno", layout_d)
while True:
    evento, valores_1 = janela_d.read()
    if evento == "Salvar dados cadastrais":
        matricular(valores_1, cursor)
        print(valores_1)
        conn.commit()
    if evento == sg.WIN_CLOSED:
        break
janela_d.close()


def atribuir_nota_falta(cadastro_nota_falta, cursor):
    comando5 = "INSERT INTO aluno_disciplina( ra_aluno, cod_discip, dt_frequencia, hora_frequencia, presente,  a1, a2, a3)" \
               + "VALUES(" + str(cadastro_nota_falta['ra_aluno']) + ", " + str(
        cadastro_nota_falta['cod_discip']) + ", \'" + cadastro_nota_falta['dt_frequencia'] + "\', \' " + \
               cadastro_nota_falta['hora_frequencia'] + "\' ," \
               + "\'" + cadastro_nota_falta['presente'] + "\', " + str(cadastro_nota_falta['a1']) + ", " + str(
        cadastro_nota_falta['a2']) + ", " + str(cadastro_nota_falta['a3']) + ")"
    cursor.execute(comando5)
    conn.commit()


layout_e = [
    [sg.Text("Coloque o registro acadêmico(ra) do aluno:"), sg.InputText(key='ra_aluno')],
    [sg.Text(" Coloque o código da disciplina:"), sg.InputText(key='cod_discip')],
    [sg.Text("Coloque a data da frequência: "), sg.InputText(key='dt_frequencia')],
    [sg.Text("Coloque a hora da frequência:"), sg.InputText(key='hora_frequencia')],
    [sg.Text("Coloque se o aluno esteve presente: (Sim/Não) "), sg.InputText(key='presente')],
    [sg.Text(" Coloque a nota da primeira avaliação do aluno:"), sg.InputText(key='a1')],
    [sg.Text("Coloque a nota da segunda avaliação do aluno: "), sg.InputText(key='a2')],
    [sg.Text("Coloque a nota da terceira avaliação do aluno:"), sg.InputText(key='a3')],
    [sg.Button("Salvar dados cadastrais")]
]
janela_e = sg.Window("Nota e falta do aluno", layout_e)
while True:
    evento, valor2 = janela_e.read()
    if evento == "Salvar dados cadastrais":
        atribuir_nota_falta(valor2, cursor)
        conn.commit()
    if evento == sg.WIN_CLOSED:
        break
janela_e.close()

# Recuperação de Resuldados


rows = cursor.fetchall()
for row in rows:
    print(row)

# Fecha a conexão do banco e o Cursor
cursor.close()
conn.close()
