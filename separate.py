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

    for index, x in enumerate(column2):
        if len(column2[index]) > 1 and len(column1[index]) > 1:  #if all is ok # greather than 1 character
            result_column2.append(column2[index])
            result_column1.append(column1[index])

        elif len(column2[index]) == 0: #if there is no last name
            if len(column1[index]) > 1: # check if there if there is anything in first name

               namesList = split_string(column1[index]) # list of all words in column 1
               lastName = namesList.pop() #get last name
               result_column2.append(lastName) # save last name
               result_column1.append(' '.join(namesList)) #everything else save as first name

            else: #there is nothing in both names
                result_column2.append(column2[index])
                result_column1.append(column1[index])
                print("Both first name and last name are empty for row {}" . format(index+1)) # +1 because first row is column name
        else: #that means column1 is empty
            if len(column2[index]) > 1:
                namesList = split_string(column2[index])  # list of all words
                firstName = namesList.pop(1)
                result_column2.append(firstName)
                result_column1.append(' '.join(namesList))


    return result_column1, result_column2

def split_string(string):
    result = string.split(" ")
    return result



def main():

    #these columns were provided from excel
    column1 = ['first_name','Felix','Luc Picard', '','Seven OF eight','', 'JackSlade']
    column2 = ['last_name','Constansa', '', 'Alan Ford', '', '', '']

    result_column1 = []
    result_column2 = []

    result_column1, result_column2 = separate_names(column1, column2, result_column1, result_column2)

    print(result_column1)
    print(result_column2)

if __name__ == '__main__':
    main()