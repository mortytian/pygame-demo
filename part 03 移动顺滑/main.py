import pygame as pg
import sys
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) # 开启持续按键
        self.load_data()
        

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder,'map.txt'),'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # 初始化
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                # 生成player同时防止生成的player在wall里面
                if tile == 'P':
                    self.player = Player(self, col, row)


    def run(self):
        # 为True则game loop 一直运行
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit(0)

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        # 画出横向方格
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        # 画出纵向方格
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # 捕捉键盘事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
        

    def show_start_screen(self):
        pass

# 开始
def main():
    try:
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()
    except SystemExit:
        print("正常退出")
if __name__ == '__main__':
    main()
