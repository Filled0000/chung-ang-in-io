# [Python pygame Game] RPG tutorial
# Made by "PrintedLove"
# Referred to DaFluffyPotato's 'Physics - Pygame Tutorial: Making a Platformer'
#-*-coding: utf-8

import pygame, sys, os, time
from datafile import *
from pygame.locals import *
import pygame.mixer


pygame.font.init()
        
mainmenu_background = pygame.image.load("assets/background.png")
mainmenu_start = pygame.image.load("assets/menu rect.png")
mainmenu_htp = pygame.image.load("assets/how rect.png")
mainmenu_credit = pygame.image.load("assets/menu rect.png")
mainmenu_quit = pygame.image.load("assets/menu rect.png")
mainmenu_start_click = pygame.image.load("assets/menu rect.png")
mainmenu_htp_click = pygame.image.load("assets/how rect.png")
mainmenu_credit_click = pygame.image.load("assets/menu rect.png")
mainmenu_quit_click = pygame.image.load("assets/menu rect.png")

simple_button = pygame.image.load("assets/play rect.png")
simple_button2 = pygame.image.load("assets/quit rect.png")

htp_background = pygame.image.load("assets/background.png") # how to play 사용법 작성한 이미지 파일 업로드
htp_back = pygame.image.load("assets/menu rect.png") # back 누를 버튼 이미지
htp_back_click = pygame.image.load("assets/menu rect.png")

credit_background = pygame.image.load("assets/background.png") # how to play 사용법 작성한 이미지 파일 업로드
credit_back = pygame.image.load("assets/menu rect.png") # back 누를 버튼 이미지
credit_back_click = pygame.image.load("assets/menu rect.png")

display_width = 960  # 화면 가로 크기
display_height = 640  # 화면 세로 크기
gameDisplay = pygame.display.set_mode((display_width, display_height))  # 화면 크기설정
pygame.display.set_caption("CAU KIUGI")  # 타이틀
clock = pygame.time.Clock()

# 폰트 설정
#def get_font(size): # Returns Press-Start-2P in the desired size
#    return pygame.font.Font("assets/font.ttf", size) 

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

class Button:  # 버튼
    def __init__(self, img_in,x, y, width, height, img_act, x_act, y_act, action=None):
        #self, 이미지, x,y,넓이,높이, 반응했을 때 이미지, 반응했을 때 x, 반응했을 때 y, 함수호출

        mouse = pygame.mouse.get_pos()  # 마우스 좌표
        click = pygame.mouse.get_pressed()  # 클릭여부
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # 마우스가 버튼안에 있을 때
            gameDisplay.blit(img_act, (x_act, y_act))  # 버튼 이미지 변경
            if click[0] and action is not None:  # 마우스가 버튼안에서 클릭되었을 때
                time.sleep(0.2) # 2초 간격
                action() # 함수 실행
        else:
            gameDisplay.blit(img_in, (x, y))



def main_menu():
    global pause
    pause=False
    menu = True

    largeText = pygame.font.SysFont("font",115)
    TextSurf, TextRect = text_objects("Title", largeText, "White")
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


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
        self.spriteSheet_player = SpriteSheet('spriteSheet1.png', 16, 16, 8, 8, 12)      # 플레이어 스프라이트 시트
        self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        self.spriteSheet_map1 = SpriteSheet('spriteSheet3.png', 8, 8, 16, 16, 87)         # 지형 1 스프라이트 시트

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

        self.player_rect = pygame.Rect((player_spon_x * 8, TILE_MAPSIZE[1] * 4 - 14), (6, 14))  # 플레이어 히트박스
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

    def run(self):

        global pause

        # 메인 루프
        while True:
            self.screen_scaled.fill(BACKGROUND_COLOR)            # 화면 초기화

            self.camera_scroll[0] += int((self.player_rect.x - self.camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
            self.camera_scroll[1] += int((self.player_rect.y - self.camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

            self.screen_scaled.blit(self.backImage, (0, 0))                                   # 배경 드로우
            self.screen_scaled.blit(self.mapImage, (-self.camera_scroll[0], -self.camera_scroll[1]))    # 맵 드로우

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

            for obj in objects:         # 오브젝트 이벤트 처리
                if obj.destroy:
                    obj.destroy_self()
                else:
                    obj.events()
                    obj.draw()
                    obj.physics_after()

            self.screen_scaled.blit(self.mapImage_front, (-self.camera_scroll[0], -self.camera_scroll[1]))    # 프론트 맵 드로우

            draw_text(self.screen_scaled, "SCORE: " + str(self.gameScore), 8, (238, 238, 230), 200, 140)

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
                        self.player_vspeed = -3.5
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

            pygame.display.update()
            self.clock.tick(60)

#game = Game()   # 게임 실행

main_menu()