# Name: Mitch Cuvar
# Program Description:
# This program manages cybersecurity tools and their primary functions.
# It allows the user to display, add, merge, sort, search, change,
# remove, and analyze cybersecurity tool / function pairs.

'''
This program uses three collections:
Tools_1 is preloaded with cybersecurity tool and function pairs.
Tools_2 is created by the user.
Tools_3 is created by merging Tools_1 and Tools_2.

The program uses functions, loops, if/elif/else statements,
strings, and built-in collection methods.
'''

# ------------------------------------------------------------
# Startup Banner Function
# ------------------------------------------------------------

def startup_banner():
    print()
    print('                =======================================')
    print('                =======================================')
    print('                ==            Welcome to             ==')
    print('                ==  Cybersecurity Tool Organizer     ==')
    print('                ==     Tools and Main Functions      ==')
    print('                =======================================')
    print('                =======================================')
    print()


# ------------------------------------------------------------
# Menu Function
# ------------------------------------------------------------

def choices_menu():
    print()
    print('                 *************************************')
    print('                 * Cybersecurity Tools and Functions *')
    print('                 *************************************')
    print('Menu Choices:')
    print(' 1. Display all the Cybersecurity Tool and Function pairs stored in Tools_1')
    print(' 2. Create and/or Add Cybersecurity Tool and Function pairs to Tools_2')
    print(' 3. Display all the Cybersecurity Tool and Function pairs stored in Tools_2')
    print(' 4. Merge Tools_1 and Tools_2 into a created Tools_3')
    print('==============================================================================')
    print('  All the remaining selections pertain to the merged collection Tools_3')
    print('==============================================================================')
    print(' 5. Display all the Cybersecurity Tool and Function pairs stored in Tools_3')
    print(' 6. Display how many Cybersecurity Tool and Function pairs exist in Tools_3')
    print(' 7. Display only all the Cybersecurity Tools in Tools_3')
    print(' 8. Display only all the Cybersecurity Functions in Tools_3')
    print(' 9. Display all Cybersecurity Functions and Tools sorted by Function')
    print('10. Add a Cybersecurity Tool and Function to Tools_3')
    print('11. Change a Cybersecurity Tool function')
    print('12. Remove a Cybersecurity Tool and Function from Tools_3')
    print('13. Look up a Cybersecurity Tool in Tools_3')
    print('14. Look up a Cybersecurity Function in Tools_3')
    print('15. Display Cybersecurity Tools starting with a chosen letter')
    print('16. Display Cybersecurity Functions starting with a chosen letter')
    print('17. Display the Cybersecurity Tool with the longest name')
    print('18. Display the Cybersecurity Function with the longest name')
    print('19. Clear all pairs from Tools_3')
    print('20. Exit the program')
    print()

    choice = int(input('Please enter your choice: '))

    while choice < 1 or choice > 20:
        choice = int(input('Enter a valid choice. Select a choice between 1-20: '))

    return choice


# ------------------------------------------------------------
# 1 - Display Tools_1
# ------------------------------------------------------------

def display_tools_one(Tools_1):
    print()
    print('========================================================')
    print('        Cybersecurity Tools and Main Functions          ')
    print('========================================================')
    print(f'{"Cybersecurity Tool":<30}{"Main Function":<30}')
    print('--------------------------------------------------------')

    if len(Tools_1) == 0:
        print('No cybersecurity tool and function pairs are currently stored.')
    else:
        for tool, function in sorted(Tools_1.items()):
            print(f'{tool:<30}{function:<30}')

    print('========================================================')
    print()


# ------------------------------------------------------------
# 2 - Create and Add to Tools_2
# ------------------------------------------------------------

def create_tools_two(Tools_2):
    print()
    amount = int(input('How many Cybersecurity Tool and Function pairs would you like to add? '))

    while amount < 1:
        amount = int(input('Please enter a number of 1 or higher: '))

    for number in range(amount):
        print()
        print(f'Cybersecurity Pair #{number + 1}')
        print('------------------------------')

        tool = input('Enter the Cybersecurity Tool name: ')
        tool = tool.title()

        function = input('Enter the Main Function: ')
        function = function.title()

        Tools_2[tool] = function

        print()
        print(f'{tool} and {function} were added to Tools_2.')

    display_tools_two(Tools_2)


