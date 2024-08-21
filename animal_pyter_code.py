import pygame
import os
import time


pygame.init()
#색상
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (230,220,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)
blue=(0,0,204)
light_blue=(51,51,235)
gray = (53, 53, 53)
light_gray = (102,102,102)
purple = (123,104,238)
light_purple = (147,112,219)
coral = (255,189,174)

#화면크기
size = [1400,700] # diplay size
display_width = size[0]
display_height = size[1] 
screen=pygame.display.set_mode(size)
player_width = display_width / 12
player_height = display_height/3

#파일위치
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images") 
sound_path = os.path.join(current_path, "sounds")

#이미지로드
gamestart = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "gamestart.png")),(display_width,display_height))
uidstart1 = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "1puid.png")),(display_width,display_height))
uidstart2 = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "2puid.png")),(display_width,display_height))
back_space = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "back_space.png")),(display_width,display_height))
back_beach = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "back_beach.png")),(display_width,display_height))
back_city = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "back_city.png")),(display_width,display_height))
game_manual_eng = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "game_manual_eng.png")),(display_width,display_height))
game_manual_kor = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "game_manual_kor.png")),(display_width,display_height))
logo = pygame.image.load(os.path.join(image_path, "logo.png"))
check = pygame.image.load(os.path.join(image_path, "check.png"))

#필살기사진
satk_fox=pygame.transform.scale(pygame.image.load(os.path.join(image_path, "satk_fox.png")),(150,100))
satk_bear=pygame.transform.scale(pygame.image.load(os.path.join(image_path, "satk_bear.png")),(150,100))
satk_cat=pygame.transform.scale(pygame.image.load(os.path.join(image_path, "satk_cat.png")),(150,100))
satk_dog=pygame.transform.scale(pygame.image.load(os.path.join(image_path, "satk_dog.png")),(150,100))

#캐릭터선택사진
select_dog = pygame.image.load(os.path.join(image_path, "select_dog.png"))
select_bear = pygame.image.load(os.path.join(image_path, "select_bear.png"))
select_fox = pygame.image.load(os.path.join(image_path, "select_fox.png"))
select_cat = pygame.image.load(os.path.join(image_path, "select_cat.png"))
p1_select_eng = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "p1selectanimal_eng.png")),(display_width,display_height))
p2_select_eng = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "p2selectanimal_eng.png")),(display_width,display_height))
p1_select_kor = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "p1selectanimal_kor.png")),(display_width,display_height))
p2_select_kor = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "p2selectanimal_kor.png")),(display_width,display_height))
option_select_eng = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "option_select_eng.png")),(display_width,display_height))
option_select_kor = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "option_select_kor.png")),(display_width,display_height))

#커스텀사진
iscustom_kor = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "iscustom_kor.png")),(display_width,display_height))
iscustom_eng = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "iscustom_eng.png")),(display_width,display_height))
custom_eng = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "custom_eng.png")),(display_width,display_height))
custom_kor = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "custom_kor.png")),(display_width,display_height))
mode_select_eng = pygame.image.load(os.path.join(image_path, "mode_select_eng.png"))
mode_select_kor = pygame.image.load(os.path.join(image_path, "mode_select_kor.png"))

#5판3선용 승리 박스
wincheckbox=pygame.transform.scale(pygame.image.load(os.path.join(image_path, "checkedbox.png")),(40,60))
winbox=pygame.transform.scale(pygame.image.load(os.path.join(image_path, "winbox.png")),(120,60))

#초기모드선택값설정 선택되면 True , 기본 False
ck1=False #5판3선승제
ck2=False#1p핸디캡
ck3=False#2p핸디캡
ck4=False#무한필살기
ck5=False#연습모드

#5판3선승제시 p1 p2 승리 횟수
p1win=0
p2win=0

#jump구현을 위한 질량값
MASS =2

#폰트
game_font = pygame.font.Font('DungGeunMo.ttf', 150)
smallfont = pygame.font.Font('DungGeunMo.ttf', 25)
small2font = pygame.font.Font('DungGeunMo.ttf', 35)
medfont = pygame.font.Font('DungGeunMo.ttf', 50)
largefont = pygame.font.Font('DungGeunMo.ttf', 80)
extralargefont = pygame.font.Font('DungGeunMo.ttf', 250)

#커스터마이징 
weapon1_color = 'none'
punch1_color = 'none'
damage1_size = 'none'

weapon2_color = 'none'
punch2_color = 'none'
damage2_size = 'none'

weapon1_point =0
punch1_point = 0
damage1_point =0
 
weapon2_point =0
punch2_point = 0
damage2_point =0

p1_custom_atk=0
p2_custom_atk=0

# 사운드 파일
weapon_sound = pygame.mixer.Sound(os.path.join(sound_path,'weapon.wav'))
jump_sound = pygame.mixer.Sound(os.path.join(sound_path,'jump.wav'))
hurt_sound = pygame.mixer.Sound(os.path.join(sound_path,'hurt.wav'))
punch_sound = pygame.mixer.Sound(os.path.join(sound_path,'punch.wav'))
city_sound = pygame.mixer.Sound(os.path.join(sound_path,'city_sound.wav'))
space_sound = pygame.mixer.Sound(os.path.join(sound_path,'space_sound.wav'))
beach_sound = pygame.mixer.Sound(os.path.join(sound_path,'beach_sound.wav'))
click_sound = pygame.mixer.Sound(os.path.join(sound_path,'click.wav'))
tick_sound = pygame.mixer.Sound(os.path.join(sound_path,'tick.wav'))
uid_sound = pygame.mixer.Sound(os.path.join(sound_path,'uid.wav'))
mp_sound = pygame.mixer.Sound(os.path.join(sound_path,'mp.wav'))
bear_sound = pygame.mixer.Sound(os.path.join(sound_path,'bear.wav'))
cat_sound = pygame.mixer.Sound(os.path.join(sound_path,'cat.wav'))
dog_sound = pygame.mixer.Sound(os.path.join(sound_path,'dog.wav'))
fox_sound = pygame.mixer.Sound(os.path.join(sound_path,'fox.wav'))

#옵션 변수
bgm_option = 0.5
effect_option = 0.9
lan_option = 'korean'
back_option = 'city'

#FPS
clock=pygame.time.Clock()
clock.tick(60)
p1_animal=[0]
p2_animal=[0]

#p1,p2 포인트 값, id init
p1_point=0
p2_point=0
p1_id=""
p2_id=""
text1p=""
text2p = ""
p1_total_point = p1_point - weapon1_point - punch1_point - damage1_point
p2_total_point = p2_point - weapon2_point - punch2_point - damage2_point   

#캡션
title="Animal pyter"
pygame.display.set_caption(title)
pygame.display.set_icon(logo)

def text_objects(text, color, text_size):
    if text_size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif text_size == 'small2':
        textSurface = small2font.render(text, True, color)
    elif text_size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif text_size == 'large':
        textSurface = largefont.render(text, True, color)
    elif text_size == 'extralarge':
        textSurface = extralargefont.render(text, True, color)        
    return textSurface, textSurface.get_rect()    

def message_to_screen(msg,color, x_displace=0, y_displace=0, text_size='small'):
    textSurf, textRect = text_objects(msg, color, text_size)
    textRect.center = (size[0]/2)+x_displace, (size[1]/2)+y_displace
    screen.blit(textSurf, textRect)

def button_text(msg,color,btnx,btny,btnw,btnh,text_size='small'):
    textSurf, textRect = text_objects(msg,color,text_size)
    textRect.center = (btnx+btnw/2, btny+btnh/2)
    screen.blit(textSurf, textRect)

