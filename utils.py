def stringToFile(string, file_path):
    '''Save a string to a file

    Params:
        string (string) - the string to save
        file_path (string) - the path of the file
    '''
    try:
        with open(file_path, "w") as text_file:
            text_file.write(string)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    except: 
        print("Unexpected error:", sys.exc_info()[0])

def dayOfTheWeek(day_number):
    if day_number == 0:
        return "Mon"

    elif day_number == 1:
        return "Tue"

    elif day_number == 2:
        return "Wed"

    elif day_number == 3:
        return "Thu"

    elif day_number == 4:
        return "Fri"

    elif day_number == 5:
        return "Sat"

    elif day_number == 6:
        return "Sun"

    else:
        return ""