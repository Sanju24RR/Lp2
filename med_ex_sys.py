class ExpertSystem:
    def __init__(self):
        self.rules = {
            'sneezing': ['common cold', 'allergy'],
            'runny_nose': ['common cold', 'allergy'],
            'coughing': ['common cold', 'flu'],
            'fever': ['flu']
        }

    def infer(self, symptoms):
        possible_conditions = set()
        for symptom, conditions in self.rules.items():
            if symptom in symptoms:
                possible_conditions.update(conditions)
        return possible_conditions

def main():
    expert_system = ExpertSystem()

    print("Welcome to the Medical Expert System")
    print("Please enter your symptoms (separated by commas):")
    user_input = input().strip().lower()

    symptoms = [symptom.strip() for symptom in user_input.split(',')]
    
    if not symptoms:
        print("No symptoms provided. Exiting...")
        return

    possible_conditions = expert_system.infer(symptoms)

    if possible_conditions:
        print("Possible conditions based on provided symptoms:")
        for condition in possible_conditions:
            print("-", condition)
    else:
        print("No conditions matched the provided symptoms.")

if __name__ == "__main__":
    main()
