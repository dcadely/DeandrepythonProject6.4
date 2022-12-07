import arcade
import random


class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Arcade Class Window Demo")
        self.player = None
        self.player_dx = 0
        self.player_dy = 0
        self.targets = arcade.SpriteList()
        self.score = 0
        self.sound1 = None

    def setup(self):
        self.sound1 = arcade.load_sound("Galaga_elec_lightning.wav")
        self.player = arcade.Sprite("galaxy_ship.png")
        self.player.center_x =200
        self.player.center_y = 500
        for number in range(5):
            rock = arcade.Sprite("meteore.png")
            self.targets.append(rock)
            rock.center_x = random.randint(16, 1184)
            rock.center_y = random.randint(16, 984)

            rock.change_x = 1000
            rock.change_y = 1000
            rock.forward(110000)

    def on_update(self, delta_time):
        self.player.center_x += self.player_dx
        self.player.center_y += self.player_dy
        self.current_location = self.player
        if self.player.center_x > 1200:
            self.player.center_x = 0
            arcade.play_sound(self.sound1)
        for rock in self.targets:
            rock.center_x -= 3
            if rock.center_x < 0:
                rock.center_x = 1200


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -3
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 3
        if symbol == arcade.key.UP:
            self.player_dy = 3
        if symbol == arcade.key.DOWN:
            self.player_dy = -3

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT or symbol == arcade.key.DOWN:
            self.player_dx = 0
        if symbol == arcade.key.UP:
            self.player_dy = 0
        if symbol == arcade.key.DOWN:
            self.player_dy = 0

  def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

 def on_mouse_press(self, x, y, button, modifiers):
        pile = arcade.Sprite("lazer.png")
        pile.center_x = self.ship.center_x
        pile.center_y = self.ship.center_y - 74
        self.goals.append(pile)
        arcade.play_sound(self.throw_sound)
        self.score -= 1
