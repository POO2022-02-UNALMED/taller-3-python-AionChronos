class TV:

    numTV = 0

    def __init__ (self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        TV.numTV += 1

    def setMarca (self,marca):
        self.marca = marca
    
    def getMarca (self):
        return self.marca

    def setControl (self,control):
        self.control = control
    
    def getControl (self):
        return self.control
    
    def setVolumen (self,volumen):
        if self.getEstado():
            self.volumen = volumen
    
    def getVolumen (self):
        return self.volumen
    
    def setPrecio (self,precio):
        self.precio = precio
    
    def getPrecio (self):
        return self.precio

    def setCanal (self, canal):
        if self.getEstado():
            if (canal>=1 and canal<=120):
                self.canal = canal
    
    def getCanal (self):
        return self.canal


    def turnOn (self):
        if self.estado == False:
            self.estado = True

    def turnOff (self):
        if self.estado == True:
            self.estado = False

    def getEstado (self):
        return self.estado
    
    def volumenUp (self):
        if (self.getEstado() == True and self.getVolumen() < 7):
            self.volumen += 1

    def volumenDown (self):
        if (self.getEstado() == True and self.getVolumen() > 0):
            self.volumen -= 1

    def canalUp (self):
        if (self.getEstado() == True):
            if (self.getCanal() < 120):
                self.canal += 1
            
    def canalDown (self): 
        if (self.getEstado() ): 
            if (self.getCanal() > 1):
                self.canal -= 1
    def setNumTV (num):
        TV.numTV =  num
    
    def getNumTV ():
        return TV.numTV