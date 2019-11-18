import csv


#function to change string answer to number, for questions 1-5 and 11-14
def convert(some_string):
    if some_string == "Strongly Disagree":
        return 1
    if some_string == "Somewhat Disagree":
        return 2
    if some_string == "Neither Agree nor Disagree":
        return 3
    if some_string == "Somewhat Agree":
        return 4
    if some_string == "Strongly Agree":
        return 5

#function to change string answer to number, for questions 6-10, 15-20
def convert_reverse(some_string):
    if some_string == "Strongly Disagree":
        return 5
    if some_string == "Somewhat Disagree":
        return 4
    if some_string == "Neither Agree nor Disagree":
        return 3
    if some_string == "Somewhat Agree":
        return 2
    if some_string == "Strongly Agree":
        return 1

#dictionary for name, personality type
name_personality = {}

#reading the rows
with open('Assessment Subset 1 - Form Responses 1.csv') as csv_file:
    csv_file.readline()
    csv_file.readline()
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        #dictionary of personality type + numbers
        personality_measures = {}
        #calculations of the personality types and adding into dictionary
        personality_measures['neuroticism'] = (convert(row[7]) + convert_reverse(row[12]) + convert(row[17])+convert_reverse(row[22]))/4
        personality_measures['extraversion'] = (convert(row[4]) + convert_reverse(row[9]) + convert(row[14]) + convert_reverse(row[19]))/4
        personality_measures['openness'] = (convert(row[8]) + convert_reverse(row[13]) + convert_reverse(row[18]) + convert_reverse(row[23]))/4
        personality_measures['agreeableness'] = (convert(row[5]) + convert_reverse(row[10]) + convert(row[15]) + convert_reverse(row[20]))/4
        personality_measures['conscientiousness'] = (convert(row[6]) + convert_reverse(row[11]) + convert(row[16]) + convert_reverse(row[21]))/4
        #getting the personality type with largest number
        personality = max(personality_measures, key = personality_measures.get)
        #row[2] is where the names are located, adding name and personality type to dictionary
        name_personality[row[2]] = personality
print(name_personality)





    
    
