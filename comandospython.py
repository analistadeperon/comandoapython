class Funcs():
    def limpar(self):
        self.entryCodigo.delete(0, END)
        self.entryNome.delete(0, END)
        self.entryTelefone.delete(0, END)
        self.entryCidade.delete(0, END)

    def conectarDB(self):
        self.conn = sqlite3.connect('bin/clientes.db')
        self.cursor = self.conn.cursor()
        # print('Conectando ao Banco de Dados...')

    def desconectarDB(self):
        self.cursor.close()
        self.conn.close()
        # print('Desconectando o Banco de Dados...')

    def montaTabelas(self):
        self.conectarDB()

        # -- Criação da Tabela --

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit()  #, print("Banco de Dados Criado...")
        self.desconectarDB()

        def variaveis(self):
        self.codigo = self.entryCodigo.get()
        self.nome = self.entryNome.get()
        self.telefone = self.entryTelefone.get()
        self.cidade = self.entryCidade.get()

        def addCliente(self):
        self.variaveis()
        self.conectarDB()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))

        self.conn.commit()
        self.desconectarDB()
        self.selectLista()
        self.limpar()

        
    def delCliente(self):
        self.variaveis()
        self.conectarDB()

        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()

        self.desconectarDB()
        self.limpar()
        self.selectLista()

    def alterarCliente(self):
        self.variaveis()
        self.conectarDB()

        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ? """,
                            (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()

        self.desconectarDB()
        self.selectLista()
        self.limpar()

    def buscaCliente(self):
        self.conectarDB()
        self.listaUser.delete(*self.listaUser.get_children())

        self.entryNome.insert(END, '%')
        nome = self.entryNome.get()

        self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)

        buscaNomeCliente = self.cursor.fetchall()
        for i in buscaNomeCliente:
            self.listaUser.insert("", END, values=i)

        self.limpar()
        self.desconectarDB()
        
#matheusdeperon
