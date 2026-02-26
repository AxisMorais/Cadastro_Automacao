
#Importação
#from arquivo AutomacaoCadastro.py import Automacao (nome da classe)

from tkinter import *
from AutomacaoCadastro import Automacao


janela = Tk()
janela.title('Cadastro Odontológico')
janela.geometry("800x500")

bg = PhotoImage(file = "imgFundo.png")

# Colocar imagem como fundo
label_fundo = Label(janela, image=bg)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


label_CaixaClassificacao = Label(janela, text="Informe a classificação:" , font=("Roboto", 12))
label_CaixaClassificacao.place(x=40, y=120)


# Caixa de texto (input)
campo_classificacao = Entry( janela, font=("Roboto", 12),    width=15 )
campo_classificacao.place(x=230, y=120)

# Botão para enviar
def enviar_dados():
    objetoOrquestrador = Automacao()

    classificacao_digitada = campo_classificacao.get()  # Pega o valor do input
    if classificacao_digitada:
        # Chama a função de automação com a classificação
        objetoOrquestrador.enviar_mensagens_por_classificacao(classificacao_digitada)

        label_resultado.config(text=f"Enviando mensagens para classificação {classificacao_digitada}...")

btn_enviar = Button(janela, text="Enviar", command=enviar_dados, font=("Roboto", 12))
btn_enviar.place(x=40, y=160)

# Label para mostrar resultado
label_resultado = Label(janela, text="", font=("Roboto", 12))
label_resultado.place(x=40, y=210)



janela.mainloop()