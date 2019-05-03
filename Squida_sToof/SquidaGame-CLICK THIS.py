#Name Incorporated
#SQUIDACUS... DA FOE IS HERE!
#Nicole Meselsohn and Preston Muirhead
#As the player, you must collect and defeat shadows to beat Da Foe -
# - and save your village from the darkness

from gamelib import *

game = Game(800, 600, "smurf_game")

bk = Image("bk.jpg", game)
game.setBackground(bk)
bk.resizeTo(game.width, game.height)

t_s = Image("title_screen.jpg", game)
t_s.resizeTo(game.width, game.height)

squid = Animation("squida.png", 6, game, 996/3, 960/2)
squid.resizeBy(-60)
s_x = 100
s_y = 500
squid.moveTo(s_x, s_y)

shadow = Image("shadoww.png", game)
shadow.resizeBy(-60)
shadow.setSpeed(3, 90)
sh_x = 760
sh_y = 200
shadow.moveTo(sh_x, sh_y)

htp = Image("htpimage.png", game)
htp.moveTo(410, 430)
play = Image("playimage.png", game)
play.moveTo(150, 430)
story = Image("storyimage.png", game)
story.moveTo(670, 430)

htpscreen = Image("htpscreen.png", game)
htpscreen.resizeTo(game.width, game.height)
storyscreen = Image("storyscreen.png", game)
storyscreen.resizeTo(game.width, game.height)

bird = Animation("army.png", 21, game, 2010/5, 2240/5)
bird.resizeBy(-70)
bird.setSpeed(3, 90)
b_x = 760
b_y = 200
bird.moveTo(b_x, b_y)

ti = Image("toolimage.png", game)
ti.resizeTo(game.width, game.height)

t = Image("tools.png", game)
t.resizeBy(-70)
t.x = 50
t.y = 20
t.moveTo(t.x, t.y)

duck = Animation("duckie.png", 15, game, 2940/4, 3680/4)
duck.x = 500
duck.y = 370

duck.moveTo(duck.x, duck.y)
duck.setSpeed(4, 90)

invent = Image("inventory.png", game)
invent.resizeBy(-10)
invent.x = 730
invent.y = 20
invent.moveTo(invent.x, invent.y)

i_bk = Image("invent_bk.png", game)
i_bk.resizeTo(game.width, game.height)

f = Font(white, 45, black, "Bookman Old Style")

#Title screen
while not game.over:
    game.processInput()

    t_s.draw()
    game.drawText("SQUIDACUS...", 260, 240, f)
    game.drawText("Da Foe IS HERE!!!", 225, 290, f)
    htp.draw()
    play.draw()
    story.draw()

    duck.move()

    if duck.x <= 0:
        duck.x = 800

    htpscreen.draw()
    htpscreen.visible = False
    storyscreen.draw()
    storyscreen.visible = False
        
    if keys.Pressed[K_SPACE]:
        game.over = True

    if mouse.collidedWith(htp):
        htpscreen.visible = True
        
    if mouse.collidedWith(play) and mouse.LeftClick:
        game.over = True

    if mouse.collidedWith(story):        
        storyscreen.visible = True
        
    game.update(60)
game.over = False

#Level 1

while not game.over:
    game.processInput()

    bk.draw()  
    squid.move()
    squid.visible = True 
    shadow.move() 
    shadow.visible = True

    invent.draw()
    i_bk.draw()
    i_bk.visible = False 

    if mouse.collidedWith(invent):
        i_bk.visible = True 
        squid.visible = False
        shadow.visible = False
        
    duck.draw()
    duck.visible = False

    if shadow.x < 0:
        shadow.x = 800
        shadow.y = randint(100, 550)

    if keys.Pressed[K_DOWN]:
        squid.y += 3

    if keys.Pressed[K_UP]:
        squid.y -= 3

    if keys.Pressed[K_RIGHT]:
        squid.x += 3

    if keys.Pressed[K_LEFT]:
        squid.x -= 3

    if squid.collidedWith(shadow):
        game.over = True
           
    game.update(60)
