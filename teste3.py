import tkinter as tk


janela = tk.Tk()
janela.title("Exemplo de Imagem com PhotoImage")

imagem = tk.PhotoImage(file="sport-recife.png")

rotulo = tk.Label(janela, image=imagem)
rotulo.pack()

janela.mainloop()
