from tkinter import ttk
#from time import perf_counter
fg = "#000000"
bg = "#00FFFF"
red = "#FF0000"
green = "#00FF00"
blue = "#0AC7C7"
white = "#FFFFFF"
def frame_style():return ttk.Style().configure("frameStyle.TFrame",background=bg)
def score_frame_style():return ttk.Style().configure("scoreFrameStyle.TFrame",foreground=bg,background=fg)
def label_style():return ttk.Style().configure("labelStyle.TLabel",background=bg,font=('Sans',18))
def header_style():return ttk.Style().configure("header.labelStyle.TLabel",font=('Sans',20,'bold'))
def equation_style():return ttk.Style().configure("equationStyle.TLabel",background=white,width=1,font=('Sans',25,'bold'))
def button_style():return ttk.Style().configure("buttonStyle.TButton",background=bg,font=('Sans',16,'bold'))
def entry_style():return ttk.Style().configure("entryStyle.TEntry",background=bg,font=('Sans',20))

def frame_init(self,parent):
    self.parent = parent
    frame_style()
    score_frame_style()
    label_style()
    header_style()
    button_style()
    equation_style()
    entry_style()
    self.config(style="frameStyle.TFrame")

class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        frame_init(self,parent)
        self.parent.title("Mad Math Menu")

        self.style = ttk.Style(self)
        self.style.configure("radioStyle.TRadiobutton",background=bg,anchor='center',font=('Sans',18,'bold'))
        self.style.map("radioStyle.TRadiobutton",background=[('active',blue),
                                                             ('selected',blue)],
                                                 foreground=[('selected',fg),
                                                             ('!selected',fg)])
        #Had to customize layout to remove indicator
        self.style.layout("radioStyle.TRadiobutton",[('Radiobutton.padding',{'sticky':'nswe','children':
                        [('Radiobutton.focus',{'side':'left','sticky':'','children':[('Radiobutton.label',
                        {'sticky':'nswe'})]})]})])

        self.additionRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Addition",width=13,
                    variable=self.parent.opVar,value="Addition").grid(column=0,row=1,padx=(20,10),pady=(10,0))

        self.subtactionRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Subtraction",width=13,
                    variable=self.parent.opVar,value="Subtraction").grid(column=0,row=2,padx=(20,10))

        self.multiplicationRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Multiplication",width=13,
                    variable=self.parent.opVar,value="Multiplication").grid(column=0,row=3,padx=(20,10))

        self.divisionRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Division",width=13,
                    variable=self.parent.opVar,value="Division").grid(column=0,row=4,padx=(20,10),pady=(0,10))

        self.easyRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Easy",width=8,
                    variable=self.parent.difVar,value="Easy").grid(column=1,row=2,padx=(10,20))

        self.mediumRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Medium",width=8,
                    variable=self.parent.difVar,value="Medium").grid(column=1,row=3,padx=(10,20))

        self.hardRadio = ttk.Radiobutton(self,style="radioStyle.TRadiobutton",text="Hard",width=8,
                    variable=self.parent.difVar,value="Hard").grid(column=1,row=4,padx=(10,20),pady=(0,10))

        self.scoresButton = ttk.Button(self,text=" Hi-Scores ",style="buttonStyle.TButton",
                    command=lambda:self.parent.switch_frame(Scoreboard)).grid(column=0,row=5,padx=(20,10),pady=(0,10))

        self.playButton = ttk.Button(self,text=" Play! ",style="buttonStyle.TButton",
                    command=lambda:self.parent.switch_frame(Quiz)).grid(column=1,row=5,
                    padx=(10,27),pady=(0,10),sticky="e")
