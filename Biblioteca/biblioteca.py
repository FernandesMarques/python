from PyQt5 import  uic,QtWidgets
import mysql.connector
import mysql
import pandas as pd
import ctypes
import datetime
from datetime import date

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
    database="biblioteca"
)
aux_ce=0
aux_login=0
def cadastrar_funcionario():
    cursor = banco.cursor()
    cpf = cadastro_funcionario.lineEdit.text()
    nomecompleto = cadastro_funcionario.lineEdit_2.text()
    cargo = cadastro_funcionario.lineEdit_3.text()
    cep = cadastro_funcionario.lineEdit_4.text()
    complemento = cadastro_funcionario.lineEdit_5.text()
    logradouro = cadastro_funcionario.lineEdit_6.text()
    bairro = cadastro_funcionario.lineEdit_7.text()
    cidade = cadastro_funcionario.lineEdit_8.text()
    uf = cadastro_funcionario.lineEdit_9.text()
    numero = cadastro_funcionario.lineEdit_10.text()
    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO endereco (cep,logradouro,bairro,cidade, UF) VALUES (%s,%s,%s,%s,%s)"
        dados = (int(cep), str(logradouro), str(bairro), str(cidade), str(uf))
        cursor.execute(comando_SQL, dados)
        banco.commit()

    except mysql.connector.Error as err:
        erro=("ERRO: {}".format(err))
        print(erro)
        if err.errno == 1062:
            try:
                cursor = banco.cursor()
                comando_SQL = "INSERT INTO funcionario (cep, nomecompleto, cargo, complemento, cpf, numero) VALUES (%s,%s,%s,%s,%s,%s)"
                dados = (int(cep), str(nomecompleto), str(cargo), str(complemento), str(cpf), int(numero))
                cursor.execute(comando_SQL, dados)
                banco.commit()
                ctypes.windll.user32.MessageBoxW(0, "cadastro feito com sucesso", "AVISO", 1)
                cadastro_funcionario.close()
            except mysql.connector.Error as err:
                erro = ("ERRO: {}".format(err))
                ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

    try:
        comando_SQL = "INSERT INTO funcionario (cep, nomecompleto, cargo, complemento, cpf) VALUES (%s,%s,%s,%s,%s)"
        dados = (int(cep), str(nomecompleto), str(cargo), str(complemento), str(cpf))
        cursor.execute(comando_SQL, dados)
        banco.commit()
        ctypes.windll.user32.MessageBoxW(0, "cadastro feito com sucesso", "AVISO", 1)
        cadastro_funcionario.close()
    except mysql.connector.Error as err:
        if err.errno != 1062:
            erro = ("ERRO: {}".format(err))
            ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def cadastrar_socio():
    cursor = banco.cursor()
    cpf = cadastro_socio.lineEdit.text()
    nomecompleto = cadastro_socio.lineEdit_2.text()
    rg = cadastro_socio.lineEdit_3.text()
    telefone = cadastro_socio.lineEdit_4.text()
    email = cadastro_socio.lineEdit_5.text()
    sexo = cadastro_socio.lineEdit_6.text()
    cep = cadastro_socio.lineEdit_7.text()
    logradouro = cadastro_socio.lineEdit_8.text()
    numero = cadastro_socio.lineEdit_9.text()
    complemento = cadastro_socio.lineEdit_10.text()
    bairro = cadastro_socio.lineEdit_11.text()
    cidade = cadastro_socio.lineEdit_12.text()
    uf = cadastro_socio.lineEdit_13.text()

    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO endereco (cep,logradouro,bairro,cidade, UF) VALUES (%s,%s,%s,%s,%s)"
        dados = (int(cep), str(logradouro), str(bairro), str(cidade), str(uf))
        cursor.execute(comando_SQL, dados)
        banco.commit()

    except mysql.connector.Error as err:
        erro=("ERRO: {}".format(err))
        print(erro)
        if err.errno == 1062:
            try:
                cursor = banco.cursor()
                comando_SQL = "INSERT INTO socio (cep, cpf, nomecompleto, rg, telefone, email, sexo, numero_casa, complemento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                dados = (int(cep), str(cpf), str(nomecompleto), str(rg), str(telefone), str(email), str(sexo), int(numero), str(complemento))
                cursor.execute(comando_SQL, dados)
                banco.commit()
                ctypes.windll.user32.MessageBoxW(0, "cadastro feito com sucesso", "AVISO", 1)
                cadastro_socio.close()
                cadastro_funcionario.show()

            except mysql.connector.Error as err:
                erro = ("ERRO: {}".format(err))
                ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

    try:
        comando_SQL = "INSERT INTO socio (cep, cpf, nomecompleto, rg, telefone, email, sexo, numero_casa, complemento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (int(cep), str(cpf), str(nomecompleto), str(rg), str(telefone), str(email), str(sexo), int(numero), str(complemento))
        cursor.execute(comando_SQL, dados)
        banco.commit()
        ctypes.windll.user32.MessageBoxW(0, "cadastro feito com sucesso", "AVISO", 1)
        cadastro_socio.close()
    except mysql.connector.Error as err:
        if err.errno != 1062:
            erro = ("ERRO: {}".format(err))
            ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def cadastrar_documento():

    titulo = cadastro_documento.lineEdit.text()
    subtitulo = cadastro_documento.lineEdit_2.text()
    autor = cadastro_documento.lineEdit_3.text()
    editora = cadastro_documento.lineEdit_4.text()
    volume = cadastro_documento.lineEdit_5.text()
    ano = cadastro_documento.lineEdit_6.text()
    num_paginas = cadastro_documento.lineEdit_7.text()
    local_publicacao = cadastro_documento.lineEdit_8.text()
    edicao = cadastro_documento.lineEdit_9.text()
    tipo_documento = cadastro_documento.lineEdit_10.text()

    aux = 0
    try:
        volume += 1
        ano += 1
        num_paginas += 1
        edicao += 1
    except TypeError:
        ctypes.windll.user32.MessageBoxW(0, "Verifique os campos volume, ano, numero de paginas, e edicao, todos devem ser numericos", "AVISO", 1)
        aux = 1
    if aux == 0:
         try:

            cursor = banco.cursor()
            comando_SQL = "INSERT INTO documento (titulo,subtitulo,autor,editora, volume, ano, num_paginas, local_publicacao, edicao, tipo_documento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (str(titulo), str(subtitulo), str(autor), str(editora), int(volume), int(ano), int(num_paginas), str(local_publicacao), int(edicao), str(tipo_documento))
            cursor.execute(comando_SQL, dados)
            banco.commit()
            ctypes.windll.user32.MessageBoxW(0, "cadastro feito com sucesso", "AVISO", 1)
         except mysql.connector.Error as err:
            erro=("ERRO: {}".format(err))
            print(erro)
            ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def cadastrar_emprestimo():

    data_emp = cadastro_emprestimo.dateEdit.text()
    data_emp = datetime.datetime.strptime(data_emp, "%d/%m/%Y").strftime('%Y-%m-%d')
    data_dev_max = cadastro_emprestimo.dateEdit_2.text()
    data_dev_max = datetime.datetime.strptime(data_dev_max, "%d/%m/%Y").strftime('%Y-%m-%d')
    cpf = cadastro_emprestimo.lineEdit.text()
    cod_doc = cadastro_emprestimo.lineEdit_2.text()
    cod_func = cadastro_emprestimo.lineEdit_5.text()
    print(cod_func)
    cursor = banco.cursor()
    global aux_ce
    if aux_ce != 1:
        try:


            comando_SQL = "INSERT INTO emprestimo (cpf_socio,cod_func,data_emprestimo, data_dev_max) VALUES (%s,%s,%s,%s)"
            dados = (int(cpf), int(cod_func), data_emp, data_dev_max)
            cursor.execute(comando_SQL, dados)
            banco.commit()
            sql = "select cod_emprestimo from emprestimo order by cod_emprestimo desc limit 1"
            cursor.execute(sql)
            myresult = cursor.fetchall()
            x = myresult[0];
            cod_emprestimo = x[0]
            comando_SQL = "INSERT INTO item (cod_emprestimo, cod_doc) VALUES (%s,%s)"
            dados = (int(cod_emprestimo), int(cod_doc))
            cursor.execute(comando_SQL, dados)
            comando_SQL = "UPDATE documento set status = 'emprestado' where cod_doc = %s" % (cod_doc)

            cursor.execute(comando_SQL)

            banco.commit()
            print(cod_emprestimo)
            ctypes.windll.user32.MessageBoxW(0, "Salve o seu código do empréstimo, ele é necessário para realizar a devolução", "AVISO", 1)
            ctypes.windll.user32.MessageBoxW(0,str(cod_emprestimo), "CODIGO DO EMPRESTIMO:", 1)
            ctypes.windll.user32.MessageBoxW(0, "Emprestimo realizado com sucesso, continue na mesma tela alterando somente o codigo do livro para continuar realizando emprestimos", "AVISO", 1)
            aux_ce = 1
        except mysql.connector.Error as err:
            erro = ("ERRO: {}".format(err))
            print(erro)
            ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)
    else:
        try:
            sql = "select cod_emprestimo from emprestimo order by cod_emprestimo desc limit 1"
            cursor.execute(sql)
            myresult = cursor.fetchall()
            x = myresult[0];
            cod_emprestimo = x[0]
            comando_SQL = "INSERT INTO item (cod_emprestimo, cod_doc) VALUES (%s,%s)"
            dados = (int(cod_emprestimo), int(cod_doc))
            cursor.execute(comando_SQL, dados)
            comando_SQL = "UPDATE documento set status = 'emprestado' where cod_doc  = %s" % (cod_doc)

            cursor.execute(comando_SQL)
            banco.commit()
            ctypes.windll.user32.MessageBoxW(0, "Emprestimo realizado com sucesso,continue na mesma tela alterando somente o codigo do livro para continuar realizando emprestimos", "AVISO", 1)
        except mysql.connector.Error as err:
            erro = ("ERRO: {}".format(err))
            print(erro)
            ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def buscar_socio():


    cpf = cadastro_emprestimo.lineEdit.text()

    try:
        cursor = banco.cursor()
        comando_SQL = """SELECT nomecompleto FROM socio WHERE cpf = '%s'""" % (cpf)

        cursor.execute(comando_SQL)

        myresult = cursor.fetchall()
        print(myresult)
        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: nenhum sócio com o CPF inserido foi encontrado", "AVISO", 1)
        else:
            x = myresult[0];
            y = x[0]
            cadastro_emprestimo.lineEdit_3.setText(y)

    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def buscar_documento():

    codlivro = cadastro_emprestimo.lineEdit_2.text()

    try:
        cursor = banco.cursor()
        comando_SQL = """SELECT * FROM documento WHERE cod_doc = '%s' and status = 'estoque'""" % (codlivro)

        cursor.execute(comando_SQL)

        myresult = cursor.fetchall()

        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: documento não encontrado/não se encontra disponível para emprestimo", "AVISO", 1)
        else:
            x = myresult[0];
            print(x)
            y = x[1]
            print (y)
            cadastro_emprestimo.lineEdit_4.setText(str(y))

    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def edita_documento():
    print("hello world")
    codlivro = editar_documento.lineEdit_11.text()

    try:
        cursor = banco.cursor()
        comando_SQL = """SELECT * FROM documento WHERE cod_doc = '%s'""" % (codlivro)

        cursor.execute(comando_SQL)

        myresult = cursor.fetchall()

        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: documento não encontrado","AVISO", 1)
        else:
            x = myresult[0];
            print(x)
            y = x[1]
            print(y)
            editar_documento.lineEdit.setText(str(y))
            y = x[2]
            editar_documento.lineEdit_2.setText(str(y))
            y = x[3]
            editar_documento.lineEdit_3.setText(str(y))
            y = x[4]
            editar_documento.lineEdit_4.setText(str(y))
            y = x[5]
            editar_documento.lineEdit_5.setText(str(y))
            y = x[6]
            editar_documento.lineEdit_6.setText(str(y))
            y = x[7]
            editar_documento.lineEdit_7.setText(str(y))
            y = x[8]
            editar_documento.lineEdit_8.setText(str(y))
            y = x[9]
            editar_documento.lineEdit_9.setText(str(y))
            y = x[10]
            editar_documento.lineEdit_10.setText(str(y))

    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def salva_edicao():
    cod_doc = editar_documento.lineEdit_11.text()
    titulo = editar_documento.lineEdit.text()
    subtitulo = editar_documento.lineEdit_2.text()
    autor = editar_documento.lineEdit_3.text()
    editora = editar_documento.lineEdit_4.text()
    volume = editar_documento.lineEdit_5.text()
    ano = editar_documento.lineEdit_6.text()
    n_pag = editar_documento.lineEdit_7.text()
    local = editar_documento.lineEdit_8.text()
    edicao = editar_documento.lineEdit_9.text()
    tipo = editar_documento.lineEdit_10.text()


    try:

        cursor = banco.cursor()
        comando_SQL = """UPDATE documento SET titulo = '%s' , subtitulo = '%s' ,autor = '%s' ,editora = '%s' , volume = '%s' , ano = '%s' , num_paginas = '%s' , local_publicacao = '%s' , edicao = '%s' , tipo_documento = '%s' WHERE cod_doc = '%s';""" % (str(titulo), str(subtitulo), str(autor), str(editora), int(volume), int(ano), int(n_pag), str(local), int(edicao), str(tipo),int(cod_doc))
        
        cursor.execute(comando_SQL)
        banco.commit()
        ctypes.windll.user32.MessageBoxW(0, "edição feita com sucesso", "AVISO", 1)
    except mysql.connector.Error as err:
        erro=("ERRO: {}".format(err))
        print(erro)
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)


