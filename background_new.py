import pygame
from enemies import Snake1, Snake2, goodMushrooms, badMushrooms, Bird

pygame.init()

SCREEN_WIDTH= 1280
SCREEN_HEIGHT= 720
win= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

tile_size= 40 

# background images 
sun= pygame.image.load("sun.png")
backg= pygame.image.load("sky.png")
exit= pygame.image.load("exit.png")
exit_n= pygame.transform.scale(exit,(tile_size*2 ,tile_size))
background_new=pygame.transform.scale(backg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# platform


# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
 # playerin büyüklüğüne ve hareketlerine göre parkur ve ekran yeniden şekillendirilebilir
def grid_screen(screen):
    for line in range(0,19):
        pygame.draw.line(screen, (255,255,255), (0, line * tile_size), (SCREEN_WIDTH, line * tile_size))
    for line in range(0,33):
        pygame.draw.line(screen, (255,255,255), (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT))

class World():
    def __init__(self, data):
        self.data = data
        self.tile_list= []
        self.all_sprites_group = pygame.sprite.Group()  # Düşmanlar ve diğer sprite'lar için grup
        self.create_world()
      
    def create_world(self):
        tile_size = 40
        dirt_img= pygame.image.load("dirt.png")
        grass_img= pygame.image.load("grass.png")
        exit= pygame.image.load("exit.png")
        exit_n= pygame.transform.scale(exit,(tile_size*2 ,tile_size))

        row_count=0
        for row in self.data:
            col_count=0
            for tile in row:
                if tile==1:
                    img= pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile) 
                
                if tile==2:
                    img= pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile) 
         
               
                if tile == 3:  # Yılan soldan sağa
                    snake2 = Snake2(y=row_count * tile_size, width=tile_size, height=tile_size, image_path="snake.png", speed=3, screen_width=SCREEN_WIDTH, new_width=tile_size, new_height=tile_size)
                    self.all_sprites_group.add(snake2)

                if tile == 4:  # Yılan sağdan sola
                    snake1 = Snake1(y=row_count * tile_size, width=tile_size, height=tile_size, image_path="snake2.png", speed=3, screen_width=SCREEN_WIDTH, new_width=tile_size, new_height=tile_size)
                    self.all_sprites_group.add(snake1)

                if tile == 5:  # İyi mantar
                    good_mushroom = goodMushrooms(x=col_count * tile_size, y=row_count * tile_size, image_path="Mushrooms.png", new_width=tile_size, new_height=tile_size)
                    self.all_sprites_group.add(good_mushroom)

                if tile == 6:  # Kötü mantar
                    bad_mushroom = badMushrooms(
                        x=col_count * tile_size,  # x koordinatını col_count ile ayarla
                        y=row_count * tile_size,  # y koordinatını row_count ile ayarla
                        image_path="BadMushrooms.png",
                        new_width=tile_size,
                        new_height=tile_size
                    )
                    self.all_sprites_group.add(bad_mushroom)

                if tile==7:
                    img= pygame.transform.scale(exit_n, (tile_size, tile_size*2))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile)              
                col_count+=1
            row_count+=1

    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        self.all_sprites_group.draw(screen)  # Düşmanları da çizer

