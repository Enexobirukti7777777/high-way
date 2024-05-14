# -*- coding: utf-8 -*-
from cs1graphics import*
highway=Canvas(1400,800, "lavender", "HIGH WAY")
rec=Rectangle(700,400, Point(80,600))
rec.setBorderWidth(0)
rec.setFillColor("forestgreen")
rec.setDepth(35)
highway.add(rec)
rec1=Rectangle(1000,400, Point(930,600))
rec1.setBorderWidth(0)
rec1.setFillColor("gray40")
rec1.setDepth(35)
highway.add(rec1)
cir1=Ellipse(10,300, Point(900,430))
cir1.setFillColor("gray")
cir1.setBorderWidth(0)
cir1.setBorderColor("blue")
cir1.setDepth(45)
highway.add(cir1)
cir2=Rectangle(800,300, Point(820,430))
cir2.setFillColor("gray")
cir2.setBorderWidth(7)
cir2.setDepth(46)
cir2.setBorderColor("gray40")
highway.add(cir2)
cir3=Rectangle(50,300, Point(470,400))
cir3.setFillColor("gray")
cir3.setDepth(40)
cir3.setBorderWidth(5)
cir3.setBorderColor("gray49")
highway.add(cir3)

cir9=Rectangle(720,80, Point(820,260))
cir9.setFillColor("gray")
cir9.setDepth(39)
cir9.setBorderWidth(3)
cir9.setBorderColor("darkgreen")
highway.add(cir9)
cir4=Rectangle(120,200, Point(810,400))
cir4.setFillColor("gray40")
cir4.setDepth(40)
cir4.setBorderWidth(5)
cir4.setBorderColor("gray49")
highway.add(cir4)
cir10=Rectangle(120,200, Point(616,405))
cir10.setFillColor("gray40")
cir10.setBorderWidth(4)
cir10.setBorderColor("gray49")
cir10.setDepth(39)
highway.add(cir10)
cir11=cir10.clone()
cir11.moveTo(1108,403)
highway.add(cir11)
cir5=cir4.clone()
cir5.moveTo(960,400)
highway.add(cir5)
cir6=cir3.clone()
cir6.moveTo(1170,400)
highway.add(cir6)
cir7=Circle(17, Point(795,280))
cir7.setDepth(35)
cir7.setFillColor("gray")
highway.add(cir7)
txt=Text("X", 18, Point(795,280))
txt.setFontColor("red")
txt.setDepth(15)
highway.add(txt)
cir8=Circle(17, Point(945,280))
cir8.setDepth(35)
cir8.setFillColor("gray")
highway.add(cir8)
txt=Text("V", 18, Point(945,280))
txt.setFontColor("forestgreen")
txt.setDepth(15)
highway.add(txt)
cir20=Circle(17, Point(1115,275))
cir20.setDepth(35)
cir20.setFillColor("gray")
highway.add(cir20)


txt=Text("V", 18, Point(1115,280))
txt.setFontColor("forestgreen")
txt.setDepth(15)
highway.add(txt)

cir30=Circle(17, Point(615,280))
cir30.setDepth(35)
cir30.setFillColor("gray")
highway.add(cir30)
txt=Text("X", 18, Point(615,280))
txt.setFontColor("red")
txt.setDepth(15)
highway.add(txt)
rec2=Polygon(Point(10,400), Point(740,400), Point(540,150), Point(10,150))
rec2.setBorderWidth(0)
rec2.setFillColor("gray40")
rec2.setBorderColor("gray40")
rec2.setDepth(48)
highway.add(rec2)
rec22=Polygon(Point(0,400), Point(440,400), Point(440,150), Point(0,150))
rec22.setFillColor("forestgreen")
rec22.setDepth(47)
highway.add(rec22)
rec3=Polygon(Point(740,400), Point(1000,400), Point(600,150), Point(540,150))
rec3.setFillColor("gray40")
rec3.setDepth(48)
highway.add(rec3)
rec4=Polygon(Point(1000,400), Point(1400,400), Point(1400,150), Point(600,150))
rec4.setFillColor("gray98")
rec4.setFillColor("gray98")
rec4.setDepth(48)
highway.add(rec4)


rec8=Polygon(Point(1010,400), Point(1050,400), Point(610,150), Point(605,150))
rec8.setFillColor("gray40")
rec8.setDepth(47)
highway.add(rec8)