# ------------------------------------------------------------
# 3 - Display Tools_2
# ------------------------------------------------------------

def display_tools_two(Tools_2):
    print()
    print('========================================================')
    print('        User Created Cybersecurity Tool List            ')
    print('========================================================')
    print(f'{"Cybersecurity Tool":<30}{"Main Function":<30}')
    print('--------------------------------------------------------')

    if len(Tools_2) == 0:
        print('No cybersecurity tool and function pairs are currently stored.')
    else:
        for tool, function in sorted(Tools_2.items()):
            print(f'{tool:<30}{function:<30}')

    print('========================================================')
    print()


# ------------------------------------------------------------
# 4 - Merge Tools_1 and Tools_2
# ------------------------------------------------------------

def merge_tools(Tools_1, Tools_2):
    Tools_3 = Tools_1.copy()
    Tools_3.update(Tools_2)

    print()
    print('Tools_1 and Tools_2 were merged into Tools_3.')

    display_tools_three(Tools_3)

    return Tools_3


# ------------------------------------------------------------
# 5 - Display Tools_3
# ------------------------------------------------------------

def display_tools_three(Tools_3):
    print()
    print('========================================================')
    print('          Merged Cybersecurity Tool List                ')
    print('========================================================')
    print(f'{"Cybersecurity Tool":<30}{"Main Function":<30}')
    print('--------------------------------------------------------')

    if len(Tools_3) == 0:
        print('No cybersecurity tool and function pairs are currently stored.')
    else:
        for tool, function in sorted(Tools_3.items()):
            print(f'{tool:<30}{function:<30}')

    print('========================================================')
    print()


# ------------------------------------------------------------
# 6 - Count Pairs in Tools_3
# ------------------------------------------------------------

def count_tools(Tools_3):
    print()
    print('-------------------------------------------------------------------')
    print(f'There are {len(Tools_3)} cybersecurity tool and function pairs in Tools_3.')
    print('-------------------------------------------------------------------')
    print()


# ------------------------------------------------------------
# 7 - Display Only Cybersecurity Tools
# ------------------------------------------------------------

def display_tool_names(Tools_3):
    print()
    print('================================')
    print('     Cybersecurity Tools        ')
    print('================================')

    names = sorted(Tools_3.keys())

    if len(names) == 0:
        print('No cybersecurity tools are currently stored.')
    else:
        for tool in names:
            print(tool)

    print('================================')
    print()


# ------------------------------------------------------------
# 8 - Display Only Cybersecurity Functions
# ------------------------------------------------------------

def display_function_names(Tools_3):
    print()
    print('================================')
    print('   Cybersecurity Functions      ')
    print('================================')

    functions = sorted(Tools_3.values())

    if len(functions) == 0:
        print('No cybersecurity functions are currently stored.')
    else:
        for function in functions:
            print(function)

    print('================================')
    print()


# ------------------------------------------------------------
# 9 - Display Functions and Tools Sorted by Function
# ------------------------------------------------------------

def display_function_tool_pairs(Tools_3):
    print()
    print('========================================================')
    print('        Cybersecurity Functions and Tools               ')
    print('========================================================')
    print(f'{"Main Function":<30}{"Cybersecurity Tool":<30}')
    print('--------------------------------------------------------')

    if len(Tools_3) == 0:
        print('No cybersecurity tool and function pairs are currently stored.')
    else:
        functions = sorted(Tools_3.values())

        for function in functions:
            for tool in sorted(Tools_3.keys()):
                if Tools_3[tool] == function:
                    print(f'{function:<30}{tool:<30}')

    print('========================================================')
    print()


# ------------------------------------------------------------
# 10 - Add Cybersecurity Tool and Function
# ------------------------------------------------------------

