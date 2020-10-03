print('welcome to the automatic bubble sorter')

inputted_list = input('please enter a list of numbers seperated by commas: ')

list = inputted_list.split(',')

number_of_items = int(len(list))

sorting_method = input('if you would like your list to be sorted in ascending order, press 1, if you would like it to be sorted in descending order, press 2')

print(list)

if sorting_method == '1':

    position = 0

    Pass = 0

    counter = 1

    while counter == 1:

        number_of_swaps = 1

        counter2 = 0

        permanent_numbers = []

        while number_of_swaps > 0:

            counter2 = counter2 + 1

            number_of_swaps = 0

            while position < number_of_items - 1:

                if int(list[position]) > int(list[position + 1]):

                    number_of_swaps = number_of_swaps + 1

                    item1 = int(list[position])

                    item2 = int(list[position + 1])

                    list[position] = item2

                    list[position + 1] = item1

                position = position + 1

            Pass =  Pass + 1

            print('pass',Pass,':',list)

            position = 0

            if Pass == number_of_items - 1:

                number_of_swaps = 0

            permanent_numbers.append(list[number_of_items - counter2])

        if number_of_swaps == 0:

            counter = 0

    print('total number of passes:', Pass)

    elif sorting_method == '2':

    position = 0

    Pass = 0

    counter = 1

    while counter == 1:

        number_of_swaps = 1

        while number_of_swaps > 0:

            number_of_swaps = 0

            while position < number_of_items - 1:

                if int(list[position]) > int(list[position + 1]):

                    number_of_swaps = number_of_swaps + 1

                    item1 = int(list[position])

                    item2 = int(list[position + 1])

                    list[position] = item2

                    list[position + 1] = item1

                position = position + 1

            Pass =  Pass + 1

            print('pass',Pass,':',list)

            position = 0

            if Pass == number_of_items - 1:

                number_of_swaps = 0

        if number_of_swaps == 0:

            counter = 0

    print('total number of passes:', Pass)  
