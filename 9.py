rules = [

    {"if" : {"fever", 'flu', 'cough'}, "then" : "flu"},
    {"if" : {'fever', 'flu', 'breathing_problem'}, "then" : "asthma"}
]


user_input = input("enter your symptoms: \n")

user_inputs = [s.strip() for s in user_input.split(',')]

symptoms = set(user_inputs)

diagnosis = []

for i in rules:
    if i["if"].issubset(symptoms):
        diagnosis.append(i["then"])
        
print(f"Diagnosis : {diagnosis}")