game.over = False

#Level 1 Battle scene

selec = Image("selec.jfif", game)
selec.resizeBy(100)
selec.width = game.width
selec.x = game.width/ 2
selec.y = game.height - 130
ax = selec.x / 2.5
ay = selec.y / 1.3

dx = ax
dy = ay + 75

hx = ax
hy = ay + 150

dia = Image("dia.png", game)
dia.resizeBy(-93)
dia.x = ax - 30
dia.y = ay + 18

squidacus = Animation("squida.png", 6, game, 996/3, 960/2)
squidacus.x = game.width/4
squidacus.y = game.width/4 - 30
squidacus.resizeBy(-50)
squida_health = 100
squida_dmg = 10

minion = Image("shadow.png", game)
minion.x = game.width / 1.4
minion.y = game.width / 4 - 30
minion.resizeBy(-75)
mini_health = 30
mini_dmg = 15

sha_bol = Animation("bol.png", 29, game, 2500/5, 3000/6)
sha_bol.x = squidacus.x + 90
sha_bol.y = squidacus.y - 30
sha_bol.resizeBy(-91)
sha_bol.setSpeed(200, -90)

bkb = Image("bkb.png", game)
bkb.resizeBy(300)
#game.setBackground(bk)

gem = Image("gem.png", game)
gem.x = minion.x
gem.y = minion.y
gem.resizeBy(-50)

f = Font(white, 30, blue, "Bookman Old Style")
f2 = Font(white, 20, black, "Bookman Old Style")
f3 = Font(black, 30, black, "Bookman Old Style")

time = 10
time_a = 10
time_a2 = 0 # squida text time
time_t = 100 #monster turn
time_t2 = 0 #squida turn
time_t3 = -1 # miss time
time_t4 = -1
time_w = 301
time_mag = 5
turn = True

squida_miss = False 
#mini_miss = False

m_miss = 0
s_miss = 0

heal = False
heal_v = 15

attack = False

stun = False

defend = False

x = 0
y = 0

while not game.over:
    game.processInput()

    bkb.draw()
    selec.draw()
    selec.visible = True
    sha_bol.draw()
    sha_bol.visible = True
    gem.draw()
    gem.visible = False

    t.draw()
    t.visible = True
    ti.draw()
    ti.visible = False

    invent.draw()
    invent.visible = True
    i_bk.draw()
    i_bk.visible = False 

    squidacus.move()
    squidacus.visible = True
    minion.draw()
    minion.visible = True

    if mouse.collidedWith(t):
        ti.visible = True
        squidacus.visible = False
        minion.visible = False
        sha_bol.visible = False
        selec.visible = False
        invent.visible = False
        x = 2
    else:
        x = 0

    if mouse.collidedWith(invent):
        i_bk.visible = True
        squidacus.visible = False
        minion.visible = False
        sha_bol.visible = False
        selec.visible = False
        t.visible = False
        y = 2
    else:
        y = 0
  
    if (turn and time_mag > 0 and x != 2 and y != 2):
        game.drawText("ATTACK", ax, ay, f)
        game.drawText("MAGIC", dx, dy, f)
        game.drawText("HEAL", hx, hy, f)
    if (turn and time_mag == 0 and x != 2 and y != 2):
        game.drawText("CONFUSION", ax, ay, f)
        game.drawText("BACK", hx, hy, f)
    if (turn and x != 2 and y != 2):
        dia.draw()

    if x != 2 and y != 2: 
        game.drawText("Health: " + str(squida_health), game.width/5.5, game.height/2.05, f2)
        game.drawText("Health: " + str(mini_health), game.width/1.5, game.height/2.05, f2)

    #MOVING SELECTOR
    if (keys.Pressed[K_DOWN] and time == 0 and x != 2 and y != 2):
        dia.y += 75
        time = 10

    if (dia.y == ay + 243 and keys.Pressed[K_DOWN] and x != 2 and y != 2):
        dia.y = ay + 18

    if (keys.Pressed[K_UP] and time == 0 and x != 2 and y != 2):
        dia.y -= 75
        time = 8
        
    if (dia.y == ay - 57 and keys.Pressed[K_UP] and x != 2 and y != 2):
        dia.y = ay + 168


    if (time <= 0 and x != 2 and y != 2):
        time = 1

