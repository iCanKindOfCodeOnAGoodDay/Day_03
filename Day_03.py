"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 3
    April 23 2024

    ------
    Description:    Treasure Island - Choices & Story line
    ------
    
    ------
    Inputs:         User Choices
    ------
    
    ------
    Outputs:        Next Question, Game Over, or Game Win after each response
    ------
    
    ------
    Dependencies:   None.
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""
def main():
        
    """
    
    Description -   Runs the game
    ----------  
    Input -         Console questions
    ----------                    
    Outputs -       Game over, or next question, or invalid input
    -------
        
    """
    
    print('Welcome to tresure island')
    game_over = False
    
    choice_1 = acceptable_input('You arrive at the island in a row boat. Did you bring sunscreen? (yes/no)', ['yes', 'no'])
    if choice_1 == 'yes':
        print('Darn. It leaked and you slip. And then YOU DIE! Game Over!')
        game_over = True
        restart_prompt()
        
    if not game_over:
        choice_2 = acceptable_input('A tidal wave is several hundrend meters away. Do you scream? (yes/no)', ['yes', 'no'])
        if choice_2 == 'yes':
            print('You\'re a whimp. Game over! You die!')   
            game_over = True
            restart_prompt()
    
    if game_over == False:
        choice_3 = acceptable_input('You have about 10 meters to dry land. What do you do? (swim/paddle)', ['swim', 'paddle'])        
        if choice_3 == 'swim':
            print('You get eaten by sharks. Game over!')  
            game_over = True
            restart_prompt()
   
    if game_over == False:
        choice_4 = acceptable_input('Oh no. Land Crabs! Do you kick them? (kick/dodge)', ['kick', 'dodge'])    
        if choice_4 == 'dodge':
            print('Oh no, they are chasing you! You cannot escape the crabs! Game Over.')   
            game_over = True
            restart_prompt()
        else:
            print('Congrats! You win!?')
            restart_prompt()
    
# main
            
    
def restart_prompt():
        
    """
    
    Description -   Play Again
    ----------
    Parameters -    type 'yes' to play again
    ----------
    Output -        Runs main 
    -------

    """
    acceptable_input('Play Again? (yes)', ['yes'])
    main()
    
# restart_prompt


def acceptable_input( prompt, choices ):
    
    """
    
    Description -   Input func modified to only accept certain values
    ----------
    Parameters -    Pass in the acceptable choices as list, and prompt
    ----------
    Output -        User's input
    -------

    """
    
    while True:
        
            
        # make sure that the result of the input is one of the acceptable choices
        
        user_input = input( prompt  ).lower() # parse string into int
        
        if user_input in choices:
            return user_input
        
        else: 
            print('Invalid input')
    
# acceptable_input


# run code
if __name__ == '__main__':
    main()

