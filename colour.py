import random
import numpy
hpoints = 50
status = ("000","SANGUINE", "CHOLERIC", "MELANCHOLIC", "PHLEGMATIC","UNWELL")

def colourtxt(x,z): # x = text z= colour 1.re 2.yel 3.blk 4. wjot 5.blu
    if z == 1: #red
        y = "\033[31m\033[1m"+ x + "\033[0m"
        print(y)
    elif z == 2: #yel
        y = "\033[33m\033[1m"+ x + "\033[0m"
        print(y) #blk
    elif z ==3:
        y = "\033[30m\033[1m"+ x + "\033[0m"
        print(y)    
    elif z == 4: #wht
        y = "\033[1m"+ x + "\033[0m"
        print(y)
    elif z == 5: #blu
        y = "\033[34m\033[1m"+ x + "\033[0m"
        print(y)
    else:
        print(x)    
        
    
def colourhtxt(x,z): # x = text z= colour 1.re 2.yel 3.blk 4. wjot 5. blu
    if z == 1: #red
        y = "\033[41m\033[1m"+ x + "\033[0m"
        print(y)
    elif z == 2: #yel
        y = "\033[43m\033[1m\033[30m"+ x + "\033[0m"
        print(y)   
    elif z ==3:
        y = "\033[40m\033[1m"+ x + "\033[0m"
        print(y)     
    elif z == 4: #wht
        y = "\033[7m\033[1m"+ x + "\033[0m"
        print(y)   
    elif z == 5: #blu
        y = "\033[44m\033[1m"+ x + "\033[0m"
        print(y)
    else:
        print(x)    




class Enemy:
    def __init__(self,name,hp,red,yel,blk,wht,sag,cho,mel,phl,unw,phr1,phr2,phr3,phr4,phr5):
        self.name = name
        self.hp = hp
        self.red = red
        self.yel = yel
        self.blk = blk
        self.wht = wht
        self.sag = sag
        self.cho = cho
        self.mel = mel
        self.phl = phl
        self.unw = unw
        self.phr1 = phr1
        self.phr2 = phr2
        self.phr3 = phr3
        self.phr4 = phr4
        self.phr5 = phr5

    def humours(self):
        humours = [self.red,self.yel,self.blk,self.wht]
        sumof = sum(humours)
        limit = (sumof/4)*1.5
        flaghum = []
        flaghum.clear()
        #print("limit is " +  str(limit))
        for i in humours:
            if i > limit:
                q = humours.index(i)
                flaghum.append(i)
            else:
                pass
        if len(flaghum) == 1:
            l = humours.index(flaghum[0])
            l =  l+1
            return l
        elif len(flaghum) == 0:
            #print("all balanced")
            return 0
        else:
            l =  max(flaghum)
            flaghum.reverse()
            w = max(flaghum)
            if w == l:
                return 5
            else:
                l =  l+1
                return l
        

    def humstat(self,x):
        if x !=0:
            text = self.name + " is " + status[x] + "!"
            colourhtxt(text,x)
            if x == 1:
                self.sag = True
            elif x == 2:
                self.cho = True
            elif x == 3:
                self.mel = True
            elif x == 4:
                self.mel = True
            elif x == 5:
                self.unw = True
        else:
            pass
    
    def showhum(self):
        humours = [self.red,self.yel,self.blk,self.wht]
        x = 0
        r = 1 
        humournam = ["blood","yellow bile","black bile","phlegm"]
        print("----------------")
        print("Humours are as follows:")
        for i in humours:
            v = humournam[x]
            colourtxt(v + ": " + str(i),r)
            x= x+1
            r= r+1
    
    def hresponse(self,x):
        list = [self.phr1,self.phr2,self.phr3,self.phr4,self.phr5]
        no = turnnumber % 5
        p = list[no]
        if x == 1:
            a = p[x]
            colourtxt(a,x)
        elif x == 2:
            a = p[x]
            colourtxt(a,x)
        elif x == 3:
            a = p[x]
            colourtxt(a,x)
        elif x ==4:
            a =p[x]
            colourtxt(a,x)
        elif x == 5:
            a = p[x]
            colourtxt(a,x)
        else:
            pass

    def jumbly(self):
        randy = []
        for i in range(4):
            p =  random.randint(0,9)
            i = p
            randy.append(p)
        print(randy)
        self.red = randy[0]
        self.yel = randy[1]
        self.blk = randy[2]
        self.wht = randy[3]

    def showhp(self):
        health = []
        brix = int(self.hp/5) + (self.hp % 5 > 0)
        jumbo = round(brix)
        for j in range(jumbo):
            q = "—"
            health.append(q)
        j = "".join(health)
        print(f"{self.name}'s Health: " + str(self.hp))
        print(j)
            