#decrement for time variables
    for i in range(1):   
        time -= 1
        time_a -= 1
        time_a2 -= 1
        time_t3 -= 1
        time_t4 -= 1
        #print("time_a = " + str(time_a))
        print("time_a2 = " + str(time_a2))
        print("time_t = " + str(time_t))
        #print("time_t2 = " + str(time_t2))
        #print(attack)
        #print("turn = " + str(turn))
        #print("squid miss = " + str(squida_miss))
        #print("time_t3 = " + str(time_t3))
                             
   # dia.draw()

#if the selector is on attack
    if (dia.y == ay + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag != 0):
        sha_bol.move() 
        time_a = 10
        time_t3 = 60
        turn = False
        s_miss = randint(1, 10)
        attack = True
        #print(s_miss)
        #print("rand: " + str(randint(1, 2)))
        print(attack)

    if (s_miss == 1):
        squida_miss = True
    else:
        squida_miss = False


#If squida misses:
    if (squida_miss == True and sha_bol.collidedWith(minion) and time_a == 0):
        sha_bol.x = squidacus.x + 90
        time_a2 = 121
        time_t2 += 150
        attack = True

#If squida hits
    if (sha_bol.collidedWith(minion) and time_a == 0 and squida_miss == False):
        sha_bol.x = squidacus.x + 90
        mini_health -= 10
        time_a2 = 60
        time_t2 += 150

#Text for miss
    if (time_t3 > 0 and squida_miss == True and attack == True and time_mag != 0 and stun == False):
        game.drawText("Oh no! You miss D:", game.width / 3, dy, f2)
        game.drawText("You do 0 damage, you suck", game.width / 3, dy + 20, f2)
        time_a2 = 0
#Text for hit
    if (time_a2 > 0 and squida_miss == False and attack == True and time_mag != 0 and mini_health != 0):
        game.drawText("You hit the shadow!", game.width / 3, dy, f2)
        game.drawText("You do " + str(squida_dmg) + " damage!", game.width / 3, dy + 20, f2)

#Heal
    if (dia.y == hy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and squida_health < 100 and attack == False):
        squida_health += heal_v
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 120
        turn = False
        print(heal)

    if (time_a2 > 0 and attack == False):
        game.drawText("You healed yourself", game.width / 3, dy, f2)
        game.drawText("You gain " + str(heal_v) + " health!", game.width / 3, dy + 20, f2)

#Magic
    if (dia.y == dy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0):
        time_mag = 0

    if (dia.y == hy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0):
        time_mag = 5

    if (dia.y == ay + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0):
        m_miss = randint(1, 2)
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 150
        turn = False
    print(m_miss)
    print(time_mag)

    if (time_t3 > 0 and time_mag == 0):
        game.drawText("You confuzzled the shadow. It now", game.width / 3, dy, f2)
        game.drawText("has a higher chance of missing", game.width / 3, dy + 20, f2)
        time_a2 = 0
    
#ensures the time variables stay at zero instead of going negative:
    if (time_a <= 0):
        time_a = 1

    if (time_a2 <= 0):
        time_a2 = 1

    if (time_t <= 0):
        time_t = 1

    if (time_t2 <= 0):
        time_t2 = 1  

    if (time_t3 <= 0):
        time_t3 = 1

    if (time_t4 <= 0):
        time_t4 = 1

    if (time_w <= 0):
        time_w = 1
        
#decrement for time specific to shadow
    if (turn == False and time_t <= 100):
        time_t -= 1
        time_t2 -= 1
    elif (turn == False or time_t > 100):
        time_t -= 1
        time_t2 -= 1

