import pygame 
import sys

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
        if (eve.type == pygame.KEYUP and eve.key == pygame.K_c and eve.mod & pygame.KMOD_CTRL):
            pygame.quit()
            sys.exit()
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
        pygame.display.update()
        return ans

def main():
    if getKey('LEFT'):
        print('LEFT KEY')
    if getKey('RIGHT'):
        print('RIGHT KEY')


if __name__ == '__main__':
    init()
    while True:
        main()
