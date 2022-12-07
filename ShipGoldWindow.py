import random
import arcade

class ShipWindow(arcade.Window):
    def __init__(self):
        super().__init__(1200, 1000, "Find the Gold")
        self.ship = None
        self.goals = arcade.SpriteList()
        self.sound = None
        self.score =0
        self.dump_sound = None

    def setup(self):
        self.ship = arcade.Sprite("pirate-galleon.png")
        self.sound = arcade.load_sound("")
        self.dump_sound = arcade.load_sound("")
        for number in range(7):
            gold = arcade.Sprite("gold-coins-large.png")
            gold.center_x = random.randint(36, 1164)
            gold.center_y = random.randint(36, 964)
            self.goals.append(gold)

    def on_update(self, delta_time):
        collided_gold = arcade.check_for_collision_with_list(self.ship,
                                                             self.goals)
        if collided_gold:
            arcade.play_sound(self.sound)
            self.score += len(collided_gold)
            for gold in collided_gold:
                self.goals.remove(gold)

    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        self.goals.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y


    def on_mouse_press(self, x, y, button, modifiers):
        pile = arcade.Sprite("gold-coins-large.png")
        pile.center_x = self.ship.center_x
        pile.center_y = self.ship.center_y - 74
        self.goals.append(pile)
        arcade.play_sound(self.dump_sound)