def button(text,x,y,w,h,inactive_color,active_color, action = None):
    
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    click_sound.set_volume(effect_option)
    if x + w > cur[0] > x and y + h > cur[1] > y:            
        pygame.draw.rect(screen, active_color, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'quit':
                click_sound.play()
                pygame.quit()
            elif action == 'select':
                click_sound.play()
                return (Select_animal())
            elif action == 'option':
                click_sound.play()
                return (Option())
            elif action =='mode':
                click_sound.play()
                return (Mode())
            elif action =='custom':
                click_sound.play()
                return (Custom())
            elif action =='game':
                click_sound.play()
                return (Game())
            elif action =='manual':
                click_sound.play()
                return (Manual())
            elif action =='Exit':
                click_sound.play()
                return 1    
    else:
        pygame.draw.rect(screen, inactive_color, (x,y,w,h))
    button_text(text,black,x,y,w,h)

def button_c(text,x,y,w,h,inactive_color,active_color, action = None):
    
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > cur[0] > x and y + h > cur[1] > y:            
        pygame.draw.rect(screen, active_color, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
            elif action == 'select':
                return (Select_animal())
            elif action == 'option':
                return (Option())
            elif action =='mode':
                return (Mode())
            elif action =='custom':
                return (Custom())
            elif action =='manual':
                return (Manual())
    else:
        pygame.draw.rect(screen, inactive_color, (x,y,w,h))
    button_text(text,red,x,y,w,h)
            
def Option():

    global bgm_option,effect_option,lan_option,back_option
    optionselect = True
    x,y,w,h=size[0]/2-180,size[1]/2-150,80,80 
    while optionselect:
        if lan_option == 'english':
            screen.blit(option_select_eng,(0,0))
        elif lan_option == 'korean':
            screen.blit(option_select_kor,(0,0))    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if lan_option == 'english':
            button("COMPLETE",x+600,y-150,w+90,h,green,light_green,None)
        if lan_option == 'korean':
            button("완료",x+600,y-150,w+90,h,green,light_green,None) 
        
        button("0",x-220,y-30,w,h,white,black,None)
        button("1",x-20,y-30,w,h,white,black,None)
        button("2",x+180,y-30,w,h,white,black,None)
        button("3",x+380,y-30,w,h,white,black,None)
       
        if bgm_option== 0:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-220,y-30)) 

        elif bgm_option== 0.3:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-20,y-30))
            
        elif bgm_option== 0.5:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+180,y-30))
        elif bgm_option== 0.9:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+380,y-30))        
        
        button("0",x-220,y+100,w,h,white,black,None)
        button("1",x-20,y+100,w,h,white,black,None)
        button("2",x+180,y+100,w,h,white,black,None)
        button("3",x+380,y+100,w,h,white,black,None)
        
        if effect_option== 0:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-220,y+100))    
        elif effect_option== 0.3:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-20,y+100))
        elif effect_option== 0.5:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+180,y+100))
        elif effect_option== 0.9:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+380,y+100))
        
        if lan_option == 'english':
            button("KOREAN",x-220,y+220,w+90,h,white,black,None)
            button("ENGLISH",x+180,y+220,w+90,h,white,black,None)
        elif lan_option == 'korean':
            button("한국어",x-220,y+220,w+90,h,white,black,None)
            button("영어",x+180,y+220,w+90,h,white,black,None)
        if lan_option== 'korean':
            screen.blit(pygame.transform.scale(check,(w,h)),(x-180,y+220))    
        elif lan_option== 'english':
            screen.blit(pygame.transform.scale(check,(w,h)),(x+220,y+220))
        if lan_option == 'english':
            button("BEACH",x-220,y+340,w+90,h,white,black,None)
            button("SPACE",x+30,y+340,w+90,h,white,black,None)
            button("CITY",x+290,y+340,w+90,h,white,black,None)
        elif lan_option == 'korean':
            button("해변",x-220,y+340,w+90,h,white,black,None)
            button("우주",x+30,y+340,w+90,h,white,black,None)
            button("도시",x+290,y+340,w+90,h,white,black,None)
        if back_option == 'beach':
            screen.blit(pygame.transform.scale(check,(w,h)),(x-180,y+340))    
        elif back_option== 'space':
            screen.blit(pygame.transform.scale(check,(w,h)),(x+70,y+340))
        elif back_option== 'city':
            screen.blit(pygame.transform.scale(check,(w,h)),(x+330,y+340))

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        tick_sound.set_volume(effect_option)
        click_sound.set_volume(effect_option)
        
        if x + 600+ w+90 > cur[0] > x + 600 and y - 150 + h > cur[1] > y - 150:
            if click[0] == 1:
                click_sound.play()
                optionselect=False

        #배경음 설정
        elif x-220 + w > cur[0] > x-220 and y-30 + h > cur[1] > y-30:
            if click[0] == 1:
                tick_sound.play()
                bgm_option = 0
                pygame.mixer.music.set_volume(0)
        elif x-20 + w > cur[0] > x-20 and y-30 + h > cur[1] > y-30:
            if click[0] == 1:
                tick_sound.play()
                bgm_option = 0.3 
                pygame.mixer.music.set_volume(0.3)
        elif x+180 + w > cur[0] > x+180 and y-30 + h > cur[1] > y-30:
            if click[0] == 1:
                tick_sound.play()
                bgm_option = 0.5   
                pygame.mixer.music.set_volume(0.5)
        elif x+380 + w > cur[0] > x+380 and y-30 + h > cur[1] > y-30:
            if click[0] == 1:
                tick_sound.play()
                bgm_option = 0.9   
                pygame.mixer.music.set_volume(0.9)

        #효과음 설정
        elif x-220 + w > cur[0] > x-220 and y+100 + h > cur[1] > y+100:
            if click[0] == 1:
                tick_sound.play()
                effect_option = 0                  
        elif x-20 + w > cur[0] > x-20 and y+100 + h > cur[1] > y+100:
            if click[0] == 1:
                tick_sound.play()
                effect_option = 0.3  
        elif x+180 + w > cur[0] > x+180 and y+100 + h > cur[1] > y+100:
            if click[0] == 1:
                tick_sound.play()
                effect_option = 0.5  
        elif x+380 + w > cur[0] > x+380 and y+100 + h > cur[1] > y+100:
            if click[0] == 1:
                tick_sound.play()
                effect_option = 0.9

        #언어 설정
        elif x-220 + w+90 > cur[0] > x-220 and y+220 + h > cur[1] > y+220:
            if click[0] == 1:
                tick_sound.play()
                lan_option = 'korean'   
        elif x+180 + w+90 > cur[0] > x+180 and y+220 + h > cur[1] > y+220:
            if click[0] == 1:
                tick_sound.play()
                lan_option = 'english'      
                
        # 배경화면 설정
        elif x-220 + w+90 > cur[0] > x-220 and y+340 + h > cur[1] > y+340:
            if click[0] == 1:
                tick_sound.play()
                back_option = 'beach'   
        elif x+30 + w+90 > cur[0] > x+30 and y+340 + h > cur[1] > y+340:
            if click[0] == 1:
                tick_sound.play()
                back_option = 'space'   
        elif x+290 + w+90 > cur[0] > x+290 and y+340 + h > cur[1] > y+340:
            if click[0] == 1:
                tick_sound.play()
                back_option = 'city'
                        
        pygame.display.update()
        

def Game_start():  
    pygame.mixer.music.load(os.path.join(sound_path,'gamestart.wav'))
    pygame.mixer.music.play(-1)
    start = True
    global text1p , text2p
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(gamestart,(0,0))       
        message_to_screen( str(text1p), black ,-410,58, 'small2')
        message_to_screen( str(p1_point), black ,-405,109, 'small2')
        message_to_screen(str(text2p), black ,+410,57, 'small2')
        message_to_screen(str(p2_point), black ,+415,109, 'small2')
        
        if lan_option == 'english':
            button("GAME START",size[0]/2-150,size[1]/2-50,300,70,green,light_green,'select')
            button("OPTION",size[0]/2-150,size[1]/2+50,300,70,yellow,light_yellow,'option')
            button("MODE",size[0]/2-150,size[1]/2+150,300,70,blue,light_blue,'mode')
            button("Game Manual",size[0]/2-150,size[1]/2+250,300,70,purple,light_purple, 'manual') 
            button("QUIT",size[0]/2+350,size[1]/2+250,150,70,red,light_red, 'quit')       
        if lan_option == 'korean':
            button("게임시작",size[0]/2-150,size[1]/2-50,300,70,green,light_green,'select')
            button("환경설정",size[0]/2-150,size[1]/2+50,300,70,yellow,light_yellow,'option')
            button("모드선택",size[0]/2-150,size[1]/2+150,300,70,blue,light_blue,'mode')
            button("게임 설명",size[0]/2-150,size[1]/2+250,300,70,purple,light_purple, 'manual') 
            button("나가기",size[0]/2+350,size[1]/2+250,150,70,red,light_red, 'quit')   
       
        pygame.display.update()
    start = False
    
def Manual():
    manual_state = True
    x,y,w,h=size[0]/2-180,size[1]/2-150,80,80 
    while manual_state :
        if lan_option == 'english':
            screen.blit(game_manual_eng,(0,0))
            button("COMPLETE",x+600,y-150,w+90,h,green,light_green,None)
        elif lan_option == 'korean':
            screen.blit(game_manual_kor,(0,0))    
            button("완료",x+600,y-150,w+90,h,green,light_green,None)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        click_sound.set_volume(effect_option)
        if x + 600+ w+90 > cur[0] > x + 600 and y - 150 + h > cur[1] > y - 150:
            if click[0] == 1:
                click_sound.play()
                manual_state = False
        pygame.display.update()
        
def Mode():  
    modeselect=True
    x,y,w,h=size[0]/2-180,size[1]/2-150,40,30 
    global ck1,ck2,ck3,ck4,ck5
    
    while modeselect:
        if lan_option == 'english':
            screen.blit(pygame.transform.scale(mode_select_eng,(display_width,display_height)),(0,0))
            message_to_screen("YES  /  NO", blue,-350,-50, 'small')
            message_to_screen("YES  /  NO", blue,+380,-60, 'small')
        elif  lan_option == 'korean':
            screen.blit(pygame.transform.scale(mode_select_kor,(display_width,display_height)),(0,0))   
            message_to_screen("예  / 아니요", blue,-350,-50, 'small')
            message_to_screen("예  / 아니요", blue,+380,-60, 'small')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        button("",x-230,y+122,w,h,black,white,None)
        button("",x-230,y+215,w,h,black,white,None)
        button("",x-230,y+310,w,h,black,white,None)
        button("",x+500,y+115,w,h,black,white,None)
        button("",x+500,y+210,w,h,black,white,None)
        
        button("",x-150,y+122,w,h,black,white,None)
        button("",x-150,y+215,w,h,black,white,None)
        button("",x-150,y+310,w,h,black,white,None)
        button("",x+580,y+115,w,h,black,white,None)
        button("",x+580,y+210,w,h,black,white,None)
       
        if ck1 == False:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-150,y+122))     
        if ck2 == False:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-150,y+215))    
        if ck3 == False:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-150,y+310)) 
        if ck4 == False:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+580,y+115)) 
        if ck5 == False:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+580,y+210))   
                   
        if ck1 == True:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-230,y+122))     
        if ck2 == True:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-230,y+215))    
        if ck3 == True:
            screen.blit(pygame.transform.scale(check,(w,h)),(x-230,y+310)) 
        if ck4 == True:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+500,y+115)) 
        if ck5 == True:
            screen.blit(pygame.transform.scale(check,(w,h)),(x+500,y+210))   
        if lan_option == 'english':
            button("COMPLETE",x+450,y+300,w+120,h+50,green,light_green,None)
        if lan_option == 'korean':
            button("완료",x+450,y+300,w+120,h+50,green,light_green,None) 
        
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        tick_sound.set_volume(effect_option)
        click_sound.set_volume(effect_option)
        if x+450+ w+120 > cur[0] > x+450 and y+300 + h+50 > cur[1] > y+300:
            if click[0] == 1:
                click_sound.play()
                modeselect=False
                  
        if x-230 + w > cur[0] > x-230 and y+122 +h> cur[1] > y+122:
            if click[0] == 1:
                tick_sound.play()
                ck1=True    
                
        if x-230+ w > cur[0] > x-230 and y+215 + h > cur[1] > y+215:
            if click[0] == 1:
                tick_sound.play()
                ck2=True
        if x-230+ w > cur[0] > x-230 and y+310 + h > cur[1] > y+310:
            if click[0] == 1:
                tick_sound.play()
                ck3=True
        if x+500 +w > cur[0] > x+500 and y+115 + h > cur[1] > y+115:
            if click[0] == 1:
                tick_sound.play()
                ck4=True
        if x+500+ w > cur[0] > x+500 and y+210 + h > cur[1] > y+210:
            if click[0] == 1:
                tick_sound.play()
                ck5=True
        
        if x-150 + w > cur[0] > x-150 and y+122 +h> cur[1] > y+122:
            if click[0] == 1:
                tick_sound.play()
                ck1=False         
        if x-150+ w > cur[0] > x-150 and y+215 + h > cur[1] > y+215:
            if click[0] == 1:
                tick_sound.play()
                ck2=False
        if x-150+ w > cur[0] > x-150 and y+310 + h > cur[1] > y+310:
            if click[0] == 1:
                tick_sound.play()
                ck3=False
        if x+580 +w > cur[0] > x+580 and y+115 + h > cur[1] > y+115:
            if click[0] == 1:
                tick_sound.play()
                ck4=False
        if x+580+ w > cur[0] > x+580 and y+210 + h > cur[1] > y+210:
            if click[0] == 1:
                tick_sound.play()
                ck5=False
        pygame.display.update()
    
