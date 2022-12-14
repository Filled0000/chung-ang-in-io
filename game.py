# [Python pygame Game] RPG tutorial
# Made by "PrintedLove"
# Referred to DaFluffyPotato's 'Physics - Pygame Tutorial: Making a Platformer'
#-*-coding: utf-8

import pygame, sys, os, time
from datafile import *
from pygame.locals import *
import pygame.mixer


pygame.font.init()
        

display_width = 960  # ȭ�� ���� ũ��
display_height = 640  # ȭ�� ���� ũ��
gameDisplay = pygame.display.set_mode((display_width, display_height))  # ȭ�� ũ�⼳��

def main_menu():
    global pause
    pause=False
    menu = True

    #largeText = pygame.font.SysFont("font",115)
    #TextSurf, TextRect = text_objects("Title", largeText, "White")
    #TextRect.center = ((display_width/2),(display_height/2))
    #gameDisplay.blit(TextSurf, TextRect)


  #  gameDisplay.fill("White")
 #   largeText = pygame.font.Font('assets/font.ttf',115)
#    TextSurf, TextRect = text_objects("CAU KIUGI", largeText)
 #   TextRect.center = (480)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(mainmenu_background, (0, 0))
        Button(mainmenu_start, 305, 290, 350, 60, mainmenu_start_click, 305, 290, game)
        Button(mainmenu_htp, 280, 370, 400, 60, mainmenu_htp_click, 280, 370, htp)
        Button(mainmenu_credit, 305, 450, 350, 60, mainmenu_credit_click, 305, 450, credit)
        Button(mainmenu_quit, 305, 530, 350, 60, mainmenu_quit_click, 305, 530, finishgame)

        pygame.display.update()
        clock.tick(15)

def game():
    Game()
def htp():
    htp = True

    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(htp_background, (0, 0))
        Button(htp_back, 305, 550, 350, 60, htp_back_click, 305, 550, main_menu)

        pygame.display.update()
        clock.tick(15)

def credit():
    credit = True
    while credit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(credit_background, (0, 0))
        Button(credit_back, 305, 550, 350, 60, credit_back_click, 305, 550, main_menu)

        pygame.display.update()
        clock.tick(15)


def finishgame():
    pygame.quit()
    sys.exit()

def unpause():
    global pause
    pause = False

def paused():

    gameDisplay.fill("White")
    largeText = pygame.font.SysFont("font",115)
    TextSurf, TextRect = text_objects("Paused", largeText, "Black")
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        Button(simple_button,50,450,370,109, simple_button,50,450, unpause)
        Button(simple_button,450,450,354,109, simple_button,450,450, main_menu)

        pygame.display.update()
        clock.tick(15)  

