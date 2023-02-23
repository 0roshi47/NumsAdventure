from kandinsky import *
from time import *
from ion import *

"""
Ce jeu a été développé par moi mais le concept a été crée par un ami. Nous sommes une équipe de jeune concepteur de jeu vidéo qui ont pour but de progresser dans le milleu.
This game was developed by me but the concept was created by a friend. We are a team of young video game designers who aim to progress in the industry.

Coding : Oroshi #3802
Game Design : Aheeee #6562
"""

class Game:

    def __init__(self):
        self.running = True
        self.gameOver = False
        self.endScreen = False
        self.level = 1
        self.time = 0

    def game_over(self):
        self.running = False
        game.gameOver = True
        fill_rect(0, 0, 320, 222, 'white')
        draw_string("Game Over", 115, 90)
        draw_string('Press "OK" to play again', 45, 120)

    def end_screen(self):
        self.running = False
        self.endScreen = True
        fill_rect(0, 0, 320, 222, 'white')
        draw_string("Thank you for playing !!!", 35, 75)

    def timing(self):
        self.time += 0.02
        draw_string(str(round(self.time, 2)), 250, 201, 'black', 'grey')

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isOnLadder = False
        self.velocity = 2

    def move_right(self):
        self.x += self.velocity
        fill_rect(player.x, player.y, -2, 20, 'white')
        fill_rect(player.x, player.y, 20, 20, 'blue')

    def move_left(self):
        self.x -= self.velocity
        fill_rect(self.x + 20, self.y, 2, 20, 'white')
        fill_rect(self.x, self.y, 20, 20, 'blue')

    def move_up(self):
        self.y -= self.velocity
        fill_rect(self.x, self.y + 20, 20, 2, 'white')
        fill_rect(self.x, self.y, 20, 20, 'blue')

    def move_down(self):
        self.y += self.velocity
        fill_rect(self.x, self.y, 20, -2, 'white')
        fill_rect(self.x, self.y, 20, 20, 'blue')

class Ladder():

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

class Zombies:

    def __init__(self, x, y, isAlive, direction):
        self.x = x
        self.y = y
        self.isAlive = isAlive
        self.direction = direction
        self.velocity = 1

    def move_right(self):
        self.x += self.velocity
        fill_rect(self.x, self.y, -2, 20, 'white')
        fill_rect(self.x, self.y, 20, 20, 'red')
        if self.x + 20 >= 320:
            self.direction = "left"

    def move_left(self):
        self.x -= self.velocity
        fill_rect(self.x + 20, self.y, 2, 20, 'white')
        fill_rect(self.x, self.y, 20, 20, 'red')
        if self.x <= 0:
            self.direction = "right"

    def main(self):
        if self.direction == "right":
            self.move_right()
        else:
            self.move_left()

class Spiders:

    def __init__(self, x, y, isAlive, isFalling):
        self.x = x
        self.y = y
        self.isAlive = isAlive
        self.isFalling = isFalling
        self.pointToReach = self.y + 52
        self.velocity = 3
    
    def searching_player(self):
        if self.isFalling == False and self.isAlive == True:
            global player
            if (self.x <= player.x <= self.x + 30 or self.x <= player.x + 20 <= self.x + 30) and (self.y <= player.y <= self.y + 52):
                self.isFalling = True

    def spider_attack(self):
        self.y += self.velocity
        if self.y + 10 >= self.pointToReach:
            fill_rect(self.x, self.y + 15, 30, -20, 'white')
            self.isFalling = False
            self.x = -50
            self.isAlive = False
            return None
        fill_rect(self.x, self.y, 30, -8, 'white')
        fill_rect(self.x, self.y, 30, 15, 'red')

    def main(self):
        if self.isFalling:
            self.spider_attack()
        else:
            self.searching_player()
        fill_rect(self.x, self.y, 30, 15, 'red')

