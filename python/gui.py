from guizero import App, Text, Picture

app = App(title="PingPong", layout="grid")

playerOneScore = Text(app, value="13", size=40, font="times New Roman", color="lightblue", grid=[0,0])
playerTwoScore = Text(app, value="17", size=40, font="Times New Roman", color="lightblue", grid=[1,0])

playerOneServe = Text(app, value="<--", size=20, font="Times New Roman" color="black", grid=[0,1])
playerTwoServe = Text(app, value="-->", size=20, font="Times New Roman" color="lightgrey", grid=[0,1])
# playerOneServe = Picture(app, "")
# playerTwoServe = Picture(app, "")

app.display()