# ���� Ŭ����
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()



        #���� ��Ʈ�� ����
        pygame.display.set_caption('RPG tutorial')                                      # â �̸� ����
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # Ȯ���� ��ũ��

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # ī�޶� �̵� ��ǥ

        self.gameScore = 0       # ����

        # ���ҽ� �ҷ�����
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 16, 16, 8, 8, 12)      # �÷��̾� ��������Ʈ ��Ʈ
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # ���� ������Ʈ ��������Ʈ ��Ʈ
        self.spriteSheet_map1 = SpriteSheet('spriteSheet3.png', 8, 8, 16, 16, 87)         # ���� 1 ��������Ʈ ��Ʈ

        self.spr_player = {}     # �÷��̾� ��������Ʈ ��Ʈ
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.spr_effect = {}     # ȿ�� ��������Ʈ ��Ʈ
        self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        self.spr_enemy = {}      # �� ��������Ʈ ��Ʈ
        self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)

        self.spr_map_struct = {}     # ������ ��������Ʈ ��Ʈ
        self.spr_map_struct['leaf'] = [55, 56]
        self.spr_map_struct['flower'] = [57, 64]
        self.spr_map_struct['obj'] = [65, 70]
        self.spr_map_struct['sign'] = [71, 74]
        self.spr_map_struct['gravestone'] = [75, 78]
        self.spr_map_struct['skull'] = [79, 80]

        self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # ���� ��������Ʈ ��Ʈ

        createMapData()                                 # �� ������ �ʱ�ȭ
        self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # �� �̹��� ����
        self.backImage = createBackImage(self.spriteSheet_object)         # ��� �̹��� ����

        #ȿ����
        self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # �� ����
        for i in range(8):
            obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
            obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)

        # �÷��̾� ��Ʈ�� ����
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1

            if floor_map[player_spon_x] != -1:
                player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 8, TILE_MAPSIZE[1] * 4 - 14), (6, 14))  # �÷��̾� ��Ʈ�ڽ�
        self.player_movement = [0, 0]            # �÷��̾� �����Ӵ� �ӵ�
        self.player_vspeed = 0                   # �÷��̾� y���ӵ�
        self.player_flytime = 0                  # ���߿� �� �ð�

        self.player_action = 'stay'              # �÷��̾� ���� �ൿ
        self.player_frame = 0                    # �÷��̾� �ִϸ��̼� ������
        self.player_frameSpeed = 1               # �÷��̾� �ִϸ��̼� �ӵ�(���� ���� ����. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # �÷��̾� �̹��� ���� ���� (False: RIGHT)
        self.player_animationMode = True         # �ִϸ��̼� ��� (False: �ݺ�, True: �ѹ�)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # �÷��̾� ���� Ÿ�̸�
        self.player_attack_speed = 15            # �÷��̾� ���� �ӵ�

        # ����� ����
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        pygame.mixer.music.play(loops = -1)


        # ���� ����
        self.run()

    def run(self):

        global pause

        # ���� ����
        while True:
            self.screen_scaled.fill(BACKGROUND_COLOR)            # ȭ�� �ʱ�ȭ

            self.camera_scroll[0] += int((self.player_rect.x - self.camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # ī�޶� �̵�
            self.camera_scroll[1] += int((self.player_rect.y - self.camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

            self.screen_scaled.blit(self.backImage, (0, 0))                                   # ��� ��ο�
            self.screen_scaled.blit(self.mapImage, (-self.camera_scroll[0], -self.camera_scroll[1]))    # �� ��ο�

            # �÷��̾� ��Ʈ��
            if self.player_attack_timer < self.player_attack_speed:
                self.player_attack_timer += 1
            self.player_movement = [0, 0]                       # �÷��̾� �̵�
            if self.keyLeft:
                self.player_movement[0] -= 2
            if self.keyRight:
                self.player_movement[0] += 2
            self.player_movement[1] += self.player_vspeed

            self.player_vspeed += 0.2
            if self.player_vspeed > 3:
                self.player_vspeed = 3

            if self.player_movement[0] != 0:                  # �÷��̾� �ȱ� �ִϸ��̼� ó�� �� ���� ��ȯ
                if self.player_flytime == 0:
                    self.player_frame, self.player_action, self.player_frameSpeed, self.player_animationMode = change_playerAction(
                        self.player_frame, self.player_action, 'run', self.player_frameSpeed, 3, self.player_animationMode, True)

                    self.player_walkSoundTimer += 1

                    if self.player_walkSoundTimer > 1:
                        self.player_walkSoundTimer = 0

                        if self.player_walkSoundToggle:
                            self.player_walkSoundToggle = False
                            self.sound_footstep0.play()
                        else:
                            self.player_walkSoundToggle = True
                            self.sound_footstep1.play()
                if self.player_movement[0] > 0:
                    self.player_flip = False
                else:
                    self.player_flip = True
            else:
                self.player_walkSoundTimer = 0

                if self.player_flytime == 0:
                    self.player_frame, self.player_action, self.player_frameSpeed, self.player_animationMode = change_playerAction(
                        self.player_frame, self.player_action, 'stay', self.player_frameSpeed, 3, self.player_animationMode, True)

            self.player_rect, player_collision = move(self.player_rect, self.player_movement)

            if player_collision['bottom']:
                self.player_vspeed = 0
                self.player_flytime = 0
            else:
                self.player_flytime += 1

            self.player_frameTimer += 1                          # �÷��̾� �ִϸ��̼� Ÿ�̸�
            if self.player_frameTimer >= self.player_frameSpeed:
                self.player_frame +=1
                self.player_frameTimer = 0

                if self.player_frame >= len(self.spr_player[self.player_action]):
                    if self.player_animationMode == True:
                        self.player_frame = 0
                    else:
                        self.player_frame -= 1

            self.screen_scaled.blit(pygame.transform.flip(self.spr_player[self.player_action][self.player_frame], self.player_flip, False)
                               , (self.player_rect.x - self.camera_scroll[0] - 5, self.player_rect.y - self.camera_scroll[1] - 2))      # �÷��̾� ��ο�

            for obj in objects:         # ������Ʈ �̺�Ʈ ó��
                if obj.destroy:
                    obj.destroy_self()
                else:
                    obj.events()
                    obj.draw()
                    obj.physics_after()

            self.screen_scaled.blit(self.mapImage_front, (-self.camera_scroll[0], -self.camera_scroll[1]))    # ����Ʈ �� ��ο�

            draw_text(self.screen_scaled, "SCORE: " + str(self.gameScore), 8, (238, 238, 230), 200, 140)

            # �̺�Ʈ ��Ʈ��
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.keyLeft = True
                    if event.key == K_RIGHT:
                        self.keyRight = True
                    if event.key == K_UP and self.player_flytime < 6:    # ����
                        self.player_vspeed = -3.5
                        self.player_flytime += 1
                 
                        self.player_frame, self.player_action, self.player_frameSpeed, self.player_animationMode = change_playerAction(
                            self.player_frame, self.player_action, 'jump', self.player_frameSpeed, 6, self.player_animationMode, False)
                    
                    # pause
                    if event.key == pygame.K_p:
                        pause = True
                        paused()

                    if event.key == K_SPACE and self.player_attack_timer >= self.player_attack_speed:        # ����
                        self.player_attack_timer = 0
                        self.player_shot = createObject(self.spr_effect['player_shot'], (self.player_rect.x, self.player_rect.y + 2), 'player_shot', self)
                        self.player_shot.direction = self.player_flip
                        self.sound_attack.play()
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.keyLeft = False
                    if event.key == K_RIGHT:
                        self.keyRight = False

                

            surf = pygame.transform.scale(self.screen_scaled, WINDOW_SIZE)       # â ���� ����
            self.screen.blit(surf, (0, 0))

            pygame.display.update()
            self.clock.tick(60)

#game = Game()   # ���� ����

main_menu()