import random
status = ("000","SANGUINE", "CHOLERIC", "MELANCHOLIC", "PHLEGMATIC","UNWELL")
checkerlim = 10

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

def compare(x_list,y_list):
    if True in y_list:
        y_list = [False,False,False,False]
    print("** hums" +  str(x_list))
    print("prevhums" + str(y_list))
    
    x = any(i != j for i, j in zip(x_list, y_list))
    if x == True:
        if True in x_list:
            return True
    else:
        return False


class Enemy:
    def __init__(self,name,hp,red,yel,blk,wht,sag,cho,mel,phl,unw,phr1,phr2,phr3,phr4,phr5,dflag,checker):
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
        self.dflag = dflag #deathflag
        self.checker = checker

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
        prevhums = [self.sag,self.mel,self.cho,self.phl] # i reckon a counter would be necessary at this point! list? raw counter? how do i make it recognise a current status? at the start?
        if x !=0:
            text = self.name + " is " + status[x] + "!"
            colourhtxt(text,x)
            if x == 1:
                self.sag = True
                self.mel = False
                self.cho = False
                self.phl = False
                self.unw = False
            elif x == 2:
                self.sag = False
                self.mel = False
                self.cho = True
                self.phl = False
                self.unw = False
            elif x == 3:
                self.sag = False
                self.mel = True
                self.cho = False
                self.phl = False
                self.unw = False
            elif x == 4:
                self.sag = False
                self.mel = False
                self.cho = False
                self.phl = True
                self.unw = False
            elif x == 5:
                self.sag = False
                self.mel = False
                self.cho = False
                self.phl = False
                self.unw = True
            else:
                print("somethings gone deeply wrong </3")
                pass
        hums = [self.sag,self.mel,self.cho,self.phl] # doesn't include unwellness as that's not going to kword someone.
        adding = compare(hums,prevhums)
        if adding == True:
            print("found. adding 1 to " + self.name)
            self.checker =  self.checker + 1
            print("checker: " + str(self.checker))
        else:
            print("nothing amiss with %s ..." % (self.name))
            self.checker = 0


    
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
    def __init__(self,name,htype, amt, dam,acc):
        self.name = name
        self.htype = htype #will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of damage -ve or +ve
        self.dam = dam #damage 
        self.acc = acc #accuracy, rated 0-100 like pokemon
    def attack(self,e): #### I RECKON add status effects at this space. 
        mult = 1
        accu = 1
        if e.mel == True:
            colourtxt("%s cannot attack..." % (e.name), 3)
            return
        if e.phl == True:
            accu = 0.5
        if e.sag == True:
            mult =  0.5
        if e.cho == True:
            mult = 2
        colourtxt("      %s used %s ! * " % (e.name,self.name), self.htype)
        a = random.randint(0,100)
        hitrate =  accu*self.acc
        if a < hitrate:
            you.hp = you.hp - self.dam * mult
            if self.htype == 1:
                you.red = you.red + self.amt
            elif self.htype == 2:
                you.yel = you.yel + self.amt
            elif self.htype == 3:
                you.blk = you.blk + self.amt
            elif self.htype == 4:
                you.wht = you.wht + self.amt
        else:
            print("       ...It missed!")        


class Spell:
    def __init__(self,name,htype,amt,dam):
        self.name = name
        self.htype = htype #will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of damage -ve or +ve
        self.dam = dam #hp gotten rid of 

    def cast(self, e): # e= enemy
        mult = 1
        if you.mel == True:
            colourtxt("Harrowed by sadness, you cannot bring yourself to attack.",3)
            return
        if you.phl == True:
            colourtxt("    * You forgot how to cast spells...",4)
            colourtxt("    * You hit " + e.name + " with your staff instead!", 4)
            e.hp =  e.hp - 4*mult
            return
        if you.sag == True:
            mult =  0.5
        if you.cho == True:
            mult = 2
        colourtxt("    * "+ self.name + " was cast on " + e.name + "!", self.htype)
        e.hp =  e.hp - self.dam*mult
        if self.htype == 1:
            e.red = e.red + self.amt
        elif self.htype == 2:
            e.yel = e.yel + self.amt
        elif self.htype == 3:
            e.blk = e.blk + self.amt
        elif self.htype == 4:
            e.wht = e.wht + self.amt

def checkhealth(x):
    if x.hp <= 0 or x.checker >= checkerlim or you.hp <= 0 or you.checker >= checkerlim:
        return False
    else:
        return True
    
def deathcheck(x):
    if x.hp <= 0:
        print("%s was defeated in battle!" % (x.name))
    elif you.hp <=0: 
        print("You were defeated in battle...")
    elif x.checker>you.checker:
        print("%s was defeated through the manupulation of humours!" % (x.name))
    else:
        print("You died from an imbalance of humours...")


#h type 1= red 2= yel 3= blk 4=wht
bld1 = Spell("BLOODLET Σ",1,-2,4)
bld2 = Spell("STIMULATE MARROW σ",1,-1,-4 )
ylb1 = Spell("EXPEL YELLOW BILE Ξ",2,-3,3)
ylb2 = Spell("INVIGORATE LIVER ξ",2,3,-1)
blk1 = Spell("PURGE BLACK BILE Δ",3,-4,3)
blk2 = Spell("ROUSE KIDNEYS δ",3,3,-2)
wht1 = Spell("EJECT PHLEGM Θ",4,-4,2)
wht2 = Spell("INCREASE PHLEGM θ",4,6,0)
clob = Spell("CLOBBER",1,-1,8)

slp1 = Attack("SLAP", 0,0,1,100)
slp2 = Attack("BACKHAND",0,0,2,20)
pch1 = Attack("LIVER PUNCH",2,-2,4,100)
stb1 = Attack("KNIFE",1,-3,7,100)
pri1 = Attack("STRIKE OF FAITH",3,8,3,85)
pri2 = Attack("DIVINE LIGHT",4,4,0,100)
pri3 = Attack("STIMULATE MARROW α",1,6,-8,100)




def turn(x):
        x.showhp()
        r = x.humours()
        x.humstat(r)
        x.hresponse(r)
        you.showhp()
        p = you.humours()
        you.humstat(p)
        you.hresponse(p)
        global turnnumber
        turnnumber = turnnumber +1


    


        
### Status effect counter. rng between 5,8 if the status stays for that long they lose health. probs 1/4 of total. 
### ofc attack modifiers, status effects. 1 is gonna regen health, 2, hits hard. 3 sad amd 4 forgetful. 
### spell repeat banner. the same spell can't be repeated when chosen thems the rules. like that one pokemon move.#
            
ene = Enemy("TEST ENEMY",20,5,5,5,5,False,False,False,False,False,("00","\"Ha... Ha ha ha!\"", "\"I'm fucking fuming!!\"", "\"What's the point in anything...?\"", "\"...Huh? What's going on?\"", "\"Christ, I feel really off.\""),
            ("00","She laughs hysterically...","She's bright red with anger!","She looks very sad.","She seems very confused.","She looks very under the weather."),
            ("00","\"Ahahaha! This is so fun!\"","\"I've had it up to here with you mate!\"","\"I'm having some really scary thoughts...\"","\"Where am I?\"","\"I think I need a lie down.\""),
            ("00","She clutches her stomach in laughter.","She's fuming!","She has a forlorn look to her.","She seem very lost in thought.","\"My humours must be all off-kilter.\""),
            ("00","\"Hahahaha... I can't stop laughing!\"","\"Right! You're getting a fucking pasting!\"","\"I think I'm having a depressive episode, you know.\"","\"I'm really confused! Who am I? What am I doing here?\"","\"I feel rotten. I need a big glass of water and a paracetamol.\""), False,0
            )

you = Enemy("The Theurgist",20,5,5,5,5,False,False,False,False,False,("00","\"My blood...\"", "Rage swells in your chest; it burns your throat.", "\"...\"", "You forgot where you are.", "\"...\""),
            ("00","This all seems very funny.", "\"Ugh...\"", "\"...\"", "\"...\"", "You grow pale, feeling the imbalance of humours inside of you."),
            ("00","You stifle a laugh.", "\"...\"", "The darkness grows near...", "You forgot your name.", "Your stomach churns unpleasantly..."),
            ("00","\"...\"", "You let out a sharp tut.", "A deep sadness cuts through your heart.", "\"What...?\"", "\"...\""),
            ("00","\"...\"", "\"...\"", "Tears roll down your cheeks", "\"...\"", "\"Urk...\""),
            False,0)


turnnumber = 1
fighting = True

while fighting == True: #### checks come after health. duh
    turn(ene) 
    slp1.attack(ene)
    fighting = checkhealth(ene) 
    bld2.cast(ene) 
    fighting = checkhealth(ene)
    turn(ene) 
    slp1.attack(ene)
    fighting = checkhealth(ene) 
    ylb2.cast(ene) 
    fighting = checkhealth(ene)
deathcheck(ene)
    

    
