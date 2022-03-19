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

dom = input("What is the dominant trait's LETTER: ")
rec = input("What is the reccesive trait's LETTER: ")


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

dom_phe = 0
rec_phe = 0


if genotype_1[0] == dom or genotype_1[1] == dom:
    dom_phe += 1
elif genotype_1[0] == rec and genotype_1[1] == rec:
    rec_phe += 1


if genotype_2[0] == dom or genotype_2[1] == dom:
    dom_phe += 1
elif genotype_2[0] == rec and genotype_2[1] == rec:
    rec_phe += 1


if genotype_3[0] == dom or genotype_3[1] == dom:
    dom_phe += 1
elif genotype_3[0] == rec and genotype_3[1] == rec:
    rec_phe += 1


if genotype_3[0] == dom or genotype_3[1] == dom:
    dom_phe += 1
elif genotype_3[0] == rec and genotype_3[1] == rec:
    rec_phe += 1

print("The dominant trait will be manifested "+str(dom_phe)+" out of 4 times")
print("The recessive trait will be manifested "+str(rec_phe)+" out of 4 times")
