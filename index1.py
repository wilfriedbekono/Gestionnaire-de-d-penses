import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk, messagebox
from tkinter import font
import customtkinter as ctk 
import webbrowser

#creation de la fenetre principale
window = Tk()

def confirmer():
    # recuperation des valeurs saisies par l'utilisateur
    
    nom = champ_nom.get()
    prenom = champ_prenom.get()
    email = champ_email.get()
    mot_de_passe = champ_motdepasse.get()
    contact = champ_contact.get()

    # Vérifier si les champs obligatoires sont remplis 
    if nom and email and mot_de_passe:
        
       print(" nouveau Compte utilisateur créé avec succès !")

       # Affiche un message de confirmation à l'utilisateur
       messagebox.showinfo("Succès", "Nouveau compte utilisateur créé avec succès !")

       # Effacer les champs de saisie après la confirmation
       champ_nom.delete(0, 'end')
       champ_prenom.delete(0, 'end')
       champ_email.delete(0, 'end')
       champ_motdepasse.delete(0, 'end')
       champ_contact.delete(0, 'end')

    else:
        # Afficher un message d'erreur si certains champs obligatoires ne sont pas remplis
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")

def ouvrir_formulaire():
    fenetre = tk.Toplevel(window)
    fenetre.title("CONNEXION")
    fenetre.geometry("500x250")
    fenetre.config(background='#008080')
    fenetre.iconbitmap("perso1.ico")

    frame = Frame(fenetre)
    frame.pack(side="bottom")

    label_titre = Label(frame, text="S'INSCRIRE")
    label_titre.pack()

    label_nom = Label(frame, text="Nom")
    label_nom.pack()
    global champ_nom
    champ_nom = Entry(frame)
    champ_nom.pack()

    label_prenom = Label(frame, text="Prénom")
    label_prenom.pack()
    global champ_prenom
    champ_prenom = Entry(frame)
    champ_prenom.pack()

    label_email = Label(frame, text="E-mail")
    label_email.pack()
    global champ_email 
    champ_email = Entry(frame)
    champ_email.pack()

    label_motdepasse = Label(frame, text="Mot de passe")
    label_motdepasse.pack()   
    global champ_motdepasse
    champ_motdepasse = Entry(frame, show="*")
    champ_motdepasse.pack()

    label_contact = Label(frame, text="contact")
    label_contact.pack()
    global champ_contact
    champ_contact = Entry(frame)
    champ_contact.pack()

    bouton_confirmer = Button(frame, text="Confirmer", command=confirmer)
    bouton_confirmer.pack(side=LEFT)

    bouton_annuler = Button(frame, text="Annuler", command=fenetre.destroy)
    bouton_annuler.pack(side=RIGHT)
    fenetre.resizable(False, False)


def ouvrir_interface():
    formulaire_fenetre = tk.Toplevel()
    print("Depenses fixes")
    print("Depenses courantes")
    print("Depenses ocasionnelles")
    #hebdo()
    global fenetre
    #fenetre.mainloop()

def hebdo():
    from tkinter import Tk, Canvas
    SIDE=500
    root=Tk()
    cnv=Canvas(root, width=SIDE, height=SIDE) 
    cnv.pack()  
    diam=400 
    A=(a,b)=(50, 80)
    B=(a+diam, b+diam)
    cnv.create_oval(A, B, fill='light blue', outline='blue', width=2) 


def mensuel():
    from tkinter import Tk, Canvas
    SIDE=500
    root=Tk()
    cnv=Canvas(root, width=SIDE, height=SIDE, bg="ivory") 
    cnv.pack()  
    diam=400 
    A=(a,b)=(50, 80)
    B=(a+diam, b+diam)
    cnv.create_oval(A, B, fill='light blue', outline='red', width=2) 
    

def annuel():
    from tkinter import Tk, Canvas
    SIDE=500
    root=Tk()
    cnv=Canvas(root, width=SIDE, height=SIDE, bg="ivory") 
    cnv.pack()  
    diam=400 
    A=(a,b)=(50, 80)
    B=(a+diam, b+diam)
    cnv.create_oval(A, B, fill='light blue', outline='green', width=2)    

