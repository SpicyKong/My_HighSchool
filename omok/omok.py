import numpy as np
import pygame

def jangmok_down(list_a):
    stone_color1=0
    end=False
    count=1
    for x in range(15):
        stone_color1=0
        count=1
        for y in range(15):
            if stone_color1 == list_a[y][x] and list_a[y][x]!=0:
                count+=1
                
            elif list_a[y][x]==1 or list_a[y][x]==2:
                stone_color1=list_a[y][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count>5:
                end=True
    return end

def jangmok_right(list_a):
    stone_color1=0
    end=False
    count=1
    for y in range(15):
        stone_color1=0
        count=1
        for x in range(15):
            if stone_color1 == list_a[y][x] and list_a[y][x]!=0:
                count+=1
                
            elif list_a[y][x]==1 or list_a[y][x]==2:
                stone_color1=list_a[y][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count>5:
                end=True
    return end

def jangmok_slash1(list_a):# o/
    stone_color1=0
    end=False
    count=1
    for y in range(4,15):
        stone_color1=0
        count=1
        for x in range(y+1):#(y+x,x)
            if stone_color1 == list_a[y-x][x] and list_a[y-x][x]!=0:
                count+=1
            elif list_a[y-x][x]==1 or list_a[y-x][x]==2:
                stone_color1=list_a[y-x][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count>5:
                end=True
    return end

def jangmok_slash2(list_a):# /o
    stone_color1=0
    end=False
    count=1
    for x in range(1,11):
        stone_color1=0
        count=1
        for y in range(15-x):#(y+x,x)
            if stone_color1 == list_a[14-y][x+y] and list_a[14-y][x+y]!=0:
                count+=1
            elif list_a[14-y][x+y]==1 or list_a[14-y][x+y]==2:
                stone_color1=list_a[14-y][x+y]
                count=1
            else:
                stone_color1=0
                count=1 
            if count>5:
                end=True
    return end

def jangmok_slash_in1(list_a):# o\
    stone_color1=0
    end=False
    count=1
    for y in reversed(range(11)):
        stone_color1=0
        count=1
        for x in range(15-y):
            #list_a[14-y-x][x]
            if stone_color1 == list_a[y+x][x] and list_a[y+x][x]!=0:
                count+=1
            elif list_a[y+x][x]==1 or list_a[y+x][x]==2:
                stone_color1=list_a[y+x][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count>5:
                end=True
    return end


def jangmok_slash_in2(list_a):# \o
    stone_color1=0
    end=False
    count=1
    for x in range(1,11):
        stone_color1=0
        count=1
        for y in range(15-x):
            if stone_color1 == list_a[y][x+y] and list_a[y][x+y]!=0:
                count+=1
            elif list_a[y][x+y]==1 or list_a[y][x+y]==2:
                stone_color1=list_a[y][x+y]
                count=1
            else:
                stone_color1=0
                count=1 
            #print(count)
            if count>5:
                end=True
    return end
def jangmok_all(list_a):
    end=False
    if jangmok_down(list_a) or jangmok_right(list_a) or jangmok_slash1(list_a) or jangmok_slash2(list_a) or jangmok_slash_in1(list_a) or jangmok_slash_in2(list_a):
        end=True
    return end

def sasa_all(list_a,turn_dol):
    list_save=[]
    end_for_ai=[]
    sasa_count=0
    torf_down=False
    torf_right=False
    torf_slash1=False
    torf_slash2=False
    torf_slash_in1=False
    torf_slash_in2=False
    for x in range(15):
        for y in range(15):
            if list_a[y][x]==0:
                list_a[y][x]=turn_dol
                if panjung_down(list_a) or panjung_right(list_a) or panjung_slash1(list_a) or panjung_slash2(list_a) or panjung_slash_in1(list_a) or panjung_slash_in2(list_a):
                    if not [y,x] in end_for_ai:
                        end_for_ai.append([y,x])
                if torf_down==False and panjung_down(list_a):
                    torf_down=True
                    sasa_count+=1
                    if not [y,x] in list_save:
                        list_save.append([y,x])
                if torf_right==False and panjung_right(list_a):
                    torf_right=True
                    sasa_count+=1
                    if not [y,x] in list_save:
                        list_save.append([y,x])
                if torf_slash1==False and panjung_slash1(list_a):
                    torf_slash1=True
                    sasa_count+=1
                    if not [y,x] in list_save:
                        list_save.append([y,x])
                if torf_slash2==False and panjung_slash2(list_a):
                    torf_slash2=True
                    sasa_count+=1
                    if not [y,x] in list_save:
                        list_save.append([y,x])
                if torf_slash_in1==False and panjung_slash_in1(list_a):
                    torf_slash_in1=True
                    sasa_count+=1
                    if not [y,x] in list_save:
                        list_save.append([y,x])
                if torf_slash_in2==False and panjung_slash_in2(list_a):
                    torf_slash_in2=True
                    sasa_count+=1
                    if not [y,x] in list_save:
                        list_save.append([y,x])
                if sasa_count>1:
                    list_a[y][x]=0
                    #print(sasa_count)
                    #print(end_for_ai)
                    return True,list_save,end_for_ai
                list_a[y][x]=0

    #print(sasa_count)
    #print("asdf",list_save,end_for_ai)

    return False,list_save,end_for_ai,sasa_count


def panjung_down(list_a):
    stone_color1=0
    end=False
    count=1
    for x in range(15):
        stone_color1=0
        count=1
        for y in range(15):
            if stone_color1 == list_a[y][x] and list_a[y][x]!=0:
                count+=1
                
            elif list_a[y][x]==1 or list_a[y][x]==2:
                stone_color1=list_a[y][x]
                count=1
            else:
                stone_color1=0
                count=1
            if count==5:
                end=True
    return end

def panjung_right(list_a):
    
    stone_color1=0
    end=False
    count=1
    for y in range(15):
        stone_color1=0
        count=1
        for x in range(15):
            if stone_color1 == list_a[y][x] and list_a[y][x]!=0:
                count+=1
                
            elif list_a[y][x]==1 or list_a[y][x]==2:
                stone_color1=list_a[y][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count==5:
                end=True
    return end
    
def panjung_slash1(list_a):# o/
    stone_color1=0
    end=False
    count=1
    for y in range(4,15):
        stone_color1=0
        count=1
        for x in range(y+1):#(y+x,x)
            if stone_color1 == list_a[y-x][x] and list_a[y-x][x]!=0:
                count+=1
            elif list_a[y-x][x]==1 or list_a[y-x][x]==2:
                stone_color1=list_a[y-x][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count==5:
                end=True
    return end

def panjung_slash2(list_a):# /o
    stone_color1=0
    end=False
    count=1
    for x in range(1,11):
        stone_color1=0
        count=1
        for y in range(15-x):#(y+x,x)
            if stone_color1 == list_a[14-y][x+y] and list_a[14-y][x+y]!=0:
                count+=1
            elif list_a[14-y][x+y]==1 or list_a[14-y][x+y]==2:
                stone_color1=list_a[14-y][x+y]
                count=1
            else:
                stone_color1=0
                count=1 
            if count==5:
                end=True
    return end

def panjung_slash_in1(list_a):# o\
    stone_color1=0
    end=False
    count=1
    for y in reversed(range(11)):
        stone_color1=0
        count=1
        for x in range(15-y):
            #list_a[14-y-x][x]
            if stone_color1 == list_a[y+x][x] and list_a[y+x][x]!=0:
                count+=1
            elif list_a[y+x][x]==1 or list_a[y+x][x]==2:
                stone_color1=list_a[y+x][x]
                count=1
            else:
                stone_color1=0
                count=1 
            if count==5:
                end=True
    return end


def panjung_slash_in2(list_a):# \o
    stone_color1=0
    end=False
    count=1
    for x in range(1,11):
        stone_color1=0
        count=1
        for y in range(15-x):
            if stone_color1 == list_a[y][x+y] and list_a[y][x+y]!=0:
                count+=1
            elif list_a[y][x+y]==1 or list_a[y][x+y]==2:
                stone_color1=list_a[y][x+y]
                count=1
            else:
                stone_color1=0
                count=1 
            #print(count)
            if count==5:
                end=True
    return end
    
def samsam_down(list_a,turn_dol):
    #print("-------")
    stone_color1=0
    stone_color_pre=0
    end=False
    sasa_count=0
    end_count=0
    list_yx=[]
    for x in range(1,14):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for y in range(1,14):
            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count==1:
                list_mid1.append([y-1,x])
                #print("[y,x] :",list_mid1)
                count+=1
            elif count==2 and list_a[y][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y][x] == 0 and end_count==0:
                list_mid1.append([y,x])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                #print(list_yx)
                count=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count1==1:
                list_mid2.append([y-1,x])
                count1+=1
            elif count1==2 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y][x] == 0:
                list_mid2.append([y,x])
                count1+=1
            elif count1==4 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y][x] == 0 and end_count==0:
                list_mid2.append([y,x])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count2==1:
                count2+=1
                list_mid3.append([y-1,x])
            elif count2==2 and list_a[y][x] == 0:
                count2+=1
                list_mid3.append([y,x])
            elif count2==3 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y][x] == 0 and end_count==0:
                list_mid3.append([y,x])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            stone_color_pre=int(list_a[y][x])
            
            if end_count>0:
                end_count-=1 # 마지막 수정 위치! 20181216, 11:49
    return sasa_count,list_yx

def samsam_right(list_a,turn_dol):
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    for y in range(1,14):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for x in range(1,14):
            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count==1:
                count+=1
                list_mid1.append([y,x-1])
            elif count==2 and list_a[y][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y][x] == 0 and end_count==0:
                list_mid1.append([y,x])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                count=1
                sasa_count+=1
                end_count=3
                #print("1")
            else:
                count=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count1==1:
                count1+=1
                list_mid2.append([y,x-1])
            elif count1==2 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y][x] == 0:
                list_mid2.append([y,x])
                count1+=1
            elif count1==4 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y][x] == 0 and end_count==0:
                list_mid2.append([y,x])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count2==1:
                count2+=1
                list_mid3.append([y,x-1])
            elif count2==2 and list_a[y][x] == 0:
                list_mid3.append([y,x])
                count2+=1
            elif count2==3 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y][x] == 0 and end_count==0:
                list_mid3.append([y,x])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            stone_color_pre=int(list_a[y][x])
            if end_count>0:
                end_count-=1
    return sasa_count,list_yx
    
