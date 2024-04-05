from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.iconbitmap("Images/burger.ico")
window.title("Test for resturant")
window.geometry("1200x620")

b =[120,140,160,200,100,180] #price of the Burgers 
p = [400,500,650,700,800,950] #price of the Pizzas 
fr = [80,100,120,150,70,90]#price of the Fries 
dri=[80,100,50,120,90,130] #price of the Drinks  
ri = [180,330,450,220,200,250] #price of the Rice Platters
co = [380,450,500,490,370,600] #price of the Combos 


global total_cost 
total_cost = 0 

global tup
tup = []

#first welcome function
def welcome():
    global intro 
    global nameofrest
    global first_button

    #assign new global variables to the menues
    global burgers
    global pizza
    global fries
    global combos
    global rice
    global drinks
    global total_cost

    global f 

    intro.destroy()

    first_button.destroy()

    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)

    burgers = Button(f,text="Burgers",pady=40,padx=60,command=lambda:menu("Burgers"),width=20,height=2)
    pizza = Button(f,text="Pizzas",pady=40,padx=60,command=lambda:menu("Pizzas"),width=20,height=2)
    fries = Button(f,text="Fries",pady=40,padx=60,command=lambda:menu("Fries"),width=20,height=2)
    combos = Button(f,text="Cobmos",pady=40,padx=60,command=lambda:menu("Combos"),width=20,height=2)
    rice = Button(f,text="Rice",pady=40,padx=60,command=lambda:menu("Rice"),width=20,height=2)
    drinks = Button(f,text="Drinks",pady=40,padx=60,command=lambda:menu("Drinks"),width=20,height=2)
    
    nameofrest.pack()
    
    burgers.grid(row=0,column= 0)
    pizza.grid(row=0,column=1)
    fries.grid(row=0,column= 2)
    combos.grid(row=1,column= 0)
    rice.grid(row=1,column= 1)
    drinks.grid(row=1,column= 2)

