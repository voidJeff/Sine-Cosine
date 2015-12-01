from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset
import math

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 950

red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0xff00ff, 1.0)
thinline = LineStyle(0, black)

xcord = range(0, 1500, 1)

mode = input("Which type of function do you have? \nl for linear, t for Trig, p for Parabola ")
if mode == "l":
    k = float(input("f(x) = kx + b, set the value of k: "))
    b = float(input("f(x) = kx + b, set the value of b: "))
elif mode == "t":
    a = int(input("f(x) = a sin h (x + k) , set the value of a: "))
    h = int(input("f(x) = a sin h (x + k) , set the value of h: "))
    k = int(input("f(x) = a sin h (x + k) , set the value of k: "))
elif mode == "p":
    a = int(input("f(x) = ax^2 + bx + c , set the value of a: "))
    b = int(input("f(x) = ax^2 + bx + c , set the value of b: "))
    c = int(input("f(x) = ax^2 + bx + c , set the value of c: "))
        
class Dot(Sprite):
    
    asset = CircleAsset(2, thinline, blue)

    def __init__(self, position):
        super().__init__(Dot.asset, position)
        self.x = 0
        self.loop = False
    
    def l(self):
        return 450-k*(self.x-750)-100*b
    
    
    def t(self):
        return 450-a*100*math.sin((self.x-750)/100)
        
    def step(self):
        if self.x < 1500:
            if mode == "l":
                n = self.y-(450-k*(self.x-750+1)-100*b)
                if not self.loop:
                    self.y = self.l()
                    sprite = Sprite(Dot.asset, (self.x, self.y))
                    
                if n > 1:
                    self.y -= 2
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    self.loop = True
                    n -= 2
                else:
                    self.loop = False
                    self.x += 1
                    
            elif mode == "t":
                n = self.y-450+a*100*math.sin(h*(self.x-750+100*k)/100)
                if not self.loop:
                    self.y = self.t()
                    sprite = Sprite(Dot.asset, (self.x, self.y))
                    print("1")
                    
                if n > 1:
                    self.y -= 2
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    self.loop = True
                    n -= 2
                    print("2")
                    
                elif n < -1:
                    self.y += 2
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    self.loop = True
                    n += 2
                    print("3")
                    
                else:
                    self.loop = False
                    self.x += 1
                    print("4")
                
            elif mode == "p":
                sprite = Sprite(Dot.asset, (self.x, 450-(a*(self.x-750)**2/100+100*b*self.x+100*c)))
                self.x += 1
              
            
            
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        #black = Color(0x000000, 1.0)
        #thinline = LineStyle(0, black)
        xaxis = RectangleAsset(1500,1, thinline, black)
        yaxis = RectangleAsset(1,950, thinline, black)
        sprite1 = Sprite(xaxis, (0, 450))
        sprite2 = Sprite(yaxis, (750, 0))
        
        Dot((0,450))
        #sprite0 = [Sprite(Dot.asset, (x, 450-k*(x-750)-100*b)) for x in xcord]
        
    def step(self):
        for dot in self.getSpritesbyClass(Dot):
            dot.step()
        #for dot in self.getSpritesbyClass(Dot):
            #dot.step()
            
myapp = Grapher(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
