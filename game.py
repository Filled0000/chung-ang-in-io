# [Python pygame Game] RPG tutorial
# Made by "PrintedLove"
# Referred to DaFluffyPotato's 'Physics - Pygame Tutorial: Making a Platformer'
#-*-coding: utf-8


# [Python pygame Game] RPG tutorial
# Made by "PrintedLove"
# Referred to DaFluffyPotato's 'Physics - Pygame Tutorial: Making a Platformer'
#-*-coding: utf-8

import pygame, sys, os, time
from datafile import *
from pygame.locals import *
import pygame.mixer
from pygame import display, movie
from ui import *

pygame.font.init()

display_width = 960  # 화면 가로 크기
display_height = 640  # 화면 세로 크기
gameDisplay = pygame.display.set_mode((display_width, display_height))  # 화면 크기설정
pygame.display.set_caption("Chungang-in-io")  # 타이틀
clock = pygame.time.Clock()


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()



# def draw_text(screen, text, size, color, x, y):
#     gameFont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME), size)
#     text_surface = gameFont.render(text, False, color)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (round(x), round(y))
#     screen.blit(text_surface, text_rect)

def main_menu():
    global pause
    pause = False
    menu = True

    # largeText = pygame.font.SysFont("font.ttf",115)
    # TextSurf, TextRect = text_objects("CAU KIUGI", largeText, "White")
    # TextRect.center = ((display_width/2),(display_height/4))
    # gameDisplay.blit(TextSurf, TextRect)

    

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#        gameDisplay.fill("White")

        gameDisplay.blit(Asset.mainmenu_background, (0, 0))
        draw_text(gameDisplay, "Chungangin.io", 115, (238, 238, 230), (display_width/2),(display_height/4))
        #gameDisplay.blit(TextSurf, TextRect)

        Button(Asset.mainmenu_start, 305, 290, 348, 63, Asset.mainmenu_start_click, 310, 280, game)
        Button(Asset.mainmenu_htp, 305, 370, 348, 63, Asset.mainmenu_htp_click, 310, 360, htp)
        Button(Asset.mainmenu_credit, 305, 450, 348, 63, Asset.mainmenu_credit_click, 310, 440, credit)
        Button(Asset.mainmenu_quit, 305, 530, 348, 63, Asset.mainmenu_quit_click, 310, 520, finishgame)

        pygame.display.update()
        clock.tick(15)


def game():
    Variables.StageLevel = 0
    Variables.LifeCount = 3
    Game()
    
def htp():
    htp = True

    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(Asset.htp_background, (0, 0))
        gameDisplay.blit(Asset.htp_image, (0, 0))
        Button(Asset.htp_back, 305, 550, 350, 60, Asset.htp_back_click, 310, 545, main_menu)

        pygame.display.update()
        clock.tick(15)

def credit():
    credit = True
    while credit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(Asset.credit_background, (0, 0))
        gameDisplay.blit(Asset.credit_image, (0, 0))
        Button(Asset.credit_back, 364, 570, 232, 42, Asset.credit_back_click, 369, 565, main_menu)

        pygame.display.update()
        clock.tick(15)

def finishgame():
    pygame.quit()
    sys.exit()

def unpause():
    global pause
    pause = False

def paused():
    global pause
    pause = True

    # gameDisplay.fill("White")
    #largeText = pygame.font.SysFont("font",115)
    #TextSurf, TextRect = text_objects("Paused", largeText, "Black")
    #TextRect.center = ((display_width/2),(display_height/2))
    # gameDisplay.blit(TextSurf, TextRect)

    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(Asset.mainmenu_background, (0, 0))
        draw_text(gameDisplay, "PAUSED", 115, (238, 238, 230), (display_width/2),(display_height/4))
        #gameDisplay.blit(TextSurf, TextRect)
        Button(Asset.continue_button,86,450,348,63, Asset.continue_button_click, 91,445, unpause)
        Button(Asset.return_menu_button,524,450,348,63, Asset.return_menu_button_click, 529,445, main_menu)

        pygame.display.update()
        clock.tick(15)
        
def gameOver():
    global gOver
    gOver = True
    # gameDisplay.fill("White")
    # largeText = pygame.font.SysFont("font",115)
    # TextSurf, TextRect = text_objects("Game Over", largeText, "Black")
    # TextRect.center = ((display_width/2),(display_height/2))
    # gameDisplay.blit(TextSurf, TextRect)

    while gOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill("white")
        #gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(Asset.mainmenu_background, (0, 0))
