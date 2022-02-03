import pyjokes


def VolumeCalc(Shape):
    
    choice = 'a'
    volume = 0
    radius = 0
    height = 0
    edge = 0
       
    if Shape == 'c':
        
        
        
        print("Wat dat Radius Cuhh?")
        radius = int(input())
        
        print("какой размер вашей башни lx effle??")
        height = int(input())
        
        volume =  3.141592653589793* radius* radius* height/3
        
        print(volume)
    
    elif Shape == 's':
    
        
        print("Wat dat Radius Cuhh?")
        radius = int(input())
        
        volume = 4/3* 3.141592653589793* radius* radius* radius
        
        print(volume)
    
    elif Shape == 'b':
        
        print("Wat dat cube gonna be Cuhh?")
        edge = int(input())
        
        volume = edge* edge* edge
        
        print(volume)
    
    else:
        print ("WAt?")
        
print(pyjokes.get_joke(language = "en", category = "all"))
print("Yo Cuhhh Waht you tynah fill wit wauhter?")
print()
print("(c)one, (s)phere, cu(b)e")

choice = input()

VolumeCalc(choice)
