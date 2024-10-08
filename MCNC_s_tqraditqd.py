import pygame, level_system
from math import ceil
from os import environ

environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("MC NC's tally quest to defeat Raditude dog")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("assets/player.png").convert_alpha()
        self.pleft = self.surf
        self.prght = pygame.transform.flip(self.pleft, 1, 0)
        self.rect = self.surf.get_rect()
        self.spdy = 0
    def mvmt(self, fps, level):
        self.spdy += (10/fps)
        for i in range(int(self.spdy)):
            self.rect.y += self.spdy
            if not self.rect.collidelist(level.platforms) == -1:
                self.rect.y -= 1
                self.spdy = 0
                break
        k = pygame.key.get_pressed()
        speed = 240 if k[pygame.K_j] else 100
        if k[pygame.K_d]:
            self.rect.x += speed/fps
            self.surf = self.prght
        if k[pygame.K_a]:
            self.rect.x -= speed/fps
            self.surf = self.pleft

def menu():
    bg = pygame.image.load("assets/title.png")
    screen.blit(bg, [0,0])
    pygame.mixer.music.load("assets/m_mus.mp3")
    pygame.mixer.music.play()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_s:
                    game()
        pygame.display.flip()

def game():
    pygame.mixer.music.load("assets/bgm.wav")
    pygame.mixer.music.play(-1)
    clk = pygame.time.Clock()
    MCNC = Player()
    lvl = level_system.level()
    lvl.load(f"levels/start.json")
    bg = lvl.bg
    all_sprites = pygame.sprite.Group()
    all_sprites.add(MCNC)
    for i in lvl.platforms:
        all_sprites.add(i)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        MCNC.mvmt(clk.get_fps() or 60, lvl)
        screen.blit(bg, [0,0])
        for i in all_sprites:
            screen.blit(i.surf, i.rect)
        pygame.display.update()
        clk.tick(60)
    
menu()