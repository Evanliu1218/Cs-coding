# import pygame
#
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((640, 480))
# g=1
# gr=1
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (0, g, 0), (320, 240), 50)
#     pygame.display.update()
#
#     g+=gr
#     if g==255:
#         gr=gr*-1
#     if g==0:
#         gr=gr+1
#
#     clock.tick(50)
# pygame.quit()
#
# import pygame
#
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((640, 480))
# g=10
# r=20
# t=30
# w=40
# l=50
# gr=1
# rr=1
# tr=1
# wr=1
# lr=0
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (255, 255, 255), (110, 240), g)
#     pygame.draw.circle(screen, (0, 0, 255), (220, 240), r)
#     pygame.draw.circle(screen, (255, 0, 0), (330, 240), t)
#     pygame.draw.circle(screen, (255, 255, 0), (440, 240), w)
#     pygame.draw.circle(screen, (0, 255, 255), (550, 240), l)
#     pygame.display.update()
#
#     g+=gr
#     if g==50:
#         gr=gr*-1
#     if g==0:
#         gr=1
#     r+=rr
#     if r==50:
#         rr=rr*-1
#     if r==0:
#         rr=1
#     t+=tr
#     if t==50:
#         tr=tr*-1
#     if t==0:
#         tr=1
#     w+=wr
#     if w==50:
#         wr=wr*-1
#     if w==0:
#         wr=1
#     l+=lr
#     if l==50:
#         lr=-1
#     if l==0:
#         lr=1
#
#
#     clock.tick(100)
# pygame.quit()

import pygame

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
g=1
gr=1
r=20
running = True
while running:
    for circles in range(10):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.draw.circle(screen, (0, g, 0), (320, 240), r)
    r += 5
    g += 20
    pygame.display.update()

pygame.quit()
