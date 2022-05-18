from re import A

#create a blank dictionary for user bio data
bio_data = {"Name": "",
            "Age": "",
            "Gender": "",
            "Occupation": ""}

#get inputs from the user
bio_data["Name"] = input("Enter your name: ")
#bio_data["Name"] = Name
Age = input("Enter your age: ")
bio_data["Age"] = Age
#set the gender and update the dictionary and the output phrase
Gender = input("What is your gender: ")
bio_data["Gender"] = Gender
gender_word = ""
if Gender == "Male":
    gender_word = "he"
else:
    gender_word = "her"
Occupation = input("Enter your occupation: ")
bio_data["Occupation"] = Occupation
#double check the dictionary
print(bio_data)
#print the user bio data phrase using f-string
print(f"The user's name is {bio_data['Name']}, and {gender_word} age is {bio_data['Age']} years old, and is a {bio_data['Occupation']}")