def buscar_socio_editar():


    cpf = editar_socio.lineEdit.text()

    try:
        cursor = banco.cursor()
        comando_SQL = """SELECT * FROM socio WHERE cpf = '%s'""" % (cpf)

        cursor.execute(comando_SQL)

        myresult = cursor.fetchall()

        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: nenhum sócio com o CPF inserido foi encontrado", "AVISO", 1)
        else:
            x = myresult[0];
            print(x)
            y = x[1]
            editar_socio.lineEdit_2.setText(y)
            y = x[2]
            editar_socio.lineEdit_3.setText(y)
            y = x[3]
            editar_socio.lineEdit_4.setText(y)
            y = x[4]
            editar_socio.lineEdit_5.setText(y)
            y = x[5]
            editar_socio.lineEdit_6.setText(y)
            y = x[7]
            y = str(y)
            editar_socio.lineEdit_9.setText(y)
            y = x[8]
            editar_socio.lineEdit_10.setText(y)

            cep = x[6]
            comando_SQL = """SELECT * FROM endereco WHERE cep = '%s'""" % (cep)
            cursor.execute(comando_SQL)
            myresult = cursor.fetchall()
            print(myresult)
            x = myresult[0];
            cep=str(cep)
            editar_socio.lineEdit_7.setText(cep)
            y = x[1]
            editar_socio.lineEdit_8.setText(y)
            y = x[2]
            editar_socio.lineEdit_11.setText(y)
            y = x[3]
            editar_socio.lineEdit_12.setText(y)
            y = x[4]
            editar_socio.lineEdit_13.setText(y)

    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def salvar_socio_editar():
    cpf = editar_socio.lineEdit.text()
    nome = editar_socio.lineEdit_2.text()
    rg = editar_socio.lineEdit_3.text()
    telefone = editar_socio.lineEdit_4.text()
    email = editar_socio.lineEdit_5.text()
    sexo = editar_socio.lineEdit_6.text()
    cep = editar_socio.lineEdit_7.text()
    logradouro = editar_socio.lineEdit_8.text()
    numero = editar_socio.lineEdit_9.text()
    complemento = editar_socio.lineEdit_10.text()
    bairro = editar_socio.lineEdit_11.text()
    cidade = editar_socio.lineEdit_12.text()
    uf = editar_socio.lineEdit_13.text()

    try:

        cursor = banco.cursor()
        comando_SQL = """UPDATE socio SET nomecompleto = '%s' , rg = '%s' ,telefone = '%s' ,email = '%s' , sexo = '%s' , numero_casa = '%s' , complemento = '%s' WHERE cpf = '%s';""" % (str(nome), str(rg), str(telefone), str(email), str(sexo), int(numero), str(complemento), str(cpf))

        cursor.execute(comando_SQL)
        banco.commit()
        comando_SQL = """UPDATE endereco SET logradouro = '%s' , bairro = '%s' ,cidade = '%s' ,uf = '%s' WHERE cep = '%s';""" % (str(logradouro), str(bairro), str(cidade), str(uf), int(cep))
        cursor.execute(comando_SQL)
        banco.commit()
        ctypes.windll.user32.MessageBoxW(0, "Edição salva com sucesso com sucesso", "AVISO", 1)
    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        print(erro)
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def buscar_funcionario_editar():


    matricula = editar_funcionario.lineEdit.text()
    matricula = int(matricula)
    try:
        cursor = banco.cursor()
        comando_SQL = """SELECT * FROM funcionario WHERE cod_func = '%s'""" % (matricula)

        cursor.execute(comando_SQL)

        myresult = cursor.fetchall()

        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: nenhum sócio com o CPF inserido foi encontrado", "AVISO", 1)
        else:
            x = myresult[0];
            print(x)
            y = x[1]
            editar_funcionario.lineEdit_2.setText(y)
            y = x[2]
            editar_funcionario.lineEdit_3.setText(y)
            y = x[3]
            editar_funcionario.lineEdit_4.setText(y)
            y = x[5]
            editar_funcionario.lineEdit_8.setText(y)
            y = x[6]
            y = str(y)
            editar_funcionario.lineEdit_7.setText(y)
            cep = x[4]
            cep = int(cep)
            comando_SQL = """SELECT * FROM endereco WHERE cep = '%s'""" % (cep)
            cursor.execute(comando_SQL)
            myresult = cursor.fetchall()
            print(myresult)
            x = myresult[0];
            cep = str(cep)
            editar_funcionario.lineEdit_5.setText(cep)
            y = x[1]
            editar_funcionario.lineEdit_6.setText(y)
            y = x[2]
            editar_funcionario.lineEdit_9.setText(y)
            y = x[3]
            editar_funcionario.lineEdit_10.setText(y)
            y = x[4]
            editar_funcionario.lineEdit_11.setText(y)


    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def salvar_funcionario_editar():

    matricula = editar_socio.lineEdit.text()
    cpf = editar_socio.lineEdit_2.text()
    nome = editar_socio.lineEdit_3.text()
    cargo = editar_socio.lineEdit_4.text()
    cep = editar_socio.lineEdit_5.text()
    logradouro = editar_socio.lineEdit_6.text()
    numero = editar_socio.lineEdit_7.text()
    complemento = editar_socio.lineEdit_8.text()
    bairro = editar_socio.lineEdit_9.text()
    cidade = editar_socio.lineEdit_10.text()
    uf = editar_socio.lineEdit_11.text()

    try:

        cursor = banco.cursor()
        comando_SQL = """UPDATE funcionario SET nomecompleto = '%s' , cargo = '%s' , complemento = '%s' , numero_casa = '%s' WHERE cod_func = '%s';""" % (str(nome), str(cargo), str(complemento), int(numero), int(matricula))
        cursor.execute(comando_SQL)
        banco.commit()
        print('foi')
        comando_SQL = """UPDATE endereco SET logradouro = '%s' , bairro = '%s' ,cidade = '%s' ,uf = '%s' WHERE cep = '%s';""" % (str(logradouro), str(bairro), str(cidade), str(uf), int(cep))
        cursor.execute(comando_SQL)
        banco.commit()
        ctypes.windll.user32.MessageBoxW(0, "Edição salva com sucesso com sucesso", "AVISO", 1)
    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        print(erro)
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def devolver_documento():
    cursor = banco.cursor()
    cod_emp = devolve_documento.lineEdit.text()

    obs = devolve_documento.textEdit.toPlainText()
    cod_emp = int(cod_emp)

    try:

        comando_SQL = """SELECT cod_emprestimo,data_dev_max FROM emprestimo WHERE data_devolucao is null and cod_emprestimo = '%s'""" % (int(cod_emp))

        cursor.execute(comando_SQL)

        myresult = cursor.fetchall()
        x = myresult[0]
        dt = x[1]
        dhj = date.today()
        print(dt)

        multa = (dhj - dt).days
        print(multa)
        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: nenhum emprestimo ativo com esse código foi encontrado", "AVISO", 1)
        else:
            comando_SQL = """update documento join item  on documento.cod_doc = item.cod_doc set documento.status = "estoque" where cod_emprestimo = '%s';""" % (int(cod_emp))
            cursor.execute(comando_SQL)
            banco.commit()
            print('1')
            comando_SQL ="update emprestimo set obs = '%s', data_devolucao = '%s' where cod_emprestimo = '%s';" % (obs, dhj, int(cod_emp))
            cursor.execute(comando_SQL)
            banco.commit()
            ctypes.windll.user32.MessageBoxW(0, "Devolução realizada com sucesso com sucesso", "AVISO", 1)
            multa = multa*0.50
            print(multa)
            tmulta = (f'{multa:1.2f}')
            if multa > 0:
                mmulta = ("O valor da multa é: R$" + str(tmulta))
                ctypes.windll.user32.MessageBoxW(0, mmulta, "AVISO", 1)
    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        print(erro)
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)

