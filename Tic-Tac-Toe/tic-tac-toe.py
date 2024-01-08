from tkinter import *
import random

def next_turn(row, column):
    
    global which

    if game_board[row][column]['text'] == '' and check_winner() is False:

        if which == symbols[0]:

            game_board[row][column]['text'] = which

            if check_winner() is False:
                which = symbols[1]
                headline.config(text =(symbols[1] +" Turn"))
            
            elif check_winner() is True:
                headline.config(text = (symbols[0]+" Wins"))
                restrat.config(bg = "grey")
            
            elif check_winner == "Tie":
                headline.config(text = ("Tie"))
                
        else:
            game_board[row][column]['text'] = which

            if check_winner() is False:
                which = symbols[0]
                headline.config(text = (symbols[0] +" Turn" ))
            
            elif check_winner() is True:
                headline.config(text = (symbols[1] + " Wins"))
                restrat.config(bg = "grey")
            
            elif check_winner() == "Tie":
                headline.config(text = ("Tie"))
                
        


def check_winner():
    for i in range(3):
        if game_board[i][0]['text'] == game_board[i][1]['text'] == game_board[i][2]['text'] != "":
            game_board[i][0].config(bg = "green")
            game_board[i][1].config(bg = "green")
            game_board[i][2].config(bg = "green")

            if i == 0:
                game_board[1][2].config(bg = "black")
                game_board[1][1].config(bg = "black")
                game_board[1][0].config(bg = "black")
                game_board[2][2].config(bg = "black")
                game_board[2][0].config(bg = "black")
                game_board[2][1].config(bg = "black")
            
            elif i == 1:
                game_board[0][2].config(bg = "black")
                game_board[0][1].config(bg = "black")
                game_board[0][0].config(bg = "black")
                game_board[2][2].config(bg = "black")
                game_board[2][0].config(bg = "black")
                game_board[2][1].config(bg = "black")
            
            elif i == 2:
                game_board[1][2].config(bg = "black")
                game_board[1][1].config(bg = "black")
                game_board[1][0].config(bg = "black")
                game_board[0][2].config(bg = "black")
                game_board[0][0].config(bg = "black")
                game_board[0][1].config(bg = "black")

            return True
        
    for j in range(3):
        if game_board[0][j]['text'] == game_board[1][j]['text'] == game_board[2][j]['text'] != "":
            game_board[0][j].config(bg = "green")
            game_board[1][j].config(bg = "green")
            game_board[2][j].config(bg = "green")

            if j == 0:
                game_board[0][1].config(bg = "black")
                game_board[1][1].config(bg = "black")
                game_board[2][1].config(bg = "black")
                game_board[2][2].config(bg = "black")
                game_board[1][2].config(bg = "black")
                game_board[0][2].config(bg = "black")
            
            elif j == 1:
                game_board[0][0].config(bg = "black")
                game_board[1][0].config(bg = "black")
                game_board[2][0].config(bg = "black")
                game_board[0][2].config(bg = "black")
                game_board[1][2].config(bg = "black")
                game_board[2][2].config(bg = "black")
            
            elif j == 2:
                game_board[0][0].config(bg = "black")
                game_board[1][0].config(bg = "black")
                game_board[2][0].config(bg = "black")
                game_board[0][1].config(bg = "black")
                game_board[1][1].config(bg = "black")
                game_board[2][1].config(bg = "black")
            return True
                
    if game_board[0][0]['text'] == game_board[1][1]['text'] == game_board[2][2]['text'] != "":
            game_board[0][0].config(bg = "green")
            game_board[1][1].config(bg = "green")
            game_board[2][2].config(bg = "green")

            game_board[0][2].config(bg = "black")
            game_board[0][1].config(bg = "black")
            game_board[1][0].config(bg = "black")
            game_board[1][2].config(bg = "black")
            game_board[2][0].config(bg = "black")
            game_board[2][1].config(bg = "black")


            return True
        
    elif game_board[0][2]['text'] == game_board[1][1]['text'] == game_board[2][0]['text']  != "":
            game_board[0][2].config(bg = "green")
            game_board[1][1].config(bg = "green")
            game_board[2][0].config(bg = "green")

            game_board[0][0].config(bg = "black")
            game_board[0][1].config(bg = "black")
            game_board[1][0].config(bg = "black")
            game_board[1][2].config(bg = "black")
            game_board[2][2].config(bg = "black")
            game_board[2][1].config(bg = "black")
            return True
        
    elif empty_spaces() is False:
            for row in range(3):
               for column in range(3):
                   game_board[row][column].config(bg="red")
            restrat.config(bg = "yellow")
        
            return "Tie"
        
    else:
            return False
        

def empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_board[row][col]["text"] != "":
                spaces -= 1

    if spaces == 0:
       return False
    else:
        return True
    
def new_game():
    global which

    which = random.choice(symbols)

    headline.config(text = which +" Turn")

    for i in range(3):
        for j in range(3):
            game_board[i][j].config(text='', bg ="#F0F0F0")
            restrat.config(bg = "#F0F0F0")


window = Tk()
window.title('Tic-Tac-Toe')

symbols = ['X','O']
which = random.choice(symbols)
game_board = [[0,0,0],
              [0,0,0],  
              [0,0,0]]

headline = Label(text= which + " turn", font = ('Times New Roman', 45))
headline.pack(side = 'top')

restrat = Button(text = "restart", font= ('Times New Roman', 25), command= new_game )
restrat.pack(side = 'bottom')

frame = Frame(window)
frame.pack()

for i in range(3):
    for j in range(3):
        game_board[i][j] = Button(frame, text = "", font= ('Times New Roman', 45), width = 5, height = 2,
                                   command= lambda row = i, column = j: next_turn(row,column))
        game_board[i][j].grid(row = i, column = j)

window.mainloop()

#took help from here (https://www.youtube.com/watch?v=V9MbQ2Xl4CE&t=747s)