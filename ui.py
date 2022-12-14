import pygame, sys, os, time
from datafile import *
from game import *
from pygame.locals import *
import pygame.mixer


display_width = 960  # 화면 가로 크기
display_height = 640  # 화면 세로 크기
gameDisplay = pygame.display.set_mode((display_width, display_height))  # 화면 크기설정


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