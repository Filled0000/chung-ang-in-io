import pygame, sys, os, time
import pygame.mixer

display_width = 960  # 화면 가로 크기
display_height = 640  # 화면 세로 크기
gameDisplay = pygame.display.set_mode((display_width, display_height))

class Asset:
    
    mainmenu_background = pygame.image.load("assets/background.png")
    mainmenu_start = pygame.image.load("buttons/01.png")
    mainmenu_htp = pygame.image.load("buttons/04.png")
    mainmenu_credit = pygame.image.load("buttons/05.png")
    mainmenu_quit = pygame.image.load("buttons/06.png")
    mainmenu_start_click = pygame.image.load("buttons/01.png")
    mainmenu_htp_click = pygame.image.load("buttons/04.png")
    mainmenu_credit_click = pygame.image.load("buttons/05.png")
    mainmenu_quit_click = pygame.image.load("buttons/06.png")

    continue_button = pygame.image.load("buttons/07.png")
    continue_button_click = pygame.image.load("buttons/07.png") # act 효과
    return_menu_button = pygame.image.load("buttons/08.png")
    return_menu_button_click = pygame.image.load("buttons/08.png") # act 효과

    next_button = pygame.image.load("buttons/09.png")
    next_button_click = pygame.image.load("buttons/09.png") # act 효과

    again_button = pygame.image.load("buttons/10.png")
    again_button_click = pygame.image.load("buttons/10.png") # act 효과

    htp_background = pygame.image.load("assets/background.png") # how to play 사용법 작성한 이미지 파일 업로드
    htp_back = pygame.image.load("buttons/13.png") # back 누를 버튼 이미지
    htp_back_click = pygame.image.load("buttons/13.png")

    credit_background = pygame.image.load("assets/background.png") # how to play 사용법 작성한 이미지 파일 업로드
    credit_back = pygame.image.load("buttons/13.png") # back 누를 버튼 이미지
    credit_back_click = pygame.image.load("buttons/13.png")

    pause_button=pygame.image.load("buttons/03.png")
    pause_button_click=pygame.image.load("buttons/03.png")


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