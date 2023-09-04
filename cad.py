    self.txtidusuario.delete(0, END)
    self.txtnome.delete(0, END)
    self.txttelefone.delete(0, END)
    self.txtemail.delete(0, END)
    self.txtusuario.delete(0, END)
    self.txtsenha.delete(0, END)



def excluirUsuario(self):
    user = Usuarios()

    user.idusuario = self.txtidusuario.get()

    self.lblmsg["text"] = user.deleteUser()

    self.txtidusuario.delete(0, END)
    self.txtnome.delete(0, END)
    self.txttelefone.delete(0, END)
    self.txtemail.delete(0, END)
    self.txtusuario.delete(0, END)
    self.txtsenha.delete(0, END)


def buscarUsuario(self):
    user = Usuarios()

    idusuario = self.txtidusuario.get()

    self.lblmsg["text"] = user.selectUser(idusuario)

    self.txtidusuario.delete(0, END)
    self.txtidusuario.insert(INSERT, user.idusuario)

    self.txtnome.delete(0, END)
    self.txtnome.insert(INSERT, user.nome)

    self.txttelefone.delete(0, END)
    self.txttelefone.insert(INSERT,user.telefone)

    self.txtemail.delete(0, END)
    self.txtemail.insert(INSERT, user.email)

    self.txtusuario.delete(0, END)
    self.txtusuario.insert(INSERT, user.usuario)

    self.txtsenha.delete(0, END)
    self.txtsenha.insert(INSERT,user.senha)



root = Tk()
Application(root)
root.mainloop()