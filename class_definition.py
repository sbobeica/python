'''' Demonstrate class definitions '''
class Base_Model(): #by convention a class name strats with capital leter
    '''' Represents the base model of a car '''
    trim = 'normal'         #data atributs that belong to the class and instances of the class
    engine_liters = 1.5     #data atributs that belong to the class and instances of the class

    def engine_sound(self):     #methods, are like normal functions exept that they require an implicit parameter 'self'
        return 'putt, putt'

    def horn_sound(self):       #Methods, are like normal functions exept that they require an implicit parameter 'self'
        return 'beep, beep'

    def __str__(self):          #A special method that should be defined when declaring a class. It is a "special string method" or "__str__".
        return 'Base Model'     #