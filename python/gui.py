from guizero import App, Text, Picture

class GUI_MATCH:
    def __init__(self, app):
        self.app = app
        self.app.bg = "lightgrey"
        app.title = "Ping Pong"
        self.playerOneScore = Text(self.app, text="0", size=200, font="Times New Roman", color="blue", grid=[0,0])
        self.playerTwoScore = Text(self.app, text="0", size=200, font="Times New Roman", color="blue", grid=[1,0])

        self.playerOneServe = Text(self.app, text="<--", size=150, font="Times New Roman", color="black", grid=[0,1])
        self.playerTwoServe = Text(self.app, text="-->", size=150, font="Times New Roman", color="lightgrey", grid=[1,1])

    def start(self):
        self.app.display()

    def updateGUI(self, server, player1Score, player2Score):
        self.playerOneScore.value = player1Score
        self.playerTwoScore.value = player2Score

        if server == 'player1':
            self.playerOneServe.text_color = 'black'
            self.playerTwoServe.text_color = 'lightgrey'
        else:
            self.playerOneServe.text_color = 'lightgrey'
            self.playerTwoServe.text_color = 'black'
            
        self.app.update()
