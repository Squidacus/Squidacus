#Name Incorporated
#SQUIDACUS... DA FOE IS HERE!
#Nicole Meselsohn and Preston Muirhead
#As the player, you must collect and defeat shadows to beat Da Foe -
# - and save your village from the darkness

from gamelib import *

game = Game(800, 600, "map")

mapp = Image("mapp.png", game)
mapp.resizeBy(220)
mapp.y = -225

mapp1 = Image("mapp1.png", game)
mapp1.resizeBy(250) 
mapp2 = Image("mapp2.png", game)
mapp2.x = 406
mapp2.y = 315
mapp2.resizeBy(180)
mapp3 = Image("mapp3.png", game)
mapp3.resizeBy(200)

tds = Image("tdsquid.png", game) #SHIP
tds.resizeBy(-35)
tds.x = 400
tds.y = 300

s = Image("sab.png", game)
s.y = -220
s.resizeBy(-50)

s.y = tds.y + 200

time_z = 16 #manage the time so the ship can turn right
time_p = 16 #manage the time so the ship can turn left
rotate = 0 #manage the angles of the ship turning

while not game.over:
    game.processInput()

    mapp.draw()
    s.draw()

    if tds.y >= 200:
        s.y = -220

    if mapp.y <= -500:
        mapp.y = -500

    if mapp.y >= 1100:
        mapp.y = 1100

    if mapp.x <= 25:
        mapp.x = 25
        
    if mapp.x >= 787:
        mapp.x = 787

    time_z -= 1
    if time_z <= 0:
        time_z = 0

    time_p -= 1
    if time_p <= 0:
        time_p = 0

    if rotate < -3:
        rotate = 0

    if rotate > 3:
        rotate = 0
    
    tds.draw()
    #map goes down with ship
    if keys.Pressed[K_DOWN]:
        mapp.y -= 3
    #map goes up with ship
    if keys.Pressed[K_UP] and rotate == 0:
        mapp.y += 3
    #ship goes right when it faces right
    if keys.Pressed[K_RIGHT] and rotate == 1 or keys.Pressed[K_RIGHT] and rotate == -3:
        tds.x += 3
        mapp.x -= 3
    #ship was supposed to move to the right when right button is pressed
    if keys.Pressed[K_RIGHT] and time_z == 0:
        time_z = 16
    #ship turns to the right
    if keys.Pressed[K_RIGHT] and time_z == 15 and rotate != 1 and rotate != -3:
        #tds.x += 3
        tds.rotateBy(90)
        rotate += 1
    #ship was supposed to move to the right
    if keys.Pressed[K_RIGHT] and time_z == 15 and rotate == 1:
        tds.x += 3
    print(rotate)
    #ship was supposed to move when it is turned left
    if keys.Pressed[K_LEFT] and time_p == 0:
        time_p = 16
    #ship rotates left
    if keys.Pressed[K_LEFT] and time_p == 15 and rotate != -1 and rotate != 3:
        #tds.x -= 3
        tds.rotateBy(-90)
        rotate -= 1
    if keys.Pressed[K_LEFT] and rotate == -1 or keys.Pressed[K_LEFT] and rotate == 3:
        tds.x -= 3
        mapp.x += 3

    if mapp.y >= 1044:
        game.over = True

    game.update(60)
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

#DaFoe Boss level

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
squida_dmg_b = 15
heal_pp = 3

minion = Image("shadow.png", game)
minion.x = game.width / 1.4
minion.y = game.width / 4 - 30
minion.resizeBy(-75)
mini_health = 30
mini_health_2 = 50
mini_dmg = 15

sha_bol = Animation("bol.png", 30, game, 2500/5, 3000/6)
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

#DA FOE:
boss = Image("boss.png", game)
boss.x = minion.x + 15
boss.y = minion.y
#boss.resizeBy(-75)
boss_health = 100
boss_dmg = 20
boss_choice = 0
boss_heal = 0
boss_attack = True
boss_heal_v = 20
b_heal = False

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

confuzzle = False

confuzzle_count = 0



#BOSS D: 

while not game.over:
    game.processInput()

    bk.draw()
    selec.draw()
    sha_bol.draw()
    gem.draw()
    gem.visible = False

    squidacus.draw()
    boss.draw()

    if (turn and time_mag == 5):
        game.drawText("ATTACK", ax, ay, f)
        game.drawText("MAGIC", dx, dy, f)
        game.drawText("HEAL", hx, hy, f)
    if (turn and time_mag == 0):
        game.drawText("CONFUSION", ax, ay, f3)
        game.drawText("STUN", dx, dy, f3)
        game.drawText("BACK", hx, hy, f4)
    if (turn):
        dia.draw()

    game.drawText("Health: " + str(squida_health), game.width/5.5, game.height/2.05, f2)
    game.drawText("Health: " + str(boss_health), game.width/1.5, game.height/2.05, f2)

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
    #print(time_heal_back)
    #print("time_a = " + str(time_a))
    #print("time_a2 = " + str(time_a2))
    #print("time_t = " + str(time_t))
    #print("time_t2 = " + str(time_t2))
    #print(attack)
    #print("turn = " + str(turn))
    #print("squid miss = " + str(squida_miss))
   # print("time_t3 = " + str(time_t3))
                             
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
        time_a2 = 191
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
        boss_health -= squida_dmg_b
        time_a2 = 60
        time_t2 += 150