def samsam_slash1(list_a,turn_dol):# o/
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    for y in range(5,15):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for x in range(y+1):#(y+x,x)
            if list_a[y-x][x] ==turn_dol and stone_color_pre==0 and count==1:
                list_mid1.append([y-x+1,x-1])
                count+=1
            elif count==2 and list_a[y-x][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y-x][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y-x][x] == 0 and end_count==0:
                list_mid1.append([y-x,x])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx] 
                end=True
                count=1
                sasa_count+=1
                end_count=3
            else:
                count=1
            
            if list_a[y-x][x] ==turn_dol and stone_color_pre==0 and count1==1:
                list_mid2.append([y-x+1,x-1])
                count1+=1
            elif count1==2 and list_a[y-x][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y-x][x] == 0:
                list_mid2.append([y-x,x])
                count1+=1
            elif count1==4 and list_a[y-x][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y-x][x] == 0 and end_count==0:
                list_mid2.append([y-x,x])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[y-x][x] ==turn_dol and stone_color_pre==0 and count2==1:
                list_mid3.append([y-x+1,x-1])
                count2+=1
            elif count2==2 and list_a[y-x][x] == 0:
                list_mid3.append([y-x,x])
                count2+=1
            elif count2==3 and list_a[y-x][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y-x][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y-x][x] == 0 and end_count==0:
                list_mid3.append([y-x,x])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[y-x][x])
    return sasa_count,list_yx

def samsam_slash2(list_a,turn_dol):# /o
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    for x in range(1,10):
        stone_color1=0
        count=1
        count1=1
        count2=1
        
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for y in range(15-x):#(y+x,x)
            if list_a[14-y][x+y] ==turn_dol and stone_color_pre==0 and count==1:
                list_mid1.append([14-y+1,x+y-1])
                count+=1
            elif count==2 and list_a[14-y][x+y] == turn_dol:
                count+=1
            elif count==3 and list_a[14-y][x+y] == turn_dol:
                count+=1
            elif count==4 and list_a[14-y][x+y] == 0 and end_count==0:
                list_mid1.append([14-y,x+y])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                count=1
                sasa_count+=1
                end_count=3
            else:
                count=1
            
            if list_a[14-y][x+y] ==turn_dol and stone_color_pre==0 and count1==1:
                count1+=1
                list_mid2.append([14-y+1,x+y-1])
            elif count1==2 and list_a[14-y][x+y] == turn_dol:
                count1+=1
            elif count1==3 and list_a[14-y][x+y] == 0:
                list_mid2.append([14-y,x+y])
                count1+=1
            elif count1==4 and list_a[14-y][x+y] == turn_dol:
                count1+=1
            elif count1==5 and list_a[14-y][x+y] == 0 and end_count==0:
                list_mid2.append([14-y,x+y])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[14-y][x+y] ==turn_dol and stone_color_pre==0 and count2==1:
                count2+=1
                list_mid3.append([14-y+1,x+y-1])
            elif count2==2 and list_a[14-y][x+y] == 0:
                count2+=1
                list_mid3.append([14-y,x+y])
            elif count2==3 and list_a[14-y][x+y] == turn_dol:
                count2+=1
            elif count2==4 and list_a[14-y][x+y] == turn_dol:
                count2+=1
            elif count2==5 and list_a[14-y][x+y] == 0 and end_count==0:
                list_mid3.append([14-y,x+y])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[14-y][x+y])
    #print(sasa_count)
    return sasa_count,list_yx