def Select_animal():
    global p1_animal, p2_animal,p1_point,p2_point
    time.sleep(0.5)
    p1_animal = Animals(1)
    time.sleep(0.5) 
    p2_animal = Animals(2)
    time.sleep(0.5) 
    if str(p1_point) == '0' and str(p2_point) == '0':
        return (Game())
    else: return (Iscustom())

def Animals(amimalrselect):
    
    select = True
    x,y,w,h=size[0]/2-180,size[1]/2-150,190,280         
    if amimalrselect == 1:
        if lan_option == 'english':
            screen.blit(p1_select_eng,(0,0))
        elif lan_option == 'korean':
            screen.blit(p1_select_kor,(0,0))    
    elif amimalrselect == 2:
        if lan_option == 'english':
            screen.blit(p2_select_eng,(0,0))
        elif lan_option == 'korean':
            screen.blit(p2_select_kor,(0,0))    
        
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        button("",x-400,y,w,h,black,white,None)
        screen.blit(pygame.transform.scale(select_dog,(w-10,h-10)),(x-396,y+5))
      
        button("",x-90,y,w,h,black,white,None)
        screen.blit(pygame.transform.scale(select_fox,(w-10,h-10)),(x-85,y+5))
        
        button("",x+235,y,w,h,black,white,None)
        screen.blit(pygame.transform.scale(select_cat,(w-10,h-10)),(x+240,y+5))
       
        button("",x+590,y,w,h,black,white,None)
        screen.blit(pygame.transform.scale(select_bear,(w-10,h-10)),(x+595,y+5))
       
        if lan_option == 'english':
            message_to_screen("Dog", blue, -485,150, 'medium')
            message_to_screen("Fox", blue, -175,150, 'medium')
            message_to_screen("Cat", blue, 150 ,150, 'medium')
            message_to_screen("Bear", blue, 505 ,150, 'medium')
            message_to_screen("Special", red, -650,195, 'small')
            message_to_screen("Attack", red, -650,215, 'small')
            
            message_to_screen("Attack speed UP", gray, -485,200, 'small')
            message_to_screen("Neutralize Attack", gray, -175,200, 'small')
            message_to_screen("HP Recover", gray, 150,200, 'small')
            message_to_screen("Damage UP", gray, 505,200, 'small')
            
            message_to_screen("speed", red, -650,260, 'small')
            message_to_screen("6", gray, -485,260, 'small')
            message_to_screen("5", gray, -175,260, 'small')
            message_to_screen("7", gray, 150,260, 'small')
            message_to_screen("5", gray, 505,260, 'small')
            
            message_to_screen("Damage", red, -650,310, 'small')
            message_to_screen("4", gray, -485,310, 'small')
            message_to_screen("5", gray, -175,310, 'small')
            message_to_screen("4", gray, 150,310, 'small')
            message_to_screen("6", gray, 505,310, 'small')
            
        elif lan_option == 'korean':
            message_to_screen("개", blue,-485,150, 'medium')
            message_to_screen("여우", blue, -175,150, 'medium')
            message_to_screen("고양이", blue, 150 ,150, 'medium')
            message_to_screen("곰", blue, 505 ,150, 'medium')
            
            message_to_screen("필살기", red, -650,200, 'small')
            message_to_screen("공격 속도 증가", gray, -485,200, 'small')
            message_to_screen("적 공격 무력화", gray, -175,200, 'small')
            message_to_screen("체력 회복", gray, 150,200, 'small')
            message_to_screen("공격력 증가", gray, 505,200, 'small')
            
            message_to_screen("이동속도", red, -650,260, 'small')
            message_to_screen("6", gray, -485,260, 'small')
            message_to_screen("5", gray, -175,260, 'small')
            message_to_screen("7", gray, 150,260, 'small')
            message_to_screen("5", gray, 505,260, 'small')
            
            message_to_screen("공격력", red, -650,310, 'small')
            message_to_screen("4", gray, -485,310, 'small')
            message_to_screen("5", gray, -175,310, 'small')
            message_to_screen("4", gray, 150,310, 'small')
            message_to_screen("6", gray, 505,310, 'small')
            
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        click_sound.set_volume(effect_option)
        # p0_animal = [character, speed, jump speed , punch damage]
       
        if x-400 + w > cur[0] > x-400 and y + h > cur[1] > y:
            if click[0] == 1:     
                click_sound.play()
                return ['dog' , 6 , 11 ,4 ]  
        if x-90+ w > cur[0] > x-90 and y + h > cur[1] > y:
            if click[0] == 1:
                click_sound.play()
                return ['fox' , 6 , 11, 5]
        if x+235 + w > cur[0] > x + 235 and y + h > cur[1] > y:
            if click[0] == 1:
                click_sound.play()
                return ['cat' , 7, 11 , 4]    
        if x+590 + w > cur[0] > x+590 and y + h > cur[1] > y:
            if click[0] == 1:
                click_sound.play()
                return ['bear' , 5 , 9 ,6]
            
        pygame.display.update()
        clock.tick(60)
    select = False

def Iscustom():
    clock=pygame.time.Clock()
    if lan_option == 'english':
        screen.blit(iscustom_eng,(0,0))
    elif lan_option == 'korean':
        screen.blit(iscustom_kor,(0,0)) 
    iscustom = True
    x,y,w,h=size[0]/2,size[1]/2,150,250
    while iscustom:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        message_to_screen(str(p1_point), black ,x-1200,y-350, 'medium')
        message_to_screen(str(p2_point), black ,x-200,y-350, 'medium')
        if lan_option == 'english':
            button("YES",x-250,y+200,w,h-150,red,light_blue,'custom') 
            button("NO",x+150,y+200,w,h-150,red,light_blue,'game')
        elif lan_option == 'korean':

            button("네",x-250,y+200,w,h-150,red,light_blue,'custom') 
            button("아니오",x+150,y+200,w,h-150,red,light_blue,'game')
        pygame.display.update()
        clock.tick(60)
        
