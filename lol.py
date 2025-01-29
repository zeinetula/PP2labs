class Time:
    def __init__(self,sec,min,hours):
        if sec>=60 or min>=60:
            print("invalid")
        elif hours>=24:
            print("invalid")
        else:
            self.sec=sec
            self.min=min
            self.hours=hours
    def __str__(self):
       return f"{self.hours}:{self.min}:{self.sec}"
    def increment_sec(self):
        if self.sec==59:
            self.sec=0
            self.min+=1
            if self.min==60:
                self.min=0
                self.hours+=1
                if self.hours==24:
                    self.hours=0
        else:
            self.sec+=1
    def decrement_sec(self):
        if self.sec==0:
            self.sec=59
            self.min-=1
            if self.min==0:
                self.min=59
                self.hours-=1
                if self.hours==0:
                    self.hours=23
        else:
            self.sec-=1
    def increment_min(self):
        if self.min==59:
            self.min=0
            self.hours+=1
        else:
            self.min+=1
    def decrement_min(self):
        if self.min==0:
            self.min=59
            self.hours-=1
        else:
            self.min-=1
a=Time(18,50,18)
print(a)
a.increment_sec()
print(a)



