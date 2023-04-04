import math 


#Lists
marbles = [4,6,2,9]

#Lists
marbles = [4,6,2,9]
print(marbles[2])

for i in range(len(marbles)):
    marbles[i] *= 5

print(marbles)

class fruit():
      def __init__(self,weight,type): #constructor 
         self.type =  type
         self.weight = weight;
         self.isFresh = True;
      
      def printInfo(self):
          print(self.type)
          print(self.weight)
          print(self.isFresh)
      
      def turnRotten(self):
          if self.isFresh == False:
              print("Turned rotten")

  
#------------------------------------------------------------------------------------------------------------------
f1 = fruit("apple",100)#constructor
f2 = fruit("Blueberry",200)
f1.printInfo()
f2.printInfo()