def samsam_slash_in1(list_a,turn_dol):# o\
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    for y in reversed(range(0,11)):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for x in range(15-y):
            #list_a[14-y-x][x]
            #if stone_color1 == list_a[y+x][x] and list_a[y+x][x]!=0:
            if list_a[y+x][x] ==turn_dol and stone_color_pre==0 and count==1:
                count+=1
                list_mid1.append([y+x-1,x-1])
            elif count==2 and list_a[y+x][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y+x][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y+x][x] == 0 and end_count==0:
                list_mid1.append([y+x,x])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                sasa_count+=1
                count=1
                end_count=3
            else:
                count=1
            
            if list_a[y+x][x] ==turn_dol and stone_color_pre==0 and count1==1:
                count1+=1
                list_mid2.append([y+x-1,x-1])
            elif count1==2 and list_a[y+x][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y+x][x] == 0:
                count1+=1
                list_mid2.append([y+x,x])
            elif count1==4 and list_a[y+x][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y+x][x] == 0 and end_count==0:
                list_mid2.append([y+x,x])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                end=True
                sasa_count+=1
                count1=1
                end_count=3
            else:
                count1=1

            if list_a[y+x][x] ==turn_dol and stone_color_pre==0 and count2==1:
                count2+=1
                list_mid3.append([y+x-1,x-1])
            elif count2==2 and list_a[y+x][x] == 0:
                count2+=1
                list_mid3.append([y+x,x])
            elif count2==3 and list_a[y+x][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y+x][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y+x][x] == 0 and end_count==0:
                list_mid3.append([y+x,x])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                end=True
                sasa_count+=1
                count2=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[y+x][x])
    return sasa_count,list_yx


def samsam_slash_in2(list_a,turn_dol):# \o
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    for x in range(1,10):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for y in range(15-x):
            #if stone_color1 == list_a[y][x+y] and list_a[y][x+y]!=0:
            if list_a[y][x+y] ==turn_dol and stone_color_pre==0 and count==1:
                count+=1
                list_mid1.append([y-1,x+y-1])
            elif count==2 and list_a[y][x+y] == turn_dol:
                count+=1
            elif count==3 and list_a[y][x+y] == turn_dol:
                count+=1
            elif count==4 and list_a[y][x+y] == 0 and end_count==0:
                list_mid1.append([y,x+y])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                count=1
                sasa_count+=1
                end_count=3
            else:
                count=1
            
            if list_a[y][x+y] ==turn_dol and stone_color_pre==0 and count1==1:
                count1+=1
                list_mid2.append([y-1,x+y-1])
            elif count1==2 and list_a[y][x+y] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y][x+y] == 0:
                list_mid2.append([y,x+y])
                count1+=1
            elif count1==4 and list_a[y][x+y] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y][x+y] == 0 and end_count==0:
                list_mid2.append([y,x+y])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                end=True
                sasa_count+=1
                count1=1
                end_count=3
            else:
                count1=1

            if list_a[y][x+y] ==turn_dol and stone_color_pre==0 and count2==1:
                count2+=1
                list_mid3.append([y-1,x+y-1])
            elif count2==2 and list_a[y][x+y] == 0:
                list_mid3.append([y,x+y])
                count2+=1
            elif count2==3 and list_a[y][x+y] == turn_dol:
                count2+=1
            elif count1==4 and list_a[y][x+y] == turn_dol:
                count1+=1
            elif count2==5 and list_a[y][x+y] == 0 and end_count==0:
                list_mid3.append([y,x+y])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                end=True
                sasa_count+=1
                count2=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[y][x+y])
    return sasa_count,list_yx

def samsam_all_non(list_a,turn_dol):
    count=0
    list_all=[]
    down,list_down=samsam_down(list_a,turn_dol)
    right,list_right=samsam_right(list_a,turn_dol)
    slash1,list_slash1=samsam_slash1(list_a,turn_dol)
    slash2,list_slash2=samsam_slash2(list_a,turn_dol)
    slash_in1,list_slash_in1=samsam_slash_in1(list_a,turn_dol)
    slash_in2,list_slash_in2=samsam_slash_in2(list_a,turn_dol)
    list_all=list_down+list_right+list_slash1+list_slash2+list_slash_in1+list_slash_in2
    #list_all=[]
    #list_all=list_down+list_down+list_right+list_slash1+list_slash2+list_slash_in1+list_slash_in2
    #print(len(list_all),list_all)
    if down:
        count+=down
        #print("down")
    if right:
        count+=right
        #print("right")
    if slash1:
        count+=slash1
        #print("slash1")
    if slash2:
        count+=slash2
        #print("slash2")
    if slash_in1:
        count+=slash_in1
        #print("slash_in1")
    if slash_in2:
        count+=slash_in2
        #print("slash_in2")
    return count, list_all

def sasam_down(list_a,turn_dol):#tturn_dol에 따른 번수 변경
    #print("-------")
    stone_color1=0
    stone_color_pre=0
    end=False
    sasa_count=0
    end_count=0
    list_yx=[]
    turn_dol1 = 2
    if turn_dol>1:
        turn_dol1=1
    for x in range(1,14):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for y in range(1,14):
            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count==1 or list_a[y][x] ==turn_dol and stone_color_pre==turn_dol1 and count==1:
                if stone_color_pre==0:
                    list_mid1.append([y-1,x])
                    list_mid1.append([y-2,x])
                count+=1
                #print("1")
            elif count==2 and list_a[y][x] == turn_dol:
                count+=1
                #print("2")
            elif count==3 and list_a[y][x] == turn_dol:
                count+=1
                #print("3")
            elif count==4 and list_a[y][x] == 0 and end_count==0 or count==4 and list_a[y][x] == turn_dol1 and end_count==0:
                if list_a[y][x]==0:
                    list_mid1.append([y,x])
                    list_mid1.append([y+1,x])
                #print(list_mid1)
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                #print("4")
                count=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count1==1 or list_a[y][x] ==turn_dol and stone_color_pre==turn_dol1 and count1==1:
                if stone_color_pre==0:
                    list_mid2.append([y-1,x])
                    list_mid2.append([y-2,x])
                count1+=1
            elif count1==2 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y][x] == 0:
                list_mid2.append([y,x])
                count1+=1
            elif count1==4 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y][x] == 0 and end_count==0 or count1==5 and list_a[y][x] == turn_dol1 and end_count==0:
                if list_a[y][x] == 0:
                    list_mid2.append([y,x])
                    list_mid2.append([y+1,x])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count2==1 or list_a[y][x] ==turn_dol and stone_color_pre==turn_dol1 and count2==1:
                count2+=1
                if stone_color_pre==0:
                    list_mid3.append([y-1,x])
                    list_mid3.append([y-2,x])
            elif count2==2 and list_a[y][x] == 0:
                count2+=1
                list_mid3.append([y,x])
            elif count2==3 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y][x] == 0 and end_count==0 or count2==5 and list_a[y][x] == turn_dol1 and end_count==0:
                if list_a[y][x] == 0:
                    list_mid3.append([y,x])
                    list_mid3.append([y+1,x])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            stone_color_pre=int(list_a[y][x])
            
            if end_count>0:
                end_count-=1 # 마지막 수정 위치! 20181216, 11:49
    #print(list_yx)
    return sasa_count,list_yx