def add_tool_function(Tools_3):
    print()
    tool = input('Enter the new Cybersecurity Tool name: ')
    tool = tool.title()
    print()

    function = input('Enter the Main Function: ')
    function = function.title()
    print()

    decide = input(f'Are you sure you want to add {tool} and {function}? Enter Y to continue: ')
    decide = decide.title()

    if decide == 'Y':
        if tool not in Tools_3:
            Tools_3[tool] = function
            print()
            print(f'{tool} and {function} were added to Tools_3.')
            display_tools_three(Tools_3)
        else:
            print()
            print(f'{tool} already exists in Tools_3.')
            print()
    else:
        print()
        print('Addition cancelled.')
        print()


# ------------------------------------------------------------
# 11 - Change Cybersecurity Tool Function
# ------------------------------------------------------------

def change_tool_function(Tools_3):
    print()
    tool = input('Enter the Cybersecurity Tool that has a new function: ')
    tool = tool.title()
    print()

    if tool in Tools_3:
        original_function = Tools_3[tool]

        function = input('Enter the new Main Function: ')
        function = function.title()
        print()

        decide = input(f'Are you sure you want to change {tool} from {original_function} to {function}? Enter Y to continue: ')
        decide = decide.title()

        if decide == 'Y':
            Tools_3[tool] = function
            print()
            print(f'{tool} and {original_function} were changed to {tool} and {function}.')
            display_tools_three(Tools_3)
        else:
            print()
            print('Change cancelled.')
            print()
    else:
        print(f'{tool} was not found in Tools_3.')
        print()


# ------------------------------------------------------------
# 12 - Remove Cybersecurity Tool and Function
# ------------------------------------------------------------

def remove_tool_function(Tools_3):
    print()
    tool = input('Enter a Cybersecurity Tool that you would like to remove: ')
    tool = tool.title()
    print()

    decide = input(f'Are you sure you want to delete {tool}? Enter Y to continue: ')
    decide = decide.title()

    if decide == 'Y':
        if tool in Tools_3:
            function = Tools_3[tool]
            Tools_3.pop(tool)

            print()
            print(f'{tool} and {function} were removed from Tools_3.')
            display_tools_three(Tools_3)
        else:
            print()
            print(f'{tool} was not found in Tools_3.')
            print()
    else:
        print()
        print('Removal cancelled.')
        print()


# ------------------------------------------------------------
# 13 - Look Up Cybersecurity Tool
# ------------------------------------------------------------

def lookup_tool(Tools_3):
    print()
    tool = input('Enter the Cybersecurity Tool name to search for: ')
    tool = tool.title()
    print()

    if tool in Tools_3:
        print(f'The Cybersecurity Tool {tool} is in Tools_3 with the Main Function {Tools_3[tool]}.')
        print()
    else:
        print(f'{tool} not found.')
        print()


# ------------------------------------------------------------
# 14 - Look Up Cybersecurity Function
# ------------------------------------------------------------

def lookup_function(Tools_3):
    print()
    function = input('Enter the Main Function to search for: ')
    function = function.title()
    print()

    if function in Tools_3.values():
        print(f'The Main Function {function} is in Tools_3.')
        print()

        for tool, stored_function in Tools_3.items():
            if stored_function == function:
                print(f'{function} is the Main Function for {tool}.')
        print()
    else:
        print(f'{function} not found.')
        print()


# ------------------------------------------------------------
# 15 - Your Choice: Tools Starting With Chosen Letter (my own)
# ------------------------------------------------------------

def tools_starting_letter(Tools_3):
    print()
    letter = input('Enter the starting letter for Cybersecurity Tools: ')
    letter = letter.title()
    print()

    print(f'Cybersecurity Tools starting with {letter}:')
    print('------------------------------------------')

    found = False

    for tool in sorted(Tools_3.keys()):
        if tool.startswith(letter):
            print(tool)
            found = True

    if found == False:
        print(f'No Cybersecurity Tools start with {letter}.')

    print()


# ------------------------------------------------------------
# 16 - Your Choice: Functions Starting With Chosen Letter (my own)
# ------------------------------------------------------------

def functions_starting_letter(Tools_3):
    print()
    letter = input('Enter the starting letter for Cybersecurity Functions: ')
    letter = letter.title()
    print()

    print(f'Cybersecurity Functions starting with {letter}:')
    print('-----------------------------------------------')

    found = False

    for function in sorted(Tools_3.values()):
        if function.startswith(letter):
            print(function)
            found = True

    if found == False:
        print(f'No Cybersecurity Functions start with {letter}.')

    print()


