#This script receives a csv report from replicon
import boto3
source_file = open("/Users/ausov/Desktop/report2.csv", "r")
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
    # print array[num]
    num = num + 1


#Create a dictionary with the IDs of the user and add to it a dictionary of the vacation/sick days

people_dic = {}
for i in arrays:
    if i[0].isdigit and not len(i[0]) == 0 and not i[0] == "Employee ID":
        id = (i[0])  #The ID of the person
        people_dic[id] = {
            'vacation' : 0,
            'sick' : 0,
            'miluim' : 0,
        }

    elif i[0].isalpha and not len(i[1]) == 0:
        if i[3] == "Vacation":
            people_dic[id]['vacation']  = people_dic[id]['vacation'] + 1
        elif i[3] == "Sick":
            people_dic[id]['sick'] = people_dic[id]['sick'] + 1
        elif i[3] == "Army reserve":
            people_dic[id]['miluim'] = people_dic[id]['miluim'] + 1

for d in people_dic:
    output_file.write("%s,%s,%s,%s \n" % (d, people_dic[d]['vacation'], people_dic[d]['sick'], people_dic[d]['miluim']))


output_file.close()

