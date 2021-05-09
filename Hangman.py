# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:07:33 2021

@author: Vidhi
"""

import random
from string import ascii_uppercase
from tkinter import messagebox
from tkinter import*
root = Tk()
root.title("Hangman")
root.iconbitmap("icon.ico")
root.geometry("670x580+300+70")
root.resizable(0,0)
root.config(bg="white")

def StartIsPressed():
    
    def FruitIsPressed():
        
        LLevel.destroy()
        Fruit.destroy()
        Sport.destroy()    
        Movie.destroy()
        Countries.destroy()
        Animal.destroy()
        Brands.destroy()
        Application.destroy()
        
        word_list = ("APPLE", "AVOCADO", "BANANA", "BLACKBERRIES","MANGO", "APRICOT", "CANTALOUPE", "ORANGE", "WATERMELON", "CARAMBOLA", "CUSTARDAPPLE", "POMEGRANATE","GUAVA",
                     "PEAR", "PLUM", "JACKFRUIT", "KIWI", "LYCHEE", "OLIVES", "PAPAYA", "RASPBERRIES", "PINEAPPLE")

        photos = [PhotoImage(file="hang0.png"), PhotoImage(file="hang1.png"), PhotoImage(file="hang2.png"), PhotoImage(file="hang3.png"), PhotoImage(file="hang4.png"), PhotoImage(file="hang5.png"), PhotoImage(file="hang6.png"),
                  PhotoImage(file="hang7.png"), PhotoImage(file="hang8.png"), PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"), PhotoImage(file="hang11.png")]
        
        def newGame():
            global the_word_withSpaces
            global numberOfGuesses
            numberOfGuesses=0
            imgLabel.config(image=photos[0])
            the_word=random.choice(word_list)
            the_word_withSpaces=" ".join(the_word)
            lblWord.set(" ".join("_"*len(the_word)))
            
        def guess(letter):
            global numberOfGuesses
            if numberOfGuesses<11:
                txt=list(the_word_withSpaces)
                guessed=list(lblWord.get())
                if the_word_withSpaces.count(letter)>0:
                    for c in range(len(txt)):
                        if txt[c]==letter:
                            guessed[c]=letter
                        lblWord.set("".join(guessed))
                        if lblWord.get()==the_word_withSpaces:
                            if numberOfGuesses <= 3:
                                messagebox.showinfo("Hangman","Your score is 3")
                            elif numberOfGuesses >3 and numberOfGuesses <=6:
                                messagebox.showinfo("Hangman","Your score is 2")
                            elif numberOfGuesses >6 and numberOfGuesses <=9:
                                messagebox.showinfo("Hangman","Your score is 1")
                            else:
                                messagebox.showinfo("Hangman","Your score is 0")
                                
                            
                else:
                    numberOfGuesses+=1
                    imgLabel.config(image=photos[numberOfGuesses])
                    if numberOfGuesses==11:
                        messagebox.showwarning("Hangman","Game Over")
                    
                
        imgLabel=Label(root)
        imgLabel.grid(row=0, column=0, columnspan=3)
        imgLabel.config(image=photos[0])
        
        lblWord=StringVar()
        Label(root, textvariable=lblWord, font=("Times New Roman", 24, "bold")).grid(row=0, column=3, columnspan=6)
        
        n=0
        for c in ascii_uppercase:
            Alphabet=Button(root, text=c, command=lambda c=c: guess(c), font=("Californian", 18, "bold"), width=4, justify="center")
            Alphabet.grid(row=1+n//9, column=n%9)
            n+=1
            
        NewGame = Button(root, text="New\n Game", font=("Californian FB", 10, "bold"), command=lambda:newGame())
        NewGame.grid(row=3, column=8, sticky="NSWE")
        newGame()
        
    
    heading.destroy()
    LPhoto.destroy()
    StartButton.destroy()

    LLevel = Label(root, text="Select Categories!!", font=("Californian FB", 35, "bold"), bg="white")
    LLevel.place(x=158, y=45)
    Fruit = Button(root, text="Fruit", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=70, pady=5, justify="center", cursor="hand2", command=FruitIsPressed)
    Fruit.place(x=240, y=120)
    Sport = Button(root, text="Sport", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=68, pady=5, justify="center", cursor="hand2",)#command=SportIsPressed
    Sport.place(x=240, y=180)
    Movie = Button(root, text="Movie", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=66, pady=5, justify="center", cursor="hand2",)#command=MovieIsPressed
    Movie.place(x=240, y=240)
    Countries = Button(root, text="Countries", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=52, pady=5, justify="center", cursor="hand2",)#command=CountriesIsPressed
    Countries.place(x=240, y=300)
    Animal = Button(root, text="Animal", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=66, pady=5, justify="center", cursor="hand2",)#command=AnimalIsPressed
    Animal.place(x=240, y=360)
    Brands = Button(root, text="Brands", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=67, pady=5, justify="center", cursor="hand2",)#command=BrandsIsPressed
    Brands.place(x=240, y=420)
    Application = Button(root, text="Application", font=("Californian FB", 15, "bold"), bg="blue", fg="white", padx=49, pady=5, justify="center", cursor="hand2" )#command=ApplicationIsPressed
    Application.place(x=240, y=480)




heading = Label(root, text="Welcome to Hangman!!", font=("Times New Roman", 40, "bold"), fg="white", bg="black", relief=GROOVE, border=10)
heading.pack(side=TOP, fill=X)
photo = PhotoImage(file="hangman1.png")
LPhoto = Label(root, image=photo, bg="white")
LPhoto.pack()
start = PhotoImage(file="start.png")
StartButton = Button(root, image=start, relief=FLAT, border=0, bg="white", cursor="hand2", command=StartIsPressed)
StartButton.place(x=250, y=490)




root.mainloop()