def Custom():
    clock=pygame.time.Clock()
    global lan_option, p1_animal, p2_animal, weapon1_color, punch1_color, damage1_size, weapon2_color, punch2_color, damage2_size,p1_point,p2_point,weapon1_point,punch1_point,damage1_point,weapon2_point,punch2_point,damage2_point
    global p1_total_point,p2_total_point,p1_custom_atk,p2_custom_atk
    
    customizing = True
    x,y,w,h=size[0]/2,size[1]/2,150,250
    
    if lan_option == 'english':
        screen.blit(custom_eng,(0,0))
    elif lan_option == 'korean':
        screen.blit(custom_kor,(0,0)) 
    
    while customizing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if lan_option == 'english':
            button("COMPLETE",x-65,y+230,w-10,h-190,green,light_green,None)
        elif lan_option == 'korean':
            button("완료",x-65,y+230,w-10,h-190,green,light_green,None) 
        
        if str(p1_point) == '0' : #p1 포인트 0 
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(p1_animal[0])+"sp_00.png")),(w,h)),(x-600,y-180))
            message_to_screen("P1 point is 0", red, x-1200,y-200, 'medium')
           
        else :#p1포인트 > 0
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(p1_animal[0])+"sp_00.png")),(w,h)),(x-600,y-180))
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(punch1_color)+"_attack1.png")),(60,60)),(x-670,y-180))
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(weapon1_color)+"_weapon.png")),(80,60)),(x-690,y-100))
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(damage1_size)+"damage.png")),(50,30)),(x-550,y-230))
            button("P1 point : "+str(p1_point - weapon1_point - punch1_point - damage1_point), x-700,y+70,w+150,h-200,coral,coral,None)    
            if lan_option == 'english':
                message_to_screen("WEAPON COLOR ( -50 Point )", gray ,x-700,y-500, 'small2')
                message_to_screen("PUNCH COLOR ( -50 Point )", gray ,x-700,y-350, 'small2')
                message_to_screen("DAMAGE UP ( -300 / -500 Point )", gray ,x-700,y-200, 'small2')
                button_c("Weapon color : " + str( weapon1_color),x-700,y+120,w+150,h-200,coral,coral,None)
                button_c("punch color : "+ str( punch1_color),x-700,y+170,w+150,h-200,coral,coral,None)
                button_c("Damage + "+ str(damage1_size),x-700,y+220,w+150,h-200,coral,coral,None)
            elif lan_option == 'korean':
                message_to_screen("무기 색상 ( -50 Point )", gray ,x-700,y-500, 'small2')
                message_to_screen("펀치 색상 ( -50 Point )", gray ,x-700,y-350, 'small2')
                message_to_screen("공격력 증가 ( -300 / -500 Point )", gray ,x-700,y-200, 'small2')  
                button_c("무기 색상 : " + str( weapon1_color),x-700,y+120,w+150,h-200,coral,coral,None)
                button_c("펀치 색상 : "+ str( punch1_color),x-700,y+170,w+150,h-200,coral,coral,None)
                button_c("공격력 + "+ str(damage1_size),x-700,y+220,w+150,h-200,coral,coral,None)
            #무기색상
            button("",x-370,y-100,w-100,h-200,blue,light_blue,None)
            button("",x-290,y-100,w-100,h-200,yellow,light_yellow,None)
            button("",x-210,y-100,w-100,h-200,green,light_green,None)
            button("NONE",x-130,y-100,w-100,h-200,white,black,None)
            #펀치 색상
            button("",x-370,y+50,w-100,h-200,blue,light_blue,None)
            button("",x-290,y+50,w-100,h-200,yellow,light_yellow,None)
            button("",x-210,y+50,w-100,h-200,green,light_green,None)
            button("NONE",x-130,y+50,w-100,h-200,white,black,None)
            #공격 데미지
            button("+ 3",x-370,y+200,w-100,h-200,white,black,None)
            button("+ 5",x-290,y+200,w-100,h-200,white,black,None)         
            button("NONE",x-210,y+200,w-100,h-200,white,black,None)         
            
            if weapon1_color == 'blue': 
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-370,y-100)) 
                if p1_total_point>=50:
                    weapon1_point = 50
            elif weapon1_color == 'yellow':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-290,y-100))
                if p1_total_point>=50:
                    weapon1_point = 50
            elif weapon1_color == 'green':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-210,y-100))
                if p1_total_point>=50:
                    weapon1_point = 50
            elif weapon1_color == 'none':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-130,y-100))
                button_c("                 ",x-700,y+120,w+150,h-200,coral,coral,None)
                weapon1_point = 0
                    
            if punch1_color == 'blue': 
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-370,y+50)) 
                if p1_total_point>=50:
                    punch1_point = 50
            elif punch1_color == 'yellow':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-290,y+50))
                if p1_total_point>=50:
                    punch1_point = 50
            elif punch1_color == 'green':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-210,y+50))
                if p1_total_point>=50:
                    punch1_point = 50
            elif punch1_color == 'none':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-130,y+50))
                button_c("                 ",x-700,y+170,w+150,h-200,coral,coral,None)
                punch1_point = 0
                
            if damage1_size == '3': 
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-370,y+200)) 
                if p1_total_point>=300:
                    damage1_point = 300
                    p1_custom_atk=3

            elif damage1_size == '5':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-290,y+200))
                if p1_total_point>=500:
                    damage1_point = 500
                    p1_custom_atk=5
            elif damage1_size == 'none':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x-210,y+200))
                button_c("          ",x-700,y+220,w+150,h-200,coral,coral,None)  
                damage1_point = 0
            
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            tick_sound.set_volume(effect_option)
            if x-370 + w-100 > cur[0] > x-370 and y-100 + h-200 > cur[1] > y-100 and p1_total_point>= 50:
                if click[0] == 1:    
                    tick_sound.play()
                    weapon1_color = 'blue'
            elif x-290 + w-100 > cur[0] > x-290 and y-100 + h-200 > cur[1] > y-100 and p1_total_point>= 50:
                if click[0] == 1:
                    tick_sound.play()
                    weapon1_color = 'yellow'
            elif x-210 + w-100 > cur[0] > x-210 and y-100 + h-200 > cur[1] > y-100 and p1_total_point>= 50:
                if click[0] == 1:    
                    tick_sound.play()
                    weapon1_color = 'green'           
            elif x-130 + w-100 > cur[0] > x-130 and y-100 + h-200 > cur[1] > y-100:
                if click[0] == 1:
                    tick_sound.play()
                    weapon1_color = 'none'
           
            if x-370 + w-100 > cur[0] > x-370 and y+50 + h-200 > cur[1] > y+50 and p1_total_point>= 50:
                if click[0] == 1:    
                    tick_sound.play()
                    punch1_color = 'blue'
            elif x-290 + w-100 > cur[0] > x-290 and y+50 + h-200 > cur[1] > y+50 and p1_total_point>= 50:
                if click[0] == 1:    
                    tick_sound.play()
                    punch1_color = 'yellow'
            elif x-210 + w-100 > cur[0] > x-210 and y+50 + h-200 > cur[1] > y+50 and p1_total_point>= 50:
                if click[0] == 1:    
                    tick_sound.play()
                    punch1_color = 'green'           
            elif x-130 + w-100 > cur[0] > x-130 and y+50 + h-200 > cur[1] > y+50:
                if click[0] == 1:    
                    tick_sound.play()
                    punch1_color = 'none'     
            
            if x-370 + w-100 > cur[0] > x-370 and y+200 + h-200 > cur[1] > y+200 and p1_total_point>= 300:
                if click[0] == 1:    
                    tick_sound.play()
                    damage1_size = '3'
            elif x-290 + w-100 > cur[0] > x-290 and y+200 + h-200 > cur[1] > y+200 and p1_total_point>= 500:
                if click[0] == 1:    
                    tick_sound.play()
                    damage1_size = '5'
            elif x-210 + w-100 > cur[0] > x-210 and y+200 + h-200 > cur[1] > y+200:
                if click[0] == 1:    
                    tick_sound.play()
                    damage1_size = 'none' 
            
        if str(p2_point) == '0' : #p2 포인트 0
            message_to_screen("P2 point is 0", red, x-200,y-200, 'medium') 
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(p2_animal[0])+"sp_00.png")),(w,h)),(x+370,y-180))
        else: #p2포인트 >= 0
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(p2_animal[0])+"sp_00.png")),(w,h)),(x+400,y-180))
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(punch2_color)+"_attack1.png")),(60,60)),(x+570,y-180))
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(weapon2_color)+"_weapon.png")),(80,60)),(x+570,y-100))
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(damage2_size)+"damage.png")),(50,30)),(x+450,y-230))
           
            button("P2 point : "+str(p2_point - weapon2_point - punch2_point - damage2_point), x+350 ,y+70,w+150,h-200,coral,coral,None)    
    
            if lan_option == 'english':
                
                message_to_screen("WEAPON COLOR ( -50 Point )", gray,x-700,y-500, 'small2')
                message_to_screen("PUNCH COLOR ( -50 Point )", gray ,x-700,y-350, 'small2')
                message_to_screen("DAMAGE UP ( -300 / -500 Point )", gray ,x-700,y-200, 'small2')
                button_c("Weapon color : " + str( weapon2_color),x+350,y+120,w+150,h-200,coral,coral,None)
                button_c("punch color : "+ str( punch2_color),x+350,y+170,w+150,h-200,coral,coral,None)
            elif lan_option == 'korean':
                message_to_screen("무기 색상 ( -50 Point )", gray ,x-700,y-500, 'small2')
                message_to_screen("펀치 색상 ( -50 Point )", gray ,x-700,y-350, 'small2')
                message_to_screen("공격력 증가 ( -300 / -500 Point )", gray ,x-700,y-200, 'small2')  
                button_c("무기 색상 : " + str( weapon2_color),x+350,y+120,w+150,h-200,coral,coral,None)
                button_c("펀치 색상 : "+ str( punch2_color),x+350,y+170,w+150,h-200,coral,coral,None)
                button_c("공격력 + "+ str(damage2_size),x+350,y+220,w+150,h-200,coral,coral,None)
            button("",x+60,y-100,w-100,h-200,blue,light_blue,None)
            button("",x+140,y-100,w-100,h-200,yellow,light_yellow,None)
            button("",x+220,y-100,w-100,h-200,green,light_green,None)
            button("NONE",x+300,y-100,w-100,h-200,white,black,None)
            
            button("",x+60,y+50,w-100,h-200,blue,light_blue,None)
            button("",x+140,y+50,w-100,h-200,yellow,light_yellow,None)
            button("",x+220,y+50,w-100,h-200,green,light_green,None)
            button("NONE",x+300,y+50,w-100,h-200,white,black,None)
            
            button("+ 3",x+140,y+200,w-100,h-200,white,black,None)
            button("+ 5",x+220,y+200,w-100,h-200,white,black,None)
            button("NONE",x+300,y+200,w-100,h-200,white,black,None)
            
            if weapon2_color == 'blue': 
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+60,y-100)) 
                if p2_total_point>=50:
                    weapon2_point = 50
            elif weapon2_color == 'yellow':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+140,y-100))
                if p2_total_point>=50:
                    weapon2_point = 50
            elif weapon2_color == 'green':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+220,y-100))
                if p2_total_point>=50:
                    weapon2_point = 50
            elif weapon2_color == 'none':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+300,y-100))
                button_c("                   ",x+350,y+120,w+150,h-200,coral,coral,None)
                weapon2_point = 0
            
            if punch2_color == 'blue': 
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+60,y+50)) 
                if p2_total_point>=50:
                    punch2_point = 50
            elif punch2_color == 'yellow':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+140,y+50))
                if p2_total_point>=50:
                    punch2_point = 50
            elif punch2_color == 'green':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+220,y+50))
                if p2_total_point>=50:
                    punch2_point = 50
            elif punch2_color == 'none':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+300,y+50))
                button_c("                 ",x+350,y+170,w+150,h-200,coral,coral,None)
                punch2_point = 0
           
            if damage2_size == '3': 
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+140,y+200)) 
                if p2_total_point>=300:
                    damage2_point = 300
                    p2_custom_atk=3
            elif damage2_size == '5':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+220,y+200))
                if p2_total_point>=500:
                    damage2_point = 500
                    p2_custom_atk=5
            elif damage2_size == 'none':
                screen.blit(pygame.transform.scale(check,(w-100,h-200)),(x+300,y+200))
                button_c("           ",x+350,y+220,w+150,h-200,coral,coral,None)    
                damage2_point = 0
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            tick_sound.set_volume(effect_option)
            click_sound.set_volume(effect_option)
           
            if x+60 + w-100 > cur[0] > x+60 and y-100 + h-200 > cur[1] > y-100 and p2_total_point>= 50:
                if click[0] == 1:     
                    tick_sound.play()
                    weapon2_color = 'blue'
            elif x+140 + w-100 > cur[0] > x+140 and y-100 + h-200 > cur[1] > y-100 and p2_total_point>= 50:
                if click[0] == 1:     
                    tick_sound.play()
                    weapon2_color = 'yellow'   
            elif x+220 + w-100 > cur[0] > x+220 and y-100 + h-200 > cur[1] > y-100 and p2_total_point>= 50:
                if click[0] == 1:     
                    tick_sound.play()
                    weapon2_color = 'green'
            elif x+300 + w-100 > cur[0] > x+300 and y-100 + h-200 > cur[1] > y-100:
                if click[0] == 1:     
                    tick_sound.play()
                    weapon2_color = 'none'
                    
            if x+60 + w-100 > cur[0] > x+60 and y+50 + h-200 > cur[1] > y+50 and p2_total_point>= 50:
                if click[0] == 1:     
                    tick_sound.play()
                    punch2_color = 'blue'
            elif x+140 + w-100 > cur[0] > x+140 and y+50 + h-200 > cur[1] > y+50 and p2_total_point>= 50:
                if click[0] == 1:     
                    tick_sound.play()
                    punch2_color = 'yellow'
            elif x+220 + w-100 > cur[0] > x+220 and y+50 + h-200 > cur[1] > y+50 and p2_total_point>= 50:
                if click[0] == 1:     
                    tick_sound.play()
                    punch2_color = 'green'
            elif x+300 + w-100 > cur[0] > x+300 and y+50 + h-200 > cur[1] > y+50:
                if click[0] == 1:     
                    tick_sound.play()
                    punch2_color = 'none'
            
            if x+140 + w-100 > cur[0] > x+140 and y+200 + h-200 > cur[1] > y+200 and p2_total_point>= 300:
                if click[0] == 1:     
                    tick_sound.play()
                    damage2_size = '3'
            elif x+220 + w-100 > cur[0] > x+220 and y+200 + h-200 > cur[1] > y+200 and p2_total_point>= 500:
                if click[0] == 1:     
                    tick_sound.play()
                    damage2_size = '5'
            elif x+300 + w-100 > cur[0] > x+300 and y+200 + h-200 > cur[1] > y+200:
                if click[0] == 1:     
                    tick_sound.play()
                    damage2_size = 'none'
        p1_total_point = p1_point - weapon1_point - punch1_point - damage1_point
        p2_total_point = p2_point - weapon2_point - punch2_point - damage2_point    
        
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x-65 + w-10 > cur[0] > x-65 and y+230 + h-190 > cur[1] > y+230:
            if click[0] == 1:  
                click_sound.play()
                customizing = False            
        
        pygame.display.update()
        clock.tick(60)
   
    p1_point=p1_total_point
    p2_point=p2_total_point
    
    return(Game())

