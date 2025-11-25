import random
prompt_reply = "Input: "
text_invalid = "Text invalid. Please try again."
status = ("000","SANGUINE", "CHOLERIC", "MELANCHOLIC", "PHLEGMATIC","UNWELL") # these are statuses
checkerlim = 2 # this is the upper limit to how high a humour can be 
tab = "     " 
anyk = "PRESS ANY KEY TO CONTINUE >>"
test_tuple = ("This is some text.",
              "This is some more text.",
              "Yippee!")

test_tuple2 = ("Long long ago...","Something happened.","And then something else happened.")

test_tuple3 = ("And then more things happened.","I guess...")

test_tuple4 = ("And then more.")

def colourtxt(x,z): # x = text z= colour 1.re 2.yel 3.blk 4. wht 5.blu
    """
    Prints coloured text.

    Parameters: 
    x (str) = text to be displayed
    z (int) = colour generated.
    
    """
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
    """
    Prints text, highlighted in a colour.

    Parameters: 
    x (str) = text to be displayed
    z (int) = highligted colour.
    
    """
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

def storytext(t): # t = tuple
    """
    t is a tuple, and it prints text. 
    """
    y = 0
    z = len(t)
    while y < z:
        print(t[y])
        y = y+1
        input(anyk)


progress = 0
def storyprog(): #prints text, and sets enemy . enemy = storyprog
    global progress
    current = progress
    progress =+1
    storytext(story_narration[current])
    return current 
    
    


def inputreply(x): #x must be +ve integer (number of poss options)
    """
    provides place for input
    returns integer typed
    """ 
    doneflag = False
    while doneflag == False:
        rawinput = input(prompt_reply)
        inputted = rawinput.strip()
        if inputted.isdigit():
            try:
                inty = int(inputted)
            except TypeError:
                print(text_invalid)
            except:
                print(text_invalid)
            if inty > 0 and inty != 0 and inty <= x:
                doneflag = True
                return inty
            else:
                print(text_invalid)
        else:
            print(text_invalid)

def compare(x_list,y_list): ##this is to compare this/last turns humours. 
    """
    This compares one list of booleans to another.
    If the same index for both are true, returns True. Otherwise False
    
    """
    #if True in y_list: wtf does this mean
    #    y_list = [False,False,False,False] what i was thinking

    #print("** hums" +  str(x_list))
    #print("prevhums" + str(y_list))
    
    x = zip(x_list, y_list) #checks between each item in both lists, if they are the same, it returns 'true'.
    if (True,True) in x:
        return True
    else:
        return False


