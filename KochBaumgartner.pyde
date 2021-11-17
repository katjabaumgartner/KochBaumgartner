
def setup():
    size(600, 600) 
    textSize(15)



def draw():
#Farbveränderung durch Mouse   
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
    
    background(r,g,b)
    
#sich wiederholende draw Funktion Achse mit Text
    text("Luftfeuchtigkeit %", 460, 595)
    text("Temperatur Grad C", 2, 20)
    fill(0,0,0)
    line(40, 560, 560, 560)
    line(40, 560, 40, 40)
    text("30", 20, 60)
    text("15", 20, 270)
    text("0", 20, 560)
    text("0", 40, 580)
    text("50", 270, 580)
    text("100", 540, 580)
   
#Bilder laden
    bilder = []
    for i in range(0, 16):
        bilder.append(loadImage("bild"+str(i + 1) +".png"))
        
    if mouseY>450 and mouseX>450: image(bilder[15], 240, 180)
    elif mouseY>450 and 300<mouseX<450: image(bilder[14], 240, 180)
    elif mouseY>450 and 150<mouseX<300: image(bilder[13], 240, 180)
    elif mouseY>450 and mouseX<150: image(bilder[12], 240, 180) 
    elif mouseY>100 and mouseX>450: image(bilder[0], 240, 180)
    elif mouseY>100 and 300<mouseX<450: image(bilder[1], 240, 180)
    elif mouseY<100 and 150<mouseX<300: image(bilder[2], 240, 180)
    elif mouseY<100 and mouseX<150: image(bilder[3], 240, 180)
