from graphics import *

class Atom():

    def __init__(self, center,radius):
        self.centerAtom = Circle(center,radius)

    def draw(self, win): 
        self.centerAtom.draw(win)

    def move(self, dx, dy): 
        self.centerAtom.move(dx, dy)

    def set_color(self, color):
        self.centerAtom.setFill(color)

    def undraw(self): 
        self.centerAtom.undraw()

    def get_size(self):
        return self.centerAtom.getRadius()

    def get_center(self):
        return self.centerAtom.getCenter()


class OxygenAtom(Atom):

    def __init__(self, center,radius=60):
        self.centerAtom = Circle(center,60)

    def draw(self, win):
        self.set_color('red')
        self.centerAtom.draw(win)

    def set_color(self, color):
        self.centerAtom.setFill(color)

    def move(self, dx, dy):
        self.centerAtom.move(dx, dy)


class HydrogenAtom(Atom):
    
    def __init__(self, center):
        self.centerAtom = Circle(center,radius=20)

    def draw(self, win):
        self.set_color('yellow')
        self.centerAtom.draw(win)
    
    def set_color(self, color):
        self.centerAtom.setFill(color)

    def move(self, dx, dy):
        self.centerAtom.move(dx, dy)


# Define a main function; if you want to display graphics, run main()
# after you load code into your interpreter
def water():
    # create a window with width = 700 and height = 500
    new_win = GraphWin('Monte Carlo', 300, 300)

    # What we'll need for the wheel...
    oxygenPos = Point(150, 150)
    hydrogen1Pos = Point(80, 80)
    hydrogen2Pos = Point(230,80)
    oradius = 60  # The radius of the outer tire is 100
    hradius = 20

    # Make a wheel object
    oxygen = OxygenAtom(oxygenPos)
    hydrogen1 = HydrogenAtom(hydrogen1Pos)
    hydrogen2 = HydrogenAtom(hydrogen2Pos)
    bond1 = Line(oxygenPos,hydrogen1Pos)
    bond2 = Line(oxygenPos,hydrogen2Pos)

    # Set its color
    oxygen.set_color('red')
    hydrogen1.set_color('yellow')
    hydrogen2.set_color('yellow')
    

    # And finally, draw it 
    oxygen.draw(new_win)
    hydrogen1.draw(new_win)
    hydrogen2.draw(new_win)
    bond1.draw(new_win)
    bond2.draw(new_win)

    # Run the window loop (must be the *last* line in your code)
    new_win.mainloop()

# Comment this call to main() when you import this code into
#  your car.py file - otherwise the Wheel will pop up when you
#  try to run your car code.
#water()

class WaterMolecule():

    def __init__(self, center,number):
        #self.oxygenPos = Point(center)
        self.xPos = center.getX()
        self.yPos = center.getY()
        self.hydrogen1Pos = Point(self.xPos-70,self.yPos-70)
        self.hydrogen2Pos = Point(self.xPos+60,self.yPos-83)
        self.oxygen=OxygenAtom(center)
        self.hydrogen1=HydrogenAtom(self.hydrogen1Pos)
        self.hydrogen2=HydrogenAtom(self.hydrogen2Pos)
        self.bond1=Line(center,self.hydrogen1Pos)
        self.bond2=Line(center,self.hydrogen2Pos)
        self.number=number
    
    def draw(self,win):
  
        self.oxygen.draw(win)
        self.hydrogen1.draw(win)
        self.hydrogen2.draw(win)
        self.bond1.draw(win)
        self.bond2.draw(win)

    def move(self,dx,dy):
        self.oxygen.move(dx,dy)
        self.hydrogen1.move(dx,dy)
        self.hydrogen2.move(dx,dy)
        self.bond1.move(dx,dy)
        self.bond2.move(dx,dy)

    #def rotate(self,deg):


win = GraphWin('tmp', 700, 700)
my_beaker=[]
for i in range(5):
    center=Point((i+1)*150,(i+1)*150)
    w=WaterMolecule(center,i)
    if (i==2):
        w.move(100,0)
    w.draw(win)
    my_beaker.append(w)

win.mainloop()
'''
center1=Point(150,150)
newwin = GraphWin('tmp', 700, 700)
w1=WaterMolecule(center1,1)
w1.move(200,200)
w1.draw(newwin)
newwin.mainloop()
'''




