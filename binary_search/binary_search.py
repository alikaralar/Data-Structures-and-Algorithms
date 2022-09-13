def binary_search(sequence,item):

    begin_index = 0
    end_index = len(sequence) - 1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

message = 'Enter with a space between the numbers: '                    
sequence = map(int,input(message).split())
item = int(input('Enter the item: '))
sequence = list(sequence)
sequence.sort()

if binary_search(sequence,item) == None:
    print('You entered an invalid number!')
else:    
    print('Found in {} steps!'.format(binary_search(sequence,item)))