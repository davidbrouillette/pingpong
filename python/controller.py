import os
import pygame

class Controller(object):
    button_data = None
    hat_data = None

    def init(self):
        self.button_data 
        self.hat_data
    
    def listen(self):
        for x in range(pygame.joystick.get_count()):    
            self.controller = pygame.joystick.Joystick(x)
            self.controller.init()
            if not self.button_data:
                self.button_data = {}
                for i in range(self.controller.get_numbuttons()):
                    self.button_data[i] = False
            
            if not self.hat_data:
                self.hat_data = {}
                for i in range(self.controller.get_numhats()):
                    self.hat_data[i] = (0,0)
            done = true
            while done:
                for event in pygame.event.get():
                    if event.type == pygame.JOYBUTTONDOWN:
                        self.button_data[event.button] = True
                    if event.type == pygame.JOYBUTTONFALSE:
                        self.button_data[event.button] = False
                    if event.type == pygame.JOYHATMOTION:
                        self.hat_data[event.hat] = event.value
                    
                    print(self.button_data)
                    print(self.hat_data)
                    joystick_count = pygame.joystick.get_count()
                    print(joystick_count)
    

pygame.init()

pygame.display.set_mode([200,200])
pygame.display.set_caption("pingpong")
pygame.joystick.init()

button_data = None
hat_data = None


for x in range(pygame.joystick.get_count()):    
    controller = pygame.joystick.Joystick(x)
    controller.init()
    if not button_data:
        button_data = {}
        for i in range(controller.get_numbuttons()):
            button_data[i] = False
    
    if not hat_data:
        hat_data = {}
        for i in range(controller.get_numhats()):
            hat_data[i] = (0,0)
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                button_data[event.button] = True
            if event.type == pygame.JOYBUTTONUP:
                button_data[event.button] = False
            if event.type == pygame.JOYHATMOTION:
                hat_data[event.hat] = event.value
            
            print(event)




pygame.quit()
