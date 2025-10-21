import customtkinter as ctk
from tkinter import ttk, messagebox

import Main

# interface gráfica

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class SistemaEscolar(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar")
        self.geometry("800x600")
        self.resizable(False, False)
        self.tela_inicial()

    # tela inicial ---------------------------------------------------------------------------------------------------------------------------
    def tela_inicial(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self, fg_color="white")
        frame.pack(expand=True, fill="both")

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        titulo = ctk.CTkLabel(frame_titulo, text="Sistema de cadastro de alunos e turmas", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
        titulo.pack(pady=20)

        ctk.CTkLabel(frame, text="").pack(pady=10)

        botoes_frame = ctk.CTkFrame(frame, fg_color="transparent")
        botoes_frame.pack()

        btn_aluno = ctk.CTkButton(botoes_frame, text="ÁREA DO ALUNO", command=self.tela_login_aluno, width=400, height=60, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white")
        btn_aluno.pack(pady=10)

        btn_admin = ctk.CTkButton(botoes_frame, text="ÁREA DO ADMINISTRADOR", command=self.tela_login_admin, width=400, height=60, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white")
        btn_admin.pack(pady=10)

    # ALUNO -----------------------------------------------------------------------------------------------------------------------------------
    # tela do login aluno ---------------------------------------------------------------------------------------------------------------------
    def tela_login_aluno(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ALUNO", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        form = ctk.CTkFrame(frame)
        form.pack(pady=10)

        campo_ra = self.criar_campo(form, "RA:", 0)
        campo_senha = self.criar_campo(form, "Senha:", 1, senha=True)
        
        ctk.CTkButton(frame, text="Entrar", command=lambda: self.login_aluno(campo_ra.get().strip(), campo_senha.get().strip()), width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack()

        ctk.CTkButton(frame, text="Voltar", command=self.tela_inicial, width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack(pady=20)

    def login_aluno(self, ra, senha):

        if not ra or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        if Main.login_aluno(ra, senha):
            self.tela_aluno()
        else:
            messagebox.showerror("Erro", "RA ou senha inválidos!")

    # tela area do aluno ----------------------------------------------------------------------------------------------------------------------
    def tela_aluno(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ALUNO", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        frame_corpo = ctk.CTkFrame(frame)
        frame_corpo.pack(fill="both", pady=10)

        texto = f"nome: {Main.usuario['nome']} \n RA: {Main.usuario['login']} \n turma: {Main.usuario['nome_turma']} - {Main.usuario['ano_turma']}"
        ctk.CTkLabel(frame_corpo, text=texto).pack(pady=10)

        ctk.CTkButton(frame, text="SAIR", command=self.tela_inicial, width=100, height=35, font=ctk.CTkFont(size=16, weight="bold")).pack(pady=20)

    # ADMINISTRADOR ---------------------------------------------------------------------------------------------------------------------------
    # login administrador ---------------------------------------------------------------------------------------------------------------------
    def tela_login_admin(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        form = ctk.CTkFrame(frame)
        form.pack(pady=10)

        campo_login = self.criar_campo(form, "Login:", 0)
        campo_senha = self.criar_campo(form, "Senha:", 1, senha=True)
        
        ctk.CTkButton(frame, text="Entrar", command=lambda: self.login_adm(campo_login.get().strip(), campo_senha.get().strip()), width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack()

        ctk.CTkButton(frame, text="Voltar", command=self.tela_inicial, width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack(pady=20)

    def login_adm(self, login, senha):

        if not login or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        if Main.login_adm(login, senha):
            self.tela_admin_menu()
        else:
            messagebox.showerror("Erro", "login ou senha inválidos!")

    # menu do administrador -------------------------------------------------------------------------------------------------------------------
    def tela_admin_menu(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        # opções
        menu_frame = ctk.CTkFrame(frame, fg_color="transparent")
        menu_frame.pack(pady=10)

        btn_cad_aluno = ctk.CTkButton(menu_frame, text="CADASTRAR ALUNO", command=self.tela_cad_aluno, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white")
        btn_cad_aluno.pack(pady=8)

        btn_ac_aluno = ctk.CTkButton(menu_frame, text="ACESSAR ALUNOS", command=self.tela_acessar_alunos, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white")
        btn_ac_aluno.pack(pady=8)

        btn_cad_turma = ctk.CTkButton(menu_frame, text="CADASTRAR TURMA", command=self.tela_cad_turma, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white")
        btn_cad_turma.pack(pady=8)

        btn_ac_turma = ctk.CTkButton(menu_frame, text="ACESSAR TURMAS", command=self.tela_acessar_turmas, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white")
        btn_ac_turma.pack(pady=8)


        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="SAIR", command=self.tela_inicial, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()
    
    # MANTER ALUNOS ---------------------------------------------------------------------------------------------------------------------------
    # tela de cadastrar alunos ----------------------------------------------------------------------------------------------------------------
    
    def tela_cad_aluno(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        ctk.CTkLabel(frame, text="Cadastrar aluno:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        form = ctk.CTkFrame(frame)
        form.pack(pady=10)

        campo_ra = self.criar_campo(form, "RA:", 0)
        campo_senha = self.criar_campo(form, "Senha:", 1)
        campo_nome = self.criar_campo(form, "Nome:", 2)
        campo_turma = self.criar_campo(form, "ID da turma:", 4)
        
        ctk.CTkButton(frame, text="Cadastrar", command=lambda: self.cad_aluno(campo_ra.get().strip(), campo_senha.get().strip(), campo_nome.get().strip(), campo_turma.get().strip()), width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack()

        ctk.CTkLabel(frame, text="", height=15).pack()

        ctk.CTkButton(frame, text="Voltar", command=self.tela_admin_menu, width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack(pady=20)

    # cadastrar aluno
    def cad_aluno(self, ra, senha, nome, turma):
        Main.cadastrar_aluno(ra, senha, nome, turma)
        self.exibir_aluno()

    # tela de acessar aluno -------------------------------------------------------------------------------------------------------------------

    def tela_acessar_alunos(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        ctk.CTkLabel(frame, text="Pesquisar por RA:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        menu_frame = ctk.CTkFrame(frame)
        menu_frame.pack(pady=10)

        campo_ra = self.criar_campo(menu_frame, "RA:", 0)

        ctk.CTkButton(frame, text="Pesquisar", command=lambda: self.acessar_aluno(campo_ra.get().strip()), width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2", text_color="white").pack()

        ctk.CTkLabel(frame, text="", height=15).pack()

        ctk.CTkLabel(frame, text="Lista completa:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        lista_frame = ctk.CTkScrollableFrame(frame)
        lista_frame.pack(fill="both")

        lista_alunos = Main.listar_alunos()

        for aluno in lista_alunos:
            texto = f" RA: {aluno[1]} | Nome: {aluno[3]} | Turma: {aluno[5]} - {aluno[6]}"
            ctk.CTkButton(lista_frame, text=texto, command=lambda ra=aluno[1]: self.acessar_aluno(ra), font=ctk.CTkFont(size=12, weight="bold"), fg_color="#969696", text_color="white").pack(fill="both")
        
        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="SAIR", command=self.tela_admin_menu, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()

    # acessar aluno
    def acessar_aluno(self, ra):
        if Main.procurar_aluno(ra):
            self.exibir_aluno()
        else:
            messagebox.showerror("Erro", "RA inválido!")

    # exibir aluno ----------------------------------------------------------------------------------------------------------------------------

    def exibir_aluno(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)
        
        frame_corpo = ctk.CTkFrame(frame)
        frame_corpo.pack(fill="both", pady=10)

        texto = f"nome: {Main.aluno_selecionado['nome']} \n RA: {Main.aluno_selecionado['ra']} \n turma: {Main.aluno_selecionado['nome_turma']} - {Main.aluno_selecionado['ano_turma']}"
        ctk.CTkLabel(frame_corpo, text=texto, font=ctk.CTkFont(size=14)).pack(pady=10)

        ctk.CTkButton(frame, text="EDITAR DADOS", command=self.tela_editar_aluno, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#005D08", text_color="white").pack(pady=5)
        
        ctk.CTkButton(frame, text="EXCLUIR ALUNO", command=self.excluir_aluno, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#D32F2F", text_color="white").pack(pady=5)

        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="SAIR", command=self.tela_admin_menu, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()

    # tela de editar aluno --------------------------------------------------------------------------------------------------------------------

    def tela_editar_aluno(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)
        
        ctk.CTkLabel(frame, text="Editar dados:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        form = ctk.CTkFrame(frame)
        form.pack(pady=10)

        campo_ra = self.criar_campo(form, "RA:", 0, Main.aluno_selecionado["ra"])
        campo_senha = self.criar_campo(form, "Senha:", 1, Main.aluno_selecionado["senha"])
        campo_nome = self.criar_campo(form, "Nome:", 2, Main.aluno_selecionado["nome"])
        campo_turma = self.criar_campo(form, "ID da turma:", 4, Main.aluno_selecionado["turma"])

        ctk.CTkButton(frame, text="SALVAR DADOS EDITADOS", command=lambda: self.editar_aluno(campo_ra.get().strip(), campo_senha.get().strip(), campo_nome.get().strip(), campo_turma.get().strip()), width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#005D08", text_color="white").pack(pady=5)

        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="VOLTAR", command=self.exibir_aluno, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()

    # editar aluno

    def editar_aluno(self, ra, senha, nome, turma):
        if Main.editar_aluno(ra, senha, nome, turma):
            self.exibir_aluno()

    # excluir aluno

    def excluir_aluno(self):
        if Main.excluir_aluno():
            self.tela_admin_menu()

    # MANTER TURMAS ----------------------------------------------------------------------------------------------------------------------------
    # tela de cadastrar turmas -----------------------------------------------------------------------------------------------------------------

    def tela_cad_turma(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        ctk.CTkLabel(frame, text="Cadastrar turma:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        form = ctk.CTkFrame(frame)
        form.pack(pady=10)

        campo_nome = self.criar_campo(form, "Nome do curso:", 0)
        campo_ano = self.criar_campo(form, "Ano de inicio:", 1)
        
        ctk.CTkButton(frame, text="Cadastrar", command=lambda: self.cad_turma(campo_nome.get().strip(), campo_ano.get().strip()), width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack()

        ctk.CTkLabel(frame, text="", height=15).pack()

        ctk.CTkButton(frame, text="Voltar", command=self.tela_admin_menu, width=120, height=35, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#1976D2").pack(pady=20)

    # cadastrar turma
    def cad_turma(self, nome, ano):
        if Main.cadastrar_turma(nome, ano):
            self.exibir_turma()

    # tela de procurar turmas ------------------------------------------------------------------------------------------------------------------
    def tela_acessar_turmas(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)

        ctk.CTkLabel(frame, text="Lista completa:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        lista_frame = ctk.CTkScrollableFrame(frame)
        lista_frame.pack(fill="both", padx=20)

        lista_turmas = Main.listar_turmas()

        for turma in lista_turmas:
            texto = f"ID: {turma[0]} | {turma[1]} - {turma[2]}"
            ctk.CTkButton(lista_frame, text=texto, command=lambda idturma=turma[0]: self.acessar_turma(idturma), font=ctk.CTkFont(size=16, weight="bold"), fg_color="#7A7A7A", text_color="white").pack(fill="both")
            for aluno in turma[3]:
                texto = f" {aluno[1]} | {aluno[3]}"
                ctk.CTkLabel(lista_frame, text=texto, anchor="w", font=ctk.CTkFont(size=14, weight="bold"), fg_color="#969696", text_color="white").pack(fill="both")
        
        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="SAIR", command=self.tela_admin_menu, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()

    # acessar turma
    def acessar_turma(self, idturma):
        if Main.procurar_turma(idturma):
            self.exibir_turma()
    
    # exibir turma ----------------------------------------------------------------------------------------------------------------------------

    def exibir_turma(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)
        
        frame_corpo = ctk.CTkFrame(frame)
        frame_corpo.pack(fill="both", pady=10, padx=20)

        texto = f" {Main.turma_selecionada['nome_curso']} - {Main.turma_selecionada['ano_inicio']}"
        ctk.CTkLabel(frame_corpo, text=texto, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#7A7A7A", text_color="white").pack(fill="both")

        for aluno in Main.turma_selecionada['alunos']:
            texto = f" {aluno[1]} | {aluno[3]}"
            ctk.CTkLabel(frame_corpo, text=texto, anchor="w", font=ctk.CTkFont(size=14, weight="bold"), fg_color="#969696", text_color="white").pack(fill="both")

        ctk.CTkButton(frame, text="EDITAR DADOS", command=self.tela_editar_turma, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#005D08", text_color="white").pack(pady=5)
        
        ctk.CTkButton(frame, text="EXCLUIR TURMA", command=self.excluir_turma, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#D32F2F", text_color="white").pack(pady=5)

        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="SAIR", command=self.tela_admin_menu, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()

    # tela de editar turma ---------------------------------------------------------------------------------------------------------------------

    def tela_editar_turma(self):
        self.limpar_tela()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        frame_titulo = ctk.CTkFrame(frame, fg_color="#000085")
        frame_titulo.pack(fill="both")

        ctk.CTkLabel(frame_titulo, text="ÁREA DO ADMINISTRADOR", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(pady=20)
        
        ctk.CTkLabel(frame, text="Editar dados:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

        form = ctk.CTkFrame(frame)
        form.pack(pady=10)

        campo_nome = self.criar_campo(form, "Nome do curso:", 0, Main.turma_selecionada["nome_curso"])
        campo_ano = self.criar_campo(form, "Ano de inicio:", 1, Main.turma_selecionada["ano_inicio"])

        ctk.CTkButton(frame, text="SALVAR DADOS EDITADOS", command=lambda: self.editar_turma(campo_nome.get().strip(), campo_ano.get().strip()), width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#005D08", text_color="white").pack(pady=5)

        ctk.CTkLabel(frame, text="", height=15).pack()

        # botão de sair
        ctk.CTkButton(frame, text="VOLTAR", command=self.exibir_turma, width=220, height=40, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, fg_color="#1976D2", text_color="white").pack()

    
    # editar turma
    def editar_turma(self, nome, ano):
        if Main.editar_turma(nome, ano):
            self.exibir_turma()
    
    # excluir turma
    def excluir_turma(self):
        if Main.excluir_turma():
            self.tela_admin_menu()

    # OUTROS -----------------------------------------------------------------------------------------------------------------------------------
    # função limpar_tela e criar_campo  --------------------------------------------------------------------------------------------------------

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def criar_campo(self, pai, texto_label, linha, texto_var="", senha=False):
        ctk.CTkLabel(pai, text=texto_label, font=ctk.CTkFont(size=12, weight="bold")).grid(row=linha, column=0, padx=5, pady=5, sticky="e")
        entry = ctk.CTkEntry(pai, width=160, show="*" if senha else "")
        entry.insert(0, texto_var)
        entry.grid(row=linha, column=1, padx=5, pady=5)
            
        return entry

# execução
if __name__ == "__main__":
    app = SistemaEscolar()
    app.mainloop()
