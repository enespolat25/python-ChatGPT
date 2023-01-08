from tkinter import *
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()


def show():
	response=""
	response = bot.ask(e1.get())
	print(response)
	veri_baslik.config(text="Chat GPT Cevabı:")
	#veri.config(text=response)

	veri.insert('end', response)
	veri.config(state='disabled')
    


root = Tk()
root.title('ChatGPT')

root.geometry("700x620")


label = Label(root, text="Ne öğrenmek istersin?")
label.grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

# Create button, it will change label text
button = Button(root, text="Cevabı Gör",
                command=show).grid(row=3, column=1)
			
veri_baslik = Label(root, text=" ")
veri_baslik.grid(row=4, column=0)

#veri = Label(root, text=" ")
veri = Text(
    root,
    height=22,
    width=50
)
veri.grid(row=4, column=1)

root.mainloop()