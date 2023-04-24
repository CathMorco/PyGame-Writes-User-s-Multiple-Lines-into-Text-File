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

    #Asks the user to enter a line
    
    #Writes the line into the file
    
    #Asks user if there are more lines to be inputted
    
        # Loop until the user enters a valid input (either 'y' or 'n')
        
            # Increment the count of invalid inputs
            
            
            # If there have been two or more invalid inputs, print an error message
            
                
                # Reset the invalid count to zero
                
                # Ask the user for input again, indicating that their previous input was invalid
                

        # If the user input is 'n', exit the loop
        


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
