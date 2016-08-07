# This script receives 2 csv report from replicon
# The ID of the user must be the first row in each row - checks if 0 is missing in the ID and adds it
from os import path
import calendar


##################Globlas#########################

VACATION = "Vacation"
SICK = "Sick"
MILUIM = "Army reserve"
BASE_PATH = "/Users/ausov/Desktop"
SOURCE_FILE_DAYSOFF = "daysoff.csv"
SOURCE_FILE_TOTALS = "total.csv"
OUTPUT_FILE = "Fundbox_Time_Summery.csv"

##################################################

source_file_daysoff = open(path.join(BASE_PATH, SOURCE_FILE_DAYSOFF), "r")
source_file_total_days = open(path.join(BASE_PATH, SOURCE_FILE_TOTALS), "r")
output_file = open(path.join(BASE_PATH,OUTPUT_FILE), "w")


###################Functions##############################

def seperate_csv_to_lines(csv_file):
    seperated_list_of_lists = []
    for csv_line in csv_file.readlines():
        split_line = csv_line.split(",")
        if len(split_line[0]) < 9 and len(split_line[0]) > 3: # If the ID is 8 digit and the "0" was removed for some reason, add it back
            split_line[0] = "0" + split_line[0]
        seperated_list_of_lists.append(split_line)
    return seperated_list_of_lists


def count_days(list_of_ids_and_daysoff, list_of_ids_and_total):
    dict_daysoff = {}
    for line in list_of_ids_and_total:
        if line[0].isdigit and len(line[0]) > 3 and not line[0] == "Employee ID": # Add the total days and hours for every ID
            dict_daysoff[line[0]] = {
                'vacation': 0,
                'sick': 0,
                'miluim': 0,
                'total_days': line[2].rstrip(),
                'total_hours': line[1],
             }

    for line in list_of_ids_and_daysoff:
        if line[0].isdigit and len(line[0]) > 3 and not line[0] == "User First Name" and not line[0] == "\r\n": # Add the off days for every ID
            if line[3] == VACATION:
                dict_daysoff[line[0]]['vacation'] += 1
            elif line[3] == SICK:
                dict_daysoff[line[0]]['sick'] += 1
            elif line[3] == MILUIM:
                dict_daysoff[line[0]]['miluim'] += 1
    return dict_daysoff



days_off_list = seperate_csv_to_lines(source_file_daysoff)
total_day_list = seperate_csv_to_lines(source_file_total_days)
dict_of_days_off_and_total = count_days(days_off_list,total_day_list)


############################  Create the new CSV file #######################

month_dict = {v: k for k,v in enumerate(calendar.month_name)}
output_file.write("004, %s, %s \n" % (total_day_list[1][4].rstrip(),month_dict[total_day_list[1][3]]))

for d in dict_of_days_off_and_total:
    #print ("%s,%s,%s,%s,%s,%s\n" % (d, dict_of_days_off_and_total[d]['total_days'],dict_of_days_off_and_total[d]['total_hours'], dict_of_days_off_and_total[d]['vacation'], dict_of_days_off_and_total[d]['sick'],dict_of_days_off_and_total[d]['miluim']))
    output_file.write("%s,%s,%s,%s,%s,%s\n" % (d, dict_of_days_off_and_total[d]['total_days'],dict_of_days_off_and_total[d]['total_hours'], dict_of_days_off_and_total[d]['vacation'], dict_of_days_off_and_total[d]['sick'],dict_of_days_off_and_total[d]['miluim']))



output_file.close()



