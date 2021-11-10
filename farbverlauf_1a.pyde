def setup():
    size(600, 600)    

def draw():
    b = (mouseY / 3)
    g = 140
    r = 50
    if mouseY<50:
        r = 250
        g = 50
    elif mouseY<100:
       r = 230 
       g = 75   
    elif mouseY<200:
       r = 210
       g = 80
    elif mouseY<300:
       r = 200
       g = 140       
    elif mouseY<400:
       r = 180
       g = 130
       
    elif mouseY<450:
       r = 140 
       g = 140      
    elif mouseY>500:
       r = 50 
       g = 140


    
    print(b)
    print (g)
    print (r)

    background(r, g, b)
    
  
