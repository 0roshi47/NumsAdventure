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



while True:

    game = Game()

    ladder1 = [200, 197]
    ladder2 = [40, 155]
    ladder3 = [200, 103]
    ladder4 = [-50, 0]

    door = [25, 51]

    player = Player(270, 177)

    zombie1 = Zombies(10, 135, True, "right")
    zombie2 = Zombies(220, 31, True, "left")

    spider1 = Spiders(-50, 0, False, False)
    spider2 = Spiders(-50, 0, False, False)
    spider3 = Spiders(-50, 0, False, False)

    bloodyPlatform1 = BloodyPlatform(-50, 0, False, "top")
    bloodyPlatform2 = BloodyPlatform(-50, 0, False, "top")

    knight1 = Knight(-50, 103, False)
    knight2 = Knight(-50, 103, False)

    skeleton1 = Skeletons(-50, 0, False, "left")
    skeleton2 = Skeletons(-50, 0, False, "left")

    canon1 = Canons(-50, 130, False, "right")
    canon2 = Canons(-50, 26, False, "left")

    fill_rect(0, 0, 320, 222, 'white')
    fill_rect(0, 222, 320, -25, 'grey')

    sleep(0.1)

    while game.running:

        sleep(0.015)

        fill_rect(0, 160, 320, -5, 'grey')
        fill_rect(ladder1[0], ladder1[1], 20, - 42, 'purple')
        fill_rect(0, 108, 320, -5, 'grey')
        fill_rect(ladder2[0], ladder2[1], 20, - 52, 'purple')
        fill_rect(0, 56, 320, -5, 'grey')
        fill_rect(ladder3[0], ladder3[1], 20, - 52, 'purple')
        fill_rect(ladder4[0], ladder4[1], 20, - 52, 'purple')

        fill_rect(door[0], door[1], 20, -30, 'green')

        fill_rect(player.x, player.y, 20, 20, 'blue')

        if zombie1.isAlive:
            zombie1.main()
        if zombie2.isAlive:
            zombie2.main()
        
        if spider1.isAlive:
            spider1.main()
        if spider2.isAlive:
            spider2.main()
        if spider3.isAlive:
            spider3.main()

        if bloodyPlatform1.isAlive:
            bloodyPlatform1.main()
        if bloodyPlatform2.isAlive:
            bloodyPlatform2.main()

        if knight1.isAlive:
            knight1.main()
        if knight2.isAlive:
            knight2.main()
        
        if skeleton1.isAlive:
            skeleton1.main()
        if skeleton2.isAlive:
            skeleton2.main()

        if canon1.isAlive:
            canon1.main()
        if canon2.isAlive:
            canon2.main()
        
        if game.level == 1:
            draw_string("1-Hi World", 5, 201)
        elif game.level == 2:
            draw_string("2-Spider Gang", 5, 201)
        elif game.level == 3:
            draw_string("3-The Bridge", 5, 201)
        elif game.level == 4:
            draw_string("4-Frozen Cave", 5, 201)
        elif game.level == 5:
            draw_string("5-Caïn Tunnel", 5, 201)
        elif game.level == 6:
            draw_string("6-The djinn Cloud", 5, 201)
        elif game.level == 7:
            draw_string("7-Midnight Climax", 5, 201)

        #player movement
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
            if (ladder1[0] <= player.x <= ladder1[0] + 20 or ladder1[0] <= player.x + 20 <= ladder1[0] + 20) and (ladder1[1] >= player.y + 20 > ladder1[1] - 42):
               player.move_up()
            elif (ladder2[0] <= player.x <= ladder2[0] + 20 or ladder2[0] <= player.x + 20 <= ladder2[0] + 20) and (ladder2[1] >= player.y + 20 > ladder2[1] - 52):
                player.move_up()
            elif (ladder3[0] <= player.x <= ladder3[0] + 20 or ladder3[0] <= player.x + 20 <= ladder3[0] + 20) and (ladder3[1] >= player.y + 20 > ladder3[1] - 52):
                player.move_up()
            elif (ladder4[0] <= player.x <= ladder4[0] + 20 or ladder4[0] <= player.x + 20 <= ladder4[0] + 20) and (ladder4[1] >= player.y + 20 > ladder4[1] - 52):
                player.move_up()
        elif keydown(KEY_DOWN):
            if (ladder1[0] <= player.x <= ladder1[0] + 20 or ladder1[0] <= player.x + 20 <= ladder1[0] + 20) and (ladder1[1] > player.y + 20 >= ladder1[1] - 42):
                player.move_down()
            elif (ladder2[0] <= player.x <= ladder2[0] + 20 or ladder2[0] <= player.x + 20 <= ladder2[0] + 20) and (ladder2[1] > player.y + 20 >= ladder2[1] - 52):
                player.move_down()
            elif (ladder3[0] <= player.x <= ladder3[0] + 20 or ladder3[0] <= player.x + 20 <= ladder3[0] + 20) and (ladder3[1] > player.y + 20 >= ladder3[1] - 52):
                player.move_down()
            elif (ladder4[0] <= player.x <= ladder4[0] + 20 or ladder4[0] <= player.x + 20 <= ladder4[0] + 20) and (ladder4[1] > player.y + 20 >= ladder4[1] - 52):
                player.move_down()

        if (ladder1[0] <= player.x <= ladder1[0] + 20 or ladder1[0] <= player.x + 20 <= ladder1[0] + 20) and (ladder1[1] - 2 >= player.y + 20 > ladder1[1] - 42):
            player.isOnLadder = True
        elif (ladder2[0] <= player.x <= ladder2[0] + 20 or ladder2[0] <= player.x + 20 <= ladder2[0] + 20) and (ladder2[1] - 2 >= player.y + 20 > ladder2[1] - 52):
            player.isOnLadder = True
        elif (ladder3[0] <= player.x <= ladder3[0] + 20 or ladder3[0] <= player.x + 20 <= ladder3[0] + 20) and (ladder3[1] - 2 >= player.y + 20 > ladder3[1] - 52):
            player.isOnLadder = True
        elif (ladder4[0] <= player.x <= ladder4[0] + 20 or ladder4[0] <= player.x + 20 <= ladder4[0] + 20) and (ladder4[1] - 2 >= player.y + 20 > ladder4[1] - 52):
            player.isOnLadder = True
        else:
            player.isOnLadder = False

        #go the next level
        #if (door[0] < player.x < door[0] + 20 or door[0] < player.x + 20 < door[0] + 20) and (player.y + 20 == door[1]):
        if (door[0] < player.x < door[0] + 20 or door[0] < player.x + 20 < door[0] + 20) and (player.y + 20 == door[1]) or keydown(KEY_SHIFT):
            game.level += 1
            fill_rect(0, 0, 320, 222, 'white')
            fill_rect(0, 222, 320, -25, 'grey')
            if game.level == 2:

                player = Player(25, 177)

                ladder1[0] = 100
                ladder2[0] = 25
                ladder3[0] = 170

                door[0] = 285

                zombie2.isAlive = False
                zombie2.x = -50

                zombie1 = Zombies(240, 83, True, "left")

                spider1 = Spiders(95, 108, True, False)
                spider2 = Spiders(165, 0, True, False)
            elif game.level == 3:

                player = Player(25, 177)

                ladder1[0] = 160
                ladder2[0] = 45
                ladder3[0] = 250

                door[0] = 20

                zombie1 = Zombies(115, 31, True, "right")

                spider1 = Spiders(145, 108, True,  False)
                spider2 = Spiders(-50, 108, False, False)

                bloodyPlatform1 = BloodyPlatform(250, 182, True, "top")
            elif game.level == 4:
                
                player = Player(275, 177)

                ladder1[0] = 75
                ladder2[0] = 270
                ladder3[0] = 100
                
                door[0] = 145
                
                zombie1 = Zombies(145, 83, True, "left")
                zombie2 = Zombies(115, 31, True, "right")

                spider1 = Spiders(-50, 108, False,  False)
                spider2 = Spiders(-50, 108, False, False)

                bloodyPlatform1 = BloodyPlatform(-50, 182, False, "top")

                knight1 = Knight(175, 125, True)
                knight2 = Knight(180, 21, True)
            elif game.level == 5:

                player = Player(25, 177)
                
                ladder1[0] = 165
                ladder2[0] = 45
                ladder3[0] = 260

                door[0] = 40

                zombie1 = Zombies(70, 83, True, "right")
                zombie2 = Zombies(-50, 0, False, "left")

                spider1 = Spiders(225, 56, True, False)
                spider2 = Spiders(285, 56, True, False)
                spider3 = Spiders(255, 0, True, False)

                bloodyPlatform1 = BloodyPlatform(250, 182, True, "top")
                bloodyPlatform2 = BloodyPlatform(35, 140, True, "top")

                knight1 = Knight(-50, 125, False)
                knight2 = Knight(-50, 21, False)
            elif game.level == 6:

                player = Player(25, 177)

                ladder1[0] = 170
                ladder2[0] = 45
                ladder4 = [255, 155]
                ladder3[0] = 150

                door[0] = 265

                zombie1 = Zombies(230, 31, True, "right")

                spider1 = Spiders(145, 51, True, False)
                spider2 = Spiders(285, 0, True, False)
                spider3 = Spiders(-50, 0, False, False)

                bloodyPlatform1 = BloodyPlatform(225, 182, True, "top")
                bloodyPlatform2 = BloodyPlatform(-50, 140, False, "top")

                skeleton1 = Skeletons(5, 135, True, "right")
                skeleton2 = Skeletons(190, 31, True, "left")
            elif game.level == 7:

                player = Player(20, 177)

                ladder1[0] = 50
                ladder2[0] = 160
                ladder3[0] = 40
                ladder4[0] = -50

                door[0] = 265

                zombie1 = Zombies(260, 177, True, "left")
                zombie2 = Zombies(235, 31, True, "right")

                spider1 = Spiders(45, 108, True, False)
                spider2 = Spiders(240, 56, True, False)

                bloodyPlatform1 = BloodyPlatform(-50, 182, False, "top")

                knight1 = Knight(15, 73, True)

                skeleton1 = Skeletons(-50, 135, False, "right")
                skeleton2 = Skeletons(-50, 31, False, "left")

                canon1 = Canons(10, 130, True, "right")
                canon2 = Canons(235, 26, True, "left")
            else:
                game.running = False
                game.endScreen = True
                fill_rect(0, 0, 320, 222, 'white')
                draw_string("Thank you for playing ", 60, 10)
                draw_string("at our game !!!", 100, 30)

                draw_string("Game design : Shahine", 55, 65)
                draw_string("Coding : Liam", 95, 85)

                draw_string("This game is still", 65, 120)
                draw_string("in development, updates", 45, 140)
                draw_string("are incoming soon !", 65, 160)

                draw_string('Press OK to restart, <3', 45, 195)
                break

        #checking colisions
        if (get_pixel(player.x -1, player.y) or get_pixel(player.x -1, player.y + 20) or get_pixel(player.x -1, player.y + 10)) == color('red') :
            game.game_over()
        elif (get_pixel(player.x + 21, player.y) or get_pixel(player.x + 21, player.y + 20) or get_pixel(player.x + 21, player.y + 10)) == color('red') :
            game.game_over()
        elif (get_pixel(player.x + 10, player.y + 21) or get_pixel(player.x + 10, player.y + 21)) == color('red'):
            game.game_over()
        elif (get_pixel(player.x -1, player.y + 17) or get_pixel(player.x + 21, player.y + 17)) == color('red'):
            game.game_over()
        elif (get_pixel(player.x -1, player.y + 3) or get_pixel(player.x + 21, player.y + 3)) == color('red'):
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