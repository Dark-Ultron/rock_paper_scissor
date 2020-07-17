import tkinter as tk
from tkinter import ttk
import random

main_application = tk.Tk()
main_application.title(
    '                                                                                                Rock Paper Scissor Game')
main_application.geometry('800x600')
main_application.configure(background='#FFB5C2')
main_application.resizable(0, 0)

headline = ttk.Label(main_application, text='Rock Paper Scissor', foreground='grey',background='#FFB5C2' )
headline.pack(side=tk.TOP)
headline.configure(font=('Calligraphy', 40))

live_status = ttk.Label(main_application, text='Let\'s Start the Game!', foreground='green', background='#FFB5C2', font=('Digital-7 Mono', 15))
live_status.pack(pady=10)
main_frame = tk.Frame(main_application,background='#FFB5C2')
main_frame.pack(fill=tk.BOTH)
option_label = ttk.Label(main_frame, text='Your Option: ', background='#FFB5C2', font=('Dungeon',10))
option_label.grid(row=0, column=0, padx=100, pady=30)

rock_icon = tk.PhotoImage(file='icon\\rock.png')
rock_button = tk.Button(main_frame, text='The Rock', image=rock_icon, width=100, borderwidth=1, background='black', foreground='white',
                        font=('vtks distress', 10), compound=tk.BOTTOM)
rock_button.grid(row=1, column=1, padx=10, pady=20)
paper_icon = tk.PhotoImage(file='icon\\paper.png')
paper_button = tk.Button(main_frame, text='Paper', image=paper_icon, width=100, borderwidth=1, background='black', foreground='white',
                         font=('vtks distress', 10),compound=tk.BOTTOM)
paper_button.grid(row=1, column=2, padx=10, pady=20)
scissor_icon = tk.PhotoImage(file='icon\\scissor .png')
scissor_button = tk.Button(main_frame, text='Scissor', image=scissor_icon, width=100, borderwidth=1, background='black', foreground='white',
                           font=('vtks distress', 10), compound=tk.BOTTOM)
scissor_button.grid(row=1, column=3, padx=10, pady=20)

score_label = ttk.Label(main_frame, text='Score:', background='#FFB5C2',font=('Dungeon',10)).grid(row=2, column=0, padx=100, pady=30 )

y_select = ttk.Label(main_frame, text='You Selected:--', font=('Century Gothic',10),background='#FFB5C2')
y_select.grid(row=3, column=1)
c_select = ttk.Label(main_frame, text='Computer Selected:--',font=('Century Gothic',10),background='#FFB5C2')
c_select.grid(row=4, column=1)

y_score = ttk.Label(main_frame, text='Your Score: ',font=('Century Gothic',10),background='#FFB5C2')
y_score.grid(row=3, column=3)
c_score = ttk.Label(main_frame, text='Computer Score: ',font=('Century Gothic',10),background='#FFB5C2')
c_score.grid(row=4, column=3)

user_won = 0
comp_won = 0

table = ['rock', 'paper', 'scissor']


def scoreboard(uchoice, cchoice):
    y_select.config(text=f'You Selected: {uchoice}')
    c_select.config(text=f'Computer Selected: {cchoice}')
    if (uchoice == 'rock' and cchoice == 'scissor') or (uchoice == 'scissor' and cchoice == 'paper') or (
            uchoice == 'paper' and cchoice == 'rock'):
        live_status.config(text='You Win')
        global user_won
        user_won += 1
        y_score.config(text=f'Your Score: {user_won}')
    elif (cchoice == 'rock' and uchoice == 'scissor') or (cchoice == 'scissor' and uchoice == 'paper') or (
            cchoice == 'paper' and uchoice == 'rock'):
        live_status.config(text='Computer Win')
        global comp_won
        comp_won += 1
        c_score.config(text=f'Computer Score: {comp_won}')
    else:
        live_status.config(text='Tie')

def rock(even=None):
    choice = random.choice(table)
    scoreboard('rock', choice)
def paper(even=None):
    choice = random.choice(table)
    scoreboard('paper', choice)

def scissor(even=None):
    choice = random.choice(table)
    scoreboard('scissor', choice)


rock_button.configure(command=rock)
paper_button.configure(command=paper)
scissor_button.configure(command=scissor)


main_application.mainloop()