#shadow hits:
    if (turn == False and time_t == 1 and time_mag != 0):
            m_miss = randint(1, 10)
            #print("m_miss: " + str(m_miss))
            #print("mini_miss: " + str(mini_miss))

    if (turn == False and time_t == 1 and squida_health >= squida_health - 15 and mini_health != 0 and m_miss != 1):
        squida_health -= mini_dmg
        #print("m_miss2: " + str(m_miss))

    if (turn == False and time_t == 0 and m_miss == 1):
        game.drawText("The shadow misses, ", game.width / 3, dy, f2)
        game.drawText("You got lucky :)", game.width / 3, dy + 20, f2)
        time_mag = 5
        
    if (turn == False and time_t == 0 and mini_health != 0 and m_miss != 1):
        game.drawText("You got hit by a shadow ...", game.width / 3, dy, f2)
        game.drawText("You take " + str(mini_dmg) + " damage!", game.width / 3, dy + 20, f2)
        time_mag = 5
    
    if (time_t2 == 1):
        time_t = 101
        turn = True
        attack = False

    if (mini_health == 0):
        minion.visible = False

    if (mini_health == 0 and time_t == 0):
        time_w -= 1


    if (mini_health == 0 and time_w > 0 and time_t == 0):
         game.drawText("You defeated the shadow!", game.width / 3, dy, f2)
         game.drawText("You get a shadow fragment.", game.width / 3, dy + 20, f2)
         game.drawText("You gain a new spell: STUN!", game.width / 3, dy + 40, f2)
         gem.visible = True

    if (mini_health <= 0 and time_t2 <= 1):
        game.over = True

    if (squida_health <= 0 and time_t2 <= 1):
        game.over = True
    
    #if (dia.y == ay + 18 and time_a == 0):
     #   sha_bol.move()
            
    game.update(30)
game.over = False

#Level 2

y = 0

squid = Animation("squida.png", 6, game, 996/3, 960/2)
squid.resizeBy(-60)
s_x = 100
s_y = 500
squid.moveTo(s_x, s_y)

bird = Animation("army.png", 21, game, 2010/5, 2240/5)
bird.resizeBy(-70)
bird.setSpeed(3, 90)
b_x = 760
b_y = 200
bird.moveTo(b_x, b_y)

g_x = 300
g_y = 300
gem.moveTo(g_x, g_y)

while not game.over:
    game.processInput()

    bk.draw()  
    squid.move()
    squid.visible = True
    bird.move()
    bird.visible = True

    invent.draw()
    i_bk.draw()
    i_bk.visible = False
    
    gem.draw()
    gem.visible = False

    if mouse.collidedWith(invent):
        i_bk.visible = True
        squid.visible = False
        bird.visible = False
        gem.visible = True
        y = 2
    else:
        y = 0

    if bird.x < 0 and y != 2:
        bird.x = 800
        bird.y = randint(100, 550)

    if keys.Pressed[K_DOWN] and y != 2:
        squid.y += 3

    if keys.Pressed[K_UP] and y != 2:
        squid.y -= 3

    if keys.Pressed[K_RIGHT] and y != 2:
        squid.x += 3

    if keys.Pressed[K_LEFT] and y != 2:
        squid.x -= 3

    if squid.collidedWith(bird):
        game.over = True
           
    game.update(60)
game.over = False

#Level 2 Battle scene
selec = Image("selec.jfif", game)

selec.resizeBy(100)
selec.width = game.width
selec.x = game.width/ 2
selec.y = game.height - 130
ax = selec.x / 2.5
ay = selec.y / 1.3

dx = ax
dy = ay + 75

hx = ax
hy = ay + 150

dia = Image("dia.png", game)
dia.resizeBy(-93)
dia.x = ax - 30
dia.y = ay + 18

squidacus = Animation("squida.png", 6, game, 996/3, 960/2)
squidacus.x = game.width/4
squidacus.y = game.width/4 - 30
squidacus.resizeBy(-50)
squida_health = 100
squida_dmg = 10

