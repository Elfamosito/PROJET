from tkinter import *
from random import *
from time import *
import numpy as np


window=Tk()
window.geometry('700x350')
window.title('Rouler à minuit')
#window.attributes('-fullscreen', True) si vous voulez grand écran
#window.overrideredirect(True) pour cacher la barre du dessus avec le nom, le logo(plume), le -, le plein-écran/réduire[], et la croix x
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

def Relancer():
    Page.destroy()
    Jeu()


frame_test=Frame(window,bg='white') #mettre l'image du menu de mignight drive si on ne veut pas mettre la même couleur partout
frame_test.pack(expand=YES,pady=0,fill=X)

titre_jeu=Label(frame_test,text='Rouler à minuit',font=("Courrier",40,'bold'),bg='white',fg='black')
titre_jeu.pack(side=TOP)

ii=0

mode=0

def changement_de_couleur():
    global couleur, fground, titre_jeu, ii, mode
    couleurs=['black','white','red','blue','green','yellow','purple']
    if ii==len(couleurs):
        ii=0
    couleur=couleurs[ii]
    ii+=1
    fground='black'
    if couleur=='black':
        fground='white'
    if mode==0:
        window.configure(bg=couleur)
        titre_jeu.configure(bg=couleur,fg=fground)
        # frame_test.configure(bg=couleur)  # si on veut mettre le même fond partout 

changement_de_couleur()

def Menu_barre():
    global menu_barre
    
    menu_barre=Menu(window)
        
    menu_fichier=Menu(menu_barre,tearoff=0,relief=GROOVE) 

    menu_fichier.add_command(label="Nouveau",command=Relancer)
    menu_fichier.add_command(label='Changer les couleurs',command=changement_de_couleur)  
    menu_fichier.add_command(label="Quitter",command=window.destroy)

    menu_barre.add_cascade(label="Options",menu=menu_fichier)

    window.config(menu=menu_barre)

def Jeu():
    global mode
    if mode==0:
        window.after(500,frame_test.destroy)
    else:
        menu_barre.destroy()
    mode=1
    window.after(500,Animation_lancement_1)
    window.after(2000,Animation_lancement_2)
    window.after(3500,Initialisation_Jeu)
    window.after(3500,Menu_barre)

Bouton_couleur=Button(frame_test,text='Changer la couleur', font=("Courrier",10), bg='#f0f0f0', fg='black', relief=GROOVE, highlightthickness=0,command=changement_de_couleur)
Bouton_couleur.pack(side=LEFT)

Bouton_quit=Button(frame_test, text='Quitter', font=("Courrier",20), bg='#f0f0f0',fg='black',relief=GROOVE, highlightthickness=0,command=window.destroy)
Bouton_quit.pack(side=BOTTOM, pady=30)

Bouton_start=Button(frame_test, text='Start', font=("Courrier",20), bg='#f0f0f0',fg='black',relief=GROOVE,highlightthickness=0,command=Jeu)
Bouton_start.pack(expand=YES, pady=30)

# highscore=[0],[1]
# infos = (highscore)   #attribuer les valeurs à sauvegarder / dernier score
# print(infos)                #test d'attribution des valeurs
 
# np.save('infos.npy', infos, allow_pickle=False, fix_imports=False) #sauvegarde des dernières données de infos dans un fichier npy
# loaded_data=np.load('infos.npy')    #récupération des données du fichier infos.npy
# print(loaded_data[1][0])          #test de récupération


def Animation_lancement_1():
    global w, Animation_1, color_anim_1
    w=0
    color_anim_1='black'
    if couleur=='black':
        color_anim_1='white'
    Animation_1 = Canvas(window, bg=color_anim_1,width=w,height=h)
    Animation_1.pack(side=RIGHT)
    for i in range(1,275):
        window.after(5*i,changement_animation_1)

def changement_animation_1():
    global w
    w+=2.56
    Animation_1.configure(width=w)

def Animation_lancement_2():
    global w, Animation_2
    w=700
    color_anim_2='white'
    if couleur=='black':
        color_anim_2='black'
    window.configure(bg=color_anim_2)
    Animation_1.destroy()
    Animation_2 = Canvas(window, bg=color_anim_1,width=w,height=h)
    Animation_2.pack(side=LEFT)
    for i in range(1,275):
        window.after(5*i,changement_animation_2)

def changement_animation_2():
    global w
    w-=2.56
    Animation_2.configure(width=w)



def Initialisation_Jeu():
    
    window.configure(bg='black')
    
    piv=35
    
    def Vehicle_p():
        global Page, r
        r=30
        Page = Canvas(window, bg='black', width=w, height=h)
        Page.pack(fill='both')
        Page.create_window(100, 100, anchor='nw')
        Page.create_oval(200-r,piv-r,200+r,piv+r/2, outline='red', fill='white')

    Vehicle_p()
    
    grille_voiture=[[1],
                    [0],
                    [0],
                    [0]]

    délai=int(50)

    def MAJHeure():

        Deplacement_voiture_p()
        window.after(délai,MAJHeure)

        
    def haut(event):
        global piv
        print('haut')
        if piv-r-5>0:
            piv-=10
        
    def hauut(event):
        print('hauut')
        piv-=5
    
    def bas(event):
        print('bas')
        if piv+r+5<h:
            piv+=10

    def Deplacement_voiture_p():
        Vehicle_p()
        window.bind("<Up>",haut)
        window.bind("<Down>",bas)
        window.bind("<KeyPress-z>",haut)
        window.bind("<KeyPress-w>",haut)
        window.bind("<KeyPress-s>",bas)
        window.bind("<KeyPress-Z>",haut)
        window.bind("<KeyPress-W>",haut)
        window.bind("<KeyPress-S>",bas)
        window.bind("<KeyPress-z-Motion",hauut)

    MAJHeure()



mainloop()