rec11=Polygon(Point(650,150),Point(1100,400),Point(1250,400),Point(710,150))
rec11.setFillColor("gray40")
rec11.setDepth(47)
highway.add(rec11)

 
##
cr=Polygon(Point(1400,160),Point(1000,160),Point(1030,180),Point(1400,180))
cr.setDepth(47)
cr.setBorderWidth(2)
cr.setFillColor("gray90")
highway.add(cr)
crA=Polygon(Point(1400,180),Point(1080,180),Point(1115,205),Point(1400,205))
crA.setDepth(48)
crA.setBorderWidth(2)
crA.setFillColor("gray90")
highway.add(crA)
crB=Polygon(Point(1400,220),Point(1190,220),Point(1300,300),Point(1400,300))
crB.setDepth(46)
crB.setBorderWidth(2)
crB.setFillColor("gray90")
highway.add(crB)
cr1=Polygon(Point(1000,160),Point(1000,210),Point(1030,230),Point(1080,230),Point(1080,180),Point(1030,180))
cr1.setDepth(47)
cr1.setFillColor("lightgray")
highway.add(cr1)
cr2=Polygon(Point(1080,180),Point(1080,230),Point(1115,255),Point(1400,255),Point(1400,205),Point(1115,205))
cr2.setFillColor("lightgray")
cr2.setDepth(47)
highway.add(cr2)
cr3=Polygon(Point(1190,220),Point(1190,255),Point(1300,340),Point(1400,340),Point(1400,300),Point(1300,300))
cr3.setFillColor("lightgray")
cr3.setDepth(47)
highway.add(cr3)
cr4=Polygon(Point(1225,245),Point(1225,282),Point(1252,302),Point(1252,264))
cr4.setFillColor("powderblue")
cr4.setDepth(47)
highway.add(cr4)
p1=Path(Point(1030,230),Point(1030,180))
p1.setDepth(47)
highway.add(p1)
p2=Path(Point(1115,255),Point(1115,205))
p2.setDepth(47)
highway.add(p2)
p3=Path(Point(1300,340),Point(1300,300))
p3.setDepth(47)
highway.add(p3)
 
## Car
car=Layer()
car.setDepth(95)
fr=Polygon(Point(300,305),Point(300,275),Point(250,245),Point(130,200),Point(80,185),Point(80,215))
fr.setFillColor("gray")
car.add(fr)
fr1=Polygon(Point(300,275),Point(400,230),Point(400,260),Point(300,305))
fr1.setFillColor("gray")
car.add(fr1)
fr2=Polygon(Point(250,245),Point(300,275),Point(400,230),Point(354,199))
fr2.setFillColor("gray")
car.add(fr2)
fr3=Polygon(Point(250,245),Point(230,205),Point(333,164),Point(354,199))
fr3.setFillColor("gray")
car.add(fr3)
fr4=Polygon(Point(230,205),Point(160,180),Point(258,140),Point(333,164))
fr4.setFillColor("gray")
car.add(fr4)
fr5=Polygon(Point(130,200),Point(80,185),Point(170,145),Point(220,157))
fr5.setFillColor("gray")
fr5.setDepth(55)
car.add(fr5)
fr6=Polygon(Point(250,245),Point(230,205),Point(160,180),Point(130,200))
fr6.setFillColor("gray")
car.add(fr6)
tire1=Ellipse(42,47,Point(256,285))
tire1.setFillColor("black")
car.add(tire1)
tire2=Ellipse(40,45, Point(125,230))            
tire2.setFillColor("black")
car.add(tire2)



## Car new
carnew=Layer()
carnew.setDepth(95)
fr=Polygon(Point(300,305),Point(300,275),Point(250,245),Point(130,200),Point(80,185),Point(80,215))
fr.setFillColor("purple")
carnew.add(fr)
fr1=Polygon(Point(300,275),Point(400,230),Point(400,260),Point(300,305))
fr1.setFillColor("purple")
carnew.add(fr1)
fr2=Polygon(Point(250,245),Point(300,275),Point(400,230),Point(354,199))
fr2.setFillColor("purple")
carnew.add(fr2)
fr3=Polygon(Point(250,245),Point(230,205),Point(333,164),Point(354,199))
fr3.setFillColor("white")
carnew.add(fr3)
fr4=Polygon(Point(230,205),Point(160,180),Point(258,140),Point(333,164))
fr4.setFillColor("purple")
carnew.add(fr4)
fr5=Polygon(Point(130,200),Point(80,185),Point(170,145),Point(220,157))
fr5.setFillColor("purple")
fr5.setDepth(55)
carnew.add(fr5)
fr6=Polygon(Point(250,245),Point(230,205),Point(160,180),Point(130,200))
fr6.setFillColor("white")
carnew.add(fr6)
tire1=Ellipse(42,47,Point(256,285))
tire1.setFillColor("black")
carnew.add(tire1)
tire2=Ellipse(40,45, Point(125,230))            
tire2.setFillColor("black")
carnew.add(tire2)