def acessa_cadastrar_socio():
    cadastro_socio.show()
    menu_principal.close()

def acessa_cadastrar_funcionario():
    cadastro_funcionario.show()
    menu_principal.close()

def acessa_alt_d_so():
    editar_socio.show()
    menu_principal.close()

def acessa_alt_d_func():
    global aux_login
    if aux_login == 1:
        editar_funcionario.show()
        menu_principal.close()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Você não possui permissão para acessar", "AVISO", 1)

def emprestimo_doc():
    cadastro_emprestimo.show()
    menu_principal.close()

def acessa_cad_doc():
    cadastro_documento.show()
    menu_principal.close()

def alt_d_doc():
    editar_documento.show()
    menu_principal.close()

def dev_doc():
    devolve_documento.show()
    menu_principal.close()

def volta_menu():
    menu_principal.show()
    devolve_documento.close()
    editar_documento.close()
    cadastro_documento.close()
    cadastro_emprestimo.close()
    editar_funcionario.close()
    editar_socio.close()
    cadastro_funcionario.close()
    cadastro_socio.close()

def logar():
    cod_func = login.lineEdit.text()
    cpf = login.lineEdit_1.text()

    try:

        cursor = banco.cursor()
        comando_SQL = """SELECT cargo FROM funcionario WHERE cod_func = '%s' and cpf = '%s';""" % (int(cod_func), str(cpf))

        cursor.execute(comando_SQL)
        myresult = cursor.fetchall()

        if not myresult:
            ctypes.windll.user32.MessageBoxW(0, "ERRO: login/senha erradas", "AVISO", 1)
        else:
            global aux_login
            x = myresult[0];
            y = x[0]
            print(y)
            if y == "admin":
                aux_login = 1
            ctypes.windll.user32.MessageBoxW(0, "Login efetuado com sucesso", "AVISO", 1)
            menu_principal.show()
            login.close()


    except mysql.connector.Error as err:
        erro = ("ERRO: {}".format(err))
        print(erro)
        ctypes.windll.user32.MessageBoxW(0, erro, "AVISO", 1)


app=QtWidgets.QApplication([])
cadastro_socio=uic.loadUi("cadastro_socio.ui")
cadastro_socio.pushButton.clicked.connect(cadastrar_socio)
cadastro_funcionario=uic.loadUi("cadastro_funcionario.ui")
cadastro_funcionario.pushButton.clicked.connect(cadastrar_funcionario)
cadastro_documento=uic.loadUi("cadastro_documento.ui")
cadastro_documento.pushButton.clicked.connect(cadastrar_documento)
cadastro_emprestimo=uic.loadUi("cadastro_emprestimo.ui")
cadastro_emprestimo.pushButton.clicked.connect(cadastrar_emprestimo)
cadastro_emprestimo.commandLinkButton.clicked.connect(buscar_socio)
cadastro_emprestimo.commandLinkButton_2.clicked.connect(buscar_documento)
editar_documento=uic.loadUi("editar_documento.ui")
editar_documento.commandLinkButton.clicked.connect(edita_documento)
editar_documento.pushButton.clicked.connect(salva_edicao)
editar_socio=uic.loadUi("editar_socio.ui")
editar_socio.commandLinkButton.clicked.connect(buscar_socio_editar)
editar_socio.pushButton.clicked.connect(salvar_socio_editar)
editar_funcionario=uic.loadUi("editar_funcionario.ui")
editar_funcionario.commandLinkButton.clicked.connect(buscar_funcionario_editar)
editar_funcionario.pushButton.clicked.connect(salvar_funcionario_editar)
devolve_documento=uic.loadUi("devolve_documento.ui")
devolve_documento.pushButton.clicked.connect(devolver_documento)


menu_principal=uic.loadUi("menu_principal.ui")
menu_principal.pushButton.clicked.connect(acessa_cadastrar_socio)
menu_principal.pushButton_2.clicked.connect(acessa_cadastrar_funcionario)
menu_principal.pushButton_3.clicked.connect(acessa_alt_d_so)
menu_principal.pushButton_4.clicked.connect(acessa_alt_d_func)
menu_principal.pushButton_5.clicked.connect(emprestimo_doc)
menu_principal.pushButton_6.clicked.connect(acessa_cad_doc)
menu_principal.pushButton_7.clicked.connect(alt_d_doc)
menu_principal.pushButton_8.clicked.connect(dev_doc)
cadastro_socio.commandLinkButton_2.clicked.connect(volta_menu)
cadastro_funcionario.commandLinkButton_2.clicked.connect(volta_menu)
cadastro_documento.commandLinkButton_2.clicked.connect(volta_menu)
cadastro_emprestimo.commandLinkButton_3.clicked.connect(volta_menu)
editar_socio.commandLinkButton_2.clicked.connect(volta_menu)
editar_funcionario.commandLinkButton_2.clicked.connect(volta_menu)
devolve_documento.commandLinkButton_2.clicked.connect(volta_menu)
editar_documento.commandLinkButton_2.clicked.connect(volta_menu)

login = uic.loadUi("login.ui")


login.lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Password)
login.pushButton.clicked.connect(logar)

login.show()
app.exec()