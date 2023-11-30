import pygame
import random

pygame.init()
white = (255, 255, 255)
X = 1200
Y = 650
doors = random.sample(range(1, 4), 3)
book1 = doors[0]
book2 = doors[1]
books = [book1, book2]
money = doors[2]
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Simulation')
image = pygame.image.load('all_doors.jpg')
change = False
msg_disp = False


def music():
    file = 'click.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def show_money(money, state):
    my_font = pygame.font.SysFont("forte", 32)
    display_surface = pygame.display.set_mode((X, Y))
    money1 = pygame.image.load('money_1.jpg')
    money2 = pygame.image.load('money_2.jpg')
    money3 = pygame.image.load('money_3.jpg')

    if money == 1:
        display_surface.blit(money1, (0, 0))
        pygame.display.update()
    elif money == 2:
        display_surface.blit(money2, (0, 0))
        pygame.display.update()
    elif money == 3:
        display_surface.blit(money3, (0, 0))
        pygame.display.update()
    if state == 1:
        the_text = my_font.render("YOU WON BY SWITCHING!!",
                                  True, (231, 0, 10))
        display_surface.blit(the_text, (350, 180))
        pygame.display.update()
    elif state == 2:
        the_text = my_font.render(
            "YOU COULD HAVE WON BY STAYING!!", True,
            (231, 0, 0))
        display_surface.blit(the_text, (350, 180))
        pygame.display.update()
    elif state == 3:
        the_text = my_font.render("YOU WON BY STAYING!!",
                                  True, (231, 0, 0))
        display_surface.blit(the_text, (350, 180))
        pygame.display.update()
    elif state == 4:
        the_text = my_font.render(
            "YOU COULD HAVE WON BY SWITCHING!!", True,
            (231, 0, 0))
        display_surface.blit(the_text, (350, 180))
        pygame.display.update()


def draw_rect():
    pygame.draw.rect(display_surface, (20, 24, 11),
                     (300, 220, 300, 40), 1)
    pygame.display.update()
    pygame.draw.rect(display_surface, (14, 2, 200),
                     (300, 260, 300, 40), 1)
    pygame.display.update()


while True:
    music()
    if change == False:
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        pygame.display.update()

        clicked = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if door 1 is pressed.
            if (event.pos[0] >= 65 and event.pos[0] <= 360
                    and event.pos[1] >= 224 and event.pos[1] <= 591):
                user = 1
                clicked = True
                music()
            # Check if door 2 is pressed.
            elif (event.pos[0] >= 419 and event.pos[0] <= 715
                  and event.pos[1] >= 224 and event.pos[1] <= 591):
                user = 2
                clicked = True
                music()
            # Check if door 3 is pressed.
            elif (event.pos[0] >= 789 and event.pos[0] <= 1085
                  and event.pos[1] >= 224 and event.pos[1] <= 591):
                user = 3

                clicked = True
                music()
        if clicked:

            image1 = pygame.image.load('book_1.jpg')
            image2 = pygame.image.load('book_2.jpg')
            image3 = pygame.image.load('book_3.jpg')
            image4 = pygame.image.load('money_1.jpg')
            image5 = pygame.image.load('money_2.jpg')
            image6 = pygame.image.load('money_3.jpg')
            wr = random.randint(0, 1)
            if (books[0] == user):
                g = books[1]
            elif (books[1] == user):
                g = books[0]
            else:
                g = books[wr]
            if g == 1:
                change = True
                display_surface.blit(image1, (0, 0))
                pygame.display.update()
            elif g == 2:
                change = True
                display_surface.blit(image2, (0, 0))
                pygame.display.update()
            elif g == 3:
                change = True
                display_surface.blit(image3, (0, 0))
                pygame.display.update()
            print(u"There were books behind the door {}".format(g))

            my_font = pygame.font.SysFont("cooper black", 28)
            the_text = my_font.render("Do you want to:", True, (231, 0, 0))
            display_surface.blit(the_text, (350, 180))
            the_text2 = my_font.render("SWITCH", True, (0, 0, 190))
            display_surface.blit(the_text2, (350, 220))
            the_text3 = my_font.render("STAY", True, (190, 0, 0))
            display_surface.blit(the_text3, (350, 260))
            draw_rect()
            clicked2 = False
            print(u"There is MONEY behind the door {}".format(money))

        # for event in pygame.event.get():
        clicked2 = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Compare click coordinates with coordinates
            # where it says 'Switch' and 'Stay'.
            if (event.pos[0] >= 299 and event.pos[0] <= 597
                    and event.pos[1] >= 220 and event.pos[1] <= 260):

                # user2 = 1 means user has chosen to switch.
                user2 = 1
                clicked2 = True
            elif (event.pos[0] >= 301 and event.pos[0] <= 598
                  and event.pos[1] >= 259 and event.pos[1] <= 297):

                # user2 = 2 means user has chosen to stay.
                user2 = 2
                clicked2 = True

        if clicked2:

            if user2 == 1:
                print("You chose to switch!")
                if user in books:
                    my_font = pygame.font.SysFont("forte", 30)
                    the_text = my_font.render(
                        "YOU WON BY SWITCHING!!", True, (231, 0, 0))
                    state = 1
                    display_surface.blit(the_text, (350, 180))
                    pygame.display.update()
                    print("YOU WON BY SWITCHING!!")

                # User has chosen the door behind which there is a car.
                else:
                    my_font = pygame.font.SysFont("forte", 30)
                    the_text2 = my_font.render(
                        "YOU COULD HAVE WON BY STAYING!!", True, (231, 0, 0))
                    state = 2
                    display_surface.blit(the_text2, (350, 180))
                    pygame.display.update()
                    print("YOU COULD HAVE WON BY SWITCHING!!")
            elif user2 == 2:
                print("You chose to stay!")
                if user == money:
                    my_font = pygame.font.SysFont("forte", 30)
                    the_text3 = my_font.render(
                        "YOU WON BY STAYING!!", True, (231, 0, 0))
                    display_surface.blit(the_text3, (350, 180))
                    state = 3
                    pygame.display.update()
                    print("YOU WON BY STAYING!!")
                else:
                    my_font = pygame.font.SysFont("forte", 30)
                    the_text4 = my_font.render(
                        "YOU COULD HAVE WON BY SWITCHING!!", True, (231, 0, 0))
                    display_surface.blit(the_text4, (350, 180))
                    state = 4
                    pygame.display.update()
                    print("YOU COULD HAVE WON BY SWITCHING!!")
            show_money(money, state)
