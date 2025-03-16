import pygame as py
import sys

py.init()

# Constants:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Game class
class ScoundrelGame:
    def __init__(self):
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        py.display.set_caption("Scoundrel")

        self.clock = py.time.Clock()
        self.fps = 60

        self.running = True

    def handle_events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        py.quit()
        sys.exit()

def main():
    game = ScoundrelGame()
    game.run()

if __name__ == "__main__":
    main()
