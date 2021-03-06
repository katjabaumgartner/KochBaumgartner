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
    print(g)
    print(r)
    
    background(r,g,b)
    
#Titel
    font = createFont("Comic Sans MS", 30)
    textFont(font)
    text("Behaglichkeitsdiagramm", 150, 40)
    
#parametrisierung (x,y veränderbar)    
    x= 40
    y= 560
    
#sich wiederholende draw Funktion Achse mit Text 
    font = createFont("Century Gotic",15)
    textFont(font)
    text("Luftfeuchtigkeit %", x+420, y+35)
    text("Grad Celsius", x-38, y-540)
    fill(0,0,0)
    line(x, y, x+520, y)
    line(x, y, x, y-520)
    text("30", x-30, y-500)
    text("20", x-30, y-375)
    text("10", x-30, y-250)
    text("0", x-30, y-125)
    text("-10", x-30, y)
    text("0", x, y+20)
    text("22.5", x+125, y+20)
    text("45", x+250, y+20)
    text("67.5", x+375, y+20)
    text("90", x+500, y+20)
   
#Bilder laden
    bilder = []
    for i in range(0, 16):
        bilder.append(loadImage("bild"+str(i + 1) +".png"))
        
    if y>mouseY>y-125 and mouseX>x+410: image(bilder[15], x+180, y-380)
    elif y>mouseY>y-125 and x+250<mouseX<x+375: image(bilder[14], x+180, y-380)
    elif y>mouseY>y-125 and x+125<mouseX<x+250: image(bilder[13], x+180, y-380)
    elif y>mouseY>y-125 and x<mouseX<x+125: image(bilder[12], x+180, y-380) 
    elif y-125>mouseY>y-250 and mouseX>x+375: image(bilder[11], x+180, y-380)
    elif y-125>mouseY>y-250 and x+250<mouseX<x+375: image(bilder[10], x+180, y-380)
    elif y-125>mouseY>y-250 and x+125<mouseX<x+250: image(bilder[9], x+180, y-380)
    elif y-125>mouseY>y-250 and x<mouseX<x+125: image(bilder[8], x+180, y-380) 
    elif y-250>mouseY>y-375 and mouseX>x+375: image(bilder[7], x+180, y-380)
    elif y-250>mouseY>y-375 and x+250<mouseX<x+375: image(bilder[6], x+180, y-380)
    elif y-250>mouseY>y-375 and x+125<mouseX<x+250: image(bilder[5], x+180, y-380)
    elif y-250>mouseY>y-375 and x<mouseX<x+125: image(bilder[4], x+180, y-380) 
    elif mouseY<y-375 and mouseX>x+375: image(bilder[3], x+180, y-380)
    elif mouseY<y-375 and x+250<mouseX<x+375: image(bilder[2], x+180, y-380)
    elif mouseY<y-375 and x+125<mouseX<x+250: image(bilder[1], x+180, y-380)
    elif mouseY<y-375 and x<mouseX<x+125: image(bilder[0], x+180, y-380)
