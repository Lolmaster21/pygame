import math 


#Lists
marbles = [4,6,2,9]

print(marbles)
print(marbles[2])
print(marbles[0]*5)
print(marbles[1]*5)
print(marbles[2]*5)
print(marbles[3]*5)

marbles.append(marbles[0]*5)
marbles.append(marbles[1]*5)
marbles.append(marbles[2]*5)
marbles.append(marbles[3]*5)
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
