status = ("SANGUINE", "CHOLERIC", "MELANCHOLIC", "PHLEGMATIC","UNWELL")

def colourtxt(x,z): # x = text z= colour 1.re 2.yel 3.blk 4. wjot
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
        
    
def colourhtxt(x,z): # x = text z= colour 1.re 2.yel 3.blk 4. wjot
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
    def __init__(self,name,red,yel,blk,wht):
        self.name = name
        self.red = red
        self.yel = yel
        self.blk = blk
        self.wht = wht
    def humours(self):
        humours = [self.red,self.yel,self.blk,self.wht]
        sumof = sum(humours)
        limit = (sumof/4)*1.5
        flaghum = []
        flaghum.clear()
        print("limit is " +  str(limit))
        for i in humours:
            if i > limit:
                q = humours.index(i)
                print (str(q) + " index humour feels a lot. " )
                flaghum.append(i)
            else:
                pass
        print(flaghum)
        if len(flaghum) == 1:
            l = humours.index(flaghum[0])
            l =  l+1
            return l
        elif len(flaghum) == 0:
            print("all balanced")
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
        


    
    def showhum(self):
        humours = [self.red,self.yel,self.blk,self.wht]
        x = 0
        r = 1 
        humournam = ["red","yellow","black","white"]
        for i in humours:
            v = humournam[x]
            colourtxt(v + ": " + str(i),r)
            x= x+1
            r= r+1
    
    def hresponse(self,x):
        if x == 1:
            a = "feeling sanguine..."
            colourtxt(a,x)
        elif x == 2:
            b = "feeling choleric..."
            colourtxt(b,x)
        elif x == 3:
            c = "feeling melancholic..."
            colourtxt(c,x)
        elif x ==4:
            d = "feeling phlegmatic..."
            colourtxt(d,x)
        elif x == 5:
            e = "feeling unwell..."
            colourtxt(e,x)
        else:
            print("either normal or it's gone terribly wrong.")

ene = Enemy("test person",5,5,5,5)



ene.showhum()
r = ene.humours()
ene.hresponse(r)
ene.red = 1
ene.yel = 7
ene.showhum()
r = ene.humours()
ene.hresponse(r)