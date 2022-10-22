import pygame

WIDTH,HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Ricochet')

SHIELD_WIDTH = 100
SHIELD_HEIGHT = 15

FPS = 60

class Shield:
    VEL = 10
    
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x , self.y, self.width, self.height))
        
    def move(self, direction=1):
        self.x = self.x + self.VEL * direction
        
class Bullet:
    VEL=10
    
    def __init__(self, x, y, radius, color):
         self.x = x
         self.y = y
         self.radius = radius
         self.color = color
         
    def move(self)
         

def draw(WINDOW, shield):
    WINDOW.fill('white')
    shield.draw(WINDOW)
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    shield = Shield(WIDTH/2 - SHIELD_WIDTH/2, HEIGHT - SHIELD_HEIGHT - 10, SHIELD_WIDTH, SHIELD_HEIGHT, "blue" )
    
    run = True
    
    while run:
        clock.tick(FPS)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] and shield.x + shield.VEL + SHIELD_WIDTH <= WIDTH:
            shield.move(1)
        if keys[pygame.K_LEFT] and shield.x - shield.VEL >= 0:
            shield.move(-1)
        
        draw(WINDOW, shield)
    
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()