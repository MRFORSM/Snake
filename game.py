import  pygame
import  time
import  random

pygame.init()
white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift",25)
score_style = pygame.font.SysFont("comicsansms",35)
def your_score(score):
    value= score_font.render("Ваш счёт " + str(score),True,yellow)
    dis.blit(value,[0,0])

def our_snake(snake_block,snake_list):
    for x in snake_list:
         pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def message(msg,color):
    mesg = font_style.reder(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/3])

def game_loop():
    game_over =False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    snake_list =[]
    Lenght_of_snake = 1
    foodx = round(random.randrange(0,dis_width - snake_block /10.0))*10.0
    foody = round(random.randrange(0,dis_height - snake_block/10.0))*10.0
    while not game_over:
        while game_close ==True: # если проиграл
            dis.fill(blue)
            message("Вы проиграли!Нажмите Q для выхода или C для повторной игры",red)
            your_score(Lenght_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUiT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                  x1_change = - snake_block
                  y1_change = 0
                elif event.key == pygame.K_RIGHT or  event.key ==pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or  event.key ==pygame.K_w:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_DOWN or  event.key ==pygame.K_s:
                    x1_change = 0
                    y1_change = - snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: