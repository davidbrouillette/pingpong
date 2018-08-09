import pygame
import os
import threading
from player import Player
from controller import Controller
from BitdoKeyMappings import initMapping

def buttonFn(score):
    fn = lambda: score = score + 1
    return fn

def PingPong():
    try:
        player1 = Player("player1", 0)
        player2 = Player("player2", 1)
        
        pygame.init()
        pygame.joystick.init()
        score = 0
        player1KeyMapping = initMapping()
        player1KeyMapping["rshoulder"] = buttonFn(score)
        player2KeyMapping = initMapping()
        player2KeyMapping["rshoulder"] = buttonFn(score)

        playerController1 = Controller(player1.name, player1.controllerId, player1KeyMapping)
        playerController2 = Controller(player2.name, player2.controllerId, player2KeyMapping)
        
                
        
        pygame.display.set_caption("HI!")
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode([700,400], pygame.NOFRAME)
        screen.fill((135,180,210))
        text = pygame.font.Font(None, 100)
        textArea = text.render("HELLO!", True, (255,255,255))
        rect = textArea.get_rect(center=(160,120))
        screen.blit(textArea, rect)
        pygame.display.update()
        
        
        playerController1.listen()
        playerController2.listen()
        
##        Thread_playerController1 = threading.Thread(target=playerController1.listen)
##        Thread_playerController2 = threading.Thread(target=playerController2.listen)
##        Thread_playerController1.setDaemon(True)
##        Thread_playerController1.start()
##        Thread_playerController2.setDaemon(True)
##        Thread_playerController2.start()
##        
        

    except KeyboardInterrupt:
        print("Closing Ping Pong Protocol...")
        pygame.quit()
        exit(0)


PingPong()


    
