from date import *
def is_game_close(): # вернуть необходимость выхода из программы
    return game_close
def display(): # Отрисовать все объекты
    pass
def quit_game(): # Выйти из программы
    quit()
def event():
    global game_close
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_close = True

def simulation():
    if snake_direction == 'right':
        snake_head['x']+=1
def display():
    dis.fill(black)
    #pygame.draw.rect(dis,(255,255,255),(75,75,50,50))
    drawSnakeHead()
    pygame.display.update()
    clock.tick(speed)
def drawSnakeHead():
    global dis
    pygame.draw.rect(dis,green,(snake_head['x']*20,snake_head['y']*20,20,20))
