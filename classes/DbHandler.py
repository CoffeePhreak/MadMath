import sqlite3

class DbHandler:
    def __init__(self,dbFile,configFile=''):
        self.con=sqlite3.connect(dbFile)
        self.cur=self.con.cursor()
        self.configFile = configFile

    def __del__(self):
        self.con.close()

    def _load_config(self,configFile):
        try:
            with open(configFile,'r') as f:
                configData = f.readlines()
                return configData
        except:
            print("Error opening: "+configFile)

    def _run_sql(self,command):
        try:
            self.cur.execute(command)
            self.con.commit()
        except sqlite3.Error as Error:
            print(Error)

    def write_tables_from_list(self):
        try:
            commandList = self._load_config(self.configFile)
            for command in commandList:
                self._run_sql(command.strip())
            self.con.commit()
        except:
            print("Something went wrong trying to setup database.")

    def check_score(self,table,score):
        query = "SELECT * FROM %s WHERE score<=%d;" %(table,score)
        self._run_sql(query)
        self.records = self.cur.fetchall()
        match len(self.records):
            case 0:
                return 0
            case 10:
                return 1
            case _:
                return 2

    def update_all(self,table,score,name,date,missed,index):
        del self.records[-1]
        if len(self.records) > 0:
            for line in self.records:
                self._update_record(table,line[1],line[2],line[3],line[4],line[0]+1)
        self._update_record(table,score,name,date,missed,index)

    def _update_record(self,table,score,name,date,missed,index):
        update = "UPDATE %s SET score=%d,name='%s',date='%s',missed=%d WHERE id=%d;" %(table,score,name,date,missed,index)
        self._run_sql(update)

    def pull_records(self,table):
        self._run_sql("SELECT * FROM %s;" %table)
        data = self.cur.fetchall()
        return data
