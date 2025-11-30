rules=[
    {"if":{"fever","cough","fatigue"},"then":"Flu"},
    {"if":{"fever","cough","shortness of breathe"},"then":"COVID"},
    {"if":{"headache","nausea","sensitivity to light"},"then":"Migraine"},
    {"if":{"sore throat","running nose","sneezing"},"then":"Common Cold"}
]


def diagnose(symptoms):
    matched_diseases=[]
    symptoms_set=set(symptoms)
    for rule in rules:
        if rule["if"].issubset(symptoms_set):
            matched_diseases.append(rule["then"])
    return matched_diseases


print("Enter Your Symptoms: ")
user_input=input().lower()

symptoms=[s.strip() for s in user_input.split(",")]

diagnoses=diagnose(symptoms)

if diagnoses:
    print("Possible Diagnoses: ")
    for disease in diagnoses:
        print(f"{disease} -")
else:
    print("No matching diseases")