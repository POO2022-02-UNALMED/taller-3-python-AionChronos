class Control:
    
    def __init__ (self):
        self.tele = None

    def getTv (self):
        return self.tele

    def setTv (self, tv):
        self.tele = tv

    def enlazar (self, tv):
        self.setTv(tv)
        self.tele.setControl(self)

    def turnOff (self):
        self.tele.turnOff()
    
    def turnOn (self):
        self.tele.turnOn()
    
    def volumenUp (self):
        self.tele.volumenUp()

    def volumenDown(self):
        self.tele.volumenDown()
    
    def canalUp (self):
        self.tele.canalUp()
        
    def canalDown (self):
        self.tele.canalDown()

    def getCanal (self):
        return self.tele.getCanal()
    
    def setCanal (self,cambio):
        self.tele.setCanal(cambio)