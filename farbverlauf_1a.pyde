def setup():
    size(600, 600)    

def draw():
    b = (mouseY / 3)
    g = 255
    r = 51
    if mouseY<50:
        r = 250
        g = 50
    elif mouseY<100:
       r = 230 
       g = 75   
    elif mouseY<200:
       r = 210
       g = 120
    elif mouseY<300:
       r = 200
       g = 130       
    elif mouseY<400:
       r = 150
       g = 150
       
    elif mouseY<450:
       r = 80 
       g = 160 
    elif mouseY<500:
       r = 70 
       g = 180     
    elif mouseY>500:
       r = 51 
       g = 200


    
    print(b)
    print (g)
    print (r)

    background(r, g, b)
