class Control:
    def __init__ (self):
        self.tev = None

    def getTv (self):
        return self.tev

    def setTv (self, tv):
        self.tev = tv

    def enlazar (self, tv):
        self.setTv(tv)
        self.tev.setControl(self)

    def turnOff (self):
        self.tev.turnOff()
    
    def turnOn (self):
        self.tev.turnOn()
    
    def volumenUp (self):
        self.tev.volumenUp()

    def volumenDown(self):
        self.tev.volumenDown()
    
    def canalUp (self):
        self.tev.canalUp()
        
    def canalDown (self):
        self.tev.canalDown()

    def getCanal (self):
        return self.tev.getCanal()
    
    def setCanal (self,cambio): 
        self.tele.setCanal(cambio)
