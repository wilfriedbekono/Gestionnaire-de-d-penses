from tkinter import *
from tkinter.filedialog import *


#creation de la premiéer fenetre
window = Tk()

#pesonnalisation de cette premiére fenetre
window.title("Gestionnaire de dépenses")
window.geometry("1080x720")
window.minsize(480,360)
window.iconbitmap("logo2.ico")
window.config(background='#008080')

#ajouter un premier texte
Label_title = Label(window, text="welcome in this application", font=("Arial", 25), bg= '#41B77F', fg='white')
Label_title.pack(expand=YES)

#creation d'une barre de menu
menubar = Menu(window)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="dépenses fixes", command='alert')
menu1.add_command(label="dépenses courantes", command='alert')
menu1.add_command(label="dépenses ocasionnelles", command='alert')
menu1.add_separator()
menu1.add_command(label="enregistrer", command=window.quit)
menubar.add_cascade(label="Entregistrement", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="hebdomadaire", command='alert')
menu2.add_command(label="mensuel", command='alert')
menu2.add_command(label="annuel", command='alert')
menubar.add_cascade(label="visualisation", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="nom de la transaction", command='alert')
menubar.add_cascade(label="recherche", menu=menu3)

menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="type de dépense", command='alert')
menu4.add_command(label="montant", command='alert')
menubar.add_cascade(label="sauvegarde", menu=menu4)

window.config(menu=menubar)


#affichage de la premiére fenetre
window.mainloop()
