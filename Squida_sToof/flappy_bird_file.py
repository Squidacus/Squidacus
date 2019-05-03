from gamelib import *
game = Game(800, 600, "Flappy Bird")
       
bk = Image("day.png", game)
bk.resizeTo(800, 600)
game.setBackground(bk)

bird = Animation("bird.png", 3, game, 44, 34)

bar = Animation("bar.png", 3, game, 2100/3, 110)
bar.resizeTo(game.width, bar.height)
bar.y = game.height - 50

coin = Animation("coins.png", 64, game, 512/8, 512/8)
coin.resizeTo(75, 75)
coin.moveTo(60, 555)

ring = Animation("ring.png", 10, game, 704/10, 90)
ring.setSpeed(3, 90)
ring.x = game.width + 50

top_pipe = Image("pipe_top.png", game)
top_pipe.x = ring.x
top_pipe.y = ring.y - 200
top_pipe.setSpeed(3, 90)

bot_pipe = Image("pipe_bot.png", game)
bot_pipe.x = ring.x
bot_pipe.y = ring.y + 200
bot_pipe.setSpeed(3, 90)

b_screen = Image("logo.png", game)

end_screen = Image("flappybird_end.png", game)

die = Sound("die.ogg", 1)
hit = Sound("hit.ogg", 2)
point = Sound("point.ogg", 3)
fly = Sound("wing.ogg", 4)

f = Font(blue, 40, red, "Bookman Old Style")
f2 = Font(black, 20, yellow, "Times New Roman")

#start screen loop
while not game.over:
    game.processInput()
    
    bk.draw()   
    b_screen.draw()
    game.drawText("PRESS [SPACE] TO START THE GAME", game.width/3.5, game.height - 100, f2)

    if keys.Pressed[K_SPACE]:
        game.over = True
    
    game.update(30)

game.over = False

while not game.over:
    game.processInput()

    game.scrollBackground("left", 3)    
     
    ring.move()
    
    top_pipe.move()
    top_pipe.x = ring.x #erase this line when submitting the game project
    top_pipe.y = ring.y - 200 

    bot_pipe.move()
    bot_pipe.x = ring.x #erase this line when submitting the game project
    bot_pipe.y = ring.y + 200 

    if ring.x < 0: #when submitting the game - use if statement below
        ring.x = game.width + ring.width/2
        ring.y = randint(0 + ring.height * 2, game.height - bar.height * 2)
        top_pipe.moveTo(top_pipe.x, top_pipe.y)
        bot_pipe.moveTo(bot_pipe.x, bot_pipe.y)
        ring.visible = True
    #or
    #if top_pipe.isOffScreen("left"):
        #ring.x = game.width + 50
        #y = randint(150, 350)
        #ring.moveTo(ring.x, y)
        #top_pipe.moveTo(ring.x, ring.y - 200)
        #bot_pipe.moveTo(ring.x, ring.y + 200)
        #ring.visible = True
       
    bird.draw()
    bird.y += 2 
    if keys.Pressed[K_SPACE]:
        bird.y -= 4
        fly.play()
        
    if bird.collidedWith(ring):
        game.score += 10
        ring.visible = False
        point.play()

    if bird.collidedWith(top_pipe, "rectangle") or bird.collidedWith(bot_pipe, "rectangle"):
        hit.play()
        game.over = True
        die.play()
        
    bar.draw()

    coin.draw()
    game.drawText("X " + str(game.score), game.width - 675, game.height - 70, f)
      
    game.update(30)

#end screen loop
game.over = False
while not game.over:
    game.processInput()

    end_screen.draw()
        
    game.update(30)
    
game.quit()


