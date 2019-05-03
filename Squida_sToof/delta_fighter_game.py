#Nicole Meselsohn
#Delta Fighter

from gamelib import *
game = Game(800, 600, "Delta Fighter")

bk = Image("field_5.png", game)
logo = Image("logo.png", game)
logo.y = 150
play = Image("play.png", game)
play.y = logo.y + 200
htp = Image("howtoplay.png", game)
htp.y = logo.y + 100
story = Image("story.png", game)
story.y = logo.y + 300
si = Image("storyImage.png", game)
hero = Image("hero.gif", game)

game.setBackground(bk)

#Title screen
while not game.over:
    game.processInput()

    game.scrollBackground("down", 2)    
    logo.draw()
    play.draw()
    story.draw()
    htp.draw()
          
    if mouse.LeftClick and mouse.collidedWith(story):
        game.over = True

    game.update(60)
game.over = False

#Story Image
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    si.draw()
    
    if mouse.LeftClick:
        game.over = True
    
    game.update(60)
game.over = False

#Level 1
asteroids = []
ammo = []

for index in range(100):
    asteroids.append(Animation("asteroids.gif", 41, game, 2173/41, 52))
    ammo.append(Animation("plasmaball1.png", 11, game, 352/11, 32))

for index in range(len(asteroids)):
    x = randint(100, 700)
    y = -randint(100, 10000)
    asteroids[index].moveTo(x, y)
    s = randint(2, 8)
    asteroids[index].setSpeed(s, 180)

for index in range(len(asteroids)):
    x = randint(100, 700)
    y = -randint(100, 10000)
    ammo[index].moveTo(x, y)
    s = randint(2, 8)
    ammo[index].setSpeed(s, 180)
  
ammo_count = 0
items = 0
ammo_items = 0

explode = Animation("explosion1.png", 22, game, 1254/22, 64)
explode.resizeBy(150)
explode.visible = False

while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    game.drawText("LEVEL 1", 350, 300)

    for index in range(len(asteroids)):
        asteroids[index].move()
        ammo[index].move()

    hero.draw()

    if keys.Pressed[K_UP]:
        hero.y -= 3

    if keys.Pressed[K_DOWN]:
        hero.y += 3

    if keys.Pressed[K_RIGHT]:
        hero.x += 3

    if keys.Pressed[K_LEFT]:
        hero.x -= 3
        
    for index in range(len(asteroids)):
        if asteroids[index].collidedWith(hero):
            hero.health -= 5 
            asteroids[index].visible = False
            explode.moveTo(hero.x - 10, hero.y - 20)
            explode.visible = True
            items += 1
            
    explode.draw(False)            

    for index in range(len(asteroids)):
        if ammo[index].collidedWith(hero):
            ammo_count += 1
            ammo[index].visible = False
            items += 1
            ammo_items += 1

        if ammo[index].isOffScreen("bottom") and ammo[index].visible:
            ammo[index].visible = False
            items += 1

        if asteroids[index].isOffScreen("bottom") and asteroids[index].visible:
            asteroids[index].visible = False        
            items += 1

    game.drawText("Health: " + str(hero.health), hero.x - 45, hero.y + 20)
    game.drawText("Ammo: " + str(ammo_count), hero.x - 40, hero.y + 40)
    game.drawText("Items: " + str(items), hero.x - 40, hero.y + 60)

    if items == 200:
        game.over = True

    if hero.health < 0:
        game.over = True
  
    game.update(60)
game.over = False
  
#Level 2

boss = Image("aliensh.png", game)
boss.resizeBy(-10)
boss.setSpeed(4, 180)

minions = []
for index in range(50):
    minions.append(Animation("scooter.png", 8, game, 396/4, 308/2))

for index in range(len(minions)):
    x = randint(100, 700)    
    y = -randint(100, 10000)
    minions[index].moveTo(x, y)
    s = randint(2, 8)
    minions[index].setSpeed(s, 180)
    minions[index].resizeBy(-70)
    
bullets = []
for index in range(ammo_count):
    bullets.append(Animation("plasmaball2.png", 10, game, 640/10, 64))                    

while not game.over and hero.health > 0:
    game.processInput()
    game.scrollBackground("down", 2)
    game.drawText("LEVEL 2", 350, 300)

    speed = randint(8, 12) 
    for index in range(len(bullets)):
        if keys.Pressed[K_SPACE]:
            bullets[index].visible = True
            bullets[index].setSpeed(speed, 0)
            ammo_count -= 1

    boss.move()

    hero.draw()

    if keys.Pressed[K_UP]:
        hero.y -= 3

    if keys.Pressed[K_DOWN]:
        hero.y += 3

    if keys.Pressed[K_RIGHT]:
        hero.x += 3

    if keys.Pressed[K_LEFT]:
        hero.x -= 3

    if hero.collidedWith(boss):
        game.over = True

    if hero.collidedWith(minions[index]):
        hero.health -= 10

    if boss.collidedWith(bullets[index]):
        boss.health -= 1

    game.drawText("Health: " + str(boss.health), boss.x - 40, boss.y - 60)

    if hero.health < 0:
        game.over = True
     
    game.update(60)
game.over = False

#End screen
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)

    game.drawText("END SCREEN", 350, 300)

    if mouse.LeftClick:
        game.over = True
    
    game.update(60)
game.over = False