def sasam_right(list_a,turn_dol):
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    turn_dol1 = 2
    if turn_dol>1:
        turn_dol1=1
    for y in range(1,14):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for x in range(1,14):
            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count==1 or list_a[y][x] ==1 and stone_color_pre==turn_dol1 and count==1:
                count+=1
                if stone_color_pre==0:
                    list_mid1.append([y,x-1])
                    list_mid1.append([y,x-2])
            elif count==2 and list_a[y][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y][x] == 0 and end_count==0 or count==4 and list_a[y][x] == turn_dol1 and end_count==0:
                if list_a[y][x] == 0:
                    list_mid1.append([y,x])
                    list_mid1.append([y,x+1])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                count=1
                sasa_count+=1
                end_count=3
                #print("1")
            else:
                count=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count1==1 or list_a[y][x] ==turn_dol and stone_color_pre==turn_dol1 and count1==1:
                count1+=1
                if stone_color_pre==0:
                    list_mid2.append([y,x-1])
                    list_mid2.append([y,x-2])
            elif count1==2 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y][x] == 0:
                list_mid2.append([y,x])
                count1+=1
            elif count1==4 and list_a[y][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y][x] == 0 and end_count==0 or count1==5 and list_a[y][x] == turn_dol1 and end_count==0:
                if list_a[y][x] == 0:
                    list_mid2.append([y,x])
                    list_mid2.append([y,x+1])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[y][x] ==turn_dol and stone_color_pre==0 and count2==1 or list_a[y][x] ==turn_dol and stone_color_pre==turn_dol1 and count2==1:
                count2+=1
                if stone_color_pre==0:
                    list_mid3.append([y,x-1])
                    list_mid3.append([y,x-2])
            elif count2==2 and list_a[y][x] == 0:
                list_mid3.append([y,x])
                count2+=1
            elif count2==3 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y][x] == 0 and end_count==0 or count2==5 and list_a[y][x] == turn_dol1 and end_count==0:
                if list_a[y][x] == 0:
                    list_mid3.append([y,x])
                    list_mid3.append([y,x+1])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            stone_color_pre=int(list_a[y][x])
            if end_count>0:
                end_count-=1
    return sasa_count,list_yx
    
def sasam_slash1(list_a,turn_dol):# o/
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    turn_dol1 = 2
    if turn_dol>1:
        turn_dol1=1
    for y in range(5,15):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for x in range(y+1):#(y+x,x)
            if list_a[y-x][x] ==turn_dol and stone_color_pre==0 and count==1 or list_a[y-x][x] ==turn_dol and stone_color_pre==turn_dol1 and count==1:
                if stone_color_pre==0:
                    list_mid1.append([y-x+1,x-1])
                    list_mid1.append([y-x+2,x-2])
                count+=1
            elif count==2 and list_a[y-x][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y-x][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y-x][x] == 0 and end_count==0 or count==4 and list_a[y-x][x] == turn_dol1 and end_count==0:
                if list_a[y-x][x] == 0:
                    list_mid1.append([y-x,x])
                    list_mid1.append([y-x-1,x+1])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx] 
                end=True
                count=1
                sasa_count+=1
                end_count=3
            else:
                count=1
            
            if list_a[y-x][x] ==turn_dol and stone_color_pre==0 and count1==1 or list_a[y-x][x] ==turn_dol and stone_color_pre==turn_dol1 and count1==1:
                if stone_color_pre==0:
                    list_mid2.append([y-x+1,x-1])
                    list_mid2.append([y-x+2,x-2])
                count1+=1
            elif count1==2 and list_a[y-x][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y-x][x] == 0:
                list_mid2.append([y-x,x])
                count1+=1
            elif count1==4 and list_a[y-x][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y-x][x] == 0 and end_count==0 or count1==5 and list_a[y-x][x] == turn_dol1 and end_count==0:
                if list_a[y-x][x]==0:
                    list_mid2.append([y-x,x])
                    list_mid2.append([y-x-1,x+1])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[y-x][x] ==turn_dol and stone_color_pre==0 and count2==1 or list_a[y-x][x] ==turn_dol and stone_color_pre==turn_dol1 and count2==1:
                if stone_color_pre==0:
                    list_mid3.append([y-x+1,x-1])
                    list_mid3.append([y-x+2,x-2])
                count2+=1
            elif count2==2 and list_a[y-x][x] == 0:
                list_mid3.append([y-x,x])
                count2+=1
            elif count2==3 and list_a[y-x][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y-x][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y-x][x] == 0 and end_count==0 or count2==5 and list_a[y-x][x] == turn_dol1 and end_count==0:
                if list_a[y-x][x]==0:
                    list_mid3.append([y-x,x])
                    list_mid3.append([y-x-1,x+1])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[y-x][x])
    #print("list_yx :",list_yx)
    return sasa_count,list_yx

