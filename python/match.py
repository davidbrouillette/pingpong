class Match:
    def __init__(self, firstServer, pointsInMatch, servesPerPlayer):
        self.pointsInMatch = pointsInMatch
        self.servesPerPlayer = servesPerPlayer
        self.player1 = {'name':'player1'}
        self.player2 = {'name':'player2'}
        self.score = {'player1':0, 'player2':0}
        self.numberOfServes = 0
        self.currentServer = firstServer

    def setServer(self, name):
        self.currentServer = name

    def scorePoint(self, name):
        self.score[name] = self.score[name] + 1
        self.numberOfServes = self.numberOfServes + 1
        self.checkScores(name)
        self.checkServes()
        print(self.score)

    def checkScores(self, name):
        print(self.score[name])
        if self.score[name] == self.pointsInMatch:
            self.winScenerio(name)

    def winScenerio(self, name):
        print(name + ' wins!')

    def checkServes(self):
        if self.numberOfServes > 0 and (self.numberOfServes % self.servesPerPlayer == 0):
            if self.currentServer == 'player1':
                self.currentServer = 'player2'
            else:
                self.currentServer = 'player1'
            
            print('CurrentServer = ' + self.currentServer)