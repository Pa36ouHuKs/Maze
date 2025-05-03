from pygame import *
font.init()
font1 = font.SysFont('Arial', 70)
win = font1.render('Победа!', True, (159, 236, 0))
lose = font1.render('Проигрыш(', True, (174, 52, 22))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick_sound = mixer.Sound('kick.ogg')
money_sound = mixer.Sound('money.ogg')
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('images (4).jfif'), (700, 500))
class Game_sprite_class(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_class(Game_sprite_class):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += 5
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += 5
class Enemy_class(Game_sprite_class):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 635:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= 4
        else:
            self.rect.x += 4
class Wall(sprite.Sprite):
    def __init__(self, w, h, color, x, y):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))#qwertyuiop[asdfghjkl;zxcvbnm,./////////////////]
player = Player_class('hero.png', 65, 65, 10, 50, 30)
cyborg = Enemy_class('cyborg.png', 65, 65, 6, 640, 250)
wood = Game_sprite_class('treasure.png', 65, 65, 0, 550, 370)
wall1 = Wall(450, 10, (247, 176, 168), 1, 100)
wall2 = Wall(300, 10, (247, 176, 168), 560, 100)
wall3 = Wall(10, 180, (247, 176, 168), 420, 220)
wall4 = Wall(325, 10, (247, 176, 168), 100, 220)
wall5 = Wall(10, 300, (247, 176, 168), 240, 320)
walls = sprite.Group()
walls.add(wall1, wall2, wall3, wall4, wall5)
game_runing = True
game_finish = False
while game_runing:
    if not game_finish:
        window.blit(background, (0, 0))
        if len(sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = 50
            player.rect.y = 30
        if sprite.collide_rect(player, wood):
            window.blit(win, (200, 150))
            game_finish = True
            money_sound.play()
        if sprite.collide_rect(player, cyborg):
            kick_sound.play()
            player.rect.x = 50
            player.rect.y = 30
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        cyborg.reset()
        player.reset()
        wood.reset()
        player.update()
        cyborg.update()
    for e in event.get():
        if e.type == QUIT:
            game_runing = False
    clock.tick(FPS)
    display.update()

