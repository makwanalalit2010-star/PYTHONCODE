class car:
    _company = None
    _model = None
    _color = None
    _year = None


def setdata (self, cm,ml,cl,yr):
   self._company = cm
   self._model = ml
   self._color = cl
   self._year = yr

   def getdata(self):
       print(f"this is company name{self._company} and model{self._model} and color{self._color} and year{self._year}")

       car1 = car()
       car1 .setdata("tata","nano","peela",2008)

       car2 = car()
       car2. setdata("bmw","m4","blue",2023)   

       car1.getdata()
       car2.getdata()