from date import *
def is_game_close(): # вернуть необходимость выхода из программы
    return game_close
def display(): # Отрисовать все объекты
    pass
def quit_game(): # Выйти из программы
    quit()
def event():
    global game_close
    global snake_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = 'left'
                print('left')
            elif event.key == pygame.K_RIGHT:
                snake_direction = 'right'
                print('right')
            elif event.key == pygame.K_UP:
                snake_direction = 'up'
                print('up')
            elif event.key == pygame.K_DOWN:
                snake_direction = 'down'
                print('down')

def simulation():
    global snake_head
    if snake_direction == 'left':
        snake_head['x']-=1
        snake_head['x'] %= field_size
    if snake_direction == 'right':
        snake_head['x']+=1
        snake_head['x'] %= field_size
    if snake_direction == 'up':
        snake_head['y']-=1
        snake_head['y'] %= field_size
    if snake_direction == 'down':
        snake_head['y']+=1
        snake_head['y'] %= field_size
    if snake_head == apple_position:
        new_apple()
def display():
    dis.fill(black)
    #pygame.draw.rect(dis,(255,255,255),(75,75,50,50))

    drawSnakeHead()
    draw_apple()
    pygame.display.update()
    clock.tick(speed)


def drawSnakeHead():
    global dis
    pygame.draw.rect(dis,green,(snake_head['x']*20,snake_head['y']*20,20,20))
def draw_apple():
    pygame.draw.rect(dis,red,(apple_position['x']*20,apple_position['y']*20,20,20))
def new_apple():
    apple_position['x'] = random.randint(0,field_size - 1)
    apple_position['y'] = random.randint(0,field_size - 1)