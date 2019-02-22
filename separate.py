#We can receive firstnames and lastnames in two columns from Excel.
#There are several variants we can expect when receiving such files.
# column1                       column2
# Felix                          Constansa
# Luc Picard
#                                Alan Ford
# Seven of Eight
#  (blank)                      (blank)



#Solution should be like this:
# column1                       column2
# Felix                          Constansa
# Luc                            Picard
# Alan                           Ford
# Seven of                      Eight
#  (blank)                      (blank) ############## This situaction should display a message with line number where.



# Ideal scenarion would be to read the Excel columns and get every column in it own list.
# This code continues from that point.

def separate_names(column1, column2, result_column1, result_column2):

    for index, x in enumerate(column1):
       if len(x) > 1: ## fist and last name are in column2  # greather than 1 character
           result_column1.append(x)
       else: #if there is no first name
           if len(column2[index]) > 1:
               namesList = split_string(column2[index]) # list of all words in column 2
            # TODO finish

def split_string(string):
    result = string.split(" ")
    return result



def main():

    column1 = ['Felix','Luc Picard', '','Seven OF eight','']
    column2 = ['Constansa', '', 'Alan Ford', '', '']

    result_column1 = []
    result_column2 = []

    separate_names(column1, column2, result_column1, result_column2)


if __name__ == '__main__':
    main()