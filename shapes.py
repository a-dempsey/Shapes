import tkinter as tk
import random
import time

window = tk.Tk()
#canvas = tk.Canvas()
start_button = tk.Button

class Startpage():
    def __init__(self):
        window.title('Shapes')
        window.geometry('720x580')
        window.maxsize(720,580)
        global canvas
        canvas = tk.Canvas(window, width=720, height=580, bg='#B0C7ED')
        self.ptsLabel()
        self.startButton()
        self.settingsMenu()
        canvas.grid(row=1, column=1)
        window.bind('<Control-c>', exitGame)

    def ptsLabel(self):
        global pointsLabel
        pointsLabel = tk.Label(window, text='Score: 0', font='Georgia 16', bg='#B0C7ED')
        pointsLabel.place(relx=0.01, rely=0.01)

    def startButton(self):
        global start_button
        start_button = tk.Button(window, text='Start Game', bg='powderblue', height=4, width=15, command=Shapes)
        start_button.place(relx=0.4, rely=0.4)

    def settingsMenu(self):
        menyou = tk.Menu(window)
        window.config(menu=menyou)
        menU = tk.Menu(menyou, bg='pink', fg='black')
        menyou.add_cascade(label='Settings', menu=menU)
        menU.add_command(label="Restart game", command=restart)

class Shapes:
    def __init__(self):
        global shapes
        shapes = [self.arc, self.circle, self.square]
        start_button.destroy()
        self.generate()

    def generate(self):
        global start_time
        start_time = int(round(time.time()) * 1000)
        global c
        colors = {1: '#FDE6CC', 2: '#FFBDDE', 3: '#B6EEBD', 4: '#DBBDE3'}
        c = colors[random.randint(1, 3)]
        random.choice(shapes)()
        if score.score > 2:
            Enemy()

    def circle(self):
        x = random.randint(1, 500)
        y = random.randint(1, 450)
        global circ
        circ = canvas.create_oval(x, y, x + 60, y + 60, fill=c)
        canvas.tag_bind(circ, '<ButtonPress-1>', click)

    def square(self):
        x = random.randint(1, 500)
        y = random.randint(1, 450)
        global reck
        reck = canvas.create_rectangle(x, y, x + 60, y + 60, fill=c)
        canvas.tag_bind(reck, '<ButtonPress-1>', click)

    def arc(self):
        x = random.randint(1, 500)
        y = random.randint(1, 450)
        global covnet
        covnet = canvas.create_arc(x, y, x + 90, y + 90, fill=c)
        canvas.tag_bind(covnet, '<ButtonPress-1>', click)

class Score:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return '%i' % self._score


def click(item):
    end_time = int(round(time.time() * 1000))
    total = end_time - start_time
    if total <= 2000:
        score.score += 1
        pointsLabel.config(text='Score: %i' % (score.score))
    canvas.delete('all')
    Shapes.generate(item)


class Enemy:
    def __init__(self):
        coords = [10, 20, 75, 35, 45, 75, 10, 20]
        self._enemy = canvas.create_polygon(coords, fill='hotpink', outline='blue', width=2)
        canvas.tag_bind(self._enemy, '<ButtonPress-1>', Enemy.collision)
        self._x = random.randint(0, 20)
        self._y = random.randint(0, 20)
        self.moveEnemy()


    def moveEnemy(self):
        e = canvas.move(self._enemy, self._x, self._y)
        canvas.after(40, self.moveEnemy)

    def collision(self):
        score.score = score.score + 2
        pointsLabel.config(text='Score: %i' % score.score)

def restart():
    canvas.delete('all')
    score.score = 0
    pointsLabel.config(text='Score: %i' % score.score)
    global start
    start = tk.Button(canvas, text='Start Game', bg='powderblue', height=4, width=15, command=delete)
    start.place(relx=0.4, rely=0.4)

def delete():
    start.destroy()
    Shapes()

def exitGame(game):
    quit()

start = Startpage()
score = Score()
window.mainloop()
