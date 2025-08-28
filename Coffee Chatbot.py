#Coffee Chatbot
#Create a python chatbot that can help cut the wait time of the normal coffe run by taking customers' order in advance..

#define a function called coffee_bot()
def coffee_bot():
    print('Welcome to the cafe!')
#Call get_size() inside coffee_bot()
    size = get_size()
#Call get_drink_type() inside coffee_bot()
    drink_type = get_drink_type()
    print('Alright, that\'s a {} {}!'.format(size, drink_type))
    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your drink will be ready shortly.'.format(name))

#next, define a function called get_size() that will ask the user for the size for their drink. 
#Use the Input() function to get the user input and store the response in a variable called res:

#Add conditional statement to get_size():    
#If res is equal to 'a', return the string 'small'
#Else if res is equal to 'b', return the string 'medium'
#Else if res is equal to 'c', return the string 'large'
    

#Add an else block to your conditional statements. Inside this block, call the get_size() function and return its returned value.
#This will continue prompting the user for a size selection until the user's response matches one of our expected inputs.
    
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

#define a function call get_drink_type() that will ask the user for their drink order
#use the input() function to get the user input and store the response in a variable called res.
    
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()
    
#call print_message() inside the else block of get_size()
def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

#At the bottom of the script, call your function. Run the script to see the greeting. 
# Call coffee_bot()!
coffee_bot()