minion = Image("shadow.png", game)
minion.x = game.width / 1.4
minion.y = game.width / 4 - 30
minion.resizeBy(-75)
mini_health = 30
mini_health_2 = 50
mini_dmg = 15

sha_bol = Animation("bol.png", 29, game, 2500/5, 3000/6)
sha_bol.x = squidacus.x + 90
sha_bol.y = squidacus.y - 30
sha_bol.resizeBy(-91)
sha_bol.setSpeed(200, -90)

bk = Image("bkb.png", game)
bk.resizeBy(300)
#game.setBackground(bk)

gem = Image("gem.png", game)
gem.x = minion.x
gem.y = minion.y
gem.resizeBy(-50)

f = Font(white, 30, blue, "Bookman Old Style")
f2 = Font(white, 20, black, "Bookman Old Style")
f3 = Font(white, 30, red, "Bookman Old Style")
f4 = Font(white, 30, green, "Bookman Old Style")

time = 10
time_a = 10
time_a2 = 0 # squida text time
time_t = 100 #monster turn
time_t2 = 0 #squida turn
time_t3 = -1 # miss time
time_t4 = -1
time_w = 301
time_mag = 5
time_menu_shift = 10
time_heal_back = 10
turn = True

squida_miss = False 
#mini_miss = False

m_miss = 0
s_miss = 0

heal = False
heal_v = 15

attack = False

magic = False

stun = False

stun_pp = 1

turn_count = 0

x = 0
y = 0

while not game.over:
    game.processInput()

    bk.draw()
    selec.draw()
    selec.visible = True
    sha_bol.draw()
    sha_bol.visible = True
    gem.draw()
    gem.visible = False

    t.draw()
    t.visible = True
    ti.draw()
    ti.visible = False

    gem.draw()
    gem.visible = False

    invent.draw()
    invent.visible = True
    i_bk.draw()
    i_bk.visible = False 

    squidacus.draw()
    squidacus.visible = True
    minion.draw()
    minion.visible = True

    if mouse.collidedWith(t):
        ti.visible = True
        squidacus.visible = False
        minion.visible = False
        sha_bol.visible = False
        selec.visible = False
        invent.visible = False
        x = 2
    else:
        x = 0

    if mouse.collidedWith(invent):
        i_bk.visible = True
        squidacus.visible = False
        minion.visible = False
        sha_bol.visible = False
        selec.visible = False
        t.visible = False
        gem.visible = True
        y = 2
    else:
        y = 0

    if (turn and time_mag == 5 and x != 2 and y != 2):
        game.drawText("ATTACK", ax, ay, f)
        game.drawText("MAGIC", dx, dy, f)
        game.drawText("HEAL", hx, hy, f)
    if (turn and time_mag == 0 and x != 2 and y != 2):
        game.drawText("CONFUSION", ax, ay, f3)
        game.drawText("STUN", dx, dy, f3)
        game.drawText("BACK", hx, hy, f4)
    if (turn and x != 2 and y != 2):
        dia.draw()

    if  x != 2 and y != 2:
        game.drawText("Health: " + str(squida_health), game.width/5.5, game.height/2.05, f2)
        game.drawText("Health: " + str(mini_health_2), game.width/1.5, game.height/2.05, f2)

    #MOVING SELECTOR
    if (keys.Pressed[K_DOWN] and time == 0):
        dia.y += 75
        time = 8
        
    if (keys.Pressed[K_UP] and time == 0):
        dia.y -= 75
        time = 8
        
    if (dia.y == ay - 57 and keys.Pressed[K_UP]):
        dia.y = ay + 168

    if (dia.y == ay + 243 and keys.Pressed[K_DOWN]):
        dia.y = ay + 18

    if (time <= 0):
        time = 1

    #print(dia.y)
    #print(dy + 18)