def rechercher():
    # Récupérer le texte saisi dans la barre de recherche
    recherche=entry.get()
    try:
        mydb = mysql.connector.connect(   host="localhost",   user="root",   password="qwerty", database="money")
        mycursor = mydb.cursor()
        
        query = "SELECT * FROM Depenses WHERE Categorie=%s"
        val = (recherche,)
        mycursor.execute(query,val)
        result=mycursor.fetchall()
        for row in result:
            print(row)
        root=Tk()
        root.title('resultat de la recherche')
        #root.config(background='#008080')
    except Exception as e:
        messagebox.showinfo("no found", f"AUCUN RESULTAT TROUVER ,{str(e)}")        


    # Effectuer l'action souhaitée avec la recherche
    treeview= ttk.Treeview(root)
    treeview.place(x= 100, y=100, width=950, height=710)
    treeview["columns"]=("id","categorie", "montant", "date", "description")
    treeview= ttk.Treeview(root)
    treeview.place(x= 640, y=100, width=950, height=710)
    treeview["columns"]=("id","categorie", "montant", "date", "description")

    treeview.column("#0", width= 0 , stretch=NO)
    treeview.column("id", width= 125 , minwidth= 25)
    treeview.column("categorie", anchor=W, width= 100)
    treeview.column("montant", anchor= W ,width= 120)
    treeview.column("date", anchor=W ,width= 90)
    treeview.column("description", anchor=W ,width= 100)

    treeview.heading("#0", text="", anchor= CENTER)
    treeview.heading("id", text="id", anchor= W)
    treeview.heading("categorie", text="categorie", anchor= W)
    treeview.heading("montant", text="montant", anchor= W)
    treeview.heading("date", text="date", anchor= W)
    treeview.heading("description", text="description", anchor= W)
    print("Résultat de la recherche : ", recherche)

    # Création  d'un élément Text pour afficher les résultats
    resultat_texte = Text(root, width=60, height=15)
    resultat_texte.place()

    # Afficher le résultat dans la zone de texte
    resultat_texte.insert(END, "Résultats de la recherche pour : " + recherche + "\n")
   
    
    # Création de la barre de recherche
entry = ctk.CTkEntry(window)
entry.place(x=785, y=25)

# Création du bouton de recherche
bouton_rechercher = ctk.CTkButton(window, text="Rechercher", command=rechercher)
bouton_rechercher.place(x=930, y=25)

# Création du bouton 
bouton_rechercher = ctk.CTkButton(window, text="cliquez ici pour vous connecter", command=ouvrir_formulaire)
bouton_rechercher.place(x=700, y=600)


# Les fonctions associées aux options de menu
def enregistrer_donnees():
    print("")
   

def visualiser_donnees():
    print("")
    

def sauvegarder_donnees():
    print("")
   
def sauvegarder_donnees_dans_fichier(gestionnaire, donnees_a_sauvegarder):
    try:
        with open(gestionnaire, "w") as file:
            # Écriture des données dans le fichier
            for donnee in donnees_a_sauvegarder:
                file.write(str(donnee) + "\n")

        print("Les données ont été sauvegardées dans le fichier :", gestionnaire)
    except IOError:
        print("Erreur : Impossible d'écrire dans le fichier")

#exemple
donnees_a_sauvegarder = ["Depenses", "Visualisation", "Recherche", "sauvegarde"]
sauvegarder_donnees_dans_fichier("sauvegarde.txt", donnees_a_sauvegarder)


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
menu1.add_command(label="categorisation", command=ouvrir_interface)
menu1.add_separator()
menubar.add_cascade(label="Depenses", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="hebdomadaire", command=hebdo)
menu2.add_command(label="mensuel", command=mensuel)
menu2.add_command(label="annuel", command=annuel)
menu2.add_separator()
menubar.add_cascade(label="visualisation", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="sauvegarder", menu=menu3)

# Association des fonctions aux éléments de menu distincts
menu1.add_command(label="Enregistrer", command=enregistrer_donnees)
menu2.add_command(label="Visualiser", command=visualiser_donnees)
menu3.add_command(label="Sauvegarde", command=sauvegarder_donnees)

window.config(menu=menubar)


