import pygame
world_data = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,6,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,2,2,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1],
    [1,0,0,6,0,2,2,0,0,1,1,1,1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
world_data2 = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,6,0,0,0,0,0,0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,2,2,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,6,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1],
    [1,0,0,0,5,2,2,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
class Princess(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image_right = pygame.image.load("princessRight.png")
        self.image_right = pygame.transform.scale(self.image_right, (40, 80)) 
        self.image_left = pygame.image.load("princessLeft.png")
        self.image_left = pygame.transform.scale(self.image_left, (40, 80)) 
        self.image_jump = pygame.image.load("princessJump.png")
        self.image_jump = pygame.transform.scale(self.image_jump, (40, 80)) 

        self.image = self.image_right  # Başlangıçta sağ a doğru bakan prenses
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_width // 2  # Prensesi ekranın ortasına yerleştir
        self.rect.y = self.screen_height - self.rect.height  # Prensesin başlangıç y pozisyonu
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.is_jumping = False
        self.jump_height = 10  # Zıplama yüksekliği
        self.jump_speed = 10
        self.gravity = 1  # Yerçekimi kuvveti
        self.velocity_y = 0
        self.velocity_x = 0
        self.move_speed = 5  # Yatay hareket hızı
        self.is_alive = True  # Prensesin canlı olup olmadığını belirler
        self.world_data = world_data
        # Prensesin başlangıç konumunu belirle
        self.find_starting_position()        

    def find_starting_position(self):
        tile_size = 40  # Eğer farklı bir tile boyutu kullanıyorsanız, burayı güncelleyin
        rows = len(self.world_data)
        cols = len(self.world_data[0])

        # Ekranın sol alt köşesinden başlamayı hedefle
        for x in range(0, cols):
            for y in range(rows - 1, -1, -1):
                # Prensesin çimenli yerlerde olmamasını sağla
                if self.world_data[y][x] == 0:
                    self.rect.x = x * tile_size
                    self.rect.y = y * tile_size
                    return

        # Eğer uygun bir yer bulunamazsa, ekranın sol alt köşesinde kal
        self.rect.x = 0
        self.rect.y = self.screen_height - self.rect.height
        
    def update(self, world, enemies):
        if not self.is_alive:
            return  # Eğer prenses ölmüşse, hiçbir işlem yapılmaz
      
        dx = 0
        dy = 0
        
        # Klavye girdileri
        key = pygame.key.get_pressed()

        # Karakterin zıplaması
        if key[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = -self.jump_speed
            self.is_jumping = True
            self.image = self.image_jump  # Zıplarken prensesin zıplama resmi gösterilir

        # Yerçekiminin düşmeye etkisi
        self.velocity_y += self.gravity
        dy += self.velocity_y

        # X düzleminde hareket - yatay
        if key[pygame.K_LEFT]:
            dx -= self.move_speed
            self.image = self.image_left  # Sola hareket ederken prensesin sola bakan resmi gösterilir
        if key[pygame.K_RIGHT]:
            dx += self.move_speed
            self.image = self.image_right  # Sağa hareket ederken prensesin sağa bakan resmi gösterilir

        # Konum güncellemesi
        self.rect.x += dx
        self.rect.y += dy

        # Zeminde zıplama işleminin sona erdirilmesi
        if self.rect.bottom >= self.screen_height:  # Eğer prenses zemine değerse
            self.rect.bottom = self.screen_height
            self.is_jumping = False
            if key[pygame.K_LEFT]:
                self.image = self.image_left
            elif key[pygame.K_RIGHT]:
                self.image = self.image_right


        # Çarpışma kontrolü
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0  # Yatay hareket durdurulur

            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.velocity_y < 0:
                    dy = tile[1].bottom - self.rect.top  # Yukarıya doğru çarpışma
                elif self.velocity_y >= 0:
                    dy = tile[1].top - self.rect.bottom  # Aşağıya doğru çarpışma
                    self.is_jumping = False
                    self.velocity_y = 0

        # Çarpışma kontrolü (düşmanlarla)
        if self.check_collision_with_enemies(enemies):
            self.is_alive = False
            print("Mario öldü!")  # Oyun sonu mesajı veya işlemi

        if self.check_collision_with_exit(world_data):
            self.world_data=world_data2
            print("yeni level'a geçtiniz!!")  # Oyun sonu mesajı veya işlemi

        # Oyuncunun koordinatları
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.is_jumping = False
            self.velocity_y = 0

        # Ekran sınırları içinde kalmasını sağla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def check_collision_with_enemies(self, enemies):
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                return True
        return False

    def check_collision_with_exit(self,world_data):
        for block in world_data:
            if block==7:
                if pygame.sprite.collide_rect(self,block):
                    return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
