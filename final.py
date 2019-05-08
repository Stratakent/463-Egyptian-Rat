import pygame
import random
from threading import Timer
from random import randint

import collections

pygame.init()
#setup code

deckImg = ["PNG/AC.png","PNG/2C.png","PNG/3C.png","PNG/4C.png","PNG/5C.png","PNG/6C.png",
"PNG/7C.png","PNG/8C.png","PNG/9C.png","PNG/10C.png","PNG/JC.png","PNG/QC.png",
"PNG/KC.png",
"PNG/AS.png","PNG/2S.png","PNG/3S.png","PNG/4S.png","PNG/5S.png","PNG/6S.png",
"PNG/7S.png","PNG/8S.png","PNG/9S.png","PNG/10S.png","PNG/JS.png","PNG/QS.png",
"PNG/KS.png",
"PNG/AD.png","PNG/2D.png","PNG/3D.png","PNG/4D.png","PNG/5D.png","PNG/6D.png",
"PNG/7D.png","PNG/8D.png","PNG/9D.png","PNG/10D.png","PNG/JD.png","PNG/QD.png",
"PNG/KD.png",
"PNG/AH.png","PNG/2H.png","PNG/3H.png","PNG/4H.png","PNG/5H.png","PNG/6H.png",
"PNG/7H.png","PNG/8H.png","PNG/9H.png","PNG/10H.png","PNG/JH.png","PNG/QH.png",
"PNG/KH.png"
]

display_height = 900
display_width = 800
cardHeight = 100
cardWidth = 70
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Egyptian Rat Screw')
turn =0

# Deque setup
player = collections.deque()
cpu1 = collections.deque()
cpu2 = collections.deque()
cpu3 = collections.deque()
stack = collections.deque()
random.shuffle(deckImg)
for i in deckImg[0:12]:  # deal cards
   player.append(i)
for i in deckImg[13:25]:  # deal cards
   cpu3.append(i)
for i in deckImg[26:38]:  # deal cards
   cpu2.append(i)
for i in deckImg[39:51]:  # deal cards
   cpu1.append(i)

#function used to create text. args are desired text and fontsize
def textObject(text,font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

#function displays text at given coordinate.
def displayText(x,y,text,size):

    font = pygame.font.Font('freesansbold.ttf',size)
    textSurf, textText = textObject(text,font)
    textText.center = (x,y)
    win.blit(textSurf,textText)

    pygame.display.update()

# display home screen and start button
def welcomeDisplay():
    titleFont = pygame.font.Font('freesansbold.ttf',50)
    instructFont = pygame.font.Font('freesansbold.ttf',30)
    titleSurf, titleText = textObject("Egyptian Rat Screw",titleFont)
    instructSurf, instructText = textObject("Press Space to Start!",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 350))
    win.blit(titleSurf,titleText)

    displayCard(display_width / 2 - 75, display_height /2 - 225 ,player[0])

    instructText.center = ((display_width/2), (display_height/2 + 150))
    win.blit(instructSurf,instructText)

    pygame.display.update()

# create initial play area
def playArea():

    #player
    if player:
        displayCard(display_width / 2 - 75 , display_height/2 + 200,  player[0])
    else:
        displayCard(display_width / 2 - 75 , display_height/2 + 200,  0)
    displayText(530,670,"Player",35)


    #cpu2
    if cpu2:
        displayCard(display_width / 2 - 75 , display_height/2 - 400,  cpu2[0])
    else:
        displayCard(display_width / 2 - 75 , display_height/2 - 400,  0)

    displayText(530,65,"CPU 2",35)

    #middle pile
    # 4 possible scenarios: empty stack, stack has one card, two cards, or more than two cards
    # must display cards in correct order to prevent overlap
    if not stack:
        displayCard(display_width / 2 - 75 , display_height/2 - 100,  0)
        displayCard(display_width / 2 - 50 , display_height/2 - 100,  0)
        displayCard(display_width / 2 - 25 , display_height/2 - 100, 0)
    elif len(stack) == 1:
        displayCard(display_width / 2 - 25 , display_height/2 - 100,  stack[0])
    elif len(stack) == 2:
        displayCard(display_width / 2 - 75 , display_height/2 - 100, 0)
        displayCard(display_width / 2 - 50 , display_height/2 - 100,  stack[0])
        displayCard(display_width / 2 - 25 , display_height/2 - 100,  stack[1])
    else:
        displayCard(display_width / 2 - 75 , display_height/2 - 100, stack[len(stack) - 3])
        displayCard(display_width / 2 - 50 , display_height/2 - 100, stack[len(stack) - 2])
        displayCard(display_width / 2 - 25 , display_height/2 - 100, stack[len(stack)- 1])

    #cpu1
    if cpu1:
        displayCard(display_width / 2 + 200 , display_height/2 - 100,  cpu1[0])
    else:
        displayCard(display_width / 2 + 200 , display_height/2 - 100,  0)
    displayText(100,300,"CPU 1",35)


    #cpu3
    if cpu3:
        displayCard(display_width / 2 - 350 , display_height/2 - 100,  cpu3[0])
    else:
        displayCard(display_width / 2 - 350 , display_height/2 - 100,  0)
    displayText(700,300,"CPU 3",35)

    pygame.display.update()



