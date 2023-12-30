import tkinter as tk
import classes.EquationGenerator as Eg
import os
import classes.DbHandler as Db
import platform
import classes.Frames as Frames
from datetime import datetime

class MadMath(tk.Tk):
    def __init__(self):
        super().__init__()
        self.opVar = tk.StringVar(self,value="Addition",name="opVar")
        self.difVar = tk.StringVar(self,value="Easy",name="difVar")
        self.inisVar = tk.StringVar(self,value='',name="inisVar")
        self.ansVar = tk.IntVar(self,value=None,name="answerVar")

        self.frame = None
        self.resizable(width=False,height=False)

        self.eg = Eg.Generator()
        self.db = self._db_init()
        self._set_sound()

        self.inisVar.trace_add('write',self._to_upper)

        self.switch_frame(Frames.Menu)

        self.topScore = False

    def _db_init(self):
        self.data = os.path.join(os.getcwd(),"data")
        dbPath = os.path.abspath(os.path.join(self.data,"MadMath.db"))
        dbScript  = os.path.abspath(os.path.join(self.data,"db.setup"))
        if not os.path.isfile(dbPath):
            db = Db.DbHandler(dbPath,dbScript)
            db.write_tables_from_list()
        else:
            db = Db.DbHandler(dbPath,dbScript)
        return db

    def _set_sound(self):
        self.correct =  os.path.abspath(os.path.join(self.data,"correct.wav"))
        self.incorrect = os.path.abspath(os.path.join(self.data,"incorrect.wav"))
        self.highscore = os.path.abspath(os.path.join(self.data,"highscore.wav"))
        self.opSys = platform.system()
        if self.opSys == 'Windows':
            self.ws = __import__('winsound')
            
    def play(self,which):
        match which:
            case 0:
                sound = self.incorrect
            case 1:
                sound = self.correct
            case 2:
                sound = self.highscore
                
        match self.opSys:
            case 'Windows':
                self.ws.PlaySound(sound,self.ws.SND_ASYNC)
            case 'Darwin':
                # os.system("afplay "+self.correct)
                pass
            case 'Linux':
                # os.system("aplay "+self.correct)
                pass
            case _:
                pass

    def switch_frame(self,frame):
        newFrame = frame(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newFrame

        #Default config for new frame
        self.frame.grid(column=0,row=0,padx=5,pady=5,sticky="nsew")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def checker(self,score,missed):
        self.table = self.get_table_name()
        self.score = score
        self.missed = missed
        
        x = self.db.check_score(self.table,self.score)

        match x:
            case 1:
                self.play(2)
                self.topScore = True
                self.switch_frame(Frames.HighScore)
                return 1
            case 2:
                self.switch_frame(Frames.HighScore)
                return 2
            case _:
                return 3

    def get_table_name(self):
        return str(self.opVar.get().lower()+self.difVar.get())

    def _to_upper(self,var,index,mode):
        self.inisVar.set(self.inisVar.get().upper())  

    def build_record(self):
        name = "%s" %self.inisVar.get()
        date = datetime.now().strftime("%m/%d/%Y")
        index = self.db.records[0][0]

        self.db.update_all(self.table,self.score,name,date,self.missed,index)
        del self.db.records
