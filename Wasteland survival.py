#JIRO Inc.
#Wasteland Survival
#Justin, Inderdeep, Richard, Oscar
#the small goomba has to go and survive harsh and empty wasteland.
#He has to avoid all spiders and escape to a alternate timeline.
from gamelib import*
from random import*

game = Game(975,975,"Wasteland Survival")

bk = Image("wasteland.jpg",game)
bk.resizeTo(game.width, game.height)
player = Animation("goomba.png",35,game,1540/7,1377/5,use_alpha=False)
player.resizeBy(-45)
player.moveTo(100,800)
End = Image("Finish_Line.png",game)


sminion = Animation("spider.png",9,game,192/3,192/3,use_alpha=False)
sminion.moveTo(450,750)
sminion.resizeBy(75)
sminion.setSpeed(50,randint(50,100))
sminion2 = Animation("sdiper.jpg",9,game,192/3,192/3,use_alpha=False)
sminion2.moveTo(450,750)
sminion2.resizeBy(75)
sminion2.setSpeed(100,randint(45,90))
End.moveTo(1110,475)
End.setSpeed(0.1,90)
game.setBackground(bk)
 
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    sminion.draw()
    sminion2.draw()
    player.draw()
    if keys.Pressed[K_RIGHT]:
        player.x += 5
    if keys.Pressed[K_LEFT]:
        player.x -= 5
    if keys.Pressed[K_UP]:
        player.y -= 5
    if keys.Pressed[K_DOWN]:
        player.y += 5
    sminion.move(True)
    sminion2.move(True)
    End.move(False)
    if player.collidedWith(sminion or sminion2):
       player.health-= 1
    End.draw()
 
    player.health = 100
    game.update(30)
game.quit()
