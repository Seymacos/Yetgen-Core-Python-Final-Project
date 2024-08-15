import pygame
import sys
from enemies import Snake1, Snake2, badMushrooms, goodMushrooms, Bird
from marioDeneme import Mario
from background_new import World
from menu import Menu


# Pygame'i başlat
pygame.init()


# Ekran boyutları
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
tile_size=40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("************")


# Renkler
LIGHT_BLUE = (173, 216, 230)


# background images
# background images 
sun= pygame.image.load("sun.png")
backg= pygame.image.load("sky.png")
exit= pygame.image.load("exit.png")
exit_n= pygame.transform.scale(exit,(tile_size*2 ,tile_size))
background_new=pygame.transform.scale(backg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
#  # mainde grid_screen func çağırılacak



world_data = [
    [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1],
    [1,0,0,0,0,2,2,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


world = World(world_data)


# Mario karakterini başlat
mario = Mario(SCREEN_WIDTH, SCREEN_HEIGHT)


# Düşmanları güncelle
all_sprites = pygame.sprite.Group()

# Menü
menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT)
in_menu = True


# Oyun döngüsü
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if in_menu:
        # Menü ekranını çiz
        menu.draw_menu(screen)


        # Menü olaylarını yönet
        action = menu.handle_events()
        if action == "start":
            in_menu = False
        elif action == "options":
            # Option ekranı burada işlenebilir
            pass
        elif action == "quit":
            pygame.quit()
            sys.exit()
    else:
        keys = pygame.key.get_pressed()


        # ekranı böl ve arka planı koy
        screen.blit(backg_new, (0, 0))
    
        world.draw(screen, background_scroll)

        # Mario'nun hareketini yönet
        mario.update(world, all_sprites)
   
        all_sprites.update()


        # Mario'yu ekrana çiz
        mario.draw(screen)

        world.draw(screen)


        # Düşmanları ekrana çiz
        all_sprites.draw(screen)
                
        # update the scroll position to make it continuous
        background_scroll += scroll_speed
        if background_scroll >= SCREEN_WIDTH:
            background_scroll = 0

        pygame.display.update()


    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)



