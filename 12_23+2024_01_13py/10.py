import pygame

# 1. 게임 초기화
pygame.init()
  
# 2. 게임창 옵션 설정
size = [400, 900]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

ss = pygame.image.load("D:/temp/ss.png").convert_alpha()
ss = pygame.transform.scale(ss, (50,80))

black = (0,0,0)
white = (255,255,255)
k = 0

# 4. 메인 이벤트
SB = 0
while SB == 0:
    
    # 4-1. fps 설정
    clock.tick(60)

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3. 입력, 시간에 따른 변화
    k += 1

    # 4-4. 그리기
    screen.fill(black)

    # 4-5. 업데이트
    pygame.display.flip()
    
    
# 5. 게임 종료
pygame.quit