def sasam_slash2(list_a,turn_dol):# /o
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    turn_dol1 = 2
    if turn_dol>1:
        turn_dol1=1
    for x in range(1,10):
        stone_color1=0
        count=1
        count1=1
        count2=1
        
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for y in range(15-x):#(y+x,x)
            if list_a[14-y][x+y] ==turn_dol and stone_color_pre==0 and count==1 or list_a[14-y][x+y] ==turn_dol and stone_color_pre==turn_dol1 and count==1:
                if stone_color_pre==0:
                    list_mid1.append([14-y+1,x+y-1])
                    list_mid1.append([14-y+2,x+y-2])
                    
                count+=1
            elif count==2 and list_a[14-y][x+y] == turn_dol:
                count+=1
            elif count==3 and list_a[14-y][x+y] == turn_dol:
                count+=1
            elif count==4 and list_a[14-y][x+y] == 0 and end_count==0 or count==4 and list_a[14-y][x+y] == turn_dol1 and end_count==0:
                if list_a[14-y][x+y]==0:
                    list_mid1.append([14-y,x+y])
                    list_mid1.append([14-y-1,x+y+1])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                count=1
                sasa_count+=1
                end_count=3
            else:
                count=1
            
            if list_a[14-y][x+y] ==turn_dol and stone_color_pre==0 and count1==1 or list_a[14-y][x+y] ==turn_dol and stone_color_pre==turn_dol1 and count1==1:
                count1+=1
                if stone_color_pre==0:
                    list_mid2.append([14-y+1,x+y-1])
                    list_mid2.append([14-y+2,x+y-2])
            elif count1==2 and list_a[14-y][x+y] == turn_dol:
                count1+=1
            elif count1==3 and list_a[14-y][x+y] == 0:
                list_mid2.append([14-y,x+y])
                count1+=1
            elif count1==4 and list_a[14-y][x+y] == turn_dol:
                count1+=1
            elif count1==5 and list_a[14-y][x+y] == 0 and end_count==0 or count1==5 and list_a[14-y][x+y] == turn_dol1 and end_count==0:
                if list_a[14-y][x+y]==0:
                    list_mid2.append([14-y,x+y])
                    list_mid2.append([14-y-1,x+y+1])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                count1=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count1=1

            if list_a[14-y][x+y] ==turn_dol and stone_color_pre==0 and count2==1 or list_a[14-y][x+y] ==turn_dol and stone_color_pre==turn_dol1 and count2==1:
                count2+=1
                if stone_color_pre==0:
                    list_mid3.append([14-y+1,x+y-1])
                    list_mid3.append([14-y+2,x+y-2])
            elif count2==2 and list_a[14-y][x+y] == 0:
                count2+=1
                list_mid3.append([14-y,x+y])
            elif count2==3 and list_a[14-y][x+y] == turn_dol:
                count2+=1
            elif count2==4 and list_a[14-y][x+y] == turn_dol:
                count2+=1
            elif count2==5 and list_a[14-y][x+y] == 0 and end_count==0 or count2==5 and list_a[14-y][x+y] == turn_dol1 and end_count==0 :
                if list_a[14-y][x+y] == 0:
                    list_mid3.append([14-y,x+y])
                    list_mid3.append([14-y-1,x+y+1])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                count2=1
                end=True
                sasa_count+=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[14-y][x+y])
    #print(sasa_count)
    return sasa_count,list_yx

def sasam_slash_in1(list_a,turn_dol):# o\
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    turn_dol1 = 2
    if turn_dol>1:
        turn_dol1=1
    for y in reversed(range(0,11)):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for x in range(15-y):
            #list_a[14-y-x][x]
            #if stone_color1 == list_a[y+x][x] and list_a[y+x][x]!=0:
            if list_a[y+x][x] ==turn_dol and stone_color_pre==0 and count==1 or list_a[y+x][x] ==turn_dol and stone_color_pre==turn_dol1 and count==1:
                count+=1
                if stone_color_pre==0:
                    list_mid1.append([y+x-1,x-1])
                    list_mid1.append([y+x-2,x-2])
            elif count==2 and list_a[y+x][x] == turn_dol:
                count+=1
            elif count==3 and list_a[y+x][x] == turn_dol:
                count+=1
            elif count==4 and list_a[y+x][x] == 0 and end_count==0 or count==4 and list_a[y+x][x] == turn_dol1 and end_count==0:
                if list_a[y+x][x]==0:
                    list_mid1.append([y+x,x])
                    list_mid1.append([y+x+1,x+1])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                sasa_count+=1
                count=1
                end_count=3
            else:
                count=1
            
            if list_a[y+x][x] ==turn_dol and stone_color_pre==0 and count1==1 or list_a[y+x][x] ==turn_dol and stone_color_pre==turn_dol1 and count1==1:
                count1+=1
                if stone_color_pre==0:
                    list_mid2.append([y+x-1,x-1])
                    list_mid2.append([y+x-2,x-2])
            elif count1==2 and list_a[y+x][x] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y+x][x] == 0:
                count1+=1
                list_mid2.append([y+x,x])
            elif count1==4 and list_a[y+x][x] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y+x][x] == 0 and end_count==0 or count1==5 and list_a[y+x][x] == turn_dol1 and end_count==0:
                if list_a[y+x][x]==0:
                    list_mid2.append([y+x,x])
                    list_mid2.append([y+x+1,x+1])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                end=True
                sasa_count+=1
                count1=1
                end_count=3
            else:
                count1=1

            if list_a[y+x][x] ==turn_dol and stone_color_pre==0 and count2==1 or list_a[y+x][x] ==turn_dol and stone_color_pre==turn_dol1 and count2==1:
                count2+=1
                if stone_color_pre==0:
                    list_mid3.append([y+x-1,x-1])
                    list_mid3.append([y+x-2,x-2])
            elif count2==2 and list_a[y+x][x] == 0:
                count2+=1
                list_mid3.append([y+x,x])
            elif count2==3 and list_a[y+x][x] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y+x][x] == turn_dol:
                count2+=1
            elif count2==5 and list_a[y+x][x] == 0 and end_count==0 or count2==5 and list_a[y+x][x] == turn_dol1 and end_count==0:
                if list_a[y+x][x]==0:
                    list_mid3.append([y+x,x])
                    list_mid3.append([y+x+1,x+1])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                end=True
                sasa_count+=1
                count2=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[y+x][x])
    return sasa_count,list_yx