class BloodyPlatform:

    def __init__(self, x, y, isAlive,direction):
        self.x = x
        self.y = y
        self.isAlive = isAlive
        self.direction = direction
        self.cd = -50

    def move_up(self):
        if self.y == 182:
            fill_rect(self.x, self.y, 40, 15, 'white')
            self.y = 140
            fill_rect(self.x, self.y, 40, 15, 'red')
        elif self.y == 140:
            fill_rect(self.x, self.y, 40, 15, 'white')
            self.y = 88
            fill_rect(self.x, self.y, 40, 15, 'red')
        elif self.y == 88:
            fill_rect(self.x, self.y, 40, 15, 'white')
            self.y = 36
            fill_rect(self.x, self.y, 40, 15, 'red')
        else:
            self.direction = "bot"
            return None
        self.cd = -50

    def move_down(self):
        if self.y == 36:
            fill_rect(self.x, self.y, 40, 15, 'white')
            self.y = 88
            fill_rect(self.x, self.y, 40, 15, 'red')
        elif self.y == 88:
            fill_rect(self.x, self.y, 40, 15, 'white')
            self.y = 140
            fill_rect(self.x, self.y, 40, 15, 'red')
        elif self.y == 140:
            fill_rect(self.x, self.y, 40, 15, 'white')
            self.y = 182
            fill_rect(self.x, self.y, 40, 15, 'red')
        else:
            self.direction = "top"
        self.cd = -50
    
    def main(self):
        self.cd += 0.75
        if self.cd > 0:
            if self.direction == "top":
                self.move_up()
            else:
                self.move_down()
        fill_rect(self.x, self.y, 40, 15, 'red')

class Knight:

    def __init__(self, x, y, isAlive):
        self.x = x
        self.y = y
        self.isAlive = isAlive
        self.velociy = 3
        self.rangeSearching = 125
        self.dashCount = 0
        self.isDashing = False
        self.directionDash = "left"
        self.cd = 0

    def searching_player(self):
        global player
        if self.y + 30 > player.y > self.y:
            if self.x - self.rangeSearching <= player.x <= self.x:
                self.isDashing = True
                self.directionDash = "left"
            elif self.x + self.rangeSearching >= player.x >= self.x:
                self.isDashing = True
                self.directionDash = "right"

    def move_right(self):
        if self.dashCount <= 16:
            self.x += self.velociy
            fill_rect(self.x, self.y, -3, 30 ,'white')
            fill_rect(self.x, self.y, 15, 30,'red')
            self.dashCount += 1
        else:
            self.cd = 75
            self.isDashing = False

    def move_left(self):
        if self.dashCount <= 16:
            self.x -= self.velociy
            fill_rect(self.x + 15, self.y, 3, 30,'white')
            fill_rect(self.x, self.y, 15, 30,'red')
            self.dashCount += 1
        else:
            self.cd = 75
            self.isDashing = False

    def main(self):
        if self.cd > 0:
            self.cd -= 1
        elif self.cd == 0:
            self.dashCount = 0
            self.cd = -1
        else:
            if self.isDashing:
                if self.directionDash == "left":
                    self.move_left()
                else:
                    self.move_right()
            else:
                self.searching_player()
        fill_rect(self.x, self.y, 15, 30, 'red')

class Skeletons:

    def __init__(self, x, y, isAlive, direction):
        self.x = x
        self.y = y
        self.isAlive = isAlive
        self.direction = direction
        self.velocity = 2

    def searching(self):
        if self.y == player.y:
            if self.x > player.x:
                self.direction = "left"
            else:
                self.direction = "right"
        
    def move_right(self):
        self.x += self.velocity
        fill_rect(self.x, self.y, 20, 20, 'red')
        fill_rect(self.x, self.y, -self.velocity, 20, 'white')
        if self.x >= 300:
            self.direction = "left"
    
    def move_left(self):
        self.x -= self.velocity
        fill_rect(self.x, self.y, 20, 20, 'red')
        fill_rect(self.x + 20, self.y, self.velocity, 20, 'white')
        if self.x <= 0:
            self.direction = "right"
    
    def main(self):
        self.searching()
        if self.direction == "left":
            self.move_left()
        else:
            self.move_right()
        fill_rect(self.x, self.y, 20, 20, 'red')

class Canons:

    def __init__(self, x, y, isAlive, direction):
        self.x = x
        self.y = y
        self.isAlive = isAlive
        self.direction = direction
        self.isShooting = False
        self.bullet = 0
        self.velocity = 2
        self.cd = 25

    def shooting(self):
        if self.isShooting:
            if self.direction == "right":
                self.bullet[0] += self.velocity
                fill_rect(self.bullet[0], self.bullet[1], 14, 7, 'red')
                fill_rect(self.bullet[0], self.bullet[1], -self.velocity, 7, 'white')
                if self.bullet[0] >= 320:
                    self.isShooting = False
            else:
                self.bullet[0] -= self.velocity
                fill_rect(self.bullet[0], self.bullet[1], 14, 7, 'red')
                fill_rect(self.bullet[0] + 14, self.bullet[1], self.velocity, 7, 'white')
                if self.bullet[0] + 14 <= 0:
                    self.isShooting = False
        else:
            if self.cd > 0:
                self.cd -= 1
            else:
                if self.direction == "right":
                    self.bullet = [self.x + 26, self.y + 4]
                    self.isShooting = True
                    self.cd = 25
                else:
                    self.bullet = [self.x -6, self.y + 4]
                    self.isShooting = True
                    self.cd = 25

    def main(self):
        self.shooting()
        if self.direction == "right":
            fill_rect(self.x, self.y, 20, 25, 'red')
            fill_rect(self.x + 20, self.y + 3, 6, 9, 'red')
        else:
            fill_rect(self.x, self.y, 20, 25, 'red')
            fill_rect(self.x, self.y + 3, -6, 9, 'red')

def climbingUp(z, y):

    if (y.x <= z.x <= y.x + 20 or y.x <= z.x + 20 <= y.x + 20) and (y.y >= z.y + 20 > y.y - y.size):
        z.move_up()

def climbingDown(z, y):
    if (y.x <= z.x <= y.x + 20 or y.x <= z.x + 20 <= y.x + 20) and (y.y > z.y + 20 >= y.y - y.size):
        z.move_down()

def ladderChecking(z, y):

    for i in range(len(y)):
        if (y[i].x <= z.x <= y[i].x + 20 or y[i].x <= z.x + 20 <= y[i].x + 20) and (y[i].y - 2 >= z.y + 20 > y[i].y - y[i].size):
            return True

while True:

    game = Game()
    
    ladders = []
    ladders.append(Ladder(200, 197, 42))
    ladders.append(Ladder(40, 155, 52))
    ladders.append(Ladder(200, 103, 52))
    for i in range(3):
        ladders.append(Ladder(-50, 0, 52))

    door = [25, 51]

    player = Player(270, 177)

    zombies = []
    zombies.append(Zombies(10, 135, True, "right"))
    zombies.append(Zombies(220, 31, True, "left"))
    zombies.append(Zombies(-50, 0, False, "left"))
    zombies.append(Zombies(-50, 0, False, "left"))

    spiders = []
    for i in range(5):
        spiders.append(Spiders(-50, 0, False, False))

    bloodyPlatforms = []
    bloodyPlatforms.append(BloodyPlatform(-50, 0, False, "top"))
    bloodyPlatforms.append(BloodyPlatform(-50, 0, False, "top"))

    knights = []
    knights.append(Knight(-50, 103, False))
    knights.append(Knight(-50, 103, False))

    skeletons = []
    skeletons.append(Skeletons(-50, 0, False, "left"))
    skeletons.append(Skeletons(-50, 0, False, "left"))

    canons = []
    canons.append(Canons(-50, 130, False, "right"))
    canons.append(Canons(-50, 26, False, "left"))

    fill_rect(0, 0, 320, 222, 'white')
    fill_rect(0, 222, 320, -25, 'grey')

    sleep(0.1)

    while game.running:

        sleep(0.015)

        fill_rect(0, 160, 320, -5, 'grey')
        fill_rect(ladders[0].x, ladders[0].y, 20, -ladders[0].size, 'purple')
        fill_rect(0, 108, 320, -5, 'grey')
        fill_rect(ladders[1].x, ladders[1].y, 20, -ladders[1].size, 'purple')
        fill_rect(0, 56, 320, -5, 'grey')
        fill_rect(ladders[2].x, ladders[2].y, 20, -ladders[2].size, 'purple')
        for i in range(3, 6, 1):
            fill_rect(ladders[i].x, ladders[i].y, 20, -ladders[i].size, 'purple')

        fill_rect(door[0], door[1], 20, -30, 'green')

        fill_rect(player.x, player.y, 20, 20, 'blue')

        for i in range(len(zombies)):
            if zombies[i].isAlive:
                zombies[i].main()
        
        for i in range(len(spiders)):
            if spiders[i].isAlive:
                spiders[i].main()

        for i in range(len(bloodyPlatforms)):
            if bloodyPlatforms[i].isAlive:
                bloodyPlatforms[i].main()

        for i in range(len(knights)):
            if knights[i].isAlive:
                knights[i].main()
        
        for i in range(len(skeletons)):
            if skeletons[i].isAlive:
                skeletons[i].main()

        for i in range(len(canons)):
            if canons[i].isAlive:
                canons[i].main()
        
        if game.level == 1:
            draw_string("1-Hi World", 5, 201, "black", 'grey')
        elif game.level == 2:
            draw_string("2-Spider Gang", 5, 201, "black", 'grey')
        elif game.level == 3:
            draw_string("3-The Bridge", 5, 201, "black", 'grey')
        elif game.level == 4:
            draw_string("4-Frozen Cave", 5, 201, "black", 'grey')
        elif game.level == 5:
            draw_string("5-Caïn Tunnel", 5, 201, "black", 'grey')
        elif game.level == 6:
            draw_string("6-The djinn Cloud", 5, 201, "black", 'grey')
        elif game.level == 7:
            draw_string("7-Midnight Climax", 5, 201, "black", 'grey')
        elif game.level == 8:
            draw_string("8-Fuskegee Limbo", 5, 201, "black", 'grey')
        else:
            draw_string("9-Storm In Hell", 5, 201, "red", 'grey')

        game.timing()

        if keydown(KEY_LEFT) and player.isOnLadder == False:
            player.move_left()

            if player.x < 0:
                fill_rect(player.x, player.y, 20, 20, 'white')
                player.x = 300
                fill_rect(player.x, player.y, 20, 20, 'blue')

        elif keydown(KEY_RIGHT) and player.isOnLadder == False:
            player.move_right()

            if player.x + 20 > 320:
                fill_rect(player.x, player.y, 20, 20, 'white')
                player.x = 0
                fill_rect(player.x, player.y, 20, 20, 'blue')

        #climbing
        if keydown(KEY_UP):
            for i in range(len(ladders)):
                climbingUp(player, ladders[i])

        elif keydown(KEY_DOWN):
            for i in range(len(ladders)):
                climbingDown(player, ladders[i])

        if keydown(KEY_BACKSPACE):
            quit()

        if ladderChecking(player, ladders):
            player.isOnLadder = True
        else:
            player.isOnLadder = False

        if ((door[0] < player.x < door[0] + 20 or door[0] < player.x + 20 < door[0] + 20) and (player.y + 20 == door[1])) or keydown(KEY_SHIFT):
            game.level += 1
            fill_rect(0, 0, 320, 222, 'white')
            fill_rect(0, 222, 320, -25, 'grey')
            #sleep(0.015)
            sleep(0.1)
            if game.level == 2:

                player = Player(25, 177)

                ladders[0].x = 100
                ladders[1].x = 25
                ladders[2].x = 170

                door[0] = 285

                zombies[1].isAlive = False
                zombies[1].x = -50

                zombies[0] = Zombies(240, 83, True, "left")

                spiders[0] = Spiders(95, 108, True, False)
                spiders[1] = Spiders(165, 0, True, False)

            elif game.level == 3:

                player = Player(25, 177)

                ladders[0].x = 160
                ladders[1].x = 45
                ladders[2].x = 250

                door[0] = 20

                zombies[0] = Zombies(115, 31, True, "right")

                spiders[0] = Spiders(145, 108, True,  False)
                spiders[1] = Spiders(-50, 108, False, False)

                bloodyPlatforms[0] = BloodyPlatform(250, 182, True, "top")

            elif game.level == 4:
                
                player = Player(275, 177)

                ladders[0].x = 75
                ladders[1].x = 270
                ladders[2].x = 100
                
                door[0] = 145
                
                zombies[0] = Zombies(145, 83, True, "left")
                zombies[1] = Zombies(115, 31, True, "right")

                spiders[0] = Spiders(-50, 108, False,  False)
                spiders[1] = Spiders(-50, 108, False, False)

                bloodyPlatforms[0] = BloodyPlatform(-50, 182, False, "top")

                knights[0] = Knight(175, 125, True)
                knights[1] = Knight(180, 21, True)

            elif game.level == 5:

                player = Player(25, 177)
                
                ladders[0].x = 165
                ladders[1].x = 45
                ladders[2].x = 260

                door[0] = 40

                zombies[0] = Zombies(70, 83, True, "right")
                zombies[1] = Zombies(-50, 0, False, "left")

                spiders[0] = Spiders(225, 56, True, False)
                spiders[1] = Spiders(285, 56, True, False)
                spiders[2] = Spiders(255, 0, True, False)

                bloodyPlatforms[0] = BloodyPlatform(250, 182, True, "top")
                bloodyPlatforms[1] = BloodyPlatform(35, 140, True, "top")

                knights[0] = Knight(-50, 125, False)
                knights[1] = Knight(-50, 21, False)
            elif game.level == 6:

                player = Player(25, 177)

                ladders[0].x = 170
                ladders[1].x = 45
                ladders[2].x = 150

                door[0] = 265

                zombies[0] = Zombies(230, 31, True, "right")

                spiders[0] = Spiders(145, 51, True, False)
                spiders[1] = Spiders(285, 0, True, False)
                spiders[2] = Spiders(-50, 0, False, False)

                bloodyPlatforms[0] = BloodyPlatform(225, 182, True, "top")
                bloodyPlatforms[1] = BloodyPlatform(-50, 140, False, "top")

                skeletons[0] = Skeletons(5, 135, True, "right")
                skeletons[1] = Skeletons(190, 31, True, "left")
            elif game.level == 7:

                player = Player(20, 177)

                ladders[0].x = 50
                ladders[1].x = 160
                ladders[2].x = 40

                door[0] = 265

                zombies[0] = Zombies(260, 177, True, "left")
                zombies[1] = Zombies(235, 31, True, "right")

                spiders[0] = Spiders(45, 108, True, False)
                spiders[1] = Spiders(240, 56, True, False)

                bloodyPlatforms[0] = BloodyPlatform(-50, 182, False, "top")

                knights[0] = Knight(15, 73, True)

                skeletons[0] = Skeletons(-50, 135, False, "right")
                skeletons[1] = Skeletons(-50, 31, False, "left")

                canons[0] = Canons(10, 130, True, "right")
                canons[1] = Canons(235, 26, True, "left")
            elif game.level == 8:

                player = Player(20, 31)

                ladders[0].x = 250
                ladders[1].x = 20
                ladders[2].x = 290

                door = [60, 197]

                zombies[0] = Zombies(120, 135, True, "left")
                zombies[1] = Zombies(-50, 31, False, "right")

                spiders[0] = Spiders(285, 0, True, False)
                spiders[1] = Spiders(245, 0, True, False)
                spiders[2] = Spiders(15, 56, True, False)
                spiders[3] = Spiders(215, 108, True, False)
                spiders[4] = Spiders(250, 108, True, False)

                bloodyPlatforms[0] = BloodyPlatform(230, 140, True, "top")
                bloodyPlatforms[1] = BloodyPlatform(50, 182, True, "top")

                knights[0] = Knight(15, 167, True)

                skeletons[0] = Skeletons(200, 83, True, "left")

                canons[0] = Canons(60, 26, True, "right")
                canons[1] = Canons(-50, 0, False, "left")
            elif game.level == 9:

                door = [35, 51]

                player.x, player.y = 275, 135

                ladders[0].x = 285
                ladders[3].x, ladders[3].y, ladders[3].size = 150, 197, 42
                ladders[4].x, ladders[4].y, ladders[4].size = 15, 197, 42

                ladders[1].x = 30

                ladders[5].x, ladders[5].y, ladders[5].size = 150, 103, 52
                ladders[2].x = 250

                zombies[0] = Zombies(25, 177, True, "right")
                zombies[1] = Zombies(185, 177, True, "left")
                zombies[2] = Zombies(285, 83, True, "left")
                zombies[3] = Zombies(60, 31, True, "left")

                spiders[0].x, spiders[0].y = 5, 0
                spiders[1].x, spiders[1].y = 240, 0
                spiders[2].x = 5
                spiders[3].x, spiders[3].y = 100, 56
                spiders[4].x, spiders[4].y = 200, 56

                knights[0] = Knight(90, 21, True)

                bloodyPlatforms[0] = BloodyPlatform(230, 182, True, "top")
                bloodyPlatforms[1] = BloodyPlatform(30, 140, True, "top")

                skeletons[0] = Skeletons(-50, 83, False, "left")

                canons[0] = Canons(75, 130, True, "right")
                canons[1] = Canons(200, 130, True, "left")
            else:
                game.running = False
                game.endScreen = True
                fill_rect(0, 0, 320, 222, 'white')
                draw_string("Thank you for playing ", 60, 10)
                draw_string("at our game !!!", 100, 30)
                draw_string("Game design : Shahine", 55, 65)
                draw_string("Coding : Liam", 95, 85)
                draw_string("You finished in", 80, 130)
                draw_string(str(round(game.time, 2)) + "s", 130, 148)
                draw_string('Press OK to restart, <3', 45, 195)
                break

        if (get_pixel(player.x -1, player.y) or get_pixel(player.x -1, player.y + 20)) == color('red') :
            game.game_over()
        elif (get_pixel(player.x + 21, player.y) or get_pixel(player.x + 21, player.y + 20)) == color('red') :
            game.game_over()
        elif (get_pixel(player.x, player.y + 21) or get_pixel(player.x + 20, player.y + 21)) == color('red'):
            game.game_over()
        elif (get_pixel(player.x, player.y -1) or get_pixel(player.x + 20, player.y -1)) == color('red'):
            game.game_over()

    while game.gameOver:
        if keydown(KEY_OK):
            game.running = True
            game.gameOver = False
            break

    while game.endScreen:
        if keydown(KEY_OK):
            game.running = True
            game.endScreen = False
            break