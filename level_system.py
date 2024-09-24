import numpy, json, pygame
class platform(pygame.sprite.Sprite):
    def __init__(self, coords: list):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(coords)
        self.surf = pygame.Surface((self.rect.width, self.rect.height))
        self.surf.fill(pygame.Color(0x836539))
        pygame.draw.rect(self.surf, pygame.Color(0x34A56F),[0,0,self.rect.width,5])
class level():
    def __init__(self):
        self.platforms = []
        self.enemies = []
        self.lava = []
        self.transitions = []
    def load(self, fpath: str):
        file_unparsed = open(fpath).read()
        file_dict = json.loads(file_unparsed)
        self.platforms = tuple([platform(x) for x in file_dict["platforms"]])
        self.bg = pygame.image.load(file_dict["bg"]).convert()