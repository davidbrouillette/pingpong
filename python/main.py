from match import Match
from time import sleep
from guizero import App, Text, Picture



def PingPong():

    
    currentMatch = Match(11,5)

    def updateText():
        playerOneScore.value = currentMatch.score['player1']
        playerTwoScore.value = currentMatch.score['player2']
        
        if currentMatch.currentServer == 'player1':
            playerOneServe.text_color = 'black'
            playerTwoServe.text_color = 'lightgrey'
        else:
            playerOneServe.text_color = 'lightgrey'
            playerTwoServe.text_color = 'black'
        
        app.update()
        sleep(1)


    app = App(title="PingPong", layout="grid")



    playerOneScore = Text(app, text=currentMatch.score['player1'], size=200, font="times New Roman", color="lightblue", grid=[0,0])
    playerTwoScore = Text(app, text=currentMatch.score['player1'], size=200, font="Times New Roman", color="lightblue", grid=[1,0])

    playerOneServe = Text(app, text="<--", size=150, font="Times New Roman", color="black", grid=[0,1])
    playerTwoServe = Text(app, text="-->", size=150, font="Times New Roman", color="lightgrey", grid=[1,1])
    # playerOneServe = Picture(app, "")
    # playerTwoServe = Picture(app, "")

    app.update()

    currentMatch.scorePoint('player1')
    updateText()
    sleep(1)
    
    currentMatch.scorePoint('player1')
    updateText()
    
    currentMatch.scorePoint('player1')
    updateText()

    currentMatch.scorePoint('player1')
    updateText()
    
    currentMatch.scorePoint('player2')
    updateText()
    
    currentMatch.scorePoint('player1')
    updateText()
    currentMatch.scorePoint('player1')
    updateText()
    currentMatch.scorePoint('player1')
    updateText()
    currentMatch.scorePoint('player2')
    updateText()
    currentMatch.scorePoint('player1')
    updateText()
    currentMatch.scorePoint('player1')
    updateText()
    currentMatch.scorePoint('player1')
    updateText()
    currentMatch.scorePoint('player1')
    updateText()
    app.display()




PingPong()



    