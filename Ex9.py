class Time:
    def __init__(self, Hr_Value = 0, Min_Value = 0, Sec_Value = 0):
        self.Hr = Hr_Value
        self.Min = Min_Value
        self.Sec = Sec_Value
    def __str__ (self):
        return str(self.Hr) + ':' + str(self.Min) + ':' + str(self.Sec)
    def __repr__(self):
        return str(self.Hr) + ':' + str(self.Min) + ':' + str(self.Sec)
    def Show(self):
        return str(self.Hr) + ':' + str(self.Min) + ':' + str(self.Sec)
    def __add__ (self, arg2):
        add_Sec = self.Sec + arg2.Sec
        add_Min = self.Min + arg2.Min
        add_Hr = self.Hr + arg2.Hr
        if add_Sec >= 60:
            add_Sec -= 60
            add_Min += 1
        if add_Min >= 60:
            add_Min -= 60
            add_Hr += 1
        return str(add_Hr) + ':' + str(add_Min) + ':' + str(add_Sec)
    def __sub__(self,arg2):
        sub_Sec = self.Sec - arg2.Sec
        sub_Min = self.Min - arg2.Min
        sub_Hr = self.Hr - arg2.Hr
        if sub_Sec < 0:
            sub_Sec += 60
            sub_Min -= 1
        if sub_Min < 0:
            sub_Min += 60
            sub_Hr -= 1
        return str(sub_Hr) + ':' + str(sub_Min) + ':' + str(sub_Sec)
    def __gt__ (self, arg2):
        self_Sec = self.Sec + (60*self.Min) + (3600*self.Hr)
        arg2_Sec = arg2.Sec + (60*arg2.Min) + (3600*arg2.Hr)
        if self_Sec > arg2_Sec:
            return True
        else:
            return False
    def __eq__ (self, arg2):
        if self.Sec == arg2.Sec and self.Min == arg2.Min and self.Hr == arg2.Hr :
            return True
        else:
            return False
       

