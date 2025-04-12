#создай игру "Лабиринт"!
import pygame as pg

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image_name, width, height, speed, x, y):
        self.image = pg.transform.scale(pg.image.load(image_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def move(self, keys_pressed):
        if keys_pressed[pg.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys_pressed[pg.K_d] and self.rect.x < w - w/10:
            self.rect.x += self.speed
        elif keys_pressed[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys_pressed[pg.K_s] and self.rect.y < h - w/10:
            self.rect.y += self.speed
    def put_bomb(self, keys_pressed):
        if keys_pressed[pg.K_SPACE]:
            pass
            # bomb = Bomb("бомба-Photoroom.png", w/10, w/10, 0, self.rect.x, self.rect.y)
            # bombs.append(bomb)

class Enemy(GameSprite):
    def move(self, keys_pressed):
        self.rect.x += self.speed
        if self.rect.x > w - w/10:
            self.speed *= -1
        elif self.rect.x < w - w/4:
            self.speed *= -1

class Bomb(GameSprite):
    def bomb(self):
        pass

class Wall(pg.sprite.Sprite):
    def __init__(self, color: tuple, wallX, wallY, wallWidth, wallHeight):
        super().__init__()
        self.color = color
        self.width = wallWidth
        self.height = wallHeight
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wallX
        self.rect.y = wallY

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


win = pg.display.set_mode((700, 500), pg.FULLSCREEN)
w, h = pg.display.get_window_size()
#print(w, h)
pg.display.set_caption('Лабиринт')

#фоновая_музыка
pg.mixer.init()
pg.mixer.music.load('jungles.ogg')
pg.mixer.music.play()

#игровые объекты
bg = pg.transform.scale(pg.image.load('background.jpg'), (w, h))
hero = Hero('hero.png', w/10, w/10, 10, 25, h - 100)
enemy = Enemy('cyborg.png', w/10, w/10, 5, w - 100, h - 175)
gold = GameSprite('treasure.png', w/10, w/10, 10, w - 100, h - 90)

wall1 = Wall((255, 255, 255), 100, 20, 450, 10)
wall2 = Wall((255, 255, 255), 100, 480, 350, 10)
wall3 = Wall((255, 255, 255), 100, 20, 10, 380)
# wall4

#переменные
bombs = {}
finish = False
run = True
clock = pg.time.Clock()

# pg.font.init()
# font = pg.font.Font(None, 70)
# win = font.render('YOU WIN!', True, (255, 215, 0))

#игровой цикл
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                win = pg.display.set_mode((700, 500))
                w = 700
                h = 500
                bg = pg.transform.scale(pg.image.load('background.jpg'), (w, h))
                hero = Hero('hero.png', w/10, w/10, 10, 25, h - 100)
                enemy = Enemy('cyborg.png', w/10, w/10, 5, w - 100, h - 150)
                gold = GameSprite('treasure.png', w/10, w/10, 10, w - 100, h - 90)
    keys_pressed = pg.key.get_pressed()

    if finish != True:
        win.blit(bg, (0, 0))
        hero.move(keys_pressed)
        hero.put_bomb(keys_pressed)
        enemy.move(keys_pressed)
        enemy.reset()
        gold.reset()
        wall1.reset()
        wall2.reset()
        wall3.reset()
        for b in bombs:
            b.reset()
        hero.reset()
        if pg.sprite.collide_rect(hero, gold):
            finish = True
            victory = True
        if pg.sprite.collide_rect(hero, wall1):
            finish = True
            victory = False
        if pg.sprite.collide_rect(hero, wall2):
            finish = True
            victory = False
        if pg.sprite.collide_rect(hero, wall3):
            finish = True
            victory = False
        # if pg.sprite.collide_rect(hero, wall4):
        #     finish = True
        #     victory = False
        if pg.sprite.collide_rect(hero, enemy):
            finish = True
            victory = False
    if finish:
        if victory:
            bg = pg.transform.scale(pg.image.load('youwin.jpg'), (w, h))
            win.blit(bg, (0, 0))
        else:
            bg = pg.transform.scale(pg.image.load('gameover.jpg'), (w, h))
            win.blit(bg, (0, 0))

    pg.display.update()
    clock.tick(60)
