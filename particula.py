from .algoritmos import distancia_euclidiana
#.algoritmos para que la carpeta principal la tome
class Particula():
    def __init__(self,id=0,origen_x=0,origen_y=0,destino_x=0,destino_y=0,velocidad=0,red=0,green=0,blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x,origen_y,destino_x,destino_y)
    
    @property
    def id(self):
        return self.__id
    
    @property
    def origen_x(self):
        return self.__origen_x
    
    @property
    def origen_y(self):
        return self.__origen_y
    
    @property
    def destino_x(self):
        return self.__destino_x
    
    @property
    def destino_y(self):
        return self.__destino_y
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def red(self):
        return self.__red
    
    @property
    def blue(self):
        return self.__blue
    
    @property
    def green(self):
        return self.__green
    
    @property
    def distancia(self):
        return self.__distancia
    
    def __str__(self) -> str:
        return(
            "id: \t"+ str(self.__id)+'\n'+
            "origen_x: \t"+ str(self.__origen_x)+'\n'+
            "origen_y: \t"+ str(self.__origen_y)+'\n'+
            "destino_x: \t"+ str(self.__destino_x)+'\n'+
            "destino_y: \t"+ str(self.__destino_y)+'\n'+
            "velocidad: \t"+ str(self.__velocidad)+'\n'+
            "red: \t"+ str(self.__red)+'\n'+
            "green: \t"+ str(self.__green)+'\n'+
            "blue: \t"+ str(self.__blue)+'\n'+
            "distancia: \t"+ str(self.__distancia)+'\n')
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
    
    def __lt__(self,other):
        return self.id < other.id