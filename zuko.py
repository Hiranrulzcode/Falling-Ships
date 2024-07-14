import pgzrun
import random
import pygame

pygame.init()
WIDTH=1000
HEIGHT=500
score=0
fireballm=False
zuko=Actor("zuko")
bullet=Actor("bullet")
ship=Actor("ship")
ships=[]
game_over=False
shipDes=0
zuko.pos=(500,450)

def create_ships():
    num=0
    for i in range(8):
        temp=Actor("ship")
        ships.append(temp)
        ships[i].pos=(125*num+33,50)
        num=num+1

create_ships()

def draw():
    global game_over, ships, shipDes
    screen.blit("bg",(0,0))
    zuko.draw()
    bullet.draw()
    for i in ships:
        i.draw()
        i.y=i.y+random.randint(0,3)-0.8
    if fireballm==True:
        bullet.y=bullet.y-7
    if shipDes==8:
        screen.clear()
        screen.fill("green")
        screen.draw.text("You Win", center=(500,250),fontsize=180)
    if game_over==True:
        screen.clear()
        screen.fill("red")
        screen.draw.text("You Lose", center=(500,250),fontsize=180)


def update():
    global game_over, ships, shipDes
    if keyboard.left:
        zuko.x=zuko.x-10
    if keyboard.right:
        zuko.x=zuko.x+10
    if keyboard[keys.SPACE]:
        fire()
    for i in ships:
        if bullet.colliderect(i):
            ships.remove(i)
            shipDes=shipDes+1
    
    for l in ships:
        if l.y>480:
            game_over=True

def fire():
    global fireballm
    bullet.pos=(zuko.x,(zuko.y-5))
    fireballm=True



















pgzrun.go()
