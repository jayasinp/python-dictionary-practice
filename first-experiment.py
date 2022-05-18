from re import A
#create a blank dictionary for user bio data
bio_data = {"Name": "",
            "Age": "",
            "Gender": "",
            "Occupation": ""}
#get inputs from the user 
#add info to the dictionary directly instead of creating variables
bio_data["Name"] = input("Enter your name: ")
bio_data["Age"] = input("Enter your age: ")
#set the gender and update the dictionary and the output phrase
#without variables to look up, use the dictionary instead
bio_data["Gender"] = input("What is your gender: ")
gender_word = ""
if bio_data["Gender"] == "Male":
    gender_word = "he"
else:
    gender_word = "her"
bio_data["Occupation"] = input("What is your occupation: ")
#double check the dictionary
print(bio_data)
#print the user bio data phrase using f-string
print(f"The user's name is {bio_data['Name']}, and {gender_word} age is {bio_data['Age']} years old, and is a {bio_data['Occupation']}")