#this contains the menu of the items
def menu(food):
    global burgers
    global pizza
    global fries
    global combos
    global rice
    global drinks

    global nameofrest

    #types of burger , pizzas, drinks ,rice and combos
    global item_1 
    global item_2
    global item_3
    global item_4
    global item_5
    global item_6
    global total_cost

    global f 
    global back
    
    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)

    

    nameofrest.pack()
    
    burgers.destroy()
    pizza.destroy()
    fries.destroy()
    combos.destroy()
    rice.destroy()
    drinks.destroy()

    if food.upper() == "BURGERS":
        
        
        item_1 = Button(f, text = "Cheese\nBurger",pady=40,padx=60,command=lambda: costing("Cheese burger",b,0),width=20,height=2)
        item_2 = Button(f, text = "Chicken\nBurger",pady=40,padx=60,command=lambda: costing("Chicken Burgers",b,1),width=20,height=2)
        item_3 = Button(f, text = "Beef\nBurger",pady=40,padx=60,command=lambda: costing("Beef Burgers",b,2),width=20,height=2)
        item_4 = Button(f, text = "Double\nDecker\nBurger",pady=40,padx=60,command=lambda: costing("Double Decker Burger",b,3),width=20,height=2)
        item_5 = Button(f, text = "Veggie\nBurger",pady=40,padx=60,command=lambda: costing("Veggie Burger",b,4),width=20,height=2)
        item_6 = Button(f, text = "HamBurger",pady=40,padx=60,command=lambda: costing("Ham Burger", b,5),width=20,height=2)

        item_1.grid(row=0,column=0)
        item_2.grid(row = 0, column=1)
        item_3.grid(row = 0, column=2)
        item_4.grid(row = 1, column=0)
        item_5.grid(row = 1, column=1)
        item_6.grid(row = 1, column=2)
        back = Button(f,text= "Back",font=("simple plan",12),padx=30,pady=20,command=welcome2 )
        back.grid(row=2, column= 1, padx= 10, pady= 10)

    elif food.upper() == "PIZZAS":

        item_1 = Button(f, text = "Meaty Onions",pady=40,padx=60,width=20,command=lambda: costing("Meaty onions",p,0) )
        item_2 = Button(f, text = "Cheese Fountain",pady=40,padx=60,width=20 ,command=lambda: costing("Cheese Fountain",p,1) )
        item_3 = Button(f, text = "BBQ Meat Machine",pady=40,padx=60,width=20,command=lambda: costing("BBQ Meat Machine",p,2)  )
        item_4 = Button(f, text = "Sausage Carnival",pady=40,padx=60,width=20,command=lambda: costing("Sausage Carnival",p,3)  )
        item_5 = Button(f, text = "Cheddar Cream",pady=40,padx=60,width=20,command=lambda: costing("Cheddar Cream",p,4) )
        item_6 = Button(f, text = "Red Sun Pepparoni",pady=40,padx=60,width=20,command=lambda: costing("Red Sun Pepparoni",p,5)  )

        item_1.grid(row=0,column=0)
        item_2.grid(row = 0, column=1)
        item_3.grid(row = 0, column=2)
        item_4.grid(row = 1, column=0)
        item_5.grid(row = 1, column=1)
        item_6.grid(row = 1, column=2)
        back = Button(f,text= "Back",font=("simple plan",12),padx=30,pady=20,command=welcome2 )
        back.grid(row=2, column= 1, padx= 10, pady= 10)

    elif food.upper() == "FRIES":

        item_1 = Button(f, text = "French Fries",pady=40,padx=60,width=20,command=lambda: costing("French Fries" ,fr,0) )
        item_2 = Button(f, text = "Fish Fingers",pady=40,padx=60,width=20,command=lambda: costing("Fish Fingers" ,fr,1) )
        item_3 = Button(f, text = "Onion Rings",pady=40,padx=60,width=20 ,command=lambda: costing("Onion Rings" ,fr,2) )
        item_4 = Button(f, text = "Chicken Fry",pady=40,padx=60,width=20 ,command=lambda: costing("Chicken Fry" ,fr,3) )
        item_5 = Button(f, text = "Chicken Nugget",pady=40,padx=60,width=20,command=lambda: costing("Chicken Nugget" , fr, 4) )
        item_6 = Button(f, text = "Chicken Lolipops",pady=40,padx=60,width=20 ,command=lambda: costing("Chicken Lolipops",fr,5) )

        item_1.grid(row=0,column=0)
        item_2.grid(row = 0, column=1)
        item_3.grid(row = 0, column=2)
        item_4.grid(row = 1, column=0)
        item_5.grid(row = 1, column=1)
        item_6.grid(row = 1, column=2)
        back = Button(f,text= "Back",font=("simple plan",12),padx=30,pady=20,command=welcome2 )
        back.grid(row=2, column= 1, padx= 10, pady= 10)

    elif food.upper() == "DRINKS":

        item_1 = Button(f, text = "Iced Cold\nCoffee",pady=40,padx=60,width=20,height=2,command=lambda: costing("Iced Cold Coffee" ,dri,0)  )
        item_2 = Button(f, text = "Oreo Shake",pady=40,padx=60,width=20,height=2,command=lambda: costing("Oreo Shake" ,dri,1)  )
        item_3 = Button(f, text = "Vanilla Milk\nShake",pady=40,padx=60,width=20,height=2,command=lambda: costing("Vanilla Milk Shake" ,dri,2)  )
        item_4 = Button(f, text = "Mango Milk\nShkae",pady=40,padx=60,width=20,height=2,command=lambda: costing("Mango Milk Shake" ,dri,3)  )
        item_5 = Button(f, text = "Lassi",pady=40,padx=60,width=20,height=2,command=lambda: costing("Lassi" ,dri,4)  )
        item_6 = Button(f, text = "Chocolate Cold Coffee",pady=40,padx=60 ,width=20,height=2,command=lambda: costing("Chocolate Cold Coffee" ,dri,5) )

        item_1.grid(row=0,column=0)
        item_2.grid(row = 0, column=1)
        item_3.grid(row = 0, column=2)
        item_4.grid(row = 1, column=0)
        item_5.grid(row = 1, column=1)
        item_6.grid(row = 1, column=2)
        back = Button(f,text= "Back",font=("simple plan",12),padx=30,pady=20,command=welcome2 )
        back.grid(row=2, column= 1, padx= 10, pady= 10)

    elif food.upper() == "RICE":

        item_1 = Button(f, text = "Fried Rice\nwith\nBeef and Garlic",pady=30,padx=60,width=20,height=2,command=lambda:costing("R1",ri,0) )
        item_2 = Button(f, text = "Fried Rice\nwith\nEgg, Beef and Green Pepper",pady=30,padx=60,width=20,height=2,command=lambda:costing("R2",ri,1)  )
        item_3 = Button(f, text = "Fried Rice\nwith\nMinced Beef and BBQ Sauce",pady=30,padx=60,width=20,height=2,command=lambda:costing("R3",ri,2)  )
        item_4 = Button(f, text = "Fried Rice\nwith\nEgg and Sausage",pady=40,padx=60,width=20,height=2,command=lambda:costing("R4",ri,3) )
        item_5 = Button(f, text = "Fried Rice\nwith\nMeat and Vegetables",pady=40,padx=60,width=20,height=2,command=lambda:costing("R5",ri,4) )
        item_6 = Button(f, text = "Rice with Chicken\nand Chili and Pepper",pady=40,padx=60,width=20,height=2,command=lambda:costing("R6",ri,5) )

        item_1.grid(row=0,column=0)
        item_2.grid(row = 0, column=1)
        item_3.grid(row = 0, column=2)
        item_4.grid(row = 1, column=0)
        item_5.grid(row = 1, column=1)
        item_6.grid(row = 1, column=2)
        back = Button(f,text= "Back",font=("simple plan",12),padx=30,pady=20,command=welcome2 )
        back.grid(row=2, column= 1, padx= 10, pady= 10)

    elif food.upper() == "COMBOS":
        item_1 = Button(f, text = "One Chicken Burger,\nOne French Fries,\nCold Coffee",pady=30,padx=60,width=20,height=2,command=lambda:costing("C1",co,0))
        item_2 = Button(f, text = "One Beef Burger,\nOnion Rings,\nVanila Milk Shake",pady=30,padx=60,width=20,height=2,command=lambda:costing("C2",co,1))
        item_3 = Button(f, text = "One Veggie Burger,\nCheddar Cream Pizza,\nOreo Shake",pady=30,padx=60,width=20,height=2,command=lambda:costing("C3",ri,2))
        item_4 = Button(f, text = "BBQ Meat Machine,\nChicken Fry,\nLassi",pady=40,padx=60,width=20,height=2,command=lambda:costing("C4",co,3))
        item_5 = Button(f, text = "Red Sun Pepparoni,\nFish Fingers,\nChocolate cold Coffee",pady=40,padx=60,width=20,height=2,command=lambda:costing("C5",co,4))
        item_6 = Button(f, text = "Double Decker Burger\nSausage Carnival\nFrench Fries,\nLassi",pady=40,padx=60,width=20,height=2,command=lambda:costing("C6",co,5))

        item_1.grid(row=0,column=0)
        item_2.grid(row = 0, column=1)
        item_3.grid(row = 0, column=2)
        item_4.grid(row = 1, column=0)
        item_5.grid(row = 1, column=1)
        item_6.grid(row = 1, column=2)
        back = Button(f,text= "Back",font=("simple plan",12),padx=30,pady=20,command=welcome2 )
        back.grid(row=2, column= 1, padx= 10, pady= 10)

