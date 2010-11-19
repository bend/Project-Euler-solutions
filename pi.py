from Tkinter import *
from Queue import *
import time
import threading


class GUI:

    global calculer,ent,lbl2,lbl3,res

    def run (self):

        global ent,aff,lbl2,lbl3,res

        root=Tk()

        lbl1=Label(root, text="Nombre d'itérations :")
        lbl2=Label(root, text="Calcul de PI")
        lbl3=Label(root, text="Ecrit et développé par Amaury")
        ent=Entry(root)
        bou=Button(root, text="Lancer!",command=calculer)
        aff=Label(root,text="- %")
        res=Text(root,width=50,height=10)

        lbl1.grid(row=0,column=0)
        ent.grid(row=0,column=1)
        bou.grid(row=0,column=2)
        lbl2.grid(row=1,column=0,columnspan=3)
        lbl3.grid(row=2,column=0,columnspan=3)
        aff.grid(row=3,column=0,columnspan=3)
        res.grid(row=4,column=0,columnspan=3)

        root.mainloop()

    def rafraichir (self,avance):
        global aff

        aff.configure(text=str(avance)+" %")

    def calculer ():
        global ent,lbl2

        lbl2.configure(text="Calcul de PI en cours...")

        calcul().start()

    def finir (self,pi,temps,boucles):
        global lbl2, lbl3,res

        calcul()._Thread__stop()
        lbl2.configure(text="PI="+str(pi))
        lbl3.configure(text="Calcul de PI effectué en " + str(temps) + " secondes !!!")
        res.insert(END,str(boucles) + " boucles     " + str(temps) + " secondes\n")

class calcul (threading.Thread):

    def run (self):

        GUI().rafraichir(0)

        t1=time.clock()

        a=1
        b=0
        somme=0
        boucles=int(ent.get())

        while (b<boucles):
                

                # PI = 4 [ 1 - 1/3 + 1/5 - 1/7 + 1/9 ... ]
                
                if b%2==0:
                        
                    somme=somme+(1./a)
                else:
                    somme=somme-(1./a)
                    
                a=a+2
                b=b+1

                GUI().rafraichir(100*b/boucles)

        t2=time.clock()

        GUI().finir(4*somme,t2-t1,boucles)

GUI().run()