#        draw_text(gameDisplay, "GAME OVER", 115, (238, 238, 230), (display_width/2),(display_height/4))
        #gameDisplay.blit(TextSurf, TextRect)

        
        over=[Asset.over01, Asset.over02, Asset.over03]
        num = random.randrange(0,2)
        rect= over[num].get_rect()
        gameDisplay.blit(Asset.mainmenu_background, (0, 0))
        gameDisplay.blit(Asset.game_over, [290, 100])
        gameDisplay.blit(over[num], [290, 380])

        Button(Asset.again_button,86,450,348,63, Asset.again_button_click,91,445, game)
        Button(Asset.return_menu_button,524,450,348,63, Asset.return_menu_button_click, 529,445, main_menu)

        pygame.display.update()
        clock.tick(15)
        
def stageClear():
    global stgClear
    stgClear = True
    # gameDisplay.fill("White")
    # largeText = pygame.font.SysFont("font",115)
    # TextSurf, TextRect = text_objects("Stage Clear", largeText, "Black")
    # TextRect.center = ((display_width/2),(display_height/2))
    # gameDisplay.blit(TextSurf, TextRect)

    while stgClear:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        
        # gameDisplay.fill("white")
        # gameDisplay.blit(TextSurf, TextRect)
        #draw_text(gameDisplay, "STAGE CLEAR", 115, (238, 238, 230), (display_width/2),(display_height/4))

        clear=[Asset.clear01, Asset.clear02, Asset.clear03]
        num = random.randrange(0,2)
        rect= clear[num].get_rect()
        gameDisplay.blit(Asset.mainmenu_background, (0, 0))
        gameDisplay.blit(Asset.game_clear, [290, 100])
        gameDisplay.blit(clear[num], [290, 380])


        #gameDisplay.blit(TextSurf, TextRect)
        Button(Asset.next_button,86,450,348,63, Asset.next_button_click, 91, 445, nextStage)
        Button(Asset.return_menu_button,524,450,348,63, Asset.return_menu_button_click, 529,445, main_menu)

        pygame.display.update()
        clock.tick(15)
        
def nextStage():
    if Variables.StageLevel == 1:
        Game2()
    elif Variables.StageLevel == 2:
        Game3()
    elif Variables.StageLevel == 3:
        Game4()
    elif Variables.StageLevel == 4:
        #BossStage()
        boss_scene()

def boss_scene():
    global bossScene
    bossScene = True

    while bossScene:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        gameDisplay.blit(Asset.mainmenu_background, (0, 0))
        gameDisplay.blit(Asset.boss_img, (0,0))
        Button(Asset.next_button,86,450,348,63, Asset.next_button_click, 91, 445, BossStage)
        Button(Asset.return_menu_button,524,450,348,63, Asset.return_menu_button_click, 529,445, main_menu)
        pygame.display.update()
        clock.tick(15)
        


class Variables:
    StageLevel = 0
    LifeCount = 3
    levelTime = [10, 20, 30, 40, 50]
    levelScore = [10, 30, 50, 70, 90]

