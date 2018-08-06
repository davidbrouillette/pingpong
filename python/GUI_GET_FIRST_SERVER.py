from guizero import Window, Text, PushButton

class GUI_GET_FIRST_SERVER:
    def __init__(self, app):
        app.title="Who Serves First?"
        self.text = Text(app, text="Who is serving first?", grid=[1,1])
        self.player1Button = PushButton(app, text="Player 1", command=self.setServerPlayer1, grid=[0,2])
        self.player2Button = PushButton(app, text="Player 2", command=self.setServerPlayer2, grid=[2,2])
        self.firstServer = ""
        app.update()        
        
    def setServerPlayer1(self):
        self.firstServer = 'player1'
        self.destroy()
    
    def setServerPlayer2(self):
        self.firstServer = 'player2'
        self.destroy()

    def getFirstServer(self):
        return self.firstServer

    def destroy(self):
        self.text.destroy()
        self.player2Button.destroy()
        self.player1Button.destroy()


