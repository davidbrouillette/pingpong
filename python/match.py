class Match:

    def __init__(self, pointsInMatch, servesPerPlayer):
        self.pointsInMatch = pointsInMatch
        self.servesPerPlayer = servesPerPlayer
        self.player1 = {'name':'player1','currentServer':True}
        self.player2 = {'name':'player2', 'currentServer':False}
        self.score = {'player1':2, 'player2':9}
        self.numberOfServes = 0
        self.currentServer = 'player1'
    
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
                self.player2['currentServer'] = True
                self.player1['currentServer'] = False
            else:
                self.currentServer = 'player1'
                self.player2['currentServer'] = False
                self.player1['currentServer'] = True
            
            print('CurrentServer = ' + self.currentServer)