#Text for miss
    if (time_t3 > 0 and squida_miss == True and attack == True and time_mag != 0 and stun == False):
        game.drawText("Oh no! You miss D:", game.width / 3, dy, f2)
        game.drawText("You do 0 damage, you suck", game.width / 3, dy + 20, f2)
        time_a2 = 0
#Text for hit
    if (time_a2 > 0 and squida_miss == False and attack == True and time_mag != 0 and boss_health != 0):
        game.drawText("You hit the Da Foe OMG!", game.width / 3, dy, f2)
        game.drawText("You do " + str(squida_dmg_b) + " damage!", game.width / 3, dy + 20, f2)

#Heal
    if (dia.y == hy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and squida_health < 100 and attack == False and time_mag == 5 and time_heal_back == 0 and heal_pp > 0):
        squida_health += heal_v
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 150
        turn = False
        #turn_count += 1
        #print(turn_count)
        heal = True
        time_heal_back = 10
        heal_pp -= 1
    #print(heal_pp)
    if (time_a2 > 0 and attack == False and heal == True and heal_pp > 0):
        game.drawText("You healed yourself", game.width / 3, dy, f2)
        game.drawText("You gain " + str(heal_v) + " health!", game.width / 3, dy + 20, f2)

    if (dia.y == hy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and squida_health < 100 and attack == False and time_mag == 5 and time_heal_back == 0 and heal_pp <= 0):
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 150
        turn == False
        heal == True
    if (time_a2 > 0 and attack == False and heal == True and heal_pp <= 0):
        game.drawText("You ran out of heal uses,", game.width / 3, dy, f2)
        game.drawText("You gain no health ...", game.width / 3, dy + 20, f2)
    if (time_a2 == 0 and attack == False and heal == True and heal_pp <= 0):
        turn == True


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
        #m_miss = randint(1, 2)
        time_a = 10
        time_t3 = 60
        time_a2 = 60
        time_t2 += 150
        turn = False
        confuzzle = True
    #print(m_miss)
    #print(time_mag)

    if (time_t3 > 0 and time_mag == 0 and stun == False):
        game.drawText("You confuzzled Da Foe! he now", game.width / 3, dy, f2)
        game.drawText("has a higher chance of missing", game.width / 3, dy + 20, f2)
        time_a2 = 0

    if (confuzzle and turn == False and time_t3 == 59 and confuzzle_count < 3):
        m_miss = randint(1, 2)
        confuzzle_count += 1
        print(m_miss)
    

#STUN
    if (dia.y == dy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0 and time_menu_shift == 0 and stun_pp > 0):
        time_a = 10
        time_t3 = 100
        time_a2 = 60
        time_t2 += 150
        stun = True
        time_mag = 1
        turn = False

    if (dia.y == dy + 18 and keys.Pressed[K_SPACE] and time_a == 0 and sha_bol.x == squidacus.x + 90 and turn and time_a2 == 0 and time_mag == 0 and time_menu_shift == 0 and stun_pp == 0):
        game.drawText("You have already used stun!", game.width / 3, dy, f2)
        game.drawText("You have no more uses ...", game.width / 3, dy + 20, f2)
        
        
    if (stun_pp == 0 and stun and turn == False and time_t3 == 60):
        turn_count += 1

    #print(turn_count)

    #if (stun_pp == 0 and stun and time_menu_shift == 0):
        #time_a = 10
        #time_t3 = 60
        #time_a2 = 60
        #time_t2 += 110
        #time_mag = 1

    if (time_t3 > 0 and time_mag == 1 and stun):
        game.drawText("You have stooned Da Foe OMG!", game.width / 3, dy, f2)
        game.drawText("he needs some time to recover (2 turns)", game.width / 3, dy + 20, f2)
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
        