def sasam_slash_in2(list_a,turn_dol):# \o
    stone_color1=0
    stone_color_pre=0
    end=False
    count=1
    sasa_count=0
    end_count=0
    list_yx=[]
    turn_dol1 = 2
    if turn_dol>1:
        turn_dol1=1
    for x in range(1,10):
        stone_color1=0
        count=1
        count1=1
        count2=1
        list_mid1=[]
        list_mid2=[]
        list_mid3=[]
        for y in range(15-x):
            #if stone_color1 == list_a[y][x+y] and list_a[y][x+y]!=0:
            if list_a[y][x+y] ==turn_dol and stone_color_pre==0 and count==1 or list_a[y][x+y] ==turn_dol and stone_color_pre==turn_dol1 and count==1:
                count+=1
                if stone_color_pre == 0:
                    list_mid1.append([y-1,x+y-1])
                    list_mid1.append([y-2,x+y-2])
            elif count==2 and list_a[y][x+y] == turn_dol:
                count+=1
            elif count==3 and list_a[y][x+y] == turn_dol:
                count+=1
            elif count==4 and list_a[y][x+y] == 0 and end_count==0 or count==4 and list_a[y][x+y] == turn_dol1 and end_count==0:
                if list_a[y][x+y] == 0:
                    list_mid1.append([y,x+y])
                    list_mid1.append([y+1,x+y+1])
                [list_yx.append(a) for a in list_mid1 if not a in list_yx]
                end=True
                count=1
                sasa_count+=1
                end_count=3
            else:
                count=1
            
            if list_a[y][x+y] ==turn_dol and stone_color_pre==0 and count1==1 or list_a[y][x+y] ==turn_dol and stone_color_pre==turn_dol1 and count1==1:
                count1+=1
                if stone_color_pre==0:
                    list_mid2.append([y-1,x+y-1])
                    list_mid2.append([y-2,x+y-2])
            elif count1==2 and list_a[y][x+y] == turn_dol:
                count1+=1
            elif count1==3 and list_a[y][x+y] == 0:
                list_mid2.append([y,x+y])
                count1+=1
            elif count1==4 and list_a[y][x+y] == turn_dol:
                count1+=1
            elif count1==5 and list_a[y][x+y] == 0 and end_count==0 or count1==5 and list_a[y][x+y] == turn_dol1 and end_count==0:
                if list_a[y][y+x]==0:
                    list_mid2.append([y,x+y])
                    list_mid2.append([y+1,x+y+1])
                [list_yx.append(a) for a in list_mid2 if not a in list_yx]
                end=True
                sasa_count+=1
                count1=1
                end_count=3
            else:
                count1=1

            if list_a[y][x+y] ==turn_dol and stone_color_pre==0 and count2==1 or list_a[y][x+y] ==turn_dol and stone_color_pre==turn_dol1 and count2==1:
                count2+=1
                if stone_color_pre==0:
                    list_mid3.append([y-1,x+y-1])
                    list_mid3.append([y-2,x+y-2])
            elif count2==2 and list_a[y][x+y] == 0:
                list_mid3.append([y,x+y])
                count2+=1
            elif count2==3 and list_a[y][x+y] == turn_dol:
                count2+=1
            elif count2==4 and list_a[y][x+y] == turn_dol:
                count1+=1
            elif count2==5 and list_a[y][x+y] == 0 and end_count==0 or count2==5 and list_a[y][x+y] == turn_dol1 and end_count==0:
                if list_a[y][y+x]==0:
                    list_mid3.append([y,x+y])
                    list_mid3.append([y+1,x+y+1])
                [list_yx.append(a) for a in list_mid3 if not a in list_yx]
                end=True
                sasa_count+=1
                count2=1
                end_count=3
            else:
                count2=1
            if end_count>0:
                end_count-=1
            stone_color_pre=int(list_a[y][x+y])
    return sasa_count,list_yx

def sasam_all_non(list_a,turn_dol):
    count=0
    list_all=[]

    list_save=[0,0,0,0,0,0]
    down,list_down=sasam_down(list_a,turn_dol)
    right,list_right=sasam_right(list_a,turn_dol)
    slash1,list_slash1=sasam_slash1(list_a,turn_dol)
    slash2,list_slash2=sasam_slash2(list_a,turn_dol)
    slash_in1,list_slash_in1=sasam_slash_in1(list_a,turn_dol)
    slash_in2,list_slash_in2=sasam_slash_in2(list_a,turn_dol)
    list_all=list_down+list_right+list_slash1+list_slash2+list_slash_in1+list_slash_in2
    #list_all=[]
    #list_all=list_down+list_down+list_right+list_slash1+list_slash2+list_slash_in1+list_slash_in2
    print(list_all)
    if down:
        count+=down
        print("down")
    if right:
        count+=right
        print("right")
    if slash1:
        count+=slash1
        print("slash1")
    if slash2:
        count+=slash2
        print("slash2")
    if slash_in1:
        count+=slash_in1
        print("slash_in1")
    if slash_in2:
        count+=slash_in2
        print("slash_in2")
    #print(list_all)
    return count, list_all

def panjung_all(list_a):
    #print(panjung_down(list_a))
    end=False
    panjung_count=0
    if panjung_down(list_a):
        panjung_count+=1
    if panjung_right(list_a):
        panjung_count+=1
    if panjung_slash1(list_a):
        panjung_count+=1
    if panjung_slash2(list_a):
        panjung_count+=1
    if panjung_slash_in1(list_a):
        panjung_count+=1
    if panjung_slash_in2(list_a):
        panjung_count+=1
    if panjung_count>0:
        print("End")
        end=True
    return end,panjung_count

def ai_first(list_a):
    list_b=list_a[:]
    re_v=False
    set_point_list=[]
    for y in range(15):
        for x in range(15):
            if list_b[y][x]==0:
                list_b[y][x]=1
                if panjung_down(list_b):
                    set_point_list.append([y,x])
                if panjung_right(list_b):
                    set_point_list.append([y,x])
                if panjung_slash1(list_b):
                    set_point_list.append([y,x])
                if panjung_slash2(list_b):
                    set_point_list.append([y,x])
                if panjung_slash_in1(list_b):
                    set_point_list.append([y,x])
                if panjung_slash_in2(list_b):
                    set_point_list.append([y,x])
                list_b[y][x]=0
    if len(set_point_list)>0:
        re_v=True
    return re_v,set_point_list

def ai_second_d(list_a,board,turn_dol):#방어
    list_re=[]
    #print("asdf :",list_a)
    #print(list_a,turn_dol)
    samsam=sasam_all_non(board,1)[0]#현재 3개수를 파악
    samsam1=samsam_all_non(board,1)[0]#현재 3개수를 파악
    #print(list_a)
    for point in list_a:
        #print(point)
        if 0 <= point[0] <15 and 0 <= point[1] <15:
            if board[point[0]][point[1]]==0:
                if samsam1==0:
                    board[point[0]][point[1]]=turn_dol
                    if samsam1  < samsam_all_non(board,1)[0]:
                        sasa_count=0
                        for x in range(15):
                            for y in range(15):
                                if board[y][x]==0:
                                    board[y][x]=turn_dol
                                    if panjung_down(board) or panjung_right(board) or panjung_slash1(board) or panjung_slash2(board) or panjung_slash_in1(board) or panjung_slash_in2(board):

                                        if not [point[0],point[1]] in list_re:
                                            list_re.append([point[0],point[1]])
                
                                    board[y][x]=0
                    board[point[0]][point[1]]=0
    print(list_re)
    #list_re
    #print(sasam,sa)
    return list_re
