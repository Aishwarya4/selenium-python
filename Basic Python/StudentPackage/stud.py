class Student:
    def __init__(self,sid,sname,sgrade):
        self.sid=sid
        self.sname=sname
        self.sgrade=sgrade
    def displaystud(self):
        print("sid:{} sname:{} sgrade:{}".format(self.sid,self.sname,self.sgrade))
