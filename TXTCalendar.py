import os, time

from CalendarManager import CalendarManager
from utils import stringToFile


def menu(calendar_manager):
    '''TXTCalendar
    Plain Text Calendar Generator
    '''
    while True:
        print('###################')
        print('    TXTCalendar    ')
        print('   A tool by GSLF  ') 
        print('###################')
        print('')
        print('1 --> Generate WEEKLY calendar')	
        print('2 --> Generate MONTLY calendar')
        print('3 --> Generate YEARLY calendar')
        print('q --> Quit Tools')
        print('')
        
        option = input('Select an option: ')

        if option == '1': 
            os.system('clear')
            print('WEEKLY CALENDAR')

            month = input('Month: ')
            year = input('Year: ')
            week = input('Week: ')
            filepath = input('File path (empty for print to console): ')

            # Cast and Check inputs
            try:
                month = int(month)
                year = int(year)
                week = int(week)
            except:
                print('Please use numeric digits for month, year and week.')
                time.sleep(3)
                continue

            calendar = calendar_manager.weekly(month, year, week)

            if filepath == "":
                print('\n')
                print(calendar)
            else:
                stringToFile(calendar, filepath)

        elif option == '2':
            os.system('clear')
            print('MONTLY CALENDAR')

            month = input('Month: ')
            year = input('Year: ')
            style = input('Formatted (y/n): ')
            filepath = input('File path (empty for print to console): ')

            # Cast and Check inputs
            try:
                month = int(month)
                year = int(year)
            except:
                print('Please use numeric digits for month and year.')
                time.sleep(3)
                continue

            if style == 'y' or style == 'Y':
                style = True
            elif style == 'n' or style == 'N':
                style = False
            else:
                print('Please use y or n in the formatted option.')
                time.sleep(3)
                continue

            calendar = calendar_manager.montly(month, year, style)

            if filepath == "":
                print('\n')
                print(calendar)
            else:
                stringToFile(calendar, filepath)

        elif option == '3':
            os.system('clear')
            print('YEARLY CALENDAR')

            year = input('Year: ')
            style = input('Formatted (y/n): ')
            filepath = input('File path (empty for print to console): ')

            # Cast and Check inputs
            try:
                year = int(year)
            except:
                print('Please use numeric digits for the year.')
                time.sleep(3)
                continue

            if style == 'y' or style == 'Y':
                style = True
            elif style == 'n' or style == 'N':
                style = False
            else:
                print('Please use y or n in the formatted option.')
                time.sleep(3)
                continue

            calendar = calendar_manager.yearly(year, style)

            if filepath == "":
                print('\n')
                print(calendar)
            else:
                stringToFile(calendar, filepath)
        
        elif option == 'q':
            break

        else:
            os.system('clear')
            print('WARNING: WRONG OPTION \n\n')
            
if __name__ == '__main__':
    menu(CalendarManager())