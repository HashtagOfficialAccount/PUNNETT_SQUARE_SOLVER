import turtle
t = turtle.Turtle()

t.speed(8)
t.bk(200)
t.lt(90)
t.fd(200)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(400)
t.bk(200)
t.left(90)
t.fd(200)
t.bk(400)

mom_1 = input("What is the mom's FIRST allele?: ")
mom_2 = input("What is the mom's SECOND allele?: ")

dad_1 = input("What is the dad's FIRST allele?: ")
dad_2 = input("What is the dad's SECOND allele?: ")

t.penup()
t.goto(-250,100)
t.write(mom_1,font = ("Calibri",40,"bold"))
t.goto(-250,-100)
t.write(mom_2,font = ("Calibri",40,"bold"))

t.goto(-100,250)
t.write(dad_1,font = ("Calibri",40,"bold"))
t.goto(100,250)
t.write(dad_2,font = ("Calibri",40,"bold"))

genotype_1 = mom_1 + dad_1
genotype_2 = mom_1 + dad_2
genotype_3 = mom_2 + dad_1
genotype_4 = mom_2 + dad_2

t.goto(-100,100)
t.write(genotype_1,font = ("Calibri",40,"bold"))
t.goto(-100,-100)
t.write(genotype_2,font = ("Calibri",40,"bold"))

t.goto(100,100)
t.write(genotype_3,font = ("Calibri",40,"bold"))
t.goto(100,-100)
t.write(genotype_4,font = ("Calibri",40,"bold"))

    