# win/lose Screen
def endGame(outcome):
    titleFont = pygame.font.Font('freesansbold.ttf',50)
    instructFont = pygame.font.Font('freesansbold.ttf',30)
    if(outcome == 1):
        titleSurf, titleText = textObject("You Win!",titleFont)
    else:
        titleSurf, titleText = textObject("You Lose!",titleFont)

    instructSurf, instructText = textObject("Play Again?",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 200))
    win.blit(titleSurf,titleText)


    instructText.center = ((display_width/2 - 15), (display_height/2 + 150))
    win.blit(instructSurf,instructText)

    pygame.display.update()



def displayCard(x,y,card):
    if card == 0:
        cardBack = pygame.image.load("PNG/blue_back.png")
    else:
        cardBack = pygame.image.load(card)
    cardBack  = pygame.transform.rotozoom(cardBack ,0,.2)
    win.blit(cardBack,(x,y))

def addCard(activePlayer):
    print(activePlayer[0])
    stack.append(activePlayer.popleft())

def order(turn):
    card=0
    print("\n",len(player),"\n",len(cpu1),"\n",len(cpu2),"\n",len(cpu3))

    if turn % 4 == 0 and player:
        print("Player plays: ",player[0])
        stack.append(player.popleft())

    elif turn % 4 == 1 and cpu1:
        print("CPU1 plays: ", cpu1[0])
        stack.append(cpu1.popleft())
    elif turn % 4 == 2 and cpu2:
            print("CPU2 plays: ", cpu2[0])
            stack.append(cpu2.popleft())
    elif turn % 4 == 3 and cpu3:
        print("CPU3 plays: ", cpu3[0])
        stack.append(cpu3.popleft())
    else:
        turn += 1


    if not player and not cpu1 and not cpu2:
        print("CPU3 wins.")
        end()
    if not player and not cpu1 and not cpu3:
        print("CPU2 wins.")
        end()
    if not player and not cpu2 and not cpu3:
        print("CPU1 wins.")
        end()
    if not cpu1 and not cpu2 and not cpu3:
        print("You win.")
        end()

    turn=slap(player, cpu1, cpu2, cpu3, stack, turn)

    if not stack:
        print("New stack.")
    elif stack[-1][4]=='J' or stack[-1][4]=='Q' or stack[-1][4]=='K' or stack[-1][4]=='A':
        turn = face(player, cpu1, cpu2, cpu3, stack, turn)
    else:
        turn += 1

    print("Priority: ", turn%4)


# home screen
def main():
    win.fill((0,0,0))
    welcomeDisplay()

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            run = False
        pygame.display.update()
    game()

# game screen
def game():
    win.fill((0,0,0))
    run = True
    turn = 0
    print('RUn',run)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        playArea()
        order(turn)
        turn +=1
        print('RUn2',run)
        #order(start)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            slapCheck()
        if keys[pygame.K_LEFT] and cpu3:
            addCard(cpu3)
        if keys[pygame.K_RIGHT] and cpu1:
            addCard(cpu1)
        if keys[pygame.K_DOWN]:
            run = False
        pygame.display.update()



# end game

