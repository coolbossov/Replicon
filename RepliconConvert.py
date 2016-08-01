



source_file = open("/Users/ausov/Desktop/report.csv", "r")
output_file = open("/Users/ausov/Desktop/daysoff.csv", "w")

# Separate the csv file, every line to an list
array = []
for line in source_file.readlines():
    array.append(line)

# Separate every line words into an list, put in a list arrays
num = 0
arrays = []
for i in array:
    arrays.append(array[num].split(",")) #create an array of arrays  - all parameters"
    print array[num]
    num = num + 1


#print the user ID and the amount of his vacation / sick / miluim  days into a csv file

num = 0
vacation = 0
miluim = 0
sick = 0

for i in arrays:
    if i[0].isdigit and not len(i[0]) == 0 and not i[0] == "Employee ID":
        output_file.write("%s , %s , %s , %s \n" % (id, vacation, sick, miluim))
        id =  (i[0])
        print ("%s , %s , %s , %s \n" % (id, vacation, sick, miluim))
        vacation = 0
        miluim = 0
        sick = 0
    elif i[0].isalpha and not len(i[1]) == 0:
        if i[3] == "Vacation":
            vacation = vacation + 1
            print ("%s , %s ") % (id, vacation)
        elif i[3] == "Sick":
            sick = sick + 1
            print ("%s , %s ") % (id, sick)
        elif i[3] == "Army reserve":
            miluim = miluim + 1
            print ("%s , %s ") % (id, miluim)


output_file.close()

    # "arrays[num][0] = arrays[num][0].replace(",,,,,,", "")
# todo add 0 in from of the ID