# 게임 클래스
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        #게임 컨트롤 변수
        pygame.display.set_caption('RPG tutorial')                                      # 창 이름 설정
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

        self.gameScore = 0       # 점수

        # 리소스 불러오기
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 32, 32, 8, 8, 12)      # 플레이어 스프라이트 시트
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        self.spriteSheet_map1 = SpriteSheet('spriteSheet3.png', 16, 16, 16, 16, 87)         # 지형 1 스프라이트 시트

        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.spr_effect = {}     # 효과 스프라이트 세트
        self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        self.spr_enemy = {}      # 적 스프라이트 세트
        self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)

        self.spr_map_struct = {}     # 구조물 스프라이트 세트
        self.spr_map_struct['leaf'] = [55, 56]
        self.spr_map_struct['flower'] = [57, 64]
        self.spr_map_struct['obj'] = [65, 70]
        self.spr_map_struct['sign'] = [71, 74]
        self.spr_map_struct['gravestone'] = [75, 78]
        self.spr_map_struct['skull'] = [79, 80]

        self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # 코인 스프라이트 세트

        createMapData()                                 # 맵 데이터 초기화
        self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # 맵 이미지 생성
        self.backImage = createBackImage(self.spriteSheet_object)         # 배경 이미지 생성

        #효과음
        self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # 적 생성
        for i in range(8):
            obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
            obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)

        # 플레이어 컨트롤 변수
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1
            if floor_map[player_spon_x] != -1:
                if floor_map[player_spon_x + 1] != -1 and floor_map[player_spon_x - 1] != -1:
                    if floor_map[player_spon_x + 2] != -1 and floor_map[player_spon_x - 2] != -1:
                        if floor_map[player_spon_x + 3] != -1 and floor_map[player_spon_x - 3] != -1:
                            if floor_map[player_spon_x + 4] != -1 and floor_map[player_spon_x - 4] != -1:
                                player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 8, TILE_MAPSIZE[1] * 4 - 14), (6, 14))  # 플레이어 히트박스

        self.player_rect = pygame.Rect((player_spon_x * 4, TILE_MAPSIZE[1] * 2 - 30), (16, 30))  # 플레이어 히트박스
        self.player_movement = [0, 0]            # 플레이어 프레임당 속도
        self.player_vspeed = 0                   # 플레이어 y가속도
        self.player_flytime = 0                  # 공중에 뜬 시간

        self.player_action = 'stay'              # 플레이어 현재 행동
        self.player_frame = 0                    # 플레이어 애니메이션 프레임
        self.player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
        self.player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # 플레이어 공격 타이머
        self.player_attack_speed = 15            # 플레이어 공격 속도

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        pygame.mixer.music.play(loops = -1)


        # 게임 실행
        self.run()
        
        #level_time -> 레벨당 시간 
        #level -> 스테이지 계수
        
    def run(self):
        self.play = True
        self.start_ticks = pygame.time.get_ticks()
        self.get_time_item = 0
        self.get_damage_item = 0
        self.get_life_item = 0
        global pause
        var = Variables

        # 메인 루프
        while True:
            self.screen_scaled.fill(BACKGROUND_COLOR)            # 화면 초기화

            self.camera_scroll[0] += int((self.player_rect.x - self.camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
            self.camera_scroll[1] += int((self.player_rect.y - self.camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

            self.screen_scaled.blit(self.backImage, (0, 0))                                   # 배경 드로우
            self.screen_scaled.blit(self.mapImage, (-self.camera_scroll[0], -self.camera_scroll[1]))    # 맵 드로우
            
            self.screen_scaled.blit(self.mapImage_front, (-self.camera_scroll[0], -self.camera_scroll[1]))    # 프론트 맵 드로우
            
             # 일시정지 버튼 생성
            Button(Asset.pause_button, 890, 15, 54, 63, Asset.pause_button_click, 890, 15, paused)
            pygame.display.update()
            
            if self.get_time_item == 0:
                self.game_timer = (pygame.time.get_ticks() - self.start_ticks) / 1000 #calculate how many seconds
            else:
                self.game_timer = (pygame.time.get_ticks() - self.start_ticks) / 1000 - 5 * self.get_time_item 


            if self.game_timer > var.levelTime[var.StageLevel] and self.gameScore < var.levelScore[var.StageLevel]: # if more than 100
                gameOver()
            else:
                if self.game_timer > var.levelTime[var.StageLevel] and self.gameScore >= var.levelScore[var.StageLevel]:
                    var.StageLevel += 1
                    stageClear()
                

            draw_text(self.screen_scaled, "Time : " + str(round(var.levelTime[var.StageLevel] - self.game_timer, 1)), 8, (238, 238, 230), 30, 140)
            draw_text(self.screen_scaled, "Level : " + str(round(var.StageLevel + 1, 1)), 8, (238, 238, 230), 30, 10)
            draw_text(self.screen_scaled, "Target Score : " + str(round(var.levelScore[var.StageLevel], 1)), 8, (238, 238, 230), 120, 140)

            # 플레이어 컨트롤
            if self.player_attack_timer < self.player_attack_speed:
                self.player_attack_timer += 1
            self.player_movement = [0, 0]                       # 플레이어 이동
            if self.keyLeft:
                self.player_movement[0] -= 2
            if self.keyRight:
                self.player_movement[0] += 2
            self.player_movement[1] += self.player_vspeed

            self.player_vspeed += 0.2
            if self.player_vspeed > 3:
                self.player_vspeed = 3

            if self.player_movement[0] != 0:                  # 플레이어 걷기 애니메이션 처리 및 방향 전환
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

            self.player_frameTimer += 1                          # 플레이어 애니메이션 타이머
            if self.player_frameTimer >= self.player_frameSpeed:
                self.player_frame +=1
                self.player_frameTimer = 0

                if self.player_frame >= len(self.spr_player[self.player_action]):
                    if self.player_animationMode == True:
                        self.player_frame = 0
                    else:
                        self.player_frame -= 1

            self.screen_scaled.blit(pygame.transform.flip(self.spr_player[self.player_action][self.player_frame], self.player_flip, False)
                               , (self.player_rect.x - self.camera_scroll[0] - 5, self.player_rect.y - self.camera_scroll[1] - 2))      # 플레이어 드로우
            
            if self.player_flytime > 100:               
                if var.LifeCount == 0:
                    gameOver()
                else:
                    self.player_rect.x = self.player_rect.x - self.camera_scroll[0] - 5
                    self.player_rect.y = TILE_MAPSIZE[1] * 4 - 14
                    self.player_vspeed = 0
                    self.player_flytime = 0
                    
                    var.LifeCount -= 1
                    
                    
                    
            if var.LifeCount == 0:
                    gameOver()

            for obj in objects:         # 오브젝트 이벤트 처리
                if obj.destroy:
                    obj.destroy_self()
                else:
                    obj.events()
                    obj.draw()
                    obj.physics_after()

            var.LifeCount += self.get_life_item
            draw_text(self.screen_scaled, "SCORE: " + str(self.gameScore), 8, (238, 238, 230), 200, 140)
            draw_text(self.screen_scaled, "LIFE: " + str(var.LifeCount), 8, (238, 238, 230), 200, 10)
            self.get_life_item = 0
            
            # 이벤트 컨트롤
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.keyLeft = True
                    if event.key == K_RIGHT:
                        self.keyRight = True
                    if event.key == K_UP and self.player_flytime < 6:    # 점프
                        self.player_vspeed = -4.5
                        self.player_flytime += 1
                 
                        self.player_frame, self.player_action, self.player_frameSpeed, self.player_animationMode = change_playerAction(
                            self.player_frame, self.player_action, 'jump', self.player_frameSpeed, 6, self.player_animationMode, False)
                    
                    # pause
                    if event.key == pygame.K_p:
                        pause = True
                        paused()

                    if event.key == K_SPACE and self.player_attack_timer >= self.player_attack_speed:        # 공격
                        self.player_attack_timer = 0
                        self.player_shot = createObject(self.spr_effect['player_shot'], (self.player_rect.x, self.player_rect.y + 2), 'player_shot', self)
                        self.player_shot.direction = self.player_flip
                        self.sound_attack.play()
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.keyLeft = False
                    if event.key == K_RIGHT:
                        self.keyRight = False

                

            surf = pygame.transform.scale(self.screen_scaled, WINDOW_SIZE)       # 창 배율 적용
            self.screen.blit(surf, (0, 0))

            self.clock.tick(60)

#game = Game()   # 게임 실행

class Game2:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        #게임 컨트롤 변수
        pygame.display.set_caption('RPG tutorial')                                      # 창 이름 설정
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

        self.gameScore = 0       # 점수

        # 리소스 불러오기
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 32, 32, 8, 8, 12)      # 플레이어 스프라이트 시트
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        self.spriteSheet_map1 = SpriteSheet('spriteSheet4.png', 16, 16, 16, 16, 87)         # 지형 1 스프라이트 시트

        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.spr_effect = {}     # 효과 스프라이트 세트
        self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        self.spr_enemy = {}      # 적 스프라이트 세트
        self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)

        self.spr_map_struct = {}     # 구조물 스프라이트 세트
        self.spr_map_struct['leaf'] = [55, 56]
        self.spr_map_struct['flower'] = [57, 64]
        self.spr_map_struct['obj'] = [65, 70]
        self.spr_map_struct['sign'] = [71, 74]
        self.spr_map_struct['gravestone'] = [75, 78]
        self.spr_map_struct['skull'] = [79, 80]

        self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # 코인 스프라이트 세트

        createMapData()                                 # 맵 데이터 초기화
        self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # 맵 이미지 생성
        self.backImage = createBackImage(self.spriteSheet_object)         # 배경 이미지 생성

        #효과음
        self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # 적 생성
        for i in range(8):
            obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
            obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)

        # 플레이어 컨트롤 변수
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1

            if floor_map[player_spon_x] != -1:
                player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 4, TILE_MAPSIZE[1] * 2 - 30), (16, 30))  # 플레이어 히트박스
        self.player_movement = [0, 0]            # 플레이어 프레임당 속도
        self.player_vspeed = 0                   # 플레이어 y가속도
        self.player_flytime = 0                  # 공중에 뜬 시간

        self.player_action = 'stay'              # 플레이어 현재 행동
        self.player_frame = 0                    # 플레이어 애니메이션 프레임
        self.player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
        self.player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # 플레이어 공격 타이머
        self.player_attack_speed = 15            # 플레이어 공격 속도

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        pygame.mixer.music.play(loops = -1)


        # 게임 실행
        Game.run(self)