def uid():
    global text1p,text2p,p1_point,p2_point,p1_id,p2_id
    uid1p=True
    
    img1p=smallfont.render(text1p, True, black)
    rect1p=img1p.get_rect()
    cursor1=pygame.Rect(rect1p.topright,(3,rect1p.height))
    
    uid2p=True
    img2p=smallfont.render(text2p, True, black)
    rect2p=img2p.get_rect()
    cursor2=pygame.Rect(rect2p.topright,(3,rect2p.height))
    uid_sound.play(-1)

    while uid1p:
        screen.blit(uidstart1,(0,0))      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    if len(text1p)>0:
                        text1p=text1p[:-1]
                        
                else:
                    text1p+=event.unicode
                    
                img1p=extralargefont.render(text1p, True, black)
                rect1p.size=img1p.get_size()
                cursor1.topleft=rect1p.topright
        screen.blit(img1p,(size[0]/2-240,size[1]/2+10))
        pygame.display.update()
        if len(text1p)==4:
            pygame.time.delay(300)
            uid1p=False
            
    while uid2p:
        screen.blit(uidstart2,(0,0))      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    if len(text2p)>0:
                        text2p=text2p[:-1]
                        
                else:
                    text2p+=event.unicode
                    
                img2p=extralargefont.render(text2p, True, black)
                rect2p.size=img2p.get_size()
                cursor2.topleft=rect2p.topright
        screen.blit(img2p,(size[0]/2-240,size[1]/2+10))
        pygame.display.update()
        if len(text2p)==4:
            pygame.time.delay(300)
            uid2p=False
            
    f=open('idlist.txt','r+')
    lines=f.readlines()
    i=0
    is_p1=False #아이디가 새로운 아이디인지 체크하기위한 변수
    is_p2=False
    while i<len(lines):
         if lines[i]==text1p+"\n":
             p1_point=int(lines[i+1])
             is_p1=True
         if lines[i]==text2p+"\n":
            p2_point=int(lines[i+1])
            is_p2=True
         i+=1
    if is_p1==False:
        f.write(text1p)
        f.write("\n")
        f.write(str(p1_point))
        f.write("\n")
    if is_p2==False:   
        f.write(text2p)
        f.write("\n")
        f.write(str(p2_point))
        f.write("\n")
    
       
    p1_id=text1p
    p2_id=text2p

    f.close()

def savepoint(id,point):
    f=open('idlist.txt','r+')
    lines=f.readlines()
    i=0
    while i<len(lines):
         if lines[i]==id+"\n":
             lines[i+1]=str(point)+"\n"
         i+=1
    f.seek(0)
    i=0
    while i<len(lines):
         f.write(str(lines[i]))
         i+=1
    f.close()
         
def Game_fight():
    global p1win,p2win,ck1
    fight_sound = pygame.mixer.Sound(os.path.join(sound_path,'fight.wav'))
    if ck1 == True:
        city_sound.stop()
        beach_sound.stop()
        space_sound.stop()
        if p1win + p2win == 0:
            fight_sound = pygame.mixer.Sound(os.path.join(sound_path,'round1.wav'))
        elif  p1win + p2win == 1:
            fight_sound = pygame.mixer.Sound(os.path.join(sound_path,'round2.wav'))
        elif   p1win + p2win == 2:
            fight_sound = pygame.mixer.Sound(os.path.join(sound_path,'round3.wav'))
        elif   p1win + p2win == 3:
            fight_sound = pygame.mixer.Sound(os.path.join(sound_path,'round4.wav'))
        elif   p1win + p2win == 4:
            fight_sound = pygame.mixer.Sound(os.path.join(sound_path,'round5.wav'))

            
    pygame.mixer.music.fadeout(1000) 
    pygame.mixer.music.stop()
    fight_sound.play()  
    screen.fill(black)
    message_to_screen("3", white, 0,0, 'extralarge')
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)
    message_to_screen("2", black, 0,0, 'extralarge')
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    message_to_screen("1", white, 0,0, 'extralarge')
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)
    if lan_option =='english':
        message_to_screen("Game Start", black, 0,0, 'extralarge')   
    elif lan_option =='korean':
        message_to_screen("게임 시작", black, 0,0, 'extralarge')       
    pygame.display.update()
    time.sleep(1)
    
