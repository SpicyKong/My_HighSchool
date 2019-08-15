from tkinter import *
import pygame
from win32api import GetSystemMetrics
import time
import sys
from math import sin,cos,pi
def save_text():
    global entry_1,entry_21,entry_22,high,speed,angle,sungbun_x,sungbun_y
    high=dpi_y*0.79-float(entry_1.get())
    speed=float(entry_21.get())
    angle=float(entry_22.get())
    sungbun_x=(cos(angle/180*pi))*speed
    sungbun_y=(sin(angle/180*pi))*speed
    print(sungbun_x,sungbun_y)
    print(high,speed,angle)
def tk_window():
    global entry_1,entry_21,entry_22
    root=Tk()
    root.title("Input Box")
    root.geometry("420x80")
    root.resizable(0,0)

    top_frame=Frame()
    top_frame.pack(side=TOP,fill=BOTH)

    p1=Frame(top_frame)#,bg='lightgreen')
    p1.pack(side=LEFT,fill=BOTH)

    middle=Frame()
    middle.pack(side=TOP,fill=BOTH)

    p21=Frame(middle)#,bg='lightgreen')
    p21.pack(side=LEFT,fill=BOTH)

    p22=Frame(middle)#,bg='lightgreen')
    p22.pack(side=LEFT,fill=BOTH)

    text_high=Label(p1,text="시작높이")
    text_high.pack(side=LEFT)

    entry_1=Entry(p1)
    entry_1.pack(side=RIGHT)

    asdf=Label(top_frame,text="   ")
    asdf.pack(side=LEFT)

    text_21=Label(p21,text="      속력")
    text_21.pack(side=LEFT)

    entry_21=Entry(p21)
    entry_21.pack(side=RIGHT)

    text_22=Label(p22,text="    발사각도")
    text_22.pack(side=LEFT)

    entry_22=Entry(p22)
    entry_22.pack(side=RIGHT)

    button1=Button(top_frame,text="적용하기",command=save_text,relief=GROOVE)#,command=send_data)
    button1.pack(side=LEFT,pady=10)
    root.mainloop()

dpi_x, dpi_y = GetSystemMetrics(0), GetSystemMetrics(1)
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (dpi_x,dpi_y))
ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball, (dpi_x//25,dpi_x//25))
ballsc = pygame.image.load('ball.png')
ballsc = pygame.transform.scale(ball, (dpi_x//25,dpi_x//25))
start = pygame.image.load('start.png')
start = pygame.transform.scale(start, (dpi_x//8,dpi_x//12))

option = pygame.image.load('option.png')
option = pygame.transform.scale(option, (dpi_x//8,dpi_x//12))

b_pause = pygame.image.load('button_pause.png')
b_pause = pygame.transform.scale(b_pause, (dpi_x//8,dpi_x//12))

b_start = pygame.image.load('button_start.png')
b_start = pygame.transform.scale(b_start, (dpi_x//8,dpi_x//12))

ball_sc = pygame.image.load('ball.png')
ball_sc = pygame.transform.scale(ball_sc, (dpi_x//15,dpi_x//15))

ball_x = pygame.image.load('ball_x.png')
ball_x = pygame.transform.scale(ball_x, (dpi_x//25,dpi_x//25))

ball_y = pygame.image.load('ball_y.png')
ball_y = pygame.transform.scale(ball_y, (dpi_x//25,dpi_x//25))

print(dpi_x, dpi_y)
pygame.init()
screen=pygame.display.set_mode((dpi_x,dpi_y), pygame.FULLSCREEN) # 크기 150*150
pygame.display.set_caption("포물선 운동 시뮬레이터")

clock=pygame.time.Clock()
time_a=60
finish = False
x=0
y=200
mouse = 0
high=0
speed=0
angle=0
button_stpa=0
sungbun_x = 0
sungbun_y = 0
t=1
#print(sin(30/180*pi))
restart = 0
while not finish:
    screen.blit(background,(0,0))
    screen.blit(start,(dpi_x*0.02,dpi_y*0.87))
    screen.blit(option,(dpi_x//8 +dpi_x*0.04 ,dpi_y*0.87))
    #screen.blit(ballsc,(x,y))
    if restart and y+5*t*t-sungbun_y <= dpi_y*0.79:
        
        x+=sungbun_x
        y+=5*t*t-sungbun_y
        t+=0.01
    print(t)
    if not button_stpa:
        screen.blit(b_start,(dpi_x//4 +dpi_x*0.06, dpi_y*0.87))
    else:
        screen.blit(b_pause,(dpi_x//4 +dpi_x*0.06, dpi_y*0.87))

    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RETURN:
                print(x,y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse=1
            if dpi_x*0.02 <= mx <=dpi_x*0.02 +dpi_x//8 and dpi_y*0.87 <= my <= dpi_y*0.87 +dpi_x//12:
                restart = 1
                t=1
                button_stpa=0
                x=0
                y=high
            if dpi_x*0.04 +dpi_x//8 <= mx <=dpi_x*0.04 +dpi_x//4 and dpi_y*0.87 <= my <= dpi_y*0.87 +dpi_x//12:
                tk_window()
            if dpi_x*0.06 +dpi_x//4 <= mx <=dpi_x*0.06 +dpi_x//2 and dpi_y*0.87 <= my <= dpi_y*0.87 +dpi_x//12:
                if not button_stpa:
                    button_stpa=1
                    restart = 0
                else:
                    button_stpa = 0
                    restart = 1
        #if mouse==1:
        #    if event.type == pygame.MOUSEBUTTONUP:
        #        print("off",mx,my)
        #        mouse=0
    screen.blit(ball,(x,y))
    screen.blit(ball_x,(x,dpi_y*0.79))
    screen.blit(ball_y,(0,y))
    pygame.draw.line(screen, (255,0,0), [0,y], [x+dpi_x//25,y], 4)
    pygame.draw.line(screen, (255,0,0), [0,y+dpi_x//25], [x+dpi_x//25,y+dpi_x//25], 4)
    pygame.draw.line(screen, (255,0,0), [x,dpi_y*0.79+dpi_x//25], [x,y], 4)
    pygame.draw.line(screen, (255,0,0), [x+dpi_x//25,dpi_y*0.79+dpi_x//25], [x+dpi_x//25,y], 4)
    clock.tick(time_a)
    pygame.display.update()
    


