from tkinter import *

expression = ""

def appuyer(touche):
      if touche == "=":
        calculer()
        return
      
      global expression
      expression += str(touche)
      equation.set(expression)

def calculer():
      try:  
           global expression
           total = str(eval(expression))   

           equation.set(total)
           expression = total
      except: 
           equation.set("erreur")  
           expression = ""   


def effacer():
      global expression 
      expression = ""
      equation.set("")

fenetre = Tk()
fenetre.geometry("370x600")
fenetre.title("Calculatrice")
fenetre["bg"] = "#101419"

 #Varible pour stocker le contenu actuel
equation = StringVar()

#Boite de résultat 
resultat = Label(fenetre, fg="black", textvariable=equation, height="2",font=2)
resultat.grid(columnspan=4)

#Boutons
boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "=" ]
ligne = 1
colonne = 0
for bouton in boutons:
        b = Label(fenetre, text=str(bouton), bg="#476C9B", fg="white", height=4, width=8, font=2)
        #Rendre texte cliquable
        b.bind("<Button-1>", lambda e,  bouton=bouton: appuyer(bouton))

        b.grid(row = ligne, column=colonne)

        colonne += 1

        if colonne == 4:
            colonne = 0
            ligne += 1

b = Label(fenetre, text="Effacer", bg="#984447", fg="white", height=4, width=28, font=2)
b.bind("<Button-1>", lambda e: effacer())
b.grid(columnspan=4)














fenetre.mainloop()