class Player1(pygame.sprite.Sprite):
    
    def __init__(self,x=0,y=0,dx=0,dy=0):
        super(Player1, self).__init__()
        self.image=""
        self.x=size[0]/5
        self.y=size[1]*7/8
        self.dx=dx
        self.dy=dy
        self.isJump=0
        self.v=0
        self.m=MASS
        self.hp=100
        self.mp=0
        self.moving = "STAND"
        self.id=""
        self.point=0
        self.walkcount = 0
        
    def draw_hpmp(self):
        self.hpimage=pygame.image.load(os.path.join(image_path, "HP.png"))
        if self.hp>=100:
            self.hpimage = pygame.transform.scale(self.hpimage, (size[0]/2, 100))
        elif self.hp>=0:                          #hp가 0이상인 경우만 동작
            self.hpimage = pygame.transform.scale(self.hpimage, (size[0]/2*self.hp/100, 100))
        else :
            self.hpimage = pygame.transform.scale(self.hpimage, (0, 100))
        screen.blit(self.hpimage,[0,0])
        
        self.mpimage=pygame.image.load(os.path.join(image_path, "MP.png"))
        if self.mp <100:                       #mp가 100이하인 경우만 동작
            self.mpimage = pygame.transform.scale(self.mpimage, (size[0]*self.mp/100/2, 50))
        else :
            self.mpimage=pygame.image.load(os.path.join(image_path, "MPfull.png"))
            self.mpimage = pygame.transform.scale(self.mpimage, (size[0]/2, 50))
        screen.blit(self.mpimage,[0,100])
        
        self.chimage = pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id) +"sp_15.png")),(100,100))
        screen.blit(self.chimage,(0,0))
    def load_char(self):
        if self.moving == "DOWN":
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "foxsp_2.png")),(player_width,player_height))
            self.rect=self.image.get_rect()
        else:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(image_path, "foxsp_10.png")),(player_width,player_height))
            self.rect=self.image.get_rect()
        self.image = pygame.Surface((player_width,player_height),pygame.SRCALPHA)    
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x=self.x
        self.rect.y=self.y
        self.rect.bottom=size[1]
    def draw_char(self):
           
           move_left = [pygame.image.load(os.path.join(image_path, str(self.id) + "sp_1.png")),pygame.image.load(os.path.join(image_path, str(self.id) + "sp_2.png")),pygame.image.load(os.path.join(image_path, str(self.id) + "sp_3.png"))]
           move_right = [pygame.transform.flip(move_left, True, False) for move_left in move_left]
           move_left = [pygame.transform.scale(move_left,(player_width,player_height)) for move_left in move_left]
           move_right = [pygame.transform.scale(move_right,(player_width,player_height)) for move_right in move_right]   
           move_jump = [pygame.image.load(os.path.join(image_path, str(self.id)+"sp_4.png")),pygame.image.load(os.path.join(image_path, str(self.id)+"sp_5.png")),pygame.image.load(os.path.join(image_path, str(self.id)+"sp_6.png"))]
           move_jump = [pygame.transform.scale(move_jump,(player_width,player_height)) for move_jump in move_jump]
           move_attack = [pygame.image.load(os.path.join(image_path, str(self.id) + "sp_16.png")),pygame.image.load(os.path.join(image_path, str(self.id) + "sp_17.png")),pygame.image.load(os.path.join(image_path, str(self.id) + "sp_18.png"))]
           move_attack = [pygame.transform.scale(move_attack,(player_height,player_width)) for move_attack in move_attack]
        
           if self.moving == "RIGHT":
               if self.isJump == 1:
                   self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id) + "sp_8.png")),(player_width,player_height)),True,False)
                   self.walkcount = 0
                   screen.blit(self.image,[self.rect.x,self.rect.y])
               else: 
                   self.image = move_right[self.walkcount//4]
                   self.walkcount += 1
                   screen.blit(self.image,[self.rect.x,self.rect.y])
                
           elif self.moving == "LEFT":
               if  self.isJump == 1:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id)+"sp_8.png")),(player_width,player_height))
                    self.walkcount = 0
                    screen.blit(self.image,[self.rect.x,self.rect.y])
               else:
                   self.image = move_left[self.walkcount//4]
                   self.walkcount += 1
                   screen.blit(self.image,[self.rect.x,self.rect.y])
           elif self.moving == "STAND":
                if  self.isJump == 1:
                     self.image = move_jump[self.walkcount//4]
                     self.walkcount += 1
                     screen.blit(self.image,[self.rect.x,self.rect.y])
                else:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id)+"sp_0.png")),(player_width,player_height))
                    self.walkcount = 0
                    screen.blit(self.image,[self.rect.x,self.rect.y])
           elif self.moving == "DOWN":
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id)+"sp_10.png")),(player_width,player_height-110))
                    self.walkcount = 0
                    screen.blit(self.image,[self.rect.x,self.rect.y+110])
           elif self.moving == "LEFT_PUNCH":
                     self.image = pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id)+"sp_12.png")),(player_width,player_height))
                     self.walkcount = 0
                     screen.blit(self.image,[self.rect.x,self.rect.y])
           elif self.moving == "RIGHT_PUNCH":
                     self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id)+"sp_12.png")),(player_width,player_height)),True , False)
                     self.walkcount = 0
                     screen.blit(self.image,[self.rect.x,self.rect.y]) 
           elif self.moving == "PUNCH":
                     self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id)+"sp_14.png")),(player_width,player_height)),True , False)
                     self.walkcount = 0
                     screen.blit(self.image,[self.rect.x,self.rect.y]) 
           elif self.moving == "ATTACK":
                     self.image = move_attack[self.walkcount//4]
                     self.walkcount += 1
                     screen.blit(self.image,[self.rect.x,self.rect.y+player_width])           
                     if self.walkcount == 11:
                         self.moving = "STAND"
           if self.walkcount + 1 >= 12:
               self.walkcount = 0
   
    def move_x(self):
        self.rect.x+=self.dx
    def move_y(self):
        self.rect.y+=self.dy
        
    def check_screen(self):         #화면밖나가기 방지
        if self.rect.right > size[0] or self.rect.x < 0:
            self.rect.x -= self.dx
        if  self.rect.y < 0:
            self.rect.y -= self.dy
        
    def jump(self,j):
        self.isJump=j
    
    def update(self):
        if self.isJump>0:
            if self.isJump==2:
                self.v = self.jp
            if self.v>0:
                F=(0.5*self.m*(self.v*self.v))
            else:
                F=-(0.5*self.m*(self.v*self.v))
            self.rect.y-=round(F)    
            self.v-=1
            
            if self.rect.bottom > size[1]:
               self.rect.bottom = size[1]
               self.isJump = 0
               self.v = self.jp
           
class Player2(Player1):
    
    def __init__(self,x=0,y=0,dx=0,dy=0):
        self.image=""
        self.x=size[0]*4/5
        self.y=size[1]*7/8
        self.dx=dx
        self.dy=dy
        self.isJump=0
        self.v=0
        self.m=MASS
        self.hp=100
        self.mp=0
        self.moving = "STAND"
        self.id=""
        self.point=0
        self.walkcount = 0
        
    def draw_hpmp(self):
        self.hpimage=pygame.image.load(os.path.join(image_path, "HP.png")) 
        if self.hp >= 8999999:
            self.hpimage = pygame.transform.scale(self.hpimage, (size[0]/2, 100))
            screen.blit(self.hpimage,[size[0]/2,0])
        elif self.hp>=100:
            self.hpimage = pygame.transform.scale(self.hpimage, (size[0]/2, 100))
            screen.blit(self.hpimage,[size[0]-size[0]/2*self.hp/100,0])
        elif self.hp>=0:
            self.hpimage = pygame.transform.scale(self.hpimage, (size[0]/2*self.hp/100, 100))
            screen.blit(self.hpimage,[size[0]-size[0]/2*self.hp/100,0])
        else :
            self.hpimage = pygame.transform.scale(self.hpimage, (0, 100))
            screen.blit(self.hpimage,[size[0]-size[0]/2*self.hp/100,0])
        
        self.mpimage=pygame.image.load(os.path.join(image_path, "MP.png"))
        if self.mp<100:
            self.mpimage = pygame.transform.scale(self.mpimage, (size[0]/2*self.mp/100, 50))
            screen.blit(self.mpimage,[size[0]-size[0]/2*self.mp/100,100])
        else :
            self.mpimage=pygame.image.load(os.path.join(image_path, "MPfull.png"))
            self.mpimage = pygame.transform.scale(self.mpimage, (size[0]/2, 50))
            screen.blit(self.mpimage,[size[0]/2,100])
        self.chimage = pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(self.id) +"sp_15.png")),(100,100))
        screen.blit(self.chimage,(1300,0))
        
