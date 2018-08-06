from match import Match
from time import sleep
from guizero import App, Text, Picture
from gui import GUI_MATCH
from GUI_GET_FIRST_SERVER import GUI_GET_FIRST_SERVER
from bluetoothControllerAdapter import ControllerR, RunEventLoop, A_BTN, GetRawInput

def updateGame(guiMatch, match, player):
    match.scorePoint(player)
    guiMatch.updateGUI(match.currentServer, match.score['player1'], match.score['player2'])

def mainLoop(app, getServer):
    currentMatch = Match(getServer.firstServer,11,5)
    guiMatch = GUI_MATCH(app)
    guiMatch.updateGUI(currentMatch.currentServer, currentMatch.score['player1'], currentMatch.score['player2'])
    updateOnScore = lambda player: updateGame(guiMatch, currentMatch, player)
    RunEventLoop(updateOnScore) 

def PingPong():
    try:
        app = App(title='Ping Pong', layout="grid", bg="lightgrey", height="720", width="1280")
        getServer = GUI_GET_FIRST_SERVER(app)
        
        while getServer.firstServer == "":
            app.update()
        
        mainLoop(app, getServer)
        
        app.display()
        

    except KeyboardInterrupt:
        print("Closing Ping Pong Protocol...")
        exit(0)


PingPong()


#GetRawOutput()

    