def ai_second_a(list_a,board,turn_dol):#방어
    list_re=[]
    #print("asdf :",list_a)
    #print(list_a,turn_dol)
    samsam=sasam_all_non(board,2)[0]#현재 3개수를 파악
    #print(list_a)
    for point in list_a:
        #print(point)
        if 0 <= point[0] <15 and 0 <= point[1] <15:
            if board[point[0]][point[1]]==0:
                board[point[0]][point[1]]=turn_dol
                if samsam  <= sasam_all_non(board,1)[0]:
                    sasa_count=0
                    for x in range(15):
                        for y in range(15):
                            if board[y][x]==0:
                                board[y][x]=turn_dol
                                if panjung_down(board) or panjung_right(board) or panjung_slash1(board) or panjung_slash2(board) or panjung_slash_in1(board) or panjung_slash_in2(board):

                                    if not [point[0],point[1]] in list_re:
                                        list_re.append([point[0],point[1]])

                                board[y][x]=0
                board[point[0]][point[1]]=0
    #print(list_re)
    #list_re
    return list_re
def ai_sa(board,turn_dol):
    board_score=[
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #_,_,save_point = sasa_all(board,turn_dol)
    #print(save_point)
    _,save_point,panquf=samsam_all_non1(board,turn_dol)#현재 3개수를 파악
    #print(samsam)
    for point in save_point:
        if board[point[0]][point[1]]==0:
            board_score[point[0]][point[1]]+=700
    return board_score
    
    #print(list_re)
def ai_defence(board,turn_dol):
    #_,sam_save = samsam_all_non(board,turn_dol)
    

    board_score=[
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    test_A,test_B = sasam_all_non(board,1)
    test_C=ai_second_d(test_B,board,1)

    for list_C in test_C:
        board_score[list_C[0]][list_C[1]] +=500
    
    for sam_save in samsam_all_non(board,1)[1]:
        board_score[sam_save[0]][sam_save[1]]+=1000
    for y in range(15):
        for x in range(15):
            if board[y][x]==1:
                if y-1>0 and x-1>0:
                    board_score[y-1][x-1]+=30
                if y-1>0:
                    board_score[y-1][x]+=30
                if y-1>0 and x+1<14:
                    board_score[y-1][x+1]+=30
                if x-1>0:
                    board_score[y][x-1]+=30
                if x+1<14:
                    board_score[y][x+1]+=30
                if y+1<14 and x-1>0:
                    board_score[y+1][x-1]+=30
                if y+1<14:
                    board_score[y+1][x]+=30
                if y+1<14 and x+1<14:
                    board_score[y+1][x+1]+=30
            if board[y][x]==2:
                if y-1>0 and x-1>0:
                    board_score[y-1][x-1]+=45
                if y-1>0:
                    board_score[y-1][x]+=40
                if y-1>0 and x+1<14:
                    board_score[y-1][x+1]+=45
                if x-1>0:
                    board_score[y][x-1]+=40
                if x+1<14:
                    board_score[y][x+1]+=40
                if y+1<14 and x-1>0:
                    board_score[y+1][x-1]+=45
                if y+1<14:
                    board_score[y+1][x]+=40
                if y+1<14 and x+1<14:
                    board_score[y+1][x+1]+=45
    for y in range(15):
        for x in range(15):
            if board[y][x]==1 or board[y][x]==2:
                board_score[y][x]=0
    return board_score
def samsam_all_non1(list_a,turn_dol):
    count=0
    list_all=[]
    list_b=[0,0,0,0,0,0]
    down,list_down=samsam_down(list_a,turn_dol)
    right,list_right=samsam_right(list_a,turn_dol)
    slash1,list_slash1=samsam_slash1(list_a,turn_dol)
    slash2,list_slash2=samsam_slash2(list_a,turn_dol)
    slash_in1,list_slash_in1=samsam_slash_in1(list_a,turn_dol)
    slash_in2,list_slash_in2=samsam_slash_in2(list_a,turn_dol)
    list_all=list_down+list_right+list_slash1+list_slash2+list_slash_in1+list_slash_in2
    #list_all=[]
    #list_all=list_down+list_down+list_right+list_slash1+list_slash2+list_slash_in1+list_slash_in2
    #print(len(list_all),list_all)
    if down:
        count+=down
        if list_b[0]==0:
            list_b[0]+=1
        #print("down")
    if right:
        if list_b[1]==0:
            list_b[1]+=1
        count+=right
        #print("right")
    if slash1:
        if list_b[2]==0:
            list_b[2]+=1
        count+=slash1
        #print("slash1")
    if slash2:
        if list_b[3]==0:
            list_b[3]+=1
        count+=slash2
        #print("slash2")
    if slash_in1:
        if list_b[4]==0:
            list_b[4]+=1
        count+=slash_in1
        #print("slash_in1")
    if slash_in2:
        if list_b[5]==0:
            list_b[5]+=1
        count+=slash_in2
        #print("slash_in2")
    return count, list_all,list_b
def ai_attack(board,turn_dol):
    board_score=[
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    samsam_save,_ = samsam_all_non(board,turn_dol)
    test_A,test_B= sasam_all_non(board,turn_dol)
    #print(samsam_save)
    test_C=ai_second_a(test_B,board,turn_dol)#43공격
    #print(test_A,test_B,test_C)
    for list_C in test_C:
        board_score[list_C[0]][list_C[1]] += 1200


    for y in range(15):
        for x in range(15):
            if board[y][x]==0:
                board[y][x]=turn_dol
                samsam_count,_=samsam_all_non(board,turn_dol)
                if samsam_count > samsam_save+1:
                    board_score[y][x]+=300
                if samsam_count > samsam_save:
                    board_score[y][x]+=100
                #if panjung_down(board) or panjung_right(board) or panjung_slash1(board) or panjung_slash2(board) or panjung_slash_in1(board) or panjung_slash_in2(board):
                #    board_score[y][x]+=10000
                board[y][x]=0
    return board_score
def ask_end(board):
    for y in range(15):
        for x in range(15):
            if board[y][x]==0:
                board[y][x]=2
                if panjung_down(board) or panjung_right(board) or panjung_slash1(board) or panjung_slash2(board) or panjung_slash_in1(board) or panjung_slash_in2(board):
                    return [y,x]
                board[y][x]=0
    return [15,15]

def abp_purning(board,list_a):
    pass
    


window_length=250*3
window_high=250*3
window_num=0#window_high/3
pygame.init()
screen=pygame.display.set_mode((window_length,window_high)) # 크기 150*150
pygame.display.set_caption("오목!")
finish=False

my_img=pygame.image.load("omok\game_board.png")
my_img=pygame.transform.scale(my_img,(window_high,window_high))

#a=300
win_black=pygame.image.load("omok\win_black.png")
win_black=pygame.transform.scale(win_black,(int(300*2.5),300))

win_white=pygame.image.load("omok\win_white.png")
win_white=pygame.transform.scale(win_white,(int(300*2.5),300))

select=pygame.image.load("omok\select2.png")
select=pygame.transform.scale(select,(int(45*5/6),int(45*5/6)))

last_sign1=pygame.image.load("omok\last_sign1.png")
last_sign1=pygame.transform.scale(last_sign1,(int(45*5/6),int(45*5/6)))

last_sign2=pygame.image.load("omok\last_sign2.png")
last_sign2=pygame.transform.scale(last_sign2,(int(45*5/6),int(45*5/6)))

stone_b=pygame.image.load("omok\wblack_stone.png")
stone_b=pygame.transform.scale(stone_b,(int(45*5/6),int(45*5/6)))

stone_w=pygame.image.load("omok\white_stone.png")
stone_w=pygame.transform.scale(stone_w,(int(45*5/6),int(45*5/6)))

#my_rect1 = pygame.Rect(0,0,window_num,window_high)
#your_rect1 =  pygame.Rect(window_length-window_num,0,window_length,window_high)

play_button=pygame.image.load("omok\play_button.png")
play_button=pygame.transform.scale(play_button,(250*2+14,250*1))

play_button2=pygame.image.load("omok\play_button2.png")
play_button2=pygame.transform.scale(play_button2,(250*2,250*1))

selected_button=pygame.image.load("omok\selected_button.png")
selected_button=pygame.transform.scale(selected_button,(250*2+14,250*1))

selected_button2=pygame.image.load("omok\selected_button2.png")
selected_button2=pygame.transform.scale(selected_button2,(250*2,250*1))
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 80)
textsurface = myfont.render('금수입니다!', False, (240, 200, 200))
check=0
y=375-18.75
x=625-18
x_1=7
y_1=7
dis=47
clock=pygame.time.Clock()
time_a=5
turn_dol=1

def make_pan(list_a):
    for a in range(len(list_a)):
        for b in range(15):
            if list_a[a][b]>0 and list_a[a][b]==1:
                screen.blit(stone_b,(625-18+(b-7)*47-250,375-18.75+(a-7)*47))
            if list_a[a][b]>0 and list_a[a][b]==2:
                screen.blit(stone_w,(625-18+(b-7)*47-250,375-18.75+(a-7)*47))
def last_stone(list_a):
    screen.blit(last_sign1,(625-18+(list_a[0]-7)*47-250,375-18.75+(list_a[1]-7)*47))

end_value=True

while end_value:
    game_end=False
    game_end1=False
    turn_dol1=1
    ai_lose=False
    finish=False
    check=0
    y=375-18.75
    x=625-18-250
    x_1=7
    y_1=7
    dis=47
    clock=pygame.time.Clock()
    time_a=5
    turn_dol=1
    last_stone_xy=[7,7]
    pan=[
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #print("asdhjkasjdklasdjklasdjldlk")
    screen.blit(my_img,(window_num,0))
    screen.blit(select,(x,y))
    pygame.display.update()
    while not finish:
        screen.fill(0)
        #pygame.draw.rect(screen, (219,188,104), my_rect1)
        #pygame.draw.rect(screen, (219,188,104), your_rect1)
        screen.blit(my_img,(window_num,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end_value=False
                finish=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if y-dis > 0:
                        y -= dis
                        x_1 -= 1
                elif event.key == pygame.K_DOWN:
                    if y+dis < window_high-dis:
                        y += dis
                        x_1 += 1
                elif event.key == pygame.K_RIGHT:
                    if x+dis < window_high+window_num-dis:
                        x += dis
                        y_1 += 1
                elif event.key == pygame.K_LEFT:
                    if x-dis >window_num:
                        x -= dis
                        y_1 -= 1
                elif event.key == pygame.K_RETURN and game_end ==False:
                    if pan[x_1][y_1]==0:
                        save_samsam,_=samsam_all_non(pan,turn_dol)
                        pan[x_1][y_1]=turn_dol
                        save_list=samsam_all_non(pan,turn_dol)[1]
                        if sasa_all(pan,turn_dol)[0]:
                            pan[x_1][y_1]=0
                        elif save_samsam+1 < samsam_all_non(pan,turn_dol)[0]:
                            pan[x_1][y_1]=0
                        elif jangmok_all(pan) and pan[x_1][y_1]==1:
                            pan[x_1][y_1]=0
                        else:
                            
                            game_end,_ = panjung_all(pan)
                            if game_end==True:
                                ai_lose=True
                            screen.blit(my_img,(window_num,0))
                            screen.blit(select,(x,y))
                            make_pan(pan)
                            pygame.display.update()
                            
                            _,test =ai_first(pan)
                            ask=ask_end(pan)
                            #print(ask)
                            if not ask==[15,15]:
                                pan[ask[0]][ask[1]]=2
                                if ai_lose==False and panjung_all(pan)[0]:
                                    game_end=True
                                    ai_lose==False
                                last_stone_xy=ask[0],ask[1]
                            elif len(test) > 0:
                                pan[test[0][0]][test[0][1]]=2
                                if ai_lose==False and panjung_all(pan)[0]:
                                    game_end=True
                                    ai_lose==False
                                last_stone_xy=test[0][0],test[0][1]
                            else:
                                print("생각중..")
                                board1=np.array(ai_defence(pan,2))
                                board2=np.array(ai_attack(pan,2))
                                board4=np.array(ai_sa(pan,2))
                                board3=board1+board2+board4
                                print(board3)
                                save=0
                                list_save_xy=[]
                                for a in range(15):
                                    for b in range(15):
                                        if board3[a][b] >save:
                                            save=int(board3[a][b])
                                            list_save_xy=[a,b]
                                pan[list_save_xy[0]][list_save_xy[1]] = 2
                                last_stone_xy=list_save_xy[0],list_save_xy[1]
                                if ai_lose==False and panjung_all(pan)[0]:
                                    game_end=True
                                    ai_lose==False
                elif event.key == pygame.K_RETURN and game_end ==True:
                        finish=True
                elif event.key == pygame.K_F5:
                    pan=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                elif event.key == pygame.K_F1:
                    pan[x_1][y_1]=0
                elif event.key == pygame.K_F2:
                    pan[x_1][y_1]=2
                elif event.key == pygame.K_F3:
                    pan[x_1][y_1]=1
                elif event.key == pygame.K_F4:
                    print(x_1,y_1)
                elif event.key == pygame.K_F10:
                    end_value=False
                    finish=True
                
                screen.blit(my_img,(window_num,0))
                screen.blit(select,(x,y))
                make_pan(pan)
                last_stone([last_stone_xy[1],last_stone_xy[0]])
                
                if game_end:
                    if ai_lose==False and not game_end1:
                        screen.blit(win_white,(0,250))
                        pygame.display.update()
                        game_end1=True
                    elif ai_lose==True and not game_end1:
                        screen.blit(win_black,(0,250))
                        pygame.display.update()
                        game_end1=True
                pygame.display.update()