#decrement for time variables
    time -= 1
    time_a -= 1
    time_a2 -= 1
    time_t3 -= 1
    time_t4 -= 1
    time_menu_shift -= 1
    time_heal_back -= 1
    print(time_heal_back)
    print("time_a = " + str(time_a))
    #print("time_a2 = " + str(time_a2))
    #print("time_t = " + str(time_t))
    #print("time_t2 = " + str(time_t2))
    #print(attack)
    #print("turn = " + str(turn))
    #print("squid miss = " + str(squida_miss))
    #print("time_t3 = " + str(time_t3))
                             
   # dia.draw()

#if the selector is on attack
    if (dia.y == ay + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag != 0):
        sha_bol.move() 
        time_a = 10
        time_t3 = 60
        turn = False
        s_miss = randint(1, 10)
        attack = True
        #turn_count += 1
        time_a2 = 121
        #print(s_miss)
        #print("rand: " + str(randint(1, 2)))
    #print("attack: " + str(attack))

    if (s_miss == 1):
        squida_miss = True
    else:
        squida_miss = False

    #print(time_mag)
    
#If squida misses:
    if (squida_miss == True and sha_bol.collidedWith(minion) and time_a == 0):
        sha_bol.x = squidacus.x + 90
        time_t2 += 110
        attack = True

#If squida hits
    if (sha_bol.collidedWith(minion) and time_a == 0 and squida_miss == False):
        sha_bol.x = squidacus.x + 90
        mini_health_2 -= 10
        time_a2 = 60
        time_t2 += 110

#Text for miss
    if (time_t3 > 0 and squida_miss == True and attack == True and time_mag != 0 and stun == False):
        game.drawText("Oh no! You miss D:", game.width / 3, dy, f2)
        game.drawText("You do 0 damage, you suck", game.width / 3, dy + 20, f2)
        time_a2 = 0
#Text for hit
    if (time_a2 > 0 and squida_miss == False and attack == True and time_mag != 0 and mini_health_2 != 0):
        game.drawText("You hit the shadow!", game.width / 3, dy, f2)
        game.drawText("You do " + str(squida_dmg) + " damage!", game.width / 3, dy + 20, f2)

#Heal
    if (dia.y == hy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and squida_health < 100 and attack == False and time_mag == 5 and time_heal_back == 0):
        squida_health += heal_v
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 110
        turn = False
        #turn_count += 1
        #print(turn_count)
        heal = True
        time_heal_back = 10
        #print(heal)

    if (time_a2 > 0 and attack == False and heal == True):
        game.drawText("You healed yourself", game.width / 3, dy, f2)
        game.drawText("You gain " + str(heal_v) + " health!", game.width / 3, dy + 20, f2)

#Magic
        
    if (dia.y == dy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and turn and time_a2 == 0 and time_mag != 0):
        while (time_mag > 0):
            time_mag -= 1
        time_menu_shift = 10
    #print(time_menu_shift)
    #print(time_mag)
        
#Back:
    if (dia.y == hy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0 and time_heal_back == 0):
        time_mag = 5
        time_heal_back = 10
        
#confuzzle
    if (dia.y == ay + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0):
        m_miss = randint(1, 2)
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 110
        turn = False
    #print(m_miss)
    #print(time_mag)

    if (time_t3 > 0 and time_mag == 0 and stun == False):
        game.drawText("You confuzzled the shadow. It now", game.width / 3, dy, f2)
        game.drawText("has a higher chance of missing", game.width / 3, dy + 20, f2)
        time_a2 = 0