# creation de ma base de donnee
mydb = mysql.connector.connect(   host="localhost",   user="root",   password="qwerty") 
mycursor = mydb.cursor() 
mycursor.execute("CREATE DATABASE IF NOT EXISTS money")
mycursor.execute("USE money")


#CREATION DE LA TABLE DEPENSES
mycursor.execute("CREATE TABLE IF NOT EXISTS Depenses (id INT AUTO_INCREMENT PRIMARY KEY, Categorie VARCHAR(25), Montant INT,  Date Date, Description VARCHAR(300))")                  
sql = "INSERT INTO Depenses (Categorie, Montant, Date, Description) VALUES (%s, %s, %s, %s)"
valeurs = ("ordinateurs", 122.000, "2023-12-10", "Achat a nimbuz store yaounde")
mycursor.execute(sql, valeurs)
sql = "INSERT INTO Depenses (Categorie, Montant, Date, Description) VALUES (%s, %s, %s, %s)"
valeurs = ("tablettes ivoco", 100.000, "2023-12-15", "Achat a nimbuz store yaounde")
mycursor.execute(sql, valeurs)
sql = "INSERT INTO Depenses (Categorie, Montant, Date, Description) VALUES (%s, %s, %s, %s)"
valeurs = ("tapis", 100.000, "2023-12-15", "Achat a nimbuz store yaounde")
mycursor.execute(sql, valeurs)
print("hhh")
mydb.commit()


#CREATION DE LA TABLE RAPPORTS
mycursor.execute("CREATE TABLE IF NOT EXISTS Rapports (id INT  AUTO_INCREMENT PRIMARY KEY, TypeRapport VARCHAR(100), DateGeneration DATE, FichierRapport VARCHAR(1000))")
sql = "INSERT INTO Rapports (TypeRapport, DateGeneration, FichierRapport) VALUES (%s, %s, %s)"
valeurs = ("hebdomadaire", "2023-12-10", "rapport hebdomadaire des differentes depenses effectues au sein de la structure")
mycursor.execute(sql, valeurs)
mydb.commit()
sql = "INSERT INTO Rapports (TypeRapport, DateGeneration, FichierRapport) VALUES (%s, %s, %s)"
valeurs = ("mensuel", "2023-12-10", "rapport mensuel des differentes depenses effectues au sein de la structure")
mycursor.execute(sql, valeurs)
mydb.commit()
sql = "INSERT INTO Rapports (TypeRapport, DateGeneration, FichierRapport) VALUES (%s, %s, %s)"
valeurs = ("annuel", "2023-12-10", "rapport Annuel des differentes depenses effectues au sein de la structure")
mycursor.execute(sql, valeurs)
mydb.commit()

#CREATION DE LA TABLE  RECHERCHE
mycursor.execute("CREATE TABLE IF NOT EXISTS Recherches (id INT AUTO_INCREMENT, CritereRecherche VARCHAR(250), ṇatsRecherche VARCHAR(1000), PRIMARY KEY(id))")
sql = "INSERT INTO Recherches (CritereRecherche, ṇatsRecherche) VALUES (%s, %s)"
valeurs = ("categorie de depenses", "differentes depenses effectues au sein de la structure")
mycursor.execute(sql, valeurs)
mydb.commit()
sql = "INSERT INTO Recherches (CritereRecherche, ṇatsRecherche) VALUES (%s, %s)"
valeurs = ("depenses ocasionnelles", "differentes depenses effectues au sein de la structure pour les les fetes")
mycursor.execute(sql, valeurs)
mydb.commit()




#CREATION DE LA TABLE SAUVEGARDE
mycursor.execute("CREATE TABLE IF NOT EXISTS Sauvegardes (id INT AUTO_INCREMENT, DateSauvegarde DATE, FichierSauvegarde VARCHAR(5000),PRIMARY KEY(id))")
sql = "INSERT INTO Sauvegardes (DateSauvegarde, FichierSauvegarde) VALUES (%s, %s)"
valeurs = ("2023-12-10", "nom du fichier a sauvegarder")
mycursor.execute(sql, valeurs)
mydb.commit()



#affichage de la premiére fenetre
window.mainloop()
