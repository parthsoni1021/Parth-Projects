class Animal:
    def __init__(self):
        self.no_of_eyes = 2
        self.drink = True    
    
    def breathe(self):
        print('Inhale, exhale')

        
        
class Fish(Animal):
    def __init__(self):
        super().__init__()    #super() refers to Animal class
# This call to super method is recommended, but now strictly required 
        self.drink = False         # Modified the attribute of parent class
    
    def swim(self):
        print('moving in water')
    
    def breathe(self):
        super().breathe()     # inputs everything from breathe method of super class
        print('doing underwater!')
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.drink)


# Concept of slicing
piano_keys = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
piano_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti')
print(piano_keys[::2])
print(piano_keys[2:5])  #index 5 not included
print(piano_keys[::-1])
print(piano_tuple[2:5])