# ------------------------------------------------------------
# 17 - Your Choice: Longest Cybersecurity Tool Name (my own)
# ------------------------------------------------------------

def longest_tool_name(Tools_3):
    print()

    if len(Tools_3) == 0:
        print('No Cybersecurity Tools are currently stored.')
    else:
        longest = ''

        for tool in Tools_3.keys():
            if len(tool) > len(longest):
                longest = tool

        print(f'The Cybersecurity Tool with the longest name is {longest}.')

    print()


# ------------------------------------------------------------
# 18 - Your Choice: Longest Cybersecurity Function Name (my own)
# ------------------------------------------------------------

def longest_function_name(Tools_3):
    print()

    if len(Tools_3) == 0:
        print('No Cybersecurity Functions are currently stored.')
    else:
        longest = ''

        for function in Tools_3.values():
            if len(function) > len(longest):
                longest = function

        print(f'The Cybersecurity Function with the longest name is {longest}.')

    print()


# ------------------------------------------------------------
# 19 - Your Choice: Clear Tools_3 (my own)
# ------------------------------------------------------------

def clear_tools_three(Tools_3):
    print()
    decide = input('Are you sure you want to clear all pairs from Tools_3? Enter Y to continue: ')
    decide = decide.title()

    if decide == 'Y':
        Tools_3.clear()
        print()
        print('All Cybersecurity Tool and Function pairs were removed from Tools_3.')
        display_tools_three(Tools_3)
    else:
        print()
        print('Clear Tools_3 task cancelled.')
        print()


# ------------------------------------------------------------
# 20 - Exit Program
# ------------------------------------------------------------

def exit_program():
    print()
    decide = input('Are you sure you would like to quit the program?\nEnter Y to quit, or any other key to continue: ')
    decide = decide.title()

    if decide == 'Y':
        print()
        print('Exiting...')
        print('Thank you for using the Cybersecurity Tool Organizer!')
        print('Stay secure and do not click sketchy links. Seriously.')
        return 20
    else:
        print()
        print('Continuing Program')
        return 0


# ------------------------------------------------------------
# Main Code
# ------------------------------------------------------------

def main():
    startup_banner()

    Tools_1 = {
        'Wireshark': 'Packet Analysis',
        'Nmap': 'Network Scanning',
        'Metasploit': 'Exploit Testing',
        'Burp Suite': 'Web Testing',
        'Splunk': 'Log Analysis',
        'Snort': 'Intrusion Detection'
    }

    Tools_2 = {}

    Tools_3 = {}

    choice = 0

    while choice != 20:

        choice = choices_menu()

        if choice == 1:
            display_tools_one(Tools_1)

        elif choice == 2:
            create_tools_two(Tools_2)

        elif choice == 3:
            display_tools_two(Tools_2)

        elif choice == 4:
            Tools_3 = merge_tools(Tools_1, Tools_2)

        elif choice == 5:
            display_tools_three(Tools_3)

        elif choice == 6:
            count_tools(Tools_3)

        elif choice == 7:
            display_tool_names(Tools_3)

        elif choice == 8:
            display_function_names(Tools_3)

        elif choice == 9:
            display_function_tool_pairs(Tools_3)

        elif choice == 10:
            add_tool_function(Tools_3)

        elif choice == 11:
            change_tool_function(Tools_3)

        elif choice == 12:
            remove_tool_function(Tools_3)

        elif choice == 13:
            lookup_tool(Tools_3)

        elif choice == 14:
            lookup_function(Tools_3)

        elif choice == 15:
            tools_starting_letter(Tools_3)

        elif choice == 16:
            functions_starting_letter(Tools_3)

        elif choice == 17:
            longest_tool_name(Tools_3)

        elif choice == 18:
            longest_function_name(Tools_3)

        elif choice == 19:
            clear_tools_three(Tools_3)

        elif choice == 20:
            choice = exit_program()

        else:
            print('Invalid selection.')


# ------------------------------------------------------------
# Program Start
# ------------------------------------------------------------

if __name__ == "__main__":
    main()