def Game():
    global screen , weapon1_color,weapon2_color,punch1_color,punch2_color,damage1_size,damage2_size,p1_total_point,p2_total_point
    clock=pygame.time.Clock()
    
    # 무기 만들기
    weapon1 =pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(weapon1_color)+"_weapon.png")),(display_width / 16, display_height / 12))
    weapon1_size = weapon1.get_rect().size
    weapon1_width = weapon1_size[0]
    weapon2 =pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(weapon2_color)+"_weapon.png")),(display_width / 16, display_height / 12)),True , False)
    weapon2_size = weapon2.get_rect().size
    weapon2_width = weapon2_size[0]
    # 무기는 한 번에 여러 발사 가능
    weapons1 = []
    weapons2 = []
    # 무기 이동 속도
    weapon1_speed = 10
    weapon2_speed = -10
    weapon1_to_remove = -1
    weapon2_to_remove = -1
    #p1근접 공격
    attack1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(punch1_color)+"_attack1.png")),(display_width / 19, display_height / 11)),-20)
    attack1_size = attack1.get_rect().size
    attack1_width = attack1_size[0]
    attack1_rect = attack1.get_rect()
    attacks1 = []
    attack1_to_remove = -1
    attack2_to_remove = -1
    attacks2 = []
    attack2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(image_path, str(punch2_color)+"_attack1.png")),(display_width / 19, display_height / 11)),-20)
    attack2_size = attack2.get_rect().size
    attack2_width = attack2_size[0]
    attack2_rect = attack2.get_rect()
    #p1,p2 공격 딜레이
    p1dll=-2000 
    p2dll=-2000 
    
    running=True
    
    p1=Player1()
    p1.id=p1_animal[0] #여기서 id는 동물의 type임  입력받는4자리 id가아님
    p1.load_char()
    p2=Player2()
    p2.id=p2_animal[0]
    p2.load_char()
    p1.jp = p1_animal[2]
    p2.jp = p2_animal[2]
    global p1_point,p2_point,p1win,p2win
    p1.point=int(p1_point)
    p2.point=int(p2_point)
    p1.punch = p1_animal[3]
    p2.punch = p2_animal[3]
    #총게임시간
    total_time=60
    #핸디캡체크
    if ck2==True:
        p1.hp-=30
    if ck3==True:
        p2.hp-=30
    #무한필살기
    if ck4==True:
        p1.mp=9999999
        p2.mp=9999999
    #연습모드
    if ck5==True:
        p1.hp=9999999
        p2.hp=9999999
        total_time=999
    
    Game_fight()
    
    if back_option == 'city':
        city_sound.set_volume(bgm_option)
        city_sound.play(-1)
    elif back_option == 'beach':
        beach_sound.set_volume(bgm_option)
        beach_sound.play(-1)    
    elif back_option == 'space':
        space_sound.set_volume(bgm_option)
        space_sound.play(-1)    
    #필살기초기값 설정
    p1_satk=False
    p2_satk=False
    p1_stime=-1
    p2_stime=-1
    p1_fox_satk=False
    p2_fox_satk=False
    p1_bear_satk=False
    p2_bear_satk=False
    p1_dog_satk=0
    p2_dog_satk=0
    p1_catimgtime=-1000  #고양이필살기는 따로처리 
    p2_catimgtime=-1000
    p1.jump(1) # 첫 점프 처리
    p2.jump(1)
    start_time=pygame.time.get_ticks()
    
    while running:
    
        clock.tick(60) # 60FPS
        
        if p1.rect.x>p2.rect.x:
            weapon1_speed=-10
            weapon2_speed=10
        if p1.rect.x<p2.rect.x:
            weapon1_speed=10
            weapon2_speed=-10
        
        # 키가 눌린 상태 체크
        keys = pygame.key.get_pressed()
        # 스페이스키가 눌려있고, isJump가 2라면 1로 변경한다.
        # 이 작업을 해주지 않으면 스페이스가 눌려있는 상태면 플레이어가 계속 위로 올라가게 된다.
        if (keys[pygame.K_w]):
            if p1.isJump == 2:
                    p1.jump(1)        
        if (keys[pygame.K_UP]):
            if p2.isJump == 2:
                    p2.jump(1)
        if (keys[pygame.K_a]) and (keys[pygame.K_s]):
            p1.moving == "DOWN_LEFT"
        for event in pygame.event.get():
            if event.type == pygame.QUIT :   #종료처리
                running=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: # 캐릭터를 왼쪽으로
                    p1.dx=-5-p1_dog_satk/500
                    p1.moving = "LEFT"
                elif event.key == pygame.K_d: # 캐릭터를 오른쪽으로
                     p1.dx=5+p1_dog_satk/500
                     p1.moving = "RIGHT"
                elif event.key == pygame.K_w:# 점프
                     if p1.isJump==0:
                        jump_sound.set_volume(effect_option)
                        jump_sound.play()
                        p1.jump(1)
                     elif p1.isJump==1:
                        p1.jump(1)
                        
                elif event.key == pygame.K_1: #펀치
                     if p1.moving == "LEFT":
                         p1.moving = "LEFT_PUNCH"
                     elif p1.moving == "RIGHT":
                         p1.moving = "RIGHT_PUNCH"    
                     elif p1.moving == "STAND":
                         p1.moving = "PUNCH"
                     attack1_x_pos =p1.rect.x
                     attack1_y_pos =p1.rect.y
                     attacks1.append([attack1_x_pos, attack1_y_pos])

                         
                elif event.key == pygame.K_s: #숙이기
                     p1.moving = "DOWN"
  
                elif event.key == pygame.K_3 and p1.mp>=100: #필살기
                    if ck4:
                        p1.mp-=100
                    else :
                        p1.mp=0
                    p1_stime=pygame.time.get_ticks()
                    p1_satk=True
                    
                elif event.key==pygame.K_2 and pygame.time.get_ticks()-p1dll+p1_dog_satk>2000 :
                    weapon_sound.set_volume(effect_option)
                    weapon_sound.play()
                    weapon1_x_pos =p1.rect.x
                    weapon1_y_pos =p1.rect.y 
                    weapons1.append([weapon1_x_pos, weapon1_y_pos])
                    p1dll=pygame.time.get_ticks()
                     
                if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                    p2.dx=-5-p2_dog_satk/500
                    p2.moving = "LEFT"
                elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                    p2.dx=5+p2_dog_satk/500
                    p2.moving = "RIGHT"
                elif event.key == pygame.K_UP:# 점프
                    if p2.isJump==0:
                        jump_sound.set_volume(effect_option)
                        jump_sound.play()
                        p2.jump(1)
                    elif p2.isJump==1:
                       p2.jump(1)
                elif event.key == pygame.K_DOWN: # 숙이기
                     p2.moving = "DOWN"
                elif event.key == pygame.K_COMMA: #펀치
                     if p2.moving == "LEFT":
                         p2.moving = "LEFT_PUNCH"
                     elif p2.moving == "RIGHT":
                         p2.moving = "RIGHT_PUNCH"    
                     elif p2.moving == "STAND":
                         p2.moving = "PUNCH"     
                     attack2_x_pos =p2.rect.x
                     attack2_y_pos =p2.rect.y
                     attacks2.append([attack2_x_pos, attack2_y_pos])
                     
                elif event.key == pygame.K_SLASH and p2.mp>=100: #필살기
                    if ck4:
                        p2.mp-=100
                    else :
                        p2.mp=0
                    
                    p2_stime=pygame.time.get_ticks()
                    p2_satk=True
                    
                elif event.key==pygame.K_PERIOD and pygame.time.get_ticks()-p2dll+p2_dog_satk>2000 :
                    weapon_sound.set_volume(effect_option)
                    weapon_sound.play()
                    weapon2_x_pos =p2.rect.x 
                    weapon2_y_pos =p2.rect.y 
                    weapons2.append([weapon2_x_pos, weapon2_y_pos])
                    p2dll=pygame.time.get_ticks()  
        
            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_a or event.key == pygame.K_d:
                     p1.dx=0
                     p1.moving = "STAND"
            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     p2.dx=0            
                     p2.moving = "STAND"
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_s:
                     p1.moving = "STAND"
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_DOWN:
                     p2.moving = "STAND"
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_1:
                    if p1.moving == "LEFT_PUNCH":
                        p1.moving = "LEFT"
                    elif p1.moving == "RIGHT_PUNCH":
                        p1.moving = "RIGHT"
                    elif p1.moving == "PUNCH":
                        p1.moving = "STAND"    
                    attacks1 = []        
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_COMMA:
                    if p2.moving == "LEFT_PUNCH":
                        p2.moving = "LEFT"
                    elif p2.moving == "RIGHT_PUNCH":
                        p2.moving = "RIGHT"
                    elif p2.moving == "PUNCH":
                        p2.moving = "STAND"
                    attacks2 = []
                 
        if back_option == 'city':
           screen.blit(back_city,(0,0))
        elif back_option == 'space':
           screen.blit(back_space,(0,0))
        elif back_option == 'beach':
           screen.blit(back_beach,(0,0))   
        
        weapons1 = [ [w[0] + weapon1_speed, w[1]] for w in weapons1]
        weapons1 = [ [w[0], w[1]] for w in weapons1 if 0 < w[0] < size[0] - weapon1_width]
        
        weapons2 = [ [w[0] + weapon2_speed, w[1]] for w in weapons2]
        weapons2 = [ [w[0], w[1]] for w in weapons2 if 0 < w[0] < size[0] - weapon2_width]  
        
        for weapon1_x_pos, weapon1_y_pos in weapons1:
            if p1.rect.x>p2.rect.x:  
                screen.blit(pygame.transform.flip(weapon1, True , False), (weapon1_x_pos, weapon1_y_pos + 100))
            elif p1.rect.x<p2.rect.x:     
                screen.blit(weapon1, (weapon1_x_pos, weapon1_y_pos+ 100))
                
        for weapon2_x_pos, weapon2_y_pos in weapons2:
            if p1.rect.x>p2.rect.x:
                screen.blit(pygame.transform.flip(weapon2, True , False), (weapon2_x_pos, weapon2_y_pos+ 100))
            elif p1.rect.x<p2.rect.x:    
                screen.blit(weapon2, (weapon2_x_pos, weapon2_y_pos+ 100))

        p1.move_x()
        p1.move_y()
        p1.update()
        p1.draw_char()
        p1.check_screen()
        
        p2.move_x()
        p2.move_y()
        p2.update()
        p2.draw_char()
        p2.check_screen()  
        
        attacks1 = [ [w[0] + p1.dx , w[1]] for w in attacks1]
        attacks1 = [ [w[0] , w[1]] for w in attacks1 if (p1.rect.x - attack1_width < w[0] < p1.rect.x + attack1_width) and (p1.rect.y - attack1_width < w[1] < p1.rect.y + attack1_width)  ]
       
        attacks2 = [ [w[0] + p2.dx, w[1]] for w in attacks2]
        attacks2 = [ [w[0], w[1]] for w in attacks2 if (p2.rect.x - attack2_width < w[0] < p2.rect.x + attack2_width) and (p2.rect.y - attack2_width < w[1] < p2.rect.y + attack2_width)  ]

        for attack1_x_pos, attack1_y_pos in attacks1:
            if p1.moving == "LEFT_PUNCH":    
             screen.blit(pygame.transform.flip(attack1, True , False), (attack1_x_pos-65, attack1_y_pos+55))
            elif p1.moving == "RIGHT_PUNCH":
             screen.blit(attack1,(attack1_x_pos+85, attack1_y_pos+55)) # 방향 좌우 반전
            elif p1.moving == "PUNCH":
             screen.blit(pygame.transform.rotate(attack1,-80),(attack1_x_pos+60, attack1_y_pos+70)) 
        
        for attack2_x_pos, attack2_y_pos in attacks2:
            if p2.moving == "LEFT_PUNCH":    
             screen.blit(pygame.transform.flip(attack2, True , False), (attack2_x_pos-65, attack2_y_pos+55))    
            elif p2.moving == "RIGHT_PUNCH":
             screen.blit(attack2,(attack2_x_pos+85, attack2_y_pos+55))
            elif p2.moving == "PUNCH":
             screen.blit(pygame.transform.rotate(attack2,-80),(attack2_x_pos+60, attack2_y_pos+70)) 
        
        #필살기처리
        #1p
        if p1_satk==True and pygame.time.get_ticks()-p1_stime<=5000:
            if p1_animal[0]=='fox':
                if pygame.time.get_ticks()-p1_stime<=50:
                    fox_sound.set_volume(effect_option)
                    fox_sound.play()
                screen.blit(satk_fox, (p1.rect.centerx-satk_fox.get_width()/2,p1.rect.top-100))
                p1_fox_satk=True     
            if p1_animal[0]=='bear':
                if pygame.time.get_ticks()-p1_stime<=50:
                    bear_sound.set_volume(effect_option)
                    bear_sound.play()
                screen.blit(satk_bear, (p1.rect.centerx-satk_bear.get_width()/2,p1.rect.top-100))
                p1_bear_satk=True
            if p1_animal[0]=='dog':
                if pygame.time.get_ticks()-p1_stime<=50:
                    dog_sound.set_volume(effect_option)
                    dog_sound.play()
                screen.blit(satk_dog, (p1.rect.centerx-satk_dog.get_width()/2,p1.rect.top-100))
                p1_dog_satk=1500
            if p1_animal[0]=='cat':
                if pygame.time.get_ticks()-p1_stime<=50:
                    cat_sound.set_volume(effect_option)
                    cat_sound.play()
                p1.hp+=30
                p1_catimgtime=pygame.time.get_ticks()
                #100초과 회복 금지
                if p1.hp>=100:
                    p1.hp=100
                p1_satk=False
        #5초지나면 필살기종료        
        if p1_satk==True and pygame.time.get_ticks()-p1_stime>5000:
            p1_satk=False
            p1_fox_satk=False
            p1_dog_satk=0
        #고양이 필살기 그려주기    
        if pygame.time.get_ticks()- p1_catimgtime<=1000:
            screen.blit(satk_cat, (p1.rect.centerx-satk_fox.get_width()/2,p1.rect.top-100))
        
        #2p   
        if p2_satk==True and pygame.time.get_ticks()-p2_stime<=5000:
            if p2_animal[0]=='fox':
                if pygame.time.get_ticks()-p2_stime<=50:
                    fox_sound.set_volume(effect_option)
                    fox_sound.play()
                screen.blit(satk_fox, (p2.rect.centerx-satk_fox.get_width()/2,p2.rect.top-100))
                p2_fox_satk=True
            if p2_animal[0]=='bear':
                if pygame.time.get_ticks()-p2_stime<=50:
                    bear_sound.set_volume(effect_option)
                    bear_sound.play()
                screen.blit(satk_bear, (p2.rect.centerx-satk_bear.get_width()/2,p2.rect.top-100))
                p2_bear_satk=True
            if p2_animal[0]=='dog':
                if pygame.time.get_ticks()-p2_stime<=50:
                    dog_sound.set_volume(effect_option)
                    dog_sound.play()
                screen.blit(satk_dog, (p2.rect.centerx-satk_dog.get_width()/2,p2.rect.top-100))
                p2_dog_satk=1500
            if p2_animal[0]=='cat': 
                if pygame.time.get_ticks()-p2_stime<=50:
                    cat_sound.set_volume(effect_option)
                    cat_sound.play()
                p2.hp+=30           
                p2_catimgtime=pygame.time.get_ticks()
                #100초과 회복 금지
                if p2.hp>=100:
                    p2.hp=100
                p2_satk=False
        #5초지나면 필살기종료        
        if p2_satk==True and pygame.time.get_ticks()-p2_stime>5000:
            p2_satk=False
            p2_fox_satk=False
            p2_bear_satk=False
            p2_dog_satk=0
        #고양이 필살기 그려주기    
        if pygame.time.get_ticks()- p2_catimgtime<=1000:
            screen.blit(satk_cat, (p2.rect.centerx-satk_fox.get_width()/2,p2.rect.top-100))        
       
        for weapon1_idx, weapon1_val in enumerate(weapons1):
            weapon1_pos_x = weapon1_val[0]
            weapon1_pos_y = weapon1_val[1]
            # 무기 rect 정보 업데이트
            weapon1_rect = weapon1.get_rect()
            weapon1_rect.left = weapon1_pos_x
            weapon1_rect.top = weapon1_pos_y
            # 충돌 체크
            if weapon1_rect.colliderect(p2.rect) and p2_fox_satk==False:
                weapon1_to_remove = weapon1_idx # 해당 무기 없애기 위한 값 설정
                hurt_sound.set_volume(effect_option)
                hurt_sound.play()
                if p2.moving != "DOWN":
                    p2.hp-=10+p1_custom_atk
                    p1.mp+=20
                    p2.moving = "ATTACK"
                if p1_bear_satk==True:
                    p2.hp-=10
                break
        for weapon2_idx, weapon2_val in enumerate(weapons2):
            weapon2_pos_x = weapon2_val[0]
            weapon2_pos_y = weapon2_val[1]
    
            # 무기 rect 정보 업데이트
            weapon2_rect = weapon2.get_rect()
            weapon2_rect.left = weapon2_pos_x
            weapon2_rect.top = weapon2_pos_y 
    
            if weapon2_rect.colliderect(p1.rect)and p1_fox_satk==False:
               weapon2_to_remove = weapon2_idx # 해당 무기 없애기 위한 값 설정
               hurt_sound.set_volume(effect_option)
               hurt_sound.play()
               if p1.moving != "DOWN":
                   p1.hp-=10+p2_custom_atk
                   p2.mp+=20
                   p1.moving = "ATTACK"
               if p2_bear_satk==True:
                   p1.hp-=10
               break
           
        for attack1_idx, attack1_val in enumerate(attacks1):
            attack1_pos_x = attack1_val[0]
            attack1_pos_y = attack1_val[1]
    
            attack1_rect = attack1.get_rect()
            attack1_rect.left = attack1_pos_x
            attack1_rect.top = attack1_pos_y
    
            if attack1_rect.colliderect(p2.rect):
                attack1_to_remove = attack1_idx
                punch_sound.set_volume(effect_option)
                punch_sound.play()
                p2.hp-=p1.punch+p1_custom_atk
                p1.mp+=10
                break 
       
        for attack2_idx, attack2_val in enumerate(attacks2):
            attack2_pos_x = attack2_val[0]
            attack2_pos_y = attack2_val[1]
    
            attack2_rect = attack2.get_rect()
            attack2_rect.left = attack2_pos_x
            attack2_rect.top = attack2_pos_y
            
            if attack2_rect.colliderect(p1.rect):
                attack2_to_remove = attack2_idx
                punch_sound.set_volume(effect_option)
                punch_sound.play()
                p1.hp-=p2.punch+p2_custom_atk
                p2.mp+=10
                break     
        #캐릭터와 충돌한 무기 제거   
        if weapon1_to_remove > -1:
            del weapons1[weapon1_to_remove]
            weapon1_to_remove = -1
        if weapon2_to_remove > -1:
            del weapons2[weapon2_to_remove]
            weapon2_to_remove = -1
        
        if attack1_to_remove > -1:
            del attacks1[attack1_to_remove]
            if p1.moving == "LEFT_PUNCH":
                p1.moving = "LEFT"
            attack1_to_remove = -1
        if attack2_to_remove > -1:
            del attacks2[attack2_to_remove]
            attack2_to_remove = -1
        p1.draw_hpmp()
        p2.draw_hpmp()
        
        global p1win,p2win
        #5판3선승제 처리
        if ck1==True and p1win<3 and p2win<3:
            screen.blit(winbox, ((0, 150)))
            screen.blit(winbox, ((size[0]-120, 150)))
        
        if p1.hp<=0 and ck1==False:
            game_result =  str(p2_id) + " WIN"
            p2.point+=1000
            p2_point=p2.point
            win_sound = pygame.mixer.Sound(os.path.join(sound_path,'p2win.wav'))
            win_sound.play()
            running = False
            
        elif p1.hp<=0 and ck1==True and p2win<3:
            p2win+=1
            win_sound = pygame.mixer.Sound(os.path.join(sound_path,'p2win.wav'))
            win_sound.play()
            if p2win==3:
                win_sound = pygame.mixer.Sound(os.path.join(sound_path,'p2win.wav'))
                win_sound.play()
                game_result= str(p2_id) + " WIN"
                screen.blit(wincheckbox, ((size[0]-40, 150)))
                screen.blit(wincheckbox, ((size[0]-80, 150)))
                screen.blit(wincheckbox, ((size[0]-120, 150)))
                pygame.display.update()
                p1win=0
                p2win=0
                p2.point+=3000
                p2_point=p2.point
                time.sleep(1)
            else:        
                screen.fill(black)
                game_result = str(p1win)+":"+str(p2win)
                msg = game_font.render(game_result, True, (255, 0, 0))
                msg_rect = msg.get_rect(center=(int(size[0] / 2), int(size[1] / 2)))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                time.sleep(2)
                Game()
            
            running = False

        if p2.hp<=0 and ck1==False:
            game_result= str(p1_id) + " WIN"
            p1.point+=1000
            p1_point=p1.point
            win_sound = pygame.mixer.Sound(os.path.join(sound_path,'p1win.wav'))
            win_sound.play()
            running = False
            
        elif p2.hp<=0 and ck1==True and p1win<3:
            p1win+=1
            win_sound = pygame.mixer.Sound(os.path.join(sound_path,'p1win.wav'))
            win_sound.play()
            if p1win==3:
                screen.fill(black)
                win_sound = pygame.mixer.Sound(os.path.join(sound_path,'p1win.wav'))
                win_sound.play()
                p1.point+=3000
                p1_point=p1.point
                game_result= str(p1_id) + " WIN"
                pygame.display.update()
                p1win=0
                p2win=0
                time.sleep(1)
            else:        
                screen.fill(black)
                game_result = str(p1win)+":"+str(p2win)
                msg = game_font.render(game_result, True, (255, 0, 0))
                msg_rect = msg.get_rect(center=(int(size[0] / 2), int(size[1] / 2)))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                time.sleep(2)
                Game()
            
            running = False
                                  
        if p1win>0:    
            screen.blit(wincheckbox, ((0, 150)))
        if p1win>1:
            screen.blit(wincheckbox, ((40, 150)))
        if p2win>0:    
            screen.blit(wincheckbox, ((size[0]-40, 150)))
        if p2win>1:
            screen.blit(wincheckbox, ((size[0]-80, 150)))
            
        #경과시간    
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 
        #0초이상만표시
        if int(total_time - elapsed_time)>=0:
            timer = game_font.render("{}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
        #0초가 된 경우
        else :
            timer = game_font.render("0", True, (255, 255, 255))
            if p1.hp>p2.hp:
                p2.hp=0
            elif p1.hp<p2.hp:
                p1.hp=0
            else:
                game_result="TIME OVER"
                win_sound = pygame.mixer.Sound(os.path.join(sound_path,'timeover.wav'))
                win_sound.play()
                if ck1:
                    msg = game_font.render(game_result, True, (255, 0, 0))
                    msg_rect = msg.get_rect(center=(int(size[0] / 2), int(size[1] / 2)))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
                    time.sleep(1)
                    Game()
                else:
                    
                    running=False
        timer=pygame.transform.scale(timer, (150,100))
        screen.blit(timer, (size[0]/2-80, 0))
        if ck5:
            tmp=button("Exit",0,160,80,50,white,red,'Exit')
            pygame.display.update()
            if tmp==1:
                game_result="Exit"
                running=False
                
        pygame.display.update()
        # 게임 오버 메시지
    screen.fill(black)
    msg = game_font.render(game_result, True, (255, 0, 0))
    msg_rect = msg.get_rect(center=(int(size[0] / 2), int(size[1] / 2)))
    screen.blit(msg, msg_rect)
    pygame.display.update()
    city_sound.stop()
    beach_sound.stop()
    space_sound.stop()
    savepoint(p1_id,p1_point)
    savepoint(p2_id,p2_point)
    pygame.time.delay(2000)
    Game_start()

uid()
uid_sound.stop()
Game_start()