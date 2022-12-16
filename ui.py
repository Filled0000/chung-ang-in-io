import pygame, sys, os, time
import pygame.mixer

display_width = 960  # ȭ�� ���� ũ��
display_height = 640  # ȭ�� ���� ũ��
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
    continue_button_click = pygame.image.load("buttons/07.png") # act ȿ��
    return_menu_button = pygame.image.load("buttons/08.png")
    return_menu_button_click = pygame.image.load("buttons/08.png") # act ȿ��

    next_button = pygame.image.load("buttons/09.png")
    next_button_click = pygame.image.load("buttons/09.png") # act ȿ��

    again_button = pygame.image.load("buttons/10.png")
    again_button_click = pygame.image.load("buttons/10.png") # act ȿ��

    htp_background = pygame.image.load("assets/background.png") # how to play ���� �ۼ��� �̹��� ���� ���ε�
    htp_back = pygame.image.load("buttons/13.png") # back ���� ��ư �̹���
    htp_back_click = pygame.image.load("buttons/13.png")

    credit_background = pygame.image.load("assets/background.png") # how to play ���� �ۼ��� �̹��� ���� ���ε�
    credit_back = pygame.image.load("buttons/13.png") # back ���� ��ư �̹���
    credit_back_click = pygame.image.load("buttons/13.png")

    pause_button=pygame.image.load("buttons/03.png")
    pause_button_click=pygame.image.load("buttons/03.png")


class Button:  # ��ư
    def __init__(self, img_in,x, y, width, height, img_act, x_act, y_act, action=None):
        #self, �̹���, x,y,����,����, �������� �� �̹���, �������� �� x, �������� �� y, �Լ�ȣ��

        mouse = pygame.mouse.get_pos()  # ���콺 ��ǥ
        click = pygame.mouse.get_pressed()  # Ŭ������
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # ���콺�� ��ư�ȿ� ���� ��
            gameDisplay.blit(img_act, (x_act, y_act))  # ��ư �̹��� ����
            if click[0] and action is not None:  # ���콺�� ��ư�ȿ��� Ŭ���Ǿ��� ��
                time.sleep(0.2) # 2�� ����
                action() # �Լ� ����
        else:
            gameDisplay.blit(img_in, (x, y))