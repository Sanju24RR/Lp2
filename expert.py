class ExpertSystem:
    def __init__(self):
        # Define rules for diagnosis
        self.rules = {
            "rule1": {"symptoms": ["fever", "cough"], "condition": "flu"},
            "rule2": {"symptoms": ["fever", "rash"], "condition": "measles"},
            "rule3": {"symptoms": ["headache", "stiff neck"], "condition": "meningitis"},
            # Add more rules as needed
        }

    def diagnose(self, symptoms):
        # Check each rule to find a match
        for rule, data in self.rules.items():
            if all(symptom in symptoms for symptom in data["symptoms"]):
                return data["condition"]
        return "Unknown condition"

# Example usage
expert_system = ExpertSystem()
patient_symptoms = []
symptoms1 = input("Symptoms1 : " )
symptoms2 = input("Symptoms2 : " )
patient_symptoms.append(symptoms1)
patient_symptoms.append(symptoms2)

diagnosis = expert_system.diagnose(patient_symptoms)
print("Diagnosis:", diagnosis)