class Game3:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        #게임 컨트롤 변수
        pygame.display.set_caption('RPG tutorial')                                      # 창 이름 설정
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

        self.gameScore = 0       # 점수

        # 리소스 불러오기
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 32, 32, 8, 8, 12)      # 플레이어 스프라이트 시트
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        self.spriteSheet_map1 = SpriteSheet('spriteSheet5.png', 16, 16, 16, 16, 87)         # 지형 1 스프라이트 시트

        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.spr_effect = {}     # 효과 스프라이트 세트
        self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        self.spr_enemy = {}      # 적 스프라이트 세트
        self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)

        self.spr_map_struct = {}     # 구조물 스프라이트 세트
        self.spr_map_struct['leaf'] = [55, 56]
        self.spr_map_struct['flower'] = [57, 64]
        self.spr_map_struct['obj'] = [65, 70]
        self.spr_map_struct['sign'] = [71, 74]
        self.spr_map_struct['gravestone'] = [75, 78]
        self.spr_map_struct['skull'] = [79, 80]

        self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # 코인 스프라이트 세트

        createMapData()                                 # 맵 데이터 초기화
        self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # 맵 이미지 생성
        self.backImage = createBackImage(self.spriteSheet_object)         # 배경 이미지 생성

        #효과음
        self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # 적 생성
        for i in range(8):
            obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
            obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)

        # 플레이어 컨트롤 변수
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1

            if floor_map[player_spon_x] != -1:
                player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 4, TILE_MAPSIZE[1] * 2 - 30), (16, 30))  # 플레이어 히트박스
        self.player_movement = [0, 0]            # 플레이어 프레임당 속도
        self.player_vspeed = 0                   # 플레이어 y가속도
        self.player_flytime = 0                  # 공중에 뜬 시간

        self.player_action = 'stay'              # 플레이어 현재 행동
        self.player_frame = 0                    # 플레이어 애니메이션 프레임
        self.player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
        self.player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # 플레이어 공격 타이머
        self.player_attack_speed = 15            # 플레이어 공격 속도

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        pygame.mixer.music.play(loops = -1)


        # 게임 실행
        Game.run(self)

