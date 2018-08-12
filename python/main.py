import pygame
import sys
from player import Player
from controller import Controller
from BitdoKeyMappings import initMapping, parseButton
from mainLoop import MainLoop
from match import Match
from gui import GUI
from serveIndicator import ServeIndicator
from textObject import TextObject
from GUI_getPlayUntil import GUI_getPlayUntil
from GUI_getFirstServer import GUI_getFirstServer
from GUI_gameOver import GUI_gameOver

class PingPong:
    def __init__(self):
        self.game = True
        self.running = True
        self.currentMatch = None
        self.joysticks = None
        self.eightBitdoKeyMapping = None
        self.gui = None
        self.numberOfServes = None
        self.firstServer = None
        self.playAgain = False
        
    def setPlayAgain(self, again):
        self.playAgain = again
        
    def setNumberOfServes(self, num):
        self.numberOfServes = num
    
    def setFirstServer(self, first):
        self.firstServer = first
        
    def setupGame(self):
        pygame.init()
        pygame.joystick.init()
        pygame.font.init()
        pygame.display.init()
        
        self.joysticks = []
        for x in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(x))
            self.joysticks[x].init()
        
        mapping_getPlayUntil = initMapping()
        mapping_getPlayUntil["rshoulder"] = lambda x: self.setNumberOfServes(11)
        mapping_getPlayUntil["lshoulder"] = lambda x: self.setNumberOfServes(21)
        
        GUI_getPlayUntil(mapping_getPlayUntil)
        
        print("Number of Serves selected: " + str(self.numberOfServes))
        
        mapping_getFirstServer = initMapping()
        mapping_getFirstServer["rshoulder"] = lambda x: self.setFirstServer('player2')
        mapping_getFirstServer["lshoulder"] = lambda x: self.setFirstServer('player1')
        
        GUI_getFirstServer(mapping_getFirstServer)
        print("First Server selected: " + str(self.firstServer))
        
        pygame.display.init()
        
        player1 = Player("player1", 0, 200, 25)
        player2 = Player("player2", 1, 500, 25)
        self.currentMatch = Match(player1, player2, self.firstServer, self.numberOfServes, 5)
        player1.textFunc = self.currentMatch.getScore
        player2.textFunc = self.currentMatch.getScore
        serveIndicatorPlayer1 = ServeIndicator("player1", "<--", 175, 200, self.currentMatch.isCurrentServer)
        serveIndicatorPlayer2 = ServeIndicator("player2", "-->", 525, 200, self.currentMatch.isCurrentServer)
        
        self.eightBitdoKeyMappingPlayer2 = initMapping()
        self.eightBitdoKeyMappingPlayer2["rshoulder"] = self.buttonFn(self.currentMatch.scorePoint)
        self.eightBitdoKeyMappingPlayer2["lshoulder"] = lambda x,y: self.currentMatch.subtractPoint(x)
        self.eightBitdoKeyMappingPlayer1 = initMapping()
        self.eightBitdoKeyMappingPlayer1["lshoulder"] = self.buttonFn(self.currentMatch.scorePoint)
        self.eightBitdoKeyMappingPlayer1["rshoulder"] = lambda x,y: self.currentMatch.subtractPoint(x)
        
        self.gui = GUI()
        self.gui.addGUIObject(player1)
        self.gui.addGUIObject(player2)
        self.gui.addGUIObject(serveIndicatorPlayer1)
        self.gui.addGUIObject(serveIndicatorPlayer2)
        self.gui.setupGUI()
        
    def startGame(self):
        MainLoop(self.running, self.eightBitdoKeyMappingPlayer1, self.eightBitdoKeyMappingPlayer2, self.gui, self.currentMatch)
        
        mapping_gameOver = initMapping()
        mapping_gameOver["rshoulder"] = lambda x: self.setPlayAgain(True)
        mapping_gameOver["lshoulder"] = lambda x: self.setPlayAgain(False)
        
        GUI_gameOver(mapping_gameOver, self.currentMatch.winner, self.currentMatch.score)
        pygame.display.quit()
    
    def addScore(self, fn, name, event):
        scorer, scores = fn(name)
    
    def buttonFn(self, fn):
        return lambda x,y: self.addScore(fn,x,y)
    


def RunGame():
    pingPong = PingPong()
    pingPong.setupGame()
    pingPong.startGame()
    return pingPong.playAgain
    
playing = True

while playing:
    playing = RunGame()
    print("Play Again: " + str(playing))
    if not playing:
        pygame.joystick.quit()
        pygame.font.quit()
        pygame.display.quit()
        pygame.quit()