#DA FOE hits:
    #if (turn == False and time_t == 1 and time_mag != 0):
    if (turn == False and time_t == 1 and confuzzle == False):
        m_miss = randint(1, 10)
        #print("m_miss: " + str(m_miss))
        #print("mini_miss: " + str(mini_miss))

    if (turn == False and time_t == 1 and squida_health >= squida_health - 15 and boss_health != 0 and m_miss != 1 and stun):
        turn = True
        time_t = 100
        time_mag = 5
    elif (turn == False and time_t == 1 and squida_health >= squida_health - 15 and boss_health != 0 and m_miss != 1 and boss_health != 40):
        squida_health -= boss_dmg
        #print("m_miss2: " + str(m_miss))

    if (turn == False and time_t < 33 and stun and turn_count > 1 and b_heal == False):
        game.drawText("The Da mighty Foe is still stooned,", game.width / 3, dy, f2)
        game.drawText("he needs another turn to recover", game.width / 3, dy + 20, f2)

#DA FOE SELF HEAL     
    if (turn == False and time_t == 1 and boss_health != 0 and boss_health <= 40 and boss_heal == 0):
        boss_health += boss_heal_v
        b_heal = True
        boss_heal = 1
    #print("turn: " + str(turn))
    #print("time_t: " + str(time_t))
    #print("boss_health: " + str(boss_health))
    #print("boss_heal: " + str(boss_heal))

    if (turn == False and time_t == 0 and stun == False and b_heal == True):
        game.drawText("OH SH!*, Da freaking Foe healed himself!", game.width / 4, dy, f2)
        game.drawText("He regains " + str(boss_heal_v) + " health" , game.width / 4, dy + 20, f2)

    #print(boss_heal)

    #if (turn == False and time_t2 == 1 and stun == False and b_heal == True):
        #boss_heal = 0


    #if (turn == False and time_t2 == 0 and boss_heal == 1):
        #boss_heal = 0

#DA FOE hit or missing
    if (turn == False and time_t == 0 and m_miss == 1 and stun == False and b_heal == False and confuzzle != 3):
        game.drawText("Da Foe misses, (somehow) ", game.width / 3, dy, f2)
        game.drawText("You got lucky :)", game.width / 3, dy + 20, f2)
        time_mag = 5

    if (turn == False and time_t == 0 and m_miss == 1 and stun == False and b_heal == False and confuzzle == 3):
        game.drawText("Da Foe misses, (somehow) ", game.width / 3, dy, f2)
        game.drawText("You got lucky :)", game.width / 3, dy + 20, f2)
        game.drawText("Da Foe is no longer confuzzled", game.width / 3, dy + 40, f2)       
        time_mag = 5
    #print("time_t: " + str(time_t))
    #print("stun: " + str(stun))
    #print("turn: " + str(turn))
    #print("m_miss: " + str(m_miss))
    #print("boss_heal: " + str(boss_heal))
        
    if (turn == False and time_t == 0 and boss_health != 0 and m_miss != 1 and stun == False and b_heal == False and confuzzle_count != 3):
        game.drawText("You got hit by Da Foe oh no!", game.width / 3, dy, f2)
        game.drawText("You take " + str(boss_dmg) + " damage!", game.width / 3, dy + 20, f2)
        time_mag = 5

    if (turn == False and time_t == 0 and boss_health != 0 and m_miss != 1 and stun == False and b_heal == False and confuzzle_count == 3):
        game.drawText("You got hit by Da Foe oh no!", game.width / 3, dy, f2)
        game.drawText("You take " + str(boss_dmg) + " damage!", game.width / 3, dy + 20, f2)
        game.drawText("Da Foe is no longer confuzzled", game.width / 3, dy + 40, f2) 
        time_mag = 5        

    #if (turn == False and time_t == 0 and stun):
     #   time_t2 = 75

    if (time_t2 == 1 and turn == False):
        time_t = 101
        turn = True
        attack = False
        b_heal = False

    #if (time_t2 == 1 and turn == False and confuzzle):
        #confuzzle_count += 1

    if (confuzzle_count == 3 and turn == False and confuzzle and time_t == 0):
        confuzzle_count = 0
        confuzzle = False
    print(confuzzle_count)

    #print(confuzzle_count)

    #print(b_heal)

    if (boss_health == 0):
        boss.visible = False

    if (boss_health <= 0):
        boss_health = 0

    if (turn_count >= 2 and turn):
        stun = False

    if (boss_health == 0 and time_t == 0):
        time_w -= 1

    #print(stun)
    #print(turn_count)
    #print("turn: " + str(turn))
    #print(time_mag)

    if (boss_health == 0 and time_w > 0):
         game.drawText("You defeated Da one and only Foe", game.width / 4, dy, f2)
         game.drawText("You have saved your lands from impending doom!", game.width / 4, dy + 20, f2)

    if (boss_health <= 0 and time_t2 <= 1):
        game.over = True

    if (squida_health <= 0 and time_t2 <= 1):
        game.over = True


    
    #if (dia.y == ay + 18 and time_a == 0):
     #   sha_bol.move()
            
    game.update(30)

game.quit()