class Game4:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        #게임 컨트롤 변수
        pygame.display.set_caption('RPG tutorial')                                      # 창 이름 설정
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

        self.gameScore = 0       # 점수

        # 리소스 불러오기
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 32, 32, 8, 8, 12)      # 플레이어 스프라이트 시트
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        self.spriteSheet_map1 = SpriteSheet('spriteSheet6.png', 16, 16, 16, 16, 87)         # 지형 1 스프라이트 시트

        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.spr_effect = {}     # 효과 스프라이트 세트
        self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        self.spr_enemy = {}      # 적 스프라이트 세트
        self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)

        self.spr_map_struct = {}     # 구조물 스프라이트 세트
        self.spr_map_struct['leaf'] = [55, 56]
        self.spr_map_struct['flower'] = [57, 64]
        self.spr_map_struct['obj'] = [65, 70]
        self.spr_map_struct['sign'] = [71, 74]
        self.spr_map_struct['gravestone'] = [75, 78]
        self.spr_map_struct['skull'] = [79, 80]

        self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # 코인 스프라이트 세트

        createMapData()                                 # 맵 데이터 초기화
        self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # 맵 이미지 생성
        self.backImage = createBackImage(self.spriteSheet_object)         # 배경 이미지 생성

        #효과음
        self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # 적 생성
        for i in range(8):
            obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
            obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)

        # 플레이어 컨트롤 변수
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1

            if floor_map[player_spon_x] != -1:
                player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 4, TILE_MAPSIZE[1] * 2 - 30), (16, 30))  # 플레이어 히트박스
        self.player_movement = [0, 0]            # 플레이어 프레임당 속도
        self.player_vspeed = 0                   # 플레이어 y가속도
        self.player_flytime = 0                  # 공중에 뜬 시간

        self.player_action = 'stay'              # 플레이어 현재 행동
        self.player_frame = 0                    # 플레이어 애니메이션 프레임
        self.player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
        self.player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # 플레이어 공격 타이머
        self.player_attack_speed = 15            # 플레이어 공격 속도

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        pygame.mixer.music.play(loops = -1)


        # 게임 실행
        Game.run(self)