#STUN
    if (dia.y == dy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0 and time_menu_shift == 0 and stun_pp > 0):
        time_a = 10
        time_t3 = 100
        time_a2 = 60
        time_t2 += 110
        stun = True
        time_mag = 1
        turn = False

    if (dia.y == dy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0 and time_menu_shift == 0 and stun_pp == 0):
        game.drawText("You have already used stun!", game.width / 3, dy, f2)
        game.drawText("You have no more uses ...", game.width / 3, dy + 20, f2)
        
        
    if (stun_pp == 0 and stun and turn == False and time_t3 == 60):
        turn_count += 1

    print(turn_count)

    #if (stun_pp == 0 and stun and time_menu_shift == 0):
        #time_a = 10
        #time_t3 = 60
        #time_a2 = 60
        #time_t2 += 110
        #time_mag = 1

    if (time_t3 > 0 and time_mag == 1 and stun):
        game.drawText("You have stooned the shadow!", game.width / 3, dy, f2)
        game.drawText("It needs some time to recover (2 turns)", game.width / 3, dy + 20, f2)
        time_a2 = 0
        stun_pp = 0



    #if (time_t3 > 0 and time_mag == 0 and stun and stun_pp > 0):
     #   game.drawText("You have stooned the shadow!", game.width / 3, dy, f2)
      #  game.drawText("It needs some time to recover", game.width / 3, dy + 20, f2)
       # time_a2 = 0
    
#ensures the time variables stay at zero instead of going negative:
    if (time_a <= 0):
        time_a = 1

    if (time_a2 <= 0):
        time_a2 = 1

    if (time_t <= 0):
        time_t = 1
 
    if (time_t2 <= 0):
        time_t2 = 1

    if (time_t3 <= 0):
        time_t3 = 1
        
    if (time_t4 <= 0):
        time_t4 = 1

    if (time_w <= 0):
        time_w = 1

    if (time_menu_shift <= 0):
        time_menu_shift = 1
        
    if (time_heal_back <= 0):
        time_heal_back = 1
        
#decrement for time specific to shadow
    if (turn == False and time_t <= 100):
        time_t -= 1
        time_t2 -= 1
    elif (turn == False or time_t > 100):
        time_t -= 1
        time_t2 -= 1

    #if (turn == False and stun and time_t == 0):
     #   game.drawText("The shadow misses, ", game.width / 3, dy, f2)
      #  game.drawText("You got lucky :)", game.width / 3, dy + 20, f2)
       # time_mag = 5
       # turn == False
        

#shadow hits:
    if (turn == False and time_t == 1 and time_mag != 0):
        m_miss = randint(1, 10)
        #print("m_miss: " + str(m_miss))
        #print("mini_miss: " + str(mini_miss))

    if (turn == False and time_t == 1 and squida_health >= squida_health - 15 and mini_health != 0 and m_miss != 1 and stun):
        #turn = True
        #time_t = 100
        time_mag = 5
    elif (turn == False and time_t == 1 and squida_health >= squida_health - 15 and mini_health != 0 and m_miss != 1):
        squida_health -= mini_dmg
        #print("m_miss2: " + str(m_miss))

    if (turn == False and time_t < 31 and stun and turn_count > 1):
        game.drawText("The shadow is still stooned", game.width / 3, dy, f2)
        game.drawText("It needs another turn to recover", game.width / 3, dy + 20, f2)
        

    if (turn == False and time_t == 0 and m_miss == 1 and stun == False):
        game.drawText("The shadow misses, ", game.width / 3, dy, f2)
        game.drawText("You got lucky :)", game.width / 3, dy + 20, f2)
        time_mag = 5
        
    if (turn == False and time_t == 0 and mini_health_2 != 0 and m_miss != 1 and stun == False):
        game.drawText("You got hit by a shadow ...", game.width / 3, dy, f2)
        game.drawText("You take " + str(mini_dmg) + " damage!", game.width / 3, dy + 20, f2)
        time_mag = 5

    #if (turn == False and time_t == 0 and stun):
     #   time_t2 = 75

    if (time_t2 == 1 and turn == False):
        time_t = 101
        turn = True
        attack = False

    if (mini_health_2 == 0):
        minion.visible = False

    if (turn_count >= 2 and turn):
        stun = False

    if (mini_health_2 == 0 and time_t == 0):
        time_w -= 1

    #print(stun)
    #print(turn_count)
    #print("turn: " + str(turn))
    #print(time_mag)

    if (mini_health_2 == 0 and time_w > 0):
         game.drawText("You defeated the shadow!", game.width / 3, dy, f2)
         game.drawText("You get another shadow fragment.", game.width / 3, dy + 20, f2)
         gem.visible = True

    if (mini_health_2 <= 0 and time_t2 <= 1):
        game.over = True

    if (squida_health <= 0 and time_t2 <= 1):
        game.over = True
    
    #if (dia.y == ay + 18 and time_a == 0):
     #   sha_bol.move()
            
    game.update(30)