## Car last
carlast=Layer()
carlast.setDepth(95)
fr=Polygon(Point(300,305),Point(300,275),Point(250,245),Point(130,200),Point(80,185),Point(80,215))
fr.setFillColor("white")
carlast.add(fr)
fr1=Polygon(Point(300,275),Point(400,230),Point(400,260),Point(300,305))
fr1.setFillColor("white")
carlast.add(fr1)
fr2=Polygon(Point(250,245),Point(300,275),Point(400,230),Point(354,199))
fr2.setFillColor("white")
carlast.add(fr2)
fr3=Polygon(Point(250,245),Point(230,205),Point(333,164),Point(354,199))
fr3.setFillColor("gray")
carlast.add(fr3)
fr4=Polygon(Point(230,205),Point(160,180),Point(258,140),Point(333,164))
fr4.setFillColor("white")
carlast.add(fr4)
fr5=Polygon(Point(130,200),Point(80,185),Point(170,145),Point(220,157))
fr5.setFillColor("white")
fr5.setDepth(55)
carlast.add(fr5)
fr6=Polygon(Point(250,245),Point(230,205),Point(160,180),Point(130,200))
fr6.setFillColor("gray")
carlast.add(fr6)
tire1=Ellipse(42,47,Point(256,285))
tire1.setFillColor("black")
carlast.add(tire1)
tire2=Ellipse(40,45, Point(125,230))            
tire2.setFillColor("black")
carlast.add(tire2)
##BUS
Bus=Layer()
r1=Polygon(Point(300,350),Point(300,270),Point(160,80),Point(160,140))
r1.setBorderWidth(2)
r1.setFillColor("darkgreen")
Bus.add(r1)
r2=Polygon(Point(300,350),Point(300,270),Point(450,270),Point(450,350))
r2.setBorderWidth(2)
r2.setFillColor("darkgreen")
Bus.add(r2)
r3=Polygon(Point(160,80),Point(270,80),Point(310,160),Point(160,140))
r3.setBorderWidth(2)
r3.setFillColor("gray")
r3.setDepth(55)
Bus.add(r3)
r4=Polygon(Point(310,160),Point(270,80),Point(450,270),Point(450,350))
r4.setBorderWidth(2)
r4.setDepth(55)
r4.setFillColor("white")
Bus.add(r4)
r5=Polygon(Point(300,270),Point(450,270),Point(270,80),Point(160,80))
r5.setBorderWidth(2)
r5.setFillColor("white")
r5.setDepth(45)
Bus.add(r5)
r6=Rectangle(150,40, Point(375,290))
r6.setFillColor("lightblue")
Bus.add(r6)
r7=Polygon(Point(300,270),Point(160,80),Point(160,110),Point(300,300))
r7.setFillColor("lightblue")
Bus.add(r7)
tr1=Ellipse(35,55,Point(260,295))
tr1.setBorderWidth(2)
tr1.setFillColor("black")
tr1.setDepth(40)
Bus.add(tr1)   
tr2=Ellipse(25,45,Point(180,170))
tr2.setBorderWidth(2)
tr2.setFillColor("black")
tr2.setDepth(40)
Bus.add(tr2)

Bus.moveTo(510,130)
Bus.scale(0.37)
Bus.setDepth(47)
highway.add(Bus)



 #minibus

miniBus=Layer()
r1=Polygon(Point(300,350),Point(300,270),Point(160,80),Point(160,140))
r1.setBorderWidth(2)
r1.setFillColor("blue")
miniBus.add(r1)
r2=Polygon(Point(300,350),Point(300,270),Point(450,270),Point(450,350))
r2.setBorderWidth(2)
r2.setFillColor("blue")
miniBus.add(r2)
r3=Polygon(Point(160,80),Point(270,80),Point(310,160),Point(160,140))
r3.setBorderWidth(2)
r3.setFillColor("blue")
r3.setDepth(55)
miniBus.add(r3)
r4=Polygon(Point(310,160),Point(270,80),Point(450,270),Point(450,350))
r4.setBorderWidth(2)
r4.setDepth(55)
r4.setFillColor("blue")
miniBus.add(r4)
r5=Polygon(Point(300,270),Point(450,270),Point(270,80),Point(160,80))
r5.setBorderWidth(2)
r5.setFillColor("blue")
r5.setDepth(45)
miniBus.add(r5)
r6=Rectangle(150,40, Point(375,290))
r6.setFillColor("blue")
miniBus.add(r6)
r7=Polygon(Point(300,270),Point(160,80),Point(160,110),Point(300,300))
r7.setFillColor("white")
miniBus.add(r7)
tr1=Ellipse(35,55,Point(260,295))
tr1.setBorderWidth(2)
tr1.setFillColor("black")
tr1.setDepth(40)
miniBus.add(tr1)   
tr2=Ellipse(25,45,Point(180,170))
tr2.setBorderWidth(2)
tr2.setFillColor("black")
tr2.setDepth(40)
miniBus.add(tr2)