class Attack:
    def __init__(self,name,dam):
        self.name = name
        self.dam = dam 


class Spell:
    def __init__(self,name,htype,amt,dam):
        self.name = name
        self.htype = htype #will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of damage -ve or +ve
        self.dam = dam #hp gotten rid of 

    def cast(self, e): # e= enemy
        colourtxt(" * "+ self.name + " was cast on " + e.name + "!", self.htype)
        e.hp =  e.hp - self.dam
        if self.htype == 1:
            e.red = e.red + self.amt
        elif self.htype == 2:
            e.yel = e.yel + self.amt
        elif self.htype == 3:
            e.blk = e.blk + self.amt
        elif self.htype == 4:
            e.wht = e.wht + self.amt

#h type 1= red 2= yel 3= blk 4=wht
bld1 = Spell("BLOODLET Σ",1,-2,4)
bld2 = Spell("STIMULATE MARROW σ",1,3,-4)
ylb1 = Spell("EXPEL YELLOW BILE Ξ",2,-3,3)
ylb2 = Spell("INVIGORATE LIVER ξ",2,3,-1)
blk1 = Spell("PURGE BLACK BILE Δ",3,-4,3)
blk2 = Spell("ROUSE KIDNEYS δ",3,3,-2)
wht1 = Spell("EJECT PHLEGM Θ",4,-4,2)
wht2 = Spell("INCREASE PHLEGM θ",4,6,0)
clob = Spell("CLOBBER",1,-1,8)

def showpoints():
    global hpoints
    healthpoints = []
    brix = int(hpoints/5) + (hpoints % 5 > 0)
    jumbo = round(brix)
    for j in range(jumbo):
        q = "—"
        healthpoints.append(q)
    p = "".join(healthpoints)
    print("Your Health: " + str(hpoints))
    print(p)


def turn():
    showpoints()
    ene.showhp()
    #ene.showhum()
    r = ene.humours()
    ene.humstat(r)
    ene.hresponse(r)
    global turnnumber
    turnnumber = turnnumber + 1

def isalive(x):
    if hpoints <= 0:
        print("You have died...")
        return False
    elif x.hp <= 0:
        print(x.name + " has been defeated!")
        return False
    else:
        return True
    


        
### Status effect counter. rng between 5,8 if the status stays for that long they lose health. probs 1/4 of total. 
### ofc attack modifiers, status effects. 1 is gonna regen health, 2, hits hard. 3 sad amd 4 forgetful. 
### spell repeat banner. the same spell can't be repeated when chosen thems the rules. like that one pokemon move.#
            
ene = Enemy("TEST ENEMY",20,5,5,5,5,False,False,False,False,False,("00","\"Ha... Ha ha ha!\"", "\"I'm fucking fuming!!\"", "\"What's the point in anything...?\"", "\"...Huh? What's going on?\"", "\"Christ, I feel really off.\""),
            ("00","She laughs hysterically...","She's bright red with anger!","She looks very sad.","She seems very confused.","She looks very under the weather."),
            ("00","\"Ahahaha! This is so fun!\"","\"I've had it up to here with you mate!\"","\"I'm having some really scary thoughts...\"","\"Where am I?\"","\"I think I need a lie down.\""),
            ("00","She clutches her stomach in laughter.","She's fuming!","She has a forlorn look to her.","She seem very lost in thought.","My humours must be all off-kilter."),
            ("00","\"Hahahaha... I can't stop laughing!\"","\"Right! You're getting a fucking pasting!\"","\"I think I'm having a depressive episode, you know.\"","\"I'm really confused! Who am I? What am I doing here?\"","\"I feel rotten. I need a big glass of water and a paracetamol.\"")
            )

fighting = True
turnnumber = 1

while fighting == True:
    turn()
    blk2.cast(ene)
    fighting = isalive(ene)
    turn()
    wht1.cast(ene)
    fighting = isalive(ene)
    turn()
    blk1.cast(ene)
    fighting = isalive(ene)
    turn()
    bld2.cast(ene)
    fighting = isalive(ene)
    turn()
    ylb2.cast(ene)
    fighting = isalive(ene)
    turn()
    bld1.cast(ene)
    fighting = isalive(ene)
    turn()
    clob.cast(ene)
    fighting = isalive(ene)
    
