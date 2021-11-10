def setup():
    size(600, 600)  
    #Achsen inklusive Beschriftung
    line(40, 560, 560, 560)
    line(40, 560, 40, 40)
    xPos = 480
    yPos = 580
    textSize(15)
    fill(0,0,0)
    text("Luftfeuchtigkeit", xPos, yPos)
    xPos = 2
    yPos = 20
    textSize (15)
    fill(0,0,0)
    text("Temperatur", xPos, yPos)
      

def draw():
    b = (mouseY / 3)


    
    print(b)

    background(0, 140, b)
