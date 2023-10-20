
#Session 4 (3Part, animal, initialization & print w/member function.)

class Chimera:
    def __init__(self,arm,legs,eyeC,tail,fuzzy):
        self.favAnimal= {
            "Arm Length: ": arm, #6.5
            "Leg Length: ": legs, #6.5 #It's on all fours. would be funny lopsided tho.
            "Number of Eyes: ": eyeC, #6 , 3 heads
            "Does it have a Tail?: ": tail,#True
            "Is it Furry?: ": fuzzy, # True Lion's fur
        }

    def describe(self):
        print("The physical characters of this animal, which happens to be my favorite, are:")
        for animalPart,value in self.favAnimal.items(): #dictionary lets us scan each item pair! 
            print(f"{animalPart}: {value}")
            
            
my_Favorite_Animal = Chimera(6.5,6.5,6,True,True) #indentation matters.
my_Favorite_Animal.describe()             #Must be outside class to operate