game.over = False

#Transition into boss level

tigger = Animation("tigger.png", 8, game, 476/4, 400/2)
tigger.setSpeed(3, 90)
tigger.resizeBy(-40)
t_x = 100
t_y = 100
tigger.moveTo(t_x, t_y)

DaFoe = Image("boss.png", game)
D_x = 400
D_y = 50
DaFoe.moveTo(D_x, D_y)
DaFoe.resizeBy(-60)

DF2 = Image("boss.png", game)
DF2.resizeBy(-40)
DF3 = Image("boss.png", game)
DF3.resizeBy(-15)
DF4 = Image("boss.png", game)
DF4.resizeBy(5)
DF5 = Image("boss.png", game)
DF5.resizeBy(30)
DF6 = Image("boss.png", game)
DF6.resizeBy(55)
DF7 = Image("boss.png", game)
DF7.resizeBy(80)

spirally = Animation("spirally.png", 30, game, 3200/5, 3840/6)
spirally.resizeTo(game.width, game.height)

h = 0

while not game.over:
    game.processInput()
    
    spirally.draw()
    spirally.visible = True

    DaFoe.draw()
    if h != 2:
        DaFoe.visible = True
        
    DF2.draw()
    if h != 2:
        DF2.visible = False
    DF2.y = DaFoe.y
    DF2.x = DaFoe.x
    
    DF3.draw()
    if h != 2:
        DF3.visible = False
    DF3.y = DF2.y
    DF3.x = DF2.x
    
    DF4.draw()
    if h != 2:
        DF4.visible = False
    DF4.y = DF3.y
    DF4.x = DF3.x
    
    DF5.draw()
    if h != 2:
        DF5.visible = False
    DF5.y = DF4.y
    DF5.x = DF4.x
    
    DF6.draw()
    if h != 2:
        DF6.visible = False
    DF6.y = DF5.y
    DF6.x = DF5.x

    DF7.draw()
    if h != 2:
        DF7.visible = False
    DF7.y = DF6.y
    DF7.x = DF6.x
    
    for times in range(10):
        DaFoe.y += .5
        
    if DaFoe.y >= 65 and DaFoe.y <= 85:
        DF2.visible = True
        DaFoe.visible = False
        h = 2
    if DaFoe.y >= 140 and DaFoe.y <= 160:
        DF3.visible = True
        DF2.visible = False
        DaFoe.visible = False
        h = 2
    if DaFoe.y >= 215 and DaFoe.y <= 235:
        DF4.visible = True
        DF3.visible = False
        DF2.visible = False
        DaFoe.visible = False
        h = 2
    if DaFoe.y >= 290 and DaFoe.y <= 310:
        DF5.visible = True
        DF4.visible = False
        DF3.visible = False
        DF2.visible = False
        DaFoe.visible = False
        h = 2
    if DaFoe.y >= 365 and DaFoe.y <= 385:
        DF6.visible = True
        DF5.visible = False
        DF4.visible = False
        DF3.visible = False
        DF2.visible = False
        DaFoe.visible = False
        h = 2
    if DaFoe.y >= 420 and DaFoe.y <= 440:
        DF7.visible = True
        DF6.visible = False
        DF5.visible = False
        DF4.visible = False
        DF3.visible = False
        DF2.visible = False
        DaFoe.visible = False
        h = 2

    if DF7.y > game.height + (DF7.height/2):
        game.over = True #fix this
    
    game.update(30)
game.over = False

#Level 3






                                                                                                                                                                                                                                                                                                                                                                                    