############################################################################################################################
class Scoreboard(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        frame_init(self,parent)

        self.style = ttk.Style(self)
        self.style.configure("radioStyle.TRadiobutton",font=('Sans',10,'bold'))
        self.scoreStyle = ttk.Style().configure("scoreStyle.labelStyle.TLabel",
                    background=bg,foreground=fg,font=('Sans',18,'bold'))

        self._populate()

    def _populate(self):
        self.parent.title("Mad Math Scoreboard - %s %s" %(self.parent.opVar.get(),self.parent.difVar.get()))
        self.table = self.parent.get_table_name()
        self.records = self.parent.db.pull_records(self.table)

        numHeader = ttk.Label(self,text="No.",style="header.labelStyle.TLabel",
                    anchor='center').grid(column=0,row=4,padx=12,pady=8,sticky="ew")
        scoreHeader = ttk.Label(self,text="Score",style="header.labelStyle.TLabel",
                    anchor='center').grid(column=1,row=4,padx=12,pady=8,sticky="ew")
        inisHeader = ttk.Label(self,text="Initials",style="header.labelStyle.TLabel",
                    anchor='center').grid(column=2,row=4,padx=12,pady=8,sticky="ew")
        dateHeader = ttk.Label(self,text="Date",style="header.labelStyle.TLabel",
                    anchor='center').grid(column=3,row=4,padx=12,pady=8,sticky="ew")
        missedHeader = ttk.Label(self,text="Missed",style="header.labelStyle.TLabel",
                    anchor='center').grid(column=4,row=4,padx=12,pady=8,sticky="ew")

        for record in self.records:
            numLabel = ttk.Label(self,text="%3d" %record[0],style="scoreStyle.labelStyle.TLabel").grid(column=0,
                        row=(record[0]+4),padx=12,sticky="ew")
            scoreLabel = ttk.Label(self,text="%3d" %record[1],style="scoreStyle.labelStyle.TLabel").grid(column=1,
                        row=(record[0]+4),padx=30,sticky="ew")
            inisLabel = ttk.Label(self,text="%4s" %record[2].strip("'"),style="scoreStyle.labelStyle.TLabel").grid(column=2,
                        row=(record[0]+4),padx=20,sticky="ew")
            dateLabel = ttk.Label(self,text="%11s" %record[3],style="scoreStyle.labelStyle.TLabel").grid(column=3,
                        row=(record[0]+4),padx=12,sticky="ew")
            missedLabel = ttk.Label(self,text="%3d" %record[4],style="scoreStyle.labelStyle.TLabel").grid(column=4,
                        row=(record[0]+4),padx=40,sticky="ew")

        self.backButton = ttk.Button(self,text=" Back ",style="buttonStyle.TButton",
                    command=lambda:self.parent.switch_frame(Menu)).grid(column=0,row=15,columnspan=5,padx=100,pady=(10,10))
#############################################################################################################################
class Quiz(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        frame_init(self,parent)

        self.op = self.parent.opVar.get()
        self.dif = self.parent.difVar.get()
        match self.op:
            case "Addition":
                self.opChar = '+'
            case "Subtraction":
                self.opChar = '–'
            case "Multiplication":
                self.opChar = '×'
            case "Division":
                self.opChar = '÷'

        self._init_config()
        self.parent.title("Mad %s %s" %(self.op,self.dif))

    def _init_config(self):
        self.remaining = 60
        self.score = 0
        self.missed = 0

        self.parent.configure(background=white)

        self.equationLabel = ttk.Label(self,text="  %3s\n%c%3s" %('X',self.opChar,'Y'),style="equationStyle.TLabel",
                    anchor='center')
        self.timerLabel = ttk.Label(self,text="Time left: 60",style="header.labelStyle.TLabel")
        self.equationLabel.grid(column=1,row=1,rowspan=2,padx=(35,0),pady=4,sticky="ew")
        self.timerLabel.grid(column=1,row=0,columnspan=2,padx=(0,20),pady=5,sticky="ew")

        self.backButton = ttk.Button(self,text=" Back ",style="buttonStyle.TButton",
                    command=lambda:self.parent.switch_frame(Menu))
        self.startButton = ttk.Button(self,text=" Start ",style="buttonStyle.TButton",
                    command=self._quiz_start)

        self.startButton.focus()
        self.startButton.bind('<Return>',self._quiz_start)

        self.backButton.grid(column=0,row=5,columnspan=2,padx=(30,20),pady=(26,10),sticky="w")
        self.startButton.grid(column=2,row=5,columnspan=2,padx=(20,30),pady=(26,10),sticky="e")

        self.answerEntry = ttk.Entry(self,textvariable=self.parent.ansVar,width=2,
                    style="entryStyle.TEntry",font=('Sans',16))
        self.answerEntry.grid(column=2,row=2,padx=(20,0),pady=5,sticky="nsew")
        self.answerEntry.delete(0,20)
        self.answerEntry.config(state='disabled')

    def _quiz_start(self,event=None):
        self.running = True
        #self.startT = perf_counter()
        self._quiz_config()
        self._generate()
        self._countdown()

    def _quiz_end(self):
        self.running = False
        #self.endT = perf_counter()
        self._eval_answer(None,1)
        self.startButton.config(state='disabled')
        self.answerEntry.config(state='disabled')
        #print("Real time: ",self.endT-self.startT)
        self.answerEntry.unbind('<Return>')

        #Data race handler if no high score to buffer self.running check in _countdown
        if self.parent.checker(self.score,self.missed) == 3:
            self.after(1000,self._init_config)

    def _quiz_config(self):
        self.startButton.unbind('<Return>')
        self.answerEntry.config(state='enabled')
        self.answerEntry.bind('<Return>',self._eval_answer)
        self.backButton.config(text=" Cancel ",command=self._quiz_end)
        self.startButton.config(text=" Check ",command=self._eval_answer)

    def _generate(self):
        self.equation = self.parent.eg.generate(self.op,self.dif)
        self.equationLabel.config(text="  %3d\n%c%3d" %(self.equation[0],self.opChar,self.equation[1]))
        self.answerEntry.focus()

    def _countdown(self):
        if self.remaining > 0 and self.running != False:
            self._tick()
        elif self.remaining == 0 and self.running != False:
            self._quiz_end()

    def _tick(self):
        self.timerLabel.configure(text="Time left: %2d" %self.remaining)
        self.remaining -= 1
        self.after(1000,self._countdown)

    def _eval_answer(self,event=None,flag=0):
        try:
            x = self.parent.ansVar.get()
            self.answerEntry.delete(0,20)
            if x == self.equation[2]:
                self.parent.configure(background=green)
                self.parent.play(1)
                self.score += 1
            else:
                self.parent.configure(background=red)
                self.parent.play(0)
                self.missed += 1
            if flag != 1:
                self._generate()
        except Exception as e:
            self.answerEntry.delete(0,20)
############################################################################################################################
class HighScore(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        frame_init(self,parent)
        self.parent.configure(background=white)

        text1,text2 = self._get_text()
        text3 = "Enter Your Initials:"

        self.text1Display = ttk.Label(self,text=text1,style="header.labelStyle.TLabel",
                    anchor='center').grid(column=0,row=0,columnspan=3,pady=8,sticky="ew")

        self.text2Display = ttk.Label(self,text=text2,style="header.labelStyle.TLabel",
                    anchor='center').grid(column=0,row=1,columnspan=3,padx=10,pady=8,sticky="ew")

        self.text3Display = ttk.Label(self,text=text3,style="header.labelStyle.TLabel",
                    anchor='center').grid(column=0,row=2,columnspan=3,pady=8,sticky="ew")

        self.inisEntry = ttk.Entry(self,textvariable=self.parent.inisVar,width=10,justify='center',
                    style="entryStyle.TEntry",font=('Sans',16,'bold'))

        self.inisEntry.config(validate='all',validatecommand=(self.parent.register(self._inis_validate),'%P'))
        self.inisEntry.grid(column=1,row=3,pady=(0,10))
        self.inisEntry.focus()

        self.okButton = ttk.Button(self,text="Ok!",style="buttonStyle.TButton",
                    command=self._submit).grid(column=1,row=4,pady=(0,10))

    def _get_text(self):
        if self.parent.topScore == True:
            text1 = "Incredible!!!" 
            text2 = "You Got The New Top Score: %d!!!" %self.parent.score
            self.parent.topScore = False
            return text1,text2
        else:
            text1 = "Good job!" 
            text2 = "You got a high score of: %d!" %self.parent.score
            return text1,text2

    def _inis_validate(self,text):
        return text.isalpha() and not text.isdigit() and len(text) <= 3

    def _submit(self):
        if len(self.parent.inisVar.get()) != 0:
            self.parent.switch_frame(Quiz)
            self.parent.build_record()
            self.parent.inisVar.set('')
