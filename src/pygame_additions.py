import pygame


class button():
    def __init__(self,x_pos,y_pos,width,height):
        self.x_start = x_pos
        self.y_start = y_pos
        self.height = height
        self.width = width
        self.x_end = x_pos + width
        self.y_end = y_pos + height
        self.collision_hitbox = pygame.Rect(x_pos,y_pos,width,height)
        self.color = (255,0,0)
        self.autoresize = True
        self.text = "text"     
    
    def set_text(self,text):
        self.text = text
    
    def set_action(self,function):
        self.action = function
    
    def handle_input(self,click_pos):
        if not self.collision_hitbox.collidepoint(click_pos):
            pass
        self.action()
    
    def draw(self,surface):
        button_visual = pygame.Surface((self.width,self.height))
        pygame.draw.rect(button_visual,(self.color),self.collision_hitbox)       
        if self.text is not None:
            font = pygame.font.SysFont('Arial',25)
            rendered_text = font.render(self.text, True, (255,255,255))
            button_visual.blit(rendered_text,(self.x_start, self.y_start))      
        surface.blit(button_visual,(self.x_start,self.y_start))         