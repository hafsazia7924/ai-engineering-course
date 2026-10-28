import pandas as pd

data = {
    "name": ["  Ali ", "SARA", " usman"],
    "city": ["lahore", "KARACHI ", "Multan"],
}
df = pd.DataFrame(data)

#Remove extra spaces from name column
print(df["name"].str.strip())

#Make the name column in small letters
print(df["name"].str.lower())

#save the clean name column
df["name"]=df["name"].str.strip()
print(df["name"])

#clean the city column
df["city"]=df["city"].str.strip().str.title()  #title makes the 1st letter capital
print(df["city"])

# Add two new columns, one value for each row
df["phone"] = ["0300-1234567", "0312-7654321", "0345-1112223"]
df["email"] = ["ali@gmail.com", "sara@yahoo.com", "usman@gmail.com"]

#Remove dash from phone numbers
df["phone"]=df["phone"].str.replace("-","")
print(df["phone"])

#keep th only place where email contains gmail
print(df["email"].str.contains("gmail"))

# Practical 
import pandas as pd

data = {
    "name": ["  ahmed ", "FATIMA", "bilal  ", " ayesha"],
    "city": ["multan ", "LAHORE", " karachi", "Multan"],
    "phone": ["0300-1111111", "0311-2222222", "0322-3333333", "0333-4444444"],
    "email": [" Ahmed@Gmail.com", "fatima@yahoo.com ", "BILAL@GMAIL.COM", " ayesha@outlook.com"],
}
df = pd.DataFrame(data)

#Task 1
df["name"] = df["name"].str.strip().str.lower()
print(df["name"])
#Task 2
df["city"] = df["city"].str.strip().str.lower()
print(df["city"])
#Task 3
df["phone"] = df["phone"].str.replace("-","")
#Task 4
df["email"] = df["email"].str.strip().str.lower()
print(["email"])
#Task 5
print(df)
#Task 6
print(df[df["email"].str.contains("gmail")])
#Task 7
print(len(df[df["email"].str.contains("gmail")]))
