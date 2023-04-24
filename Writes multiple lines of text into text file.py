#Imports the necessary modules
import pygame

#Sets the value for the width and height of the display screen
W, H = 800, 600

#Creates the display screen
display = pygame.Surface ((W, H))
screen = pygame.display.set_mode ((W, H))
clock = pygame.time.Clock()

#RGB example values
black = (0,0,0)
white = (255,255,255)

#The rate of change in colors
col_spd = 1

#The color directory & its values
col_dir =[[-1,1,1]]
def_col = [[120,120,240]]



# Opens the text file
with open("mylife.txt", "w") as file:
    #Asks the user to enter a line
    line = input(str("Enter line: "))
    #Writes the line into the file
    file.write(line + "\n")
    #Asks user if there are more lines to be inputted
    inputLines = input(str("Are there more lines y/n? "))
    count = 0
    while not inputLines or inputLines[0].lower() not in ['y', 'n']:
        print("ERROR: Please input either 'y' or 'n'. Please try again: ")
        inputLines = input("Are there more lines y/n? ")
    while inputLines[0].lower() == 'y':
        line = input(str("Enter line: "))
        file.write(line + "\n")
        inputLines = input(str("Are there more lines y/n? "))
        count = 0
        # Loop until the user enters a valid input (either 'y' or 'n')
        while not inputLines or inputLines[0].lower() not in ['y', 'n']:
            # Increment the count of invalid inputs
            count += 1
            
            # If there have been two or more invalid inputs, print an error message
            if count >= 2:
                print("ERROR: Please input either 'y' or 'n'. Please try again: ")
                
                # Reset the invalid count to zero
                count = 0
            else:
                # Ask the user for input again, indicating that their previous input was invalid
                inputLines = input("ERROR: Please input either 'y' or 'n'. Please try again: ")

        # If the user input is 'n', exit the loop
        if inputLines[0].lower() == 'n':
            break


#Opens and reads each individual line in the text file
with open("mylife.txt") as file:
    lines = [line.rstrip() for line in file]

#Creates the main program
def mainProgram(lines,texts,title):

    #Sets the title for the screen display
    pygame.display.set_caption(title)

    #Multiplies the color directory and its values in accordance to the number of items in its list
    for i in lines:
        col_dir.append(col_dir[0])
        def_col.append(def_col[0])

    #Initialized values for functions
    minimum = 0
    maximum = 255

    #Draws the text
    def draw_text(text, size, col, x, y):
        font = pygame.font.get_default_font()
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, col)
        text_rect=text_surface.get_rect()
        text_rect.center = (x,y)
        intermediate.blit(text_surface, text_rect)

    #Creates the color change
    def col_change(col,dir):
        for i in range(1):
            col[i] += col_spd * dir[i]
            if col[i] >=maximum or col[i] <=minimum:
                dir[i] *= -1

    #Combines the color change and draw text into one function
    def array_func(col,dir,text,size,x,y):
        for i in range(len(text)):
            draw_text(text[i],size,col[i],x,y + i*20)
            col_change(col[i],dir[i])

    # Initialising pygame
    pygame.init()

    #Creates the properties of the background screen so it can scroll
    intermediate = pygame.surface.Surface((W, 5000))
    i_a = intermediate.get_rect()
    x1 = i_a[0]
    x2 = x1 + i_a[2]
    a, b = (255, 255, 255), (0, 0, 0)
    y1 = i_a[1]
    y2 = y1 + i_a[3]
    h = y2-y1
    rate = (float((b[0]-a[0])/h),
            (float(b[1]-a[1])/h),
            (float(b[2]-a[2])/h)
            )
    for line in range(y1,y2):
        color = (min(max(a[0]+(rate[0]*line),0),255),
                min(max(a[1]+(rate[1]*line),0),255),
                min(max(a[2]+(rate[2]*line),0),255)
                )
        pygame.draw.line(intermediate, color, (x1, line),(x2, line))

    y = 100
    f = pygame.font.SysFont('', 17)
    for i in lines:

        y += 100

    clock = pygame.time.Clock()    
    quit = False

    #Runs the program
    run=True

    scroll_y = 0

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                if event.button == 5: scroll_y = max(scroll_y - 15, -3000)

        screen.blit(intermediate, (0, scroll_y))

        array_func(def_col,col_dir,texts,20, W / 2 , 20)

        clock.tick()

        display.blit(screen,(0,0))
        pygame.display.update()

#Runs the program for the text file
print ("\n Look back at the display screen, scroll if your texts were too long :D")
mainProgram(lines,lines,"My Life Display Screen")