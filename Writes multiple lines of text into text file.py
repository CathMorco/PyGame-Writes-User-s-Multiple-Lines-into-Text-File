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
    moreLines = input(str("Are there more lines y/n? "))
    invalid_count = 0
    while not moreLines or moreLines[0].lower() not in ['y', 'n']:
        moreLines=input(str("Invalid input, please only enter 'y', or 'n'"))
    while moreLines[0].lower() == 'y':
        line = input(str("Enter line: "))
        file.write(line + "\n")
        moreLines = input(str("Are there more lines y/n? "))
        invalid_count = 0
        # Loop until the user enters a valid input (either 'y' or 'n')
        while not moreLines or moreLines[0].lower() not in ['y', 'n']:
            # Increment the count of invalid inputs
            invalid_count += 1
            
            # If there have been two or more invalid inputs, print an error message
            if invalid_count >= 2:
                print("Invalid input, please only enter 'y', or 'n'")
                
                # Reset the invalid count to zero
                invalid_count = 0
            else:
                # Ask the user for input again, indicating that their previous input was invalid
                moreLines = input("Invalid input, please only enter 'y', or 'n'")

        # If the user input is 'n', exit the loop
        if moreLines[0].lower() == 'n':
            break


#Opens and reads each individual line in the text file


#Creates the main program


    #Sets the title for the screen display
    

    #Multiplies the color directory and its values in accordance to the number of items in its list
    

    #Initialized values for functions
    

    #Draws the text
    

    #Creates the color change
    

    #Combines the color change and draw text into one function
    

    # Initialising pygame
    

    #Creates the properties of the background screen so it can scroll
    

    #Runs the program
   

#Runs the program for the text file
