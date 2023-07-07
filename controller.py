import pygame
jscNum = 0
pygame.init()
pygame.joystick.init()
def findcontrolers(maxplayers,lastjoysticamouunt):
    status = ''
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    if pygame.joystick.get_count() != lastjoysticamouunt:
        status = str(pygame.joystick.get_count() + 1)+" controlers conected"
    if status != '':
        print(status)
        return(status)
    return()

findcontrolers(4,jscNum)