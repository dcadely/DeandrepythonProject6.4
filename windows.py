import arcade
import random


class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Arcade Class Window Demo")
        self.score = 0
        self.player = None
        self.targets = arcade.SpriteList()
        self.player_dx = 0
        self.player_dy = 0
        self.laser = arcade.Sprite("lazer.png")
        self.lasers = arcade.SpriteList()
        self.winner = False
        self.loser = False
        self.counter = 0

    def setup(self):
        self.player = arcade.Sprite("galaxy_ship.png")
        self.player.center_x = 500
        self.player.center_y = 100
        for enemy in range(6):
            self.target = arcade.Sprite("galaxy_ship.png")
            self.target.center_x = random.randint(200, 997)
            self.target.center_y = random.randint(925, 997)
            self.targets.append(self.target)
        for laser in range(0):
            self.laser = arcade.Sprite("ImagesForClass/lazer.png")
            self.lasers.append(self.laser)
        for number in range(9):
            rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.targets.append(rock)
            rock.center_x = random.randint(16, 1184)
            rock.center_y = random.randint(16, 984)
            self.winnersound = arcade.load_sound("arcade_resources_sounds_coin5.wav")
            self.losersound = arcade.load_sound("arcade_resources_sounds_gameover4.wav")
            self.hitsound = arcade.load_sound("arcade_resources_sounds_rockHit2.wav")
            self.gunsound = arcade.load_sound("arcade_resources_sounds_upgrade4.wav")

    def on_update(self, time_since_update):
        self.player.center_x += self.player_dx
        self.player.center_y += self.player_dy
        if self.player.center_x > 1200:
            self.player.center_x = 0
            arcade.play_sound(self.sound1)
        for rock in self.targets:
            rock.center_x -= 3
            if rock.center_x < 0:
                rock.center_x = 1200
        self.player.center_x += self.player_dx
        if self.player.center_x > 1200:
            self.player.center_x = 0
        if self.player.center_x < 0:
            self.player.center_x = 1200
            self.player.center_y += self.player_dy
        if self.player.center_y > 1000:
            self.player.center_y = 0
        if self.player.center_y < 0:
            self.player.center_y = 1000
        for enemy in self.targets:
            game_over = arcade.check_for_collision_with_list(self.player, self.targets)
            enemy.center_y -= random.randint(0, 1)
            if enemy.center_y <= 0:
                enemy.center_y = 1000
            enemy.center_x += random.randint(0, 0)
            if game_over:
                self.loser = True

        for laser in self.lasers:
            enemy_collision = arcade.check_for_collision_with_list(laser, self.targets)
            laser.center_y += 30
            if enemy_collision:
                self.score += len(enemy_collision)
                for enemy_down in enemy_collision:
                    self.targets.remove(enemy_down)
                    arcade.play_sound(self.hitsound)

                self.lasers.remove(laser)
            if self.score == 20:
                self.winner = True

    def on_draw(self):
        arcade.start_render()
        self.counter += 1
        if self.counter == 100:
            self.counter = 0
            for ogre in range(1):
                self.target = arcade.Sprite("galaxy_ship.png")
                self.target.center_x = random.randint(200, 997)
                self.target.center_y = random.randint(925, 997)
                self.targets.append(self.target)
        if self.winner == True:
            arcade.play_sound(self.winnersound)
            arcade.draw_text(f"WINNER!", 50, 470,
                             arcade.color.BLACK, 150)
            arcade.finish_render()
            return
        if self.loser == True:
            arcade.play_sound(self.losersound)
            arcade.draw_text(f"GAME OVER!", 50, 470,
                             arcade.color.RED, 150)
            arcade.finish_render()
            return

        self.player.draw()
        self.targets.draw()
        self.lasers.draw()
        arcade.draw_text(f"Current Score: {self.score}", 50, 970,
                         arcade.color.GREEN, 15)

        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -3
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 3
        if symbol == arcade.key.UP:
            self.player_dy = 3
        if symbol == arcade.key.DOWN:
            self.player_dy = - 3
        elif symbol == arcade.key.Z:
            laser = arcade.Sprite("lazer.png")
            arcade.play_sound(self.gunsound)

            laser.center_y = self.player.center_y
            laser.center_x = self.player.center_x
            self.lasers.append(laser)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_dx = 0
        if symbol == arcade.key.UP:
            self.player_dy = 0
        if symbol == arcade.key.DOWN:
            self.player_dy = 0