def face(player, cpu1, cpu2, cpu3, stack, original):
    turn = original+1
    pygame.display.update()
    if stack[-1][4]=='J':
        print("A jack has been played, set one: ")
        x = 1
    if stack[-1][4]=='Q':
        print("A queen has been played, set two: ")
        x = 2
    if stack[-1][4]=='K':
        print("A king has been played, set three: ")
        x = 3
    if stack[-1][4]=='A':
        print("An ace has been played, set four: ")
        x = 4

    card=0
    while (card==0):
        pygame.display.update()

        if turn % 4 == 0:
            while x > 0:
                if player:
                    print("Player places: ", player[0])
                    stack.append(player.popleft())
                    original=slap(player, cpu1, cpu2, cpu3, stack, original)
                    if len(stack) == 0:
                        return original
                    x-=1
                    if stack[-1][4]=='J' or stack[-1][4]=='Q' or stack[-1][4]=='K' or stack[-1][4]=='A':
                        original=turn
                        original=face(player, cpu1, cpu2, cpu3, stack, original)
                        return original
                else:
                    turn += 1
                    break

        if turn % 4 == 1:
            while x > 0:
                if cpu1:
                    print("CPU1 places: ", cpu1[0])
                    stack.append(cpu1.popleft())
                    original=slap(player, cpu1, cpu2, cpu3, stack, original)
                    if len(stack)==0:
                        return original
                    x-=1
                    if stack[-1][4]=='J' or stack[-1][4]=='Q' or stack[-1][4]=='K' or stack[-1][4]=='A':
                        original = turn
                        original = face(player, cpu1, cpu2, cpu3, stack, original)
                        return original
                else:
                    turn += 1
                    break

        if turn % 4 == 2:
            while x > 0:
                if cpu2:
                    print("CPU2 places: ", cpu2[0])
                    stack.append(cpu2.popleft())
                    original=slap(player, cpu1, cpu2, cpu3, stack,original)
                    if len(stack)==0:
                        return original
                    x-=1
                    if stack[-1][4]=='J' or stack[-1][4]=='Q' or stack[-1][4]=='K' or stack[-1][4]=='A':
                        original = turn
                        original = face(player, cpu1, cpu2, cpu3, stack, original)
                        return original
                else:
                    turn += 1
                    break

        if turn % 4 == 3:
            while x >  0:
                if cpu3:
                    print("CPU3 places: ", cpu3[0])
                    stack.append(cpu3.popleft())
                    original=slap(player, cpu1, cpu2, cpu3, stack, original)
                    if len(stack)==0:
                        return original
                    x -= 1
                    if stack[-1][4]=='J' or stack[-1][4]=='Q' or stack[-1][4]=='K' or stack[-1][4]=='A':
                        original = turn
                        original = face(player, cpu1, cpu2, cpu3, stack, original)
                        return original
                else:
                    turn += 1
                    break
        if not player and not cpu1 and not cpu2:
            print("CPU3 wins.")
            end()
        if not player and not cpu1 and not cpu3:
            print("CPU2 wins.")
            end()
        if not player and not cpu2 and not cpu3:
            print("CPU1 wins.")
            end()
        if not cpu1 and not cpu2 and not cpu3:
            print("You win.")
            end()
        if x==0:
            card=1



    if not stack[-1][4]=='J' or stack[-1][4]=='Q' or stack[-1][4]=='K' or stack[-1][4]=='A':

        # append everything to one who put down face card.
        if original % 4 == 0:
            print("You won the stack.", stack)
            while stack:
                player.append(stack.popleft())

        if original % 4 == 1:
            print("CPU1 won the stack.", stack)
            while stack:
                cpu1.append(stack.popleft())
        if original % 4 == 2:
            print("CPU2 won the stack.", stack)
            while stack:
                cpu2.append(stack.popleft())

        if original % 4 == 3:
            print("CPU3 won the stack.", stack)
            while stack:
                cpu3.append(stack.popleft())
        print(original%4)
        return original
        time.sleep(2)

def slap(player, cpu1, cpu2, cpu3, stack, turn):
    if not stack:
        return
    t = Timer(3.0, print, ["Continue."])

    t.start()
    print("Stack: ", stack)
    slapper = input("Will you slap?")
    if slapper == 'y' and t:
        if len(stack) == 1:
            print("Dipshit. There is only one card.... well not anymore.\n You lost cards: ")
            if player:
                print(player[-1])
                stack.appendleft(player.pop())
            if player:
                print(player[-1])
                stack.appendleft(player.pop())
            if not player:
                print("Stop losing cards!")
        elif len(stack) == 2:
            if stack[-1][4] == stack[-2][4]:
                print("You got the stack.")
                while stack:
                    player.append(stack.popleft())
                    while turn % 4 != 0:
                        turn += 1
                print(turn % 4)
                t.cancel()
                return turn
            else:
                print("Dipshit. You lost cards: ")
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if not player:
                    print("Stop losing cards!")
        elif len(stack) >= 2:
            if stack[-1][4] == stack[-2][4] or stack[-1][4] == stack[-3][4]:
                print("You got the stack.")
                while stack:
                    player.append(stack.popleft())
                    while turn % 4 != 0:
                        turn += 1
                print(turn % 4)
                t.cancel()
                return turn
            else:
                print("Dipshit. You lost cards: ")
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if not player:
                    print("Stop losing cards!")

    elif slapper == 'n':
            print("You passed.")

    t.cancel()

    # after input
    if len(stack)>2:
        if stack[-1][4] == stack[-2][4] or stack[-1][4] == stack[-3][4]:
             steal = randint(1, 3)
             if steal == 1:
                print("CPU1 slapped the stack.", stack)
                while stack:
                    cpu1.append(stack.popleft())
                    while turn % 4 != 1:
                        turn += 1
             if steal == 2:
                print("CPU2 slapped the stack.", stack)
                while stack:
                    cpu2.append(stack.popleft())
                    while turn % 4 != 2:
                        turn += 1
             if steal == 3:
                print("CPU3 slapped the stack.", stack)
                while stack:
                    cpu3.append(stack.popleft())
                    while turn % 4 != 3:
                        turn += 1
    print(turn % 4)
    return turn

def end():
    choice = input("Do you wanna play again?(y/n)")
    if choice == "y" or choice == "Y":
        play()
    # no
    else:
        exit()

'''
def endDisplay():
    win.fill((0,0,0))
    outcome = random.randint(0,1)
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        endGame(outcome)
        button(display_height / 2 - 50,display_width / 2 - 75,cardWidth,cardHeight,(128,128,0), (0,128,0), end)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()
'''


#function calls
main()

pygame.quit()
quit()