miniBus.moveTo(510,130)
miniBus.scale(0.37)
miniBus.setDepth(47)

 
#car3
car3 = Layer()
tire1 = Circle(10, Point(50,210))
tire1.setFillColor('black')
car3.add(tire1)
tire1_part = Circle(4, Point(50,210))
tire1_part.setFillColor("white")
car3.add(tire1_part)
tire2 = Circle(10, Point(100,210))
tire2.setFillColor('black')
car3.add(tire2)
tire2_part = Circle(4, Point(100,210))
tire2_part.setFillColor("white")
car3.add(tire2_part)
body1 = Rectangle(85, 26, Point(76,200))
body1.setFillColor('lavender')
body1.setBorderColor("lavender")
body1.setDepth(61)
car3.add(body1)
body2 = Ellipse(65,40,Point(76,190))
body2.setFillColor('lightblue')
body2.setBorderColor("lavender")
body2.setDepth(62)
car3.add(body2)
r1=Path(Point(43.5,186),Point(108.5,186))
car3.add(r1)
r2=Path(Point(76,186),Point(76,170))
car3.add(r2)
body3 = Ellipse(30,26, Point(120,200))
body3.setFillColor("lavender")
body3.setBorderColor("lavender")
car3.add(body3)
body3.setDepth(65)
body4 = Ellipse(30,26, Point(32,200))
body4.setFillColor("red")
body4.setBorderColor("lavender")
body4.setDepth(65)
car3.add(body4)
car3.setDepth(-10)
car3.moveTo(1400,300)
car3.scale(1.8)
highway.add(car3)
 

 
##Tree
Tree=Layer()
br=Polygon(Point(200,300),Point(210,80),Point(220,300))
br.setFillColor("brown")
Tree.add(br)
lv=Polygon(Point(210,80),Point(225,120),Point(220,120),Point(240,150),Point(230,150),Point(250,180),Point(240,180),Point(260,210),Point(250,210),Point(270,240),Point(150,240),Point(170,210),Point(160,210),Point(180,180),Point(170,180),Point(190,150),Point(180,150),Point(200,120),Point(195,120),Point(210,80))
lv.setFillColor("darkgreen")                                                                                                                                                                                  
Tree.add(lv)
Tree.setDepth(30)
Tree.moveTo(10,300)
highway.add(Tree)
T1=Tree.clone()
T1.scale(0.7)
T1.moveTo(150,500)
highway.add(T1)
T2=Tree.clone()
T2.scale(0.6)
T2.setDepth(20)
T2.moveTo(-100,140)
highway.add(T2)
T3=Tree.clone()
T3.scale(0.6)
T3.setDepth(20)
T3.moveTo(150,210)
highway.add(T3)
T4=Tree.clone()
T4.scale(0.5)
T4.setDepth(20)
T4.moveTo(210,100)
highway.add(T4)
T5=Tree.clone()
T5.scale(0.4)
T5.setDepth(20)
T5.moveTo(110,50)
highway.add(T5)
T5=Tree.clone()
T5.scale(0.4)
T5.setDepth(20)
T5.moveTo(-50,40)
highway.add(T5)
T5=Tree.clone()
T5.scale(0.4)
T5.setDepth(20)
T5.moveTo(10,100)
highway.add(T5)
 
##Tree2
Tr=Layer()
zaf=Polygon(Point(125,160),Point(170,260),Point(80,260))
zaf.setFillColor("darkgreen")
Tr.add(zaf)
rec1=Rectangle(15,50,Point(125,285))
rec1.setFillColor("brown")
Tr.add(rec1)
Tr.scale(0.6)
Tr.setDepth(35)
highway.add(Tr)
Tr1=Tr.clone()
Tr1.moveTo(100,200)
highway.add(Tr1)
Tr2=Tr.clone()
Tr2.moveTo(150,110)
highway.add(Tr2)
Tr3=Tr.clone()
Tr3.moveTo(250,50)
highway.add(Tr3)
 
##Cloud
cloud = Layer()
body2 = Ellipse(75,60,Point(506,50))
body2.setFillColor('white')
body2.setBorderColor("white")
body2.setDepth(62)
cloud.add(body2)
body3 = Ellipse(50,40, Point(550,50))
body3.setFillColor("white")
body3.setBorderColor("white")
cloud.add(body3)
body3.setDepth(60)
body4 = Ellipse(70,40, Point(455,48))
body4.setFillColor("white")
body4.setBorderColor("white")
body4.setDepth(60)
cloud.add(body4)
cloud.scale(0.5)
cloud.setDepth(35)
cloud.moveTo(400,0)
highway.add(cloud)
Cl=cloud.clone()
Cl.moveTo(250,10)
highway.add(Cl)
Cl1=cloud.clone()
Cl1.moveTo(950,0)
Cl1.scale(1.2)
highway.add(Cl1)
Cl2=cloud.clone()
Cl2.moveTo(550,10)
Cl2.scale(0.8)
highway.add(Cl2)
Cl3=cloud.clone()
Cl3.moveTo(650,-20)
Cl3.scale(1.5)
highway.add(Cl3)




#car3

 
##Sun
sun=Circle(24,Point(300,24))
sun.setFillColor("yellow")
sun.setBorderColor("yellow")
sun.setBorderWidth(6)
highway.add(sun)
 
##Mountain
m=Spline(Point(0,40),Point(100,40),Point(200,0),Point(280,70),Point(1150,75),Point(1350,-5),Point(1550,170))
m.setBorderWidth(2)
m.setBorderColor("transparent")

m.setDepth(70)
highway.add(m)
 
##Zebra
Zebra=Layer()
z1=Rectangle(100,30,Point(500,700))
z1.setDepth(15)
Zebra.add(z1)
highway.add(Zebra)
 
             
txt=Text("TULU DIMTU MAIN TOLL GATE", 8, Point(880,255))
txt.setFontColor("darkblue")
txt.setDepth(15)
highway.add(txt)
txt=Text("ቱሉ ዲምቱ ዋና የከፍያ ጣቢያ", 18, Point(880,238))
txt.setFontColor("darkblue")
txt.setDepth(15)
highway.add(txt)

for i in range(218):
    miniBus.move(1,2.1)
    miniBus.scale(1.001)
Bus1=miniBus.clone()
Bus1.moveTo(
            500,314)
Bus1.scale(1.1)
Bus1.setDepth(30)
highway.add(Bus1)




   
car1=car.clone()
car1.moveTo(1340,500)
car1.scale(0.5)
car1.setDepth(30)
car1.rotate(10)
highway.add(car1)





for i in range(230):
    car1.move(-1.32,-1)
    car1.scale(0.999)
    Bus1.move(1,1.2)
   
 
highway.remove(car1)
for i in range(190):
    Bus1.move(6.1,3.1)
 
 
car2=car1.clone()
car2.moveTo(780,180)
car2.scale(0.7)
highway.add(car2)

for i in range(140):
    car2.move(-0.7,-0.5)
    car2.scale(0.999)
    
highway.remove(car2)


















for i in range(218):
    Bus.move(1,2.1)
    Bus.scale(1.001)
Bus1=Bus.clone()
Bus1.moveTo(
            700,314)
Bus1.scale(1.1)
Bus1.setDepth(30)
highway.add(Bus1)




   
car5=carnew.clone()
car5.moveTo(1200,500)
car5.scale(0.5)
car5.setDepth(30)
car5.rotate(10)
highway.add(car5)





for i in range(230):
    car5.move(-1.32,-1)
    car5.scale(0.999)
    Bus1.move(1,1.2)
   
 
highway.remove(car5)


for i in range(190):
    Bus1.move(6.1,3.1)
 
 
car6=car5.clone()
car6.moveTo(675,170)
car6.scale(0.7)
highway.add(car6)

for i in range(140):
    car6.move(-0.7,-0.5)
    car6.scale(0.999)
    
highway.remove(car6)



















#lastcar move

for i in range(218):
      carlast.move(1,2.1)
      carlast.scale(1.001)

car7=carlast.clone()
car7.moveTo(1200,500)
car7.scale(0.4)
car7.setDepth(30)
car7.rotate(10)
highway.add(car7)



for i in range(230):
    car7.move(-1.32,-1)
    car7.scale(0.999) 
highway.remove(car7)

for i in range(190):  
    car7=car7.clone()
car7.moveTo(675,170)
car7.scale(0.7)
highway.add(car7)
for i in range(140):
    car7.move(-0.7,-0.5)
    car7.scale(0.999)
    
highway.remove(car7)





















