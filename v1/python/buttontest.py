import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

player1CurrentServer = True
player2CurrentServer = False
player1Score = 0;
player2Score = 0;


def PrintScore():
    print("Player 1: " + str(player1Score))
    print("Player 2: " + str(player2Score))
    print("")

def PrintCurrentServer():
    print("CurrentServer: ")
    print("p1: " + str(player1CurrentServer))
    print("p2: " + str(player2CurrentServer))
    print("")
    
def LedOn(pin):
    GPIO.output(pin, GPIO.HIGH)

def LedOff(pin):
    GPIO.output(pin, GPIO.LOW)


def CheckServer():
    global player1CurrentServer
    global player2CurrentServer
    global player1Score
    global player2Score
    
    if (player1Score + player2Score) % 5 == 0:   
       player1CurrentServer = not player1CurrentServer
       player2CurrentServer = not player2CurrentServer
       if player1CurrentServer:
           LedOn(19)
           LedOff(4)
       if player2CurrentServer:
               LedOff(19)
               LedOn(4)

def getScoreText():
    return str(player1Score) + " " + str(player2Score)

def MainLoop():
    global player1CurrentServer
    global player2CurrentServer
    global player1Score
    global player2Score

    pygame.init()
    pygame.font.init()
    pygame.display.init()
    


    LedOff(19)
    LedOff(4)
    LedOn(19)
    while True:
        player1 = GPIO.input(18)
        player2 = GPIO.input(24)
        reset = GPIO.input(25)
        if reset:
            break;
        if player1 == False:
            print('Player 1 Scored')
            player1Score = player1Score + 1
            CheckServer()
            PrintScore()
            PrintCurrentServer()
            time.sleep(1)
        if player2 == False:
            print('Player 2 Scored')
            player2Score = player2Score + 1
            CheckServer()
            PrintScore()
            PrintCurrentServer()
            time.sleep(1)

    LedOff(19)
    LedOff(4)