#Takes the info on the name of item and the prices
def costing(name,lst, prices):
    global item_1 
    global item_2
    global item_3
    global item_4
    global item_5
    global item_6 
    global back
    
    global nameofrest
    global f
    global total_cost 
    nameofrest.pack()

    #new global variables
    global show1
    global show2
    global size
    global next
    global yes 
    global no

    item_1.destroy()
    item_2.destroy()
    item_3.destroy()
    item_4.destroy()
    item_5.destroy()
    item_6.destroy()
    back.destroy()

    if lst == b:
        show1 = Label(f,text= f"{name} costs {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
        show1.grid(row=0,column=0,columnspan=2)
        show2 = Label(f,text= f"Do you want to add it?", font=("simple plan",25))
        show2.grid(row=1,column=0,columnspan=2)

        yes = Button(f,text = "Yes", font=("simple plan",10),padx=30,pady=20,command=lambda: [extras("bu",lst[prices]), storing(name,lst[prices])])
        no = Button(f,text = "No", font=("simple plan",10),padx=30,pady=20,command=lambda:menu("burgers"))
        
        yes.grid(row=2,column=0,pady=20)
        no.grid(row=2,column=1,pady=20 )



    elif lst == p:
            show1 = Label(f,text= f"{name} costs {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)

            show2 = Label(f,text= f"Do you want to add it?", font=("simple plan",25))
            show2.grid(row=1,column=0,columnspan=2)

            yes = Button(f,text = "Yes", font=("simple plan",10),padx=30,pady=20,command =lambda: [size_of_pizza(lst[prices],p),storing(name,lst[prices])])
            no = Button(f,text = "No", font=("simple plan",10),padx=30,pady=20,command=lambda:menu("pizzas"))
            
            yes.grid(row=2,column=0,pady=20)
            no.grid(row=2,column=1,pady=20) 

    elif lst == fr:
            show1 = Label(f,text= f"{name} costs {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)

            show2 = Label(f,text= f"Do you want to add it?", font=("simple plan",25))
            show2.grid(row=1,column=0,columnspan=2)
            
            if name == "Chicken Fry":
                show3 = Label(f,text= "Large Fries have 4 extra pieces", font=("simple plan",10))
                show3.grid(row=3,column=0,columnspan=2)
                

            yes = Button(f,text = "Yes", font=("simple plan",10),padx=30,pady=20,command=lambda: [largesmall("Fry",lst[prices]),storing(name,lst[prices])])
            no = Button(f,text = "No", font=("simple plan",10),padx=30,pady=20,command=lambda:menu("fries"))
            
            yes.grid(row=2,column=0,pady=20)
            no.grid(row=2,column=1,pady=20)
    
    elif lst == dri:
            show1 = Label(f,text= f"{name} costs {lst[prices]}", font=("simple plan",25),bg="grey",width=30)
            show1.grid(row=0,column=0,columnspan=2)

            show2 = Label(f,text= f"Do you want to add it?", font=("simple plan",25))
            show2.grid(row=1,column=0,columnspan=2)

            yes = Button(f,text = "Yes", font=("simple plan",10),padx=30,pady=20,command=lambda: [largesmall("Dri",lst[prices]),storing(name,lst[prices])])
            no = Button(f,text = "No", font=("simple plan",10),padx=30,pady=20,command=lambda:menu("drinks"))
            
            yes.grid(row=2,column=0,pady=20)
            no.grid(row=2,column=1,pady=20)
    
    elif lst == ri:
        if name == "R1":
            show1 = Label(f,text= f"The Rice Platter 1 serves Fried Rice with Beef & garlic with the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)

        elif name == "R2":
            show1 = Label(f,text= f"The Rice Platter 2 serves Fried Rice with Egg, Beef & Green Pepper with the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)

        elif name == "R3":
            show1 = Label(f,text= f"The Rice Platter 3 serves Fried Rice with Minced Beef & BBQ sauce with the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)
        
        elif name == "R4":
            show1 = Label(f,text= f"The Rice Platter 4 serves Fried Rice with Egg & Sausage with the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)

        elif name == "R5":
            show1 = Label(f,text= f"The Rice Platter 5 serves Fried Rice with Meat & Vegetables with the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)

        elif name == "R6":
            show1 = Label(f,text= f"The Rice Platter 6 serves Fried Rice with Chicken & Chili and Pepper with the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=70)
            show1.grid(row=0,column=0,columnspan=2)
        
        show2 = Label(f,text= f"Do you want to add it?", font=("simple plan",25))
        show2.grid(row=1,column=0,columnspan=2)

        yes = Button(f,text = "Yes", font=("simple plan",15),padx=60,pady=30,command=lambda:[orderitornot("Rice",lst[prices]),storing(name,lst[prices])])
        no = Button(f,text = "No", font=("simple plan",15),padx=60,pady=30,command=lambda:menu("rice"))
        
        yes.grid(row=2,column=0,pady=10)
        no.grid(row=2,column=1,pady=10)
    
    elif lst == co:
        if name == "C1":
            show1 = Label(f,text= f"The Combo Platter 1 serves Two Chicken Burger,\nOne Large French Fries and a small Cold coffee \nwith the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)
        
        elif name == "C2":
            show1 = Label(f,text= f"The Combo Platter 2 serves Two Beef Burger,\nOne Large Onion Rings and a Large Vanilla Milk Shake \nwith the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)
        
        elif name == "C3":
            show1 = Label(f,text= f"The Combo Platter 1 serves Three Veggie Burger,\nOne Medium Cheddar Cream Pizza and Two small Oreo Shake \nwith the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)
        
        elif name == "C4":
            show1 = Label(f,text= f"The Combo Platter 4 serves One Large BBQ Meat Machine Pizza,\n2 Pieces of Chicken Fries and Two small Lassi \nwith the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)
        
        elif name == "C5":
            show1 = Label(f,text= f"The Combo Platter 5 serves One Red Sun Pepparonni Pizza,\nOne Large Fish Fingers and Two Chocolate Cold Coffee \nwith the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)
        
        elif name == "C6":
            show1 = Label(f,text= f"The Combo Platter 6 serves One Double Decker Burger,\nOne Large Sausage carnival Pizza and Two Lassi \nwith the cost of {lst[prices]}", font=("simple plan",25),bg="grey",width=60)
            show1.grid(row=0,column=0,columnspan=2)
        show2 = Label(f,text= f"Do you want to add it?", font=("simple plan",25))
        show2.grid(row=1,column=0,columnspan=2)

        yes = Button(f,text = "Yes", font=("simple plan",15),padx=60,pady=30,command=lambda:[orderitornot("Combos",lst[prices]),storing(name,lst[prices])])
        no = Button(f,text = "No", font=("simple plan",15),padx=60,pady=30,command=lambda:menu("Combos"))
        
        yes.grid(row=2,column=0,pady=10)
        no.grid(row=2,column=1,pady=10)

#if we want to add the extra sauce spice or any thing
def extras(name_of_dish,amount = 0):

    global var1
    global var2
    global var3
    global var4

    global f

    global total_cost

    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

    if name_of_dish == "p":


        sauce = Checkbutton(f,text='More Sauce',variable=var1,font=("noodle soup",15))
        sauce.pack(anchor=W)

        cheese = Checkbutton(f,text='More Cheese',variable=var2,font=("noodle soup",15))
        cheese.pack(anchor=W)

        Sausage = Checkbutton(f,text='More Sausage',variable=var3,font=("noodle soup",15))
        Sausage.pack(anchor=W)

        Less_spicy = Checkbutton(f,text='Less spicy',variable=var4,font=("noodle soup",15))
        Less_spicy.pack(anchor=W)

        next = Button(f,text="next",width=10,padx=20,pady=30,command=lambda: orderitornot("Pizza"))
        next.pack(anchor=W)
    
    elif name_of_dish == "bu":

        total_cost += amount

        sauce = Checkbutton(f,text='More Sauce',variable=var1,font=("noodle soup",15))
        sauce.pack(anchor=W)

        cheese = Checkbutton(f,text='More Cheese',variable=var2,font=("noodle soup",15))
        cheese.pack(anchor=W)

        MIld_spicy = Checkbutton(f,text='More Spicy',variable=var3,font=("noodle soup",15))
        MIld_spicy.pack(anchor=W)

        Less_spicy = Checkbutton(f,text='Less spicy',variable=var4,font=("noodle soup",15))
        Less_spicy.pack(anchor=W)

        next = Button(f,text="next",width=10,padx=20,pady=30,command=lambda: orderitornot("Burger"))
        next.pack(anchor=W)

#only for fries and drinks
def largesmall(type,price):
    global f
    global total_cost

    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)

    total_cost += price
    x  = IntVar()
    
    if type == "Fry":
        question = Label(f,text="Which size do you want?",
                    font= ("new times roman",25),
                    padx=10,
                    pady=10)
        question.grid(columnspan=2)

        radio = Radiobutton(f,
                            text="Large",
                            variable=x,
                            value =  1,
                            font=("yellow ginger",15)
                            )
        radio.grid(columnspan=2)
        radio.deselect()

        radio = Radiobutton(f,
                            text="Small",
                            variable=x,
                            value =  2,
                            font=("yellow ginger",15)
                            )
        radio.grid(columnspan=2)
        radio.deselect()

        next = Button(f,text="next",width=10,padx=20,pady=30,command=lambda: orderitornot("Fry",x.get()))
        next.grid(columnspan=2)

    elif type == "Dri":

        question = Label(f,text="Which size do you want?",
                    font= ("new times roman",25),
                    padx=10,
                    pady=10)
        question.grid(columnspan=2)

        radio = Radiobutton(f,
                            text="Large",
                            variable=x,
                            value =  3,
                            font=("yellow ginger",15)
                            )
        radio.grid(columnspan=2)
        radio.deselect()

        radio = Radiobutton(f,
                            text="Small",
                            variable=x,
                            value =  4,
                            font=("yellow ginger",15)
                            )
        radio.grid(columnspan=2)
        radio.deselect()

        next = Button(f,text="next",width=10,padx=20,pady=30,command=lambda: orderitornot("Dri",x.get()))
        next.grid(columnspan=2)

#setting the size of pizza
def getting_size(some):
    global item_1 
    global item_2
    global item_3
    global item_4
    global item_5
    global item_6

    global f

    global total_cost
    global further

    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)
    if some == 0:
        total_cost += 0

    elif some == 1:
        total_cost += 30
    
    elif some == 2:
        total_cost += 60
    
    elif some == 3:
        total_cost += 90

    further = Label(f,text= f"Do you want to add something more?", font=("simple plan",25))
    further.grid(row=0,column=0,columnspan=2)

    yes = Button(f,text = "Yes", font=("simple plan",10),padx=30,pady=20,command=lambda: extras("p"))
    no = Button(f,text = "No", font=("simple plan",10),padx=30,pady=20,command=lambda: orderitornot("pizz"))
    
    yes.grid(row=1,column=0,pady=20)
    no.grid(row=1,column=1,pady=20) 


def size_of_pizza(cost,name):
    global item_1 
    global item_2
    global item_3
    global item_4
    global item_5
    global item_6

    global f

    global question
    global radio
    global size
    global next
    global total_cost

    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)
     
    size=["Small","Medium", "Large","Family Size"]
    
    x = IntVar()
    x.set(100)


    question = Label(f,text="Which size do you want?",
                    font= ("new times roman",25),
                    padx=10,
                    pady=10)
    question.grid(columnspan=2)

    for i in range(len(size)):
        radio = Radiobutton(f,
                            text=size[i],
                            variable=x,
                            value = i,
                            font=("yellow ginger",15)
                            )
        radio.grid(columnspan=2)
    
    next = Button(f,text="next",width=10,padx=20,pady=30,command=lambda: getting_size(x.get()))
    next.grid(columnspan=2)
    total_cost += cost

#a new welcome
def welcome2():
    global intro 
    global nameofrest
    global first_button

    #assign new global variables to the menues
    global burgers
    global pizza
    global fries
    global combos
    global rice
    global drinks
    global total_cost

    global f 

    intro.destroy()

    first_button.destroy()
    
    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)

    burgers = Button(f,text="Burgers",pady=40,padx=60,command=lambda:menu("Burgers"),width=20,height=2)
    pizza = Button(f,text="Pizzas",pady=40,padx=60,command=lambda:menu("Pizzas"),width=20,height=2)
    fries = Button(f,text="Fries",pady=40,padx=60,command=lambda:menu("Fries"),width=20,height=2)
    combos = Button(f,text="Cobmos",pady=40,padx=60,command=lambda:menu("Combos"),width=20,height=2)
    rice = Button(f,text="Rice",pady=40,padx=60,command=lambda:menu("Rice"),width=20,height=2)
    drinks = Button(f,text="Drinks",pady=40,padx=60,command=lambda:menu("Drinks"),width=20,height=2)
    
    nameofrest.pack()
    
    burgers.grid(row=0,column= 0)
    pizza.grid(row=0,column=1)
    fries.grid(row=0,column= 2)
    combos.grid(row=1,column= 0)
    rice.grid(row=1,column= 1)
    drinks.grid(row=1,column= 2)

#order the items or not
def orderitornot(name_of_dish, amount = 0):

    global var1
    global var2
    global var3
    global var4
    global f
    global total_cost

    
    
    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)

    if name_of_dish== "Pizza":
        sum = var1.get()+var2.get()+var3.get()+var4.get()
        total_cost += 30*sum

    elif name_of_dish == "pizz":
        total_cost = total_cost
    
    elif name_of_dish == "Burger":
        sum = var1.get()+var2.get()+var3.get()+var4.get()
        total_cost += 20*sum

    elif name_of_dish == "Fry":
        if amount == 2:
            total_cost+= 0
        elif amount == 1:
            total_cost +=50
    
    elif name_of_dish == "Dri":
        if amount == 4:
            total_cost += 0 
        elif amount == 3:
            total_cost += 60
    
    elif name_of_dish == "Rice":
        total_cost += amount
    elif name_of_dish == "Combos":
        total_cost += amount
    
    further = Label(f,text= f"Do you want to add something any other items", font=("simple plan",25))
    further.grid(row=0,column=0,columnspan=2)

    yes = Button(f,text = "Yes", font=("simple plan",10),padx=30,pady=20,command=welcome2)
    no = Button(f,text = "No", font=("simple plan",10),padx=30,pady=20,command=confirmornot)
    
    yes.grid(row=1,column=0,pady=20)
    no.grid(row=1,column=1,pady=20) 

#confirm the order or not 
def confirmornot():
    global tup
    global f
    
    x = 1
    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)
    
    show0 = Label(f,text="You Ordered:",font=("brownies",25))
    show0.grid(row=0,column=0,columnspan=2)

    for i in tup:
        show1 = Label(f, text=f"{i[0]}: {i[1]} Taka",font=("Yummycupcakes", 20), width=50)
        show1.grid(row=x,column=0,columnspan=2,padx=5,pady=5)

        x+=1
    
    show2 = Label(f,text=f"Total cost: {total_cost}",font=("brownies",25))
    show2.grid(row=x+1,column=0,columnspan=2)


    confirm = Button(f,text= "Confirm", font=("croissant one", 18),padx=10,pady=20, width= 20, command= confirmnow)
    no = Button(f,text= "No", font=("croissant one", 18),padx=10,pady=20, width= 20,command=orderaginorquit)
    confirm.grid(row = x+2, column= 0, padx=10,pady=10)
    no.grid(row = x+2, column= 1, padx=10,pady=10)    

#order again it or quit
def orderaginorquit():
    
    global total_cost
    global f
    global tup

    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)
    tup = []
    total_cost = 0

    show1 = Label(f,text="Do you want to  order again?",font=("brownies",25))
    show1.grid(row=0,column=0,columnspan=2,pady=10)

    yes = Button(f,text= "Yes", font=("croissant one", 18),padx=10,pady=20, width= 20,command= welcome2)
    no = Button(f,text= "No", font=("croissant one", 18),padx=10,pady=20, width= 20,command=quit)

    yes.grid(row = 1, column= 0, padx=10,pady=10)
    no.grid(row = 1, column= 1, padx=10,pady=10)

#storing the informations
def storing(name,price):
    global tup
    tup.append((name,price))

#confirming the order 
def confirmnow():
    global f 
    global tup 
    global total_cost

    f.destroy()
    f = LabelFrame(window,padx=20,pady=20)
    f.pack(padx=15,pady=15)
    tup = []
    total_cost = 0
    messagebox.showinfo("The Eaters Palace","Your order has been places")
    Button(f,text= "Re-Order", padx=30,pady=20, font=("croissant one", 18),command=welcome2).grid(row=0, column=0, padx=15)
    Button(f,text= "Quit", padx=30,pady=20, font=("croissant one", 18),command=quit).grid(row=0, column=1, padx=15)


#image that will go in the first window
introimg = ImageTk.PhotoImage(Image.open("Images/burger.png"))
intro = Label(window,image=introimg)

#the name of the resturant 
nameofrest = Label(window,text="The Eaters Palace",font=("baguette",50,),bg="gold",padx=720)
nameofrest.pack()

intro.pack(pady=15,anchor="center")

first_button = Button(window,text="welcome",font=("yellow ginger" ,15),bg="#008000",activebackground="#008000",bd=5,command= welcome)
first_button.pack(side="bottom", pady=20)

window.mainloop()