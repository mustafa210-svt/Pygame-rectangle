import pygame

#screen
WIDTH = 600
HEIGHT = 600
TITLE = "rectangle"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

#class for the rectangle 
class Rectangle():
    def __init__(self,x,y,colour,width,height):
        self.x = x
        self.y = y
        self.colour = colour 
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height),0)

rectangle1 = Rectangle(100,100,"yellow",400,200)
rectangle2 = Rectangle(200,100,"Red",300,150)
run = True
screen.fill("White")
while run == True:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            rectangle1.draw()
            rectangle2.draw()

    
    pygame.display.update()
        
