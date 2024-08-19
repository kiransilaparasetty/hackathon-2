import random

states_capitals_india = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def conduct_quiz():
    states = list(states_capitals_india.keys())
    random.shuffle(states) 

    score = 0
    total_questions = len(states)
    
    print("Welcome to the Indian State and Capital Quiz Competition!")
    print("Try to answer the following questions:")

    for state in states:
        correct_capital = states_capitals_india[state]
        user_answer = input(f"What is the capital of {state}? ").strip()
        
        if user_answer.lower() == correct_capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_capital}.")
        
        print()  
    print(f"Quiz finished! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    conduct_quiz()
