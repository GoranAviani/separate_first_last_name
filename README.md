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