class BossStage:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        #게임 컨트롤 변수
        pygame.display.set_caption('RPG tutorial')                                      # 창 이름 설정
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

        self.gameScore = 0       # 점수

        # 리소스 불러오기
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 32, 32, 8, 8, 12)      # 플레이어 스프라이트 시트
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        self.spriteSheet_map1 = SpriteSheet('spriteSheet7.png', 16, 16, 16, 16, 87)        # 지형 1 스프라이트 시트
        self.spriteSheet_boss = SpriteSheet('spriteSheet_boss.png', 64, 64, 4, 4, 12)

        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.spr_effect = {}     # 효과 스프라이트 세트
        self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        self.spr_enemy = {}      # 적 스프라이트 세트
        self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)
        
        self.spr_boss = {}       # 보스 스프라이트 세트
        self.spr_boss['Boss'] = createSpriteSet(self.spriteSheet_boss, 0, 6)
        self.spr_boss['Boss_Dash'] = createSpriteSet(self.spriteSheet_boss, 7, 9)
        self.spr_boss['Boss_Jump'] = createSpriteSet(self.spriteSheet_boss, 10, 11)

        self.spr_map_struct = {}     # 구조물 스프라이트 세트
        self.spr_map_struct['leaf'] = [55, 56]
        self.spr_map_struct['flower'] = [57, 64]
        self.spr_map_struct['obj'] = [65, 70]
        self.spr_map_struct['sign'] = [71, 74]
        self.spr_map_struct['gravestone'] = [75, 78]
        self.spr_map_struct['skull'] = [79, 80]

        self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # 코인 스프라이트 세트

        createBossMapData()                            # 맵 데이터 초기화
        self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # 맵 이미지 생성
        self.backImage = createBackImage(self.spriteSheet_object)         # 배경 이미지 생성

        #효과음
        self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # 적 생성
        for i in range(8):
            obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
            obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)
        
        obj_snake = createObject(self.spr_boss['Boss'], (TILE_MAPSIZE[0], 100), 'Boss', self)  # 레벨 구현 미정
        
        Boss_sponOK = True                        # 보스 생성 설정 변수
        Boss_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(Boss_sponOK):
            Boss_spon_x += 1

            if floor_map[Boss_spon_x] != -1:      # 보스가 땅이 없는 곳에 생성되지 X
                Boss_sponOK = False

        self.Boss_rect = pygame.Rect((Boss_spon_x * 8, TILE_MAPSIZE[1] * 4 - 28), (10, 26))  #  보스 히트박스

        # 플레이어 컨트롤 변수
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1

            if floor_map[player_spon_x] != -1:
                player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 4, TILE_MAPSIZE[1] * 2 - 30), (16, 30))  # 플레이어 히트박스
        self.player_movement = [0, 0]            # 플레이어 프레임당 속도
        self.player_vspeed = 0                   # 플레이어 y가속도
        self.player_flytime = 0                  # 공중에 뜬 시간

        self.player_action = 'stay'              # 플레이어 현재 행동
        self.player_frame = 0                    # 플레이어 애니메이션 프레임
        self.player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
        self.player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # 플레이어 공격 타이머
        self.player_attack_speed = 15            # 플레이어 공격 속도

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        pygame.mixer.music.play(loops = -1)
        
        Game.run(self)

main_menu()