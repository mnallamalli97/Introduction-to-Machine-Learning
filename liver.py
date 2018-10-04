import pandas as pd

#store the csv into a panda data frame
try:
    df_indian_liver_patients = pd.read_csv("indian_liver_patient.csv")
except IOError:
    print("could not find the file")
finally:
    print("try-except executed")


#print the age of the patients who have liver disease
for i in range(len(df_indian_liver_patients)):
    if df_indian_liver_patients.at[i,"Dataset"] == 1:
        print("Age:", df_indian_liver_patients.at[i, "Age"])


#print number of males and females with disease
maleCount = 0
femaleCount = 0

for i in range(len(df_indian_liver_patients)):
    if df_indian_liver_patients.at[i,"Gender"] == "Male":
        maleCount+=1
    else:
        femaleCount +=1

print("male patients w/ disease:", maleCount)
print("female patients w/ disease:", femaleCount)


#minimum age of patients
print("min age:", min(df_indian_liver_patients["Age"]))


#minimum age of patients with disease
validMinAgeWithDiseaseIndex = df_indian_liver_patients["Age"] ==1
currMin = 100000

for i in range(len(validMinAgeWithDiseaseIndex)):
    if df_indian_liver_patients.at[i,"Age"] < currMin:
        currMin = df_indian_liver_patients.at[i,"Age"]

print("min age with disease:", currMin)

#why wont this work?
# print("min age with disease:", min(df_indian_liver_patients["Age"] and (df_indian_liver_patients["Dataset"]==1)))