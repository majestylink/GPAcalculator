import time

average = []


def collect():
    num_of_courses = int(input('How many courses are you offering? '))
    while num_of_courses >= 1:
        for numbers in range(1, num_of_courses + 1):
            course = (input('{}). Enter course title: '.format(numbers)))
            a = average.append(course)
            num_of_courses -= 1
    calculate()


def calculate():
    grades = []
    units = []
    for course in average:
        grade = input('Enter grade for {}: '.format(course))
        unit = int(input('Enter unit for {}: '.format(course)))
        p = units.append(unit)
        grade = grade.upper()
        if grade == 'A':
            calculated = unit * 5
            b = grades.append(calculated)
        elif grade == 'B':
            calculated = unit * 4
            b = grades.append(calculated)
        elif grade == 'C':
            calculated = unit * 3
            b = grades.append(calculated)
        elif grade == 'D':
            calculated = unit * 2
            b = grades.append(calculated)
        elif grade == 'F':
            calculated = unit * 0
            b = grades.append(calculated)
        else:
            print('invalid grade format')
    grades = tuple(grades)
    units = tuple(units)
    units = sum(units)
    grades = sum(grades)
    total = grades / units
    print('')
    print('calculating, please wait...')
    print('')
    time.sleep(2)
    print('YOUR TOTOAL GPA FOR THE SEMESTER IS:', total)
    average.clear()

    exit()


def exit():
    print('')
    print('')
    exit_input = input('Type (EXIT) to quit or (CONTINUE) to continue the program: ')
    print('')
    exit_input = exit_input.upper()
    if exit_input == 'EXIT':
        quit()
    else:
        still_cal = input('Are you still calculating? (YES to continue): ')
        print('')
        still_cal = still_cal.upper()
        if still_cal == 'YES':
            print('Restarting the program')
            print('')
            time.sleep(2)
        elif still_cal == 'NO':
            quit()
        else:
            print('')
            print('Invalid command')
            print('')
            print('Closing the program...')
            time.sleep(2)
            quit()
        collect()