class Enemy:
    def __init__(self,name,hp,red,yel,blk,wht,sag,cho,mel,phl,unw,phr1,phr2,phr3,phr4,phr5,dflag,dphrase,checker,moveset):
        self.name = name
        self.hp = hp
        self.red = red #blood points
        self.yel = yel #y bile points
        self.blk = blk #b bile points
        self.wht = wht #pleghm points
        self.sag = sag #Boolean. T = affected 
        self.cho = cho #Boolean. T = affected 
        self.mel = mel #Boolean. T = affected 
        self.phl = phl #Boolean. T = affected 
        self.unw = unw #Boolean. T = affected 
        self.phr1 = phr1 #tuple with phrases, index corresponds with status number
        self.phr2 = phr2 # " 
        self.phr3 = phr3 # " 
        self.phr4 = phr4 # "
        self.phr5 = phr5 # " 
        self.dflag = dflag #deathflag
        self.dphrase = dphrase #deathphrase. tuple. 
        self.checker = checker
        self.moveset = moveset

    def humours(self): #functions to check one's humours
        """
        Checks 'health', and returns an integer, corresponding to a health status.
        
        """
        humours = [self.red,self.yel,self.blk,self.wht] 
        sumof = sum(humours) # adding all humour points
        limit = (sumof/4)*1.5 #average
        flaghum = [] #this is what decides one's affliction if any
        flaghum.clear() # cleared from previous go.
        #print("limit is " +  str(limit))
        for i in humours: #checking if each humour surpasses the limit, mean of sum of all humour points
            if i > limit:
                q = humours.index(i)
                flaghum.append(i) # if it's above limit, added to flaghum
            else:
                pass #idk nothing igyess
        if len(flaghum) == 1: #we can only get an affliction from one humour being too much. 
            l = humours.index(flaghum[0]) #we go back from the 1,2,3,4 code to decide the affliction
            l =  l+1 # +1 since index sharts from 0
            return l #we return the index, which is the 'code' for the condition
        elif len(flaghum) == 0: #if theres nothing in flaghum, one is healthy.
            #print("all balanced")
            return 0
        else: #in the instance that there's more than one in flaghum
            l =  max(flaghum) #finding max
            flaghum.reverse() #reversing..
            w = max(flaghum) #finding max in reverse
            if w == l: #if the two 'maximums' are the same in reverse, they are the same amount.
                return 5 #therefore, unwellness.
            else: #...something happened. idk how it would. but we have to return something.
                l =  l+1
                return l
            


        
    def humstat(self,x):
        """
        This either adds number to the 'checker' number, by comparing status from previous round?
        """
        prevhums = [self.sag,self.mel,self.cho,self.phl] # noting 'previous' hums
        if x !=0:
            text = "  << " + self.name + " is " + status[x] + "! >>  " #printing status
            colourhtxt(text,x) 
            if x == 1: #this sets the correct boolean to true, and falses for the other
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
        hums = [self.sag,self.mel,self.cho,self.phl] # 'new' humours
        adding = compare(hums,prevhums) #compares previous and current statuses
        if adding == True: 
            #print("found. adding 1 to " + self.name) 
            self.checker =  self.checker + 1 #this is the death counter, adding one
            print("checker: " + str(self.checker))
            prevhums = hums
        else:
            #print("nothing amiss with %s ..." % (self.name))
            self.checker = 0 #no consecutive status effect, so no number added


    
    def showhum(self):
        """
        prints humours
        """
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
    
    def hresponse(self,x): #character line for status effect.
        """
        prints response to status effect
        x = int corresponding to status effect. 1-5
        """
        list = [self.phr1,self.phr2,self.phr3,self.phr4,self.phr5]
        no = turnnumber % 5 #number from turn number, remainder of 5, which generates the index of what tuple from text it takes
        p = list[no]
        if x == 1:
            a = p[x]
            colourtxt(tab + a,x)
        elif x == 2:
            a = p[x]
            colourtxt(tab + a,x)
        elif x == 3:
            a = p[x]
            colourtxt(tab + a,x)
        elif x ==4:
            a =p[x]
            colourtxt(tab + a,x)
        elif x == 5:
            a = p[x]
            colourtxt(tab + a,x)
        else:
            pass

    def jumbly(self): #???
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

    def showhp(self): #prints hp in bars
        """
        prints hp as a range of bars.
        """
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
        self.htype = htype # int will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of humour affected, -ve or +ve
        self.dam = dam #damage to hp
        self.acc = acc #accuracy, rated 0-1 like pokemon
    def attack(self,e): 
        """
        e = the attack
        """ 
        mult = 1
        accu = 1
        if e.mel == True: ##too depressed to attack
            colourtxt("%s cannot attack..." % (e.name), 3)
            return
        if e.phl == True: # too weak, accuracy goes down
            accu = 0.5
        if e.sag == True: #too happy, mult down
            mult =  0.5
        if e.cho == True: #angy, mult up, acc down
            mult = 2
            accu = 0.75
        colourtxt("      %s used %s ! * " % (e.name,self.name), self.htype)
        a = random.randint(0,100)
        hitrate =  accu*self.acc #accu = accuracy from status effect. acc is from attack only. 
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
        self.htype = htype #int will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of humour damage -ve or +ve
        self.dam = dam #hp gotten rid of 

    def cast(self, e): # e= enemy
        mult = 1
        if you.mel == True: #melancholy status effect, depression
            colourtxt("Harrowed by sadness, you cannot bring yourself to attack.",3)
            return  #return brings it out, no continue
        if you.phl == True: #phlegmatic status effest, forget
            colourtxt("    * You forgot how to cast spells...",4)
            colourtxt("    * You hit " + e.name + " with your staff instead!", 4)
            e.hp =  e.hp - 4*mult
            return #return brings it out, no continue
        if you.sag == True: #sanguine effct
            mult =  0.5 #multiplier from 
        if you.cho == True: #chloreric effect
            mult = 2
        colourtxt("    * "+ self.name + " was cast on " + e.name + "!", self.htype) #printiny text
        e.hp =  e.hp - self.dam*mult #damage to hp calculation
        if self.htype == 1: #humour related dmg
            e.red = e.red + self.amt
        elif self.htype == 2:
            e.yel = e.yel + self.amt
        elif self.htype == 3:
            e.blk = e.blk + self.amt
        elif self.htype == 4:
            e.wht = e.wht + self.amt

def checkhealth(x): #where x = enemy
    """
    checks for death flags. 
    find and prints death reason.
    Returns boolean.
    False = someone raised deadflags. True = alive
    """
    global checkerlim
    if x.hp <= 0:
        print("%s has been killed." % (x.name))
        x.dflag = True
        return False
    elif x.checker >= checkerlim:
        print("%s was weakened through the manupulation of humours." % (x.name))
        options = ['YES',"NO"]
        z=1
        print("Kill " + x.name + "?")
        for i in options:
            print(str(z) + ". " + i )
            z=z+1
        ans = inputreply(2)
        if ans == 1:
            print(x.dphrase[0])
            print("You extinguised %s'S life." % x.name)
            x.dflag = True
        else:
            print("%s was spared." % x.name)
            print(x.dphrase[1])
        return False
    elif you.hp <= 0:
        print("You were defeated in battle...")
        you.dflag = True
        return False
    elif you.checker >= checkerlim:
        print("The Theurgist has met their worse end: the imbalance of their own humours.")
        you.dflag = True
        return False
    else:
        return True
    

""" for spells
        self.name = name
        self.htype = htype #int will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of humour damage -ve or +ve
        self.dam = dam #hp gotten rid of 
"""

bld1 = Spell("BLOODLET Σ",1,-4,4)
bld2 = Spell("STIMULATE MARROW σ",1,1,-4 )
ylb1 = Spell("EXPEL YELLOW BILE Ξ",2,-3,3)
ylb2 = Spell("INVIGORATE LIVER ξ",2,3,-1)
blk1 = Spell("PURGE BLACK BILE Δ",3,-4,3)
blk2 = Spell("ROUSE KIDNEYS δ",3,3,-2)
wht1 = Spell("EJECT PHLEGM Θ",4,-4,2)
wht2 = Spell("INCREASE PHLEGM θ",4,6,0)
clob = Spell("CLOBBER",1,-1,8)

spellbook = [bld1,bld2,ylb1,ylb2,blk1,blk2,wht1,wht2]

""" for attacks
        self.name = name
        self.htype = htype # int. will be 0=none 1 =red 2=yel 3=blk 4=wht
        self.amt = amt #degree of humour affected, -ve or +ve
        self.dam = dam #damage to hp
        self.acc = acc #accuracy, rated 0-1 like pokemon
"""

slp1 = Attack("SLAP", 0,0,1,100)
slp2 = Attack("BACKHAND",0,0,2,80)
pch1 = Attack("LIVER PUNCH",2,-2,4,100)
dpr1 = Attack("WHINGE",3,2,0,100)
stb1 = Attack("KNIFE",1,-3,7,10)
kni1 = Attack("POMMEL STRIKE",0,0,3,80)
kni2 = Attack("THRUST",1,-1,2,95)
kni3 = Attack("UPPERCUT",1,-2,5,50)
kni4 = Attack("SPIRITED YELL",2,2,0,100)
dog1 = Attack("NIP",1,-1,2,85)
dog2 = Attack("SNARL",2,1,0,100)
dog3 = Attack("WHIMPER",3,1,0,100)
dog4 = Attack("VICIOUS BITE",1,-3,5,50)
pri1 = Attack("STRIKE OF FAITH",3,8,3,85)
pri2 = Attack("DIVINE LIGHT",4,4,0,100)
pri3 = Attack("STIMULATE MARROW α",1,6,-8,100)
pri4 = Attack("PURGE BLACK BILE Δ",3,-4,3,100)
pri5 = Attack("ADMONISH",2,2,0,100)




def randommove(e): 
    """
    e is the enemy it belongs to. returns move y in that list, but doesn't use the same move in a row.
    returns y - item in Attack list
    """
    choosing = False
    z = 7 #to begin with
    y = random.choice(e.moveset)
    choosing = True
    while choosing == True:
        if e.moveset.index(y) != z:
            z = e.moveset.index(y) #registering previous index
            y.attack(e)
            choosing = False
        else:
            y = random.choice(e.moveset)

def pickspell(e): #e = enemy
    """
    list of spells made from total. player picks one and casts by inputting
    """
    spellchoice = []
    z = 1
    spellchoice = random.sample(spellbook, k=5)
    print(" *Choose a spell to cast:")
    for i in spellchoice:
        j=i.name
        print(str(z) + ". " + j )
        z=z+1
    ans = inputreply(5)
    indy = ans - 1
    p = spellchoice[indy]
    spellchoice.clear
    p.cast(e)

def turn(x):
        x.showhp() # shows hp
        r = x.humours() # checks ones humours
        x.humstat(r) # checks humour symptoms
        x.hresponse(r) # generates humour response line
        you.showhp() #shows player hp
        p = you.humours() #checks players humours
        you.humstat(p) #checks humour symptoms
        you.hresponse(p) #prints humour response line
        global turnnumber
        turnnumber = turnnumber +1







        
### Status effect counter. rng between 5,8 if the status stays for that long they lose health. probs 1/4 of total. 
### ofc attack modifiers, status effects. 1 is gonna regen health, 2, hits hard. 3 sad and 4 forgetful. 
### spell repeat banner. the same spell can't be repeated when chosen thems the rules. like that one pokemon move.#
"""" # for enemy generation
        self.name = name
        self.hp = hp
        self.red = red #blood points
        self.yel = yel #y bile points
        self.blk = blk #b bile points
        self.wht = wht #pleghm points
        self.sag = sag #Boolean. T = affected 
        self.cho = cho #Boolean. T = affected 
        self.mel = mel #Boolean. T = affected 
        self.phl = phl #Boolean. T = affected 
        self.unw = unw #Boolean. T = affected 
        self.phr1 = phr1 #tuple with phrases, index corresponds with status number
        self.phr2 = phr2 # " 
        self.phr3 = phr3 # " 
        self.phr4 = phr4 # "
        self.phr5 = phr5 # " 
        self.dflag = dflag #deathflag
        self.dphrase =dphrase #deathphrase words tuple/ 0= kiled 1=spared
        self.checker = checker
"""
ene = Enemy("TEST ENEMY",20,5,5,5,5,False,False,False,False,False,("00","\"Ha... Ha ha ha!\"", "\"I'm fucking fuming!!\"", "\"What's the point in anything...?\"", "\"...Huh? What's going on?\"", "\"Christ, I feel really off.\""),
            ("00","She laughs hysterically...","She's bright red with anger!","She looks very sad.","She seems very confused.","She looks very under the weather."),
            ("00","\"Ahahaha! This is so fun!\"","\"I've had it up to here with you mate!\"","\"I'm having some really scary thoughts...\"","\"Where am I?\"","\"I think I need a lie down.\""),
            ("00","She clutches her stomach in laughter.","She's fuming!","She has a forlorn look to her.","She seem very lost in thought.","\"My humours must be all off-kilter.\""),
            ("00","\"Hahahaha... I can't stop laughing!\"","\"Right! You're getting a fucking pasting!\"","\"I think I'm having a depressive episode, you know.\"","\"I'm really confused! Who am I? What am I doing here?\"","\"I feel rotten. I need a big glass of water and a paracetamol.\""),
            False,("\"I guess it's all over\"","\"Really? Thanks!\""),0,(slp1,slp2,pch1,stb1),
            )

you = Enemy("The THEURGIST",50,5,5,5,5,False,False,False,False,False,("00","\"My blood...!\"", "Rage swells in your chest; it burns your throat.", "\"The black bile weighs down your very soul.\"", "You forgot where you are.", "A headache roils behind your eyeballs"),
            ("00","This all seems very funny.", "\"Ugh...!\"", "It feels difficult to be alive.", "You look around in wonder of all your surroundings.", "You grow pale, feeling the imbalance of humours inside of you."),
            ("00","You stifle a laugh.", "It feels usual for you to be this angry", "The darkness grows near...", "You forgot your name.", "Your stomach churns unpleasantly..."),
            ("00","\"Ha... haha!\"", "You let out a sharp tut.", "A deep sadness cuts through your heart.", "\"What...? What is going on?\"", "\"...\""),
            ("00","You do not remember the last time you had this much fun.", "\"I have slain every enemy of mine! You are next!\"", "Warm tears roll down your cheeks...", "\"...Where is this?\"", "\"Urk...\""),
            False,("Death...?","I..."),0,(""))

bra = Enemy("BRAVE KNIGHT",20,5,5,5,5,False,False,False,False,False,("00","\"Ha!\"", "\"You've drawn your last breath!\"", "\"...\"", "\"...What in the devil is going on?\"", "*COUGH* *COUGH*"),
            ("00","He laughs hysterically...","He's bright red with anger!","He looks as though he's about to cry.","He seems very confused.","He looks very under the weather."),
            ("00","\"Ahahaha! This is some good fun!\"","\"I have had it up to here with you!\"","\"What is the point in all of this? Just kill me.\"","\"Remind me, madam, where am I?\"","\"Urk...\""),
            ("00","He clutches her stomach in laughter.","He's fuming!","He has a forlorn look to him.","He seems very lost in thought.","The BRAVE KNIGHT seems poorly."),
            ("00","\"Hahahaha... HAHAHA!\"","\"Prepare to die!\"","\"Finish me. I have no desire to be alive.\"","The BRAVE KNIGHT observes the sword in his hand like a foreign object","\"I feel rotten. I need a big glass of water and a paracetamol.\""),
            False,("\"Don't kill me, please!\"","The BRAVE KNIGHT gave a bow before limping away..."),0,(kni1,kni2,kni3,kni4)
            )

dog = Enemy("DOG",10,5,5,5,5,False,False,False,False,False,("00","The DOG wags its tail.", "\"Grrr... ARF!\"", "The DOG is despondent.", "The DOG sniffs the ground", "*whimper*"),
            ("00","\"Arf!\"","The DOG lets out a growl...","","The DOG doesn't react to its surroundings.","The DOG seems very interested in its tail.","The DOG curls up on the ground."),
            ("00","The DOG pants, its tongue lolling our from its mouth.","The DOG will not stop barking.","The DOG doesn't blink.","It regards you as a stranger.","The DOG whimpers..."),
            ("00","The DOG looks like it wants to play.","The DOG bares its teeth...","It does not respond to your attacks.","It paws at the ground.","The DOG seems upset..."),
            ("00","*pant* *pant*","\"ARF! ARF! ARF!\"","It does not move.","*sniff* *sniff*","It takes a submissive position, with its tail in between its legs."),
            False,("You see fear, rage - a desire to live in this creature's eyes.","The DOG ran away..."),0,(dog1,dog2,dog3,dog4)
            )

pri = Enemy("PRINCESS",50,5,5,5,5,False,False,False,False,False,("00","The PRINCESS lets out a hearty laugh.", "\"It ends here, Magister! Die!\"", "A tear rolls down PRINCESS's cheek.", "\"Salve, Magister. What are we learning today?\"", "The PRINCESS puts a hand to her mouth."),
            ("00","\"Ahahaha!\"","The PRINCESS spits onto the ground","","\"Oh, Magister... Oh, Magister...\"","\"Ave, Magister. What are you doing here?\"","The PRINCESS looks like she's about to be sick."),
            ("00","\"Magister! Look what I can do!\"","\"Attone with your blood!\"","\"Where did it all go wrong, Magister?\"","The PRINCESS expresses deep concern. \"Magister... Did I have homework? I'm sorry, Magister. I forgot.\"","The PRINCESS grimaces. \"My humours...!\""),
            ("00","The PRINCESS chuckles \"I do not remember the last time I laughed this much!\"","\"I should have done this years ago!\"","The PRINCESS bursts into tears, weeping.","\"Hmm... Magister, remind me what we're doing?\"","\"...\""),
            ("00","The PRINCESS is delighted.","\"The walls will be stained with your blood!\"","\"I missed you, Magister...\"","The PRINCESS observes her nails","The PRINCESS struggles to stay standing."),
            False,("\"My ghost will haunt you until your very last breath. Remember that, THEURGIST.\"","\"...Coward!\""),0,(pri1,pri2,pri3,pri4,pri5)
            )


story_narration = (test_tuple,test_tuple2,test_tuple3,test_tuple4)
story_enemies = (dog,ene,bra,pri)
c=0
while c < 5:
    c = storyprog()
    enemy = story_enemies[c]
    turnnumber = 1
    fighting = True
    while fighting == True:
        turn(enemy)
        randommove(enemy)
        pickspell(enemy)
        fighting = checkhealth(enemy)