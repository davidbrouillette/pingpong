import pygame
import threading
from BitdoKeyMappings import BITDO_KEY_MAPPINGS_JOYBUTTON, BITDO_KEY_MAPPINGS_JOYAXIS, parseButton

class Controller:
    def __init__(self, name, id, keyMapping):
        self.button_data = None
        self.hat_data = None
        self.done = True
        self.controllerInstance = None
        self.name = name
        self.keyMapping = keyMapping
        self.thread = threading.Thread(target=self.listenLoop)
        
        self.controllerInstance = pygame.joystick.Joystick(id)
        self.controllerInstance.init()
        if not self.button_data:
            self.button_data = {}
            for i in range(self.controllerInstance.get_numbuttons()):
                self.button_data[i] = False
                
        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controllerInstance.get_numhats()):
                self.hat_data[i] = (0,0)
    
    def listen(self):
        self.thread.setDaemon(True)
        self.thread.start()
    
    def listenLoop(self):
        while self.done:
            for event in pygame.event.get():
                button = parseButton(event)
                if button in self.keyMapping and self.keyMapping[button] is not None:
                    self.keyMapping[button](self.name, event)
##                if event.type == pygame.JOYBUTTONDOWN:
##                    self.button_data[event.button] = True
##                if event.type == pygame.JOYBUTTONUP:
##                    self.button_data[event.button] = False
##                if event.type == pygame.JOYHATMOTION:
##                    self.hat_data[event.hat] = event.value

                




pygame.quit()
