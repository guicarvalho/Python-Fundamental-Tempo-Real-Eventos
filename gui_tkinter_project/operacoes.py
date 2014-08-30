# coding: utf-8

import sqlite3 as db


class Controlador(object):
	
	def __init__(self, base_name='default.db'):
		self.con = db.connect(base_name if base_name.endswith('.db') else base_name+'.db')
		self.cur = self.con.cursor()
		
		# cria a tabela
		sql = 'CREATE TABLE IF NOT EXISTS books (	\
				id INTEGER PRIMARY KEY, isbn VARCHAR(30), \
				autor VARCHAR(80), titulo VARCHAR(80), \
				ano INTEGER)'
		
		self.cur.execute(sql)

	def cadastrar(self, isbn, autor, titulo, ano):
	    sql = 'INSERT INTO books (isbn, autor, titulo, ano) VALUES (?,?,?,?)'
	    self.cur.execute(sql, (isbn, autor, titulo, ano))
	    self.con.commit()

	def ler(self):
		sql = 'SELECT * FROM books'
		self.cur.execute(sql)
		return self.cur.fetchall()

	def alterar(self, titulo_antigo, isbn, autor, titulo, ano):
		sql = 'UPDATE books SET isbn=(?), autor=(?), titulo=(?), ano=(?) WHERE titulo=(?)'
		self.cur.execute(sql, (isbn, autor, titulo, ano, titulo_antigo))
		self.con.commit()

	def buscar_livro_por_titulo(self, titulo):
		sql = 'SELECT * FROM books WHERE titulo = (?)'
		self.cur.execute(sql, (titulo,))
		return self.cur.fetchall() # retorna uma tupla
		
	def excluir(self, titulo):
		sql = 'DELETE FROM books WHERE id = ?'
		id = self.buscar_livro_por_titulo(titulo)[0][0]
		self.cur.execute(sql, (id,))
		self.con.commit()
		
