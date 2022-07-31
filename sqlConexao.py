#mysql.exe -uroot -p
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
);

cursor = banco.cursor();

def criar_banco():
    #criando o banco
    cursor.execute("CREATE DATABASE IF NOT EXISTS usuarios;");
    #selecionando o banco
    cursor.execute("USE usuarios;");
    banco.commit();

def criar_tabela():
    #criando  a tabela
    cursor.execute("CREATE TABLE IF NOT EXISTS usuario(nome VARCHAR(20) NOT NULL, senha INT(50) NOT NULL, PRIMARY KEY(nome(20)));");
    banco.commit();

def adicionar_linha(nome, senha):
    #inserindo valores
    try:
        comando = "INSERT INTO usuario (nome, senha) VALUES ('{nome}',{senha});".format(nome=nome,senha=senha);
        cursor.execute(comando);
        banco.commit();
    except mysql.connector.errors.IntegrityError:
        return False;

    return True;

def pesquisa(nome):
    #pesquisa
    comando = "SELECT * FROM usuario WHERE nome='{nome}';".format(nome = nome);
    cursor.execute(comando);
    valores = cursor.fetchall();

    return valores;