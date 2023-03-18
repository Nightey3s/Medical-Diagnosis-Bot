"""
Medical Diagnosis Bot

- Project Definition

    - Diagnose user's state of dehydration based on a short questionnaire
        - Yes or No questions
        - Previous responses determine next questions
        - Severe/Some/No Dehydration

    - Retreive and add dehydration diagnosis
        - Display a list of patients and diagnoses
        - Store new diagnoses in the list
        
- Project Design

    - 2 main functions
        1. Run a new diagnosis and store results
        2. Display a list of previous patients and diagnoses

- How will it work

    - Text-based interface
        1. Display prompt/question
        2. Process user text input

- Algorithm

                                                                1. Assess general appearance
                                                                               |
                                                                               |
                                                            ---------------------------------------------
                                                            |                                           |
                                                          Normal                             Irritable or Lethargic
                                                            |                                           |
                                                            |                                           |   
                                                       2.Assess Eyes                            2.Assess Skin Pinch
                                                            |                                           |   
                                   --------------------------------------                   ---------------------------------
                                   |                                    |                   |                               | 
                       Eyes normal or slightly sunken            Eyes very sunken     Skin pinch normal                Skin pinch slow
                                   |                                    |                   |                               |
                                   |                                    |                   |                               |        
                            3. No Dehydration                 3. Severe Dehydration     3. Some Dehydration               3. Severe Dehydration

"""
# Clear the terminal
import os
os.system('cls')

""" Prompts """
welcome_prompt = "\n\nWelcome to the Medical Diagnosis Bot, what would you like to do? \n 1. List all patients, press 1 \n 2. Run a new diagnosis, press 2 \n 3. To Exit, press Q \n\n"
name_prompt = "\nWhat is the patient's name\n"
appearance_prompt = "\nHow does the patient look? \n 1. Normal Appearance\n 2. Irritable or Lethargic \n\n"
eye_prompt = "\nHow do the patient's eyes look? \n 1. Eyes normal or slightly sunken \n 2. Eyes very sunken \n\n"
skin_prompt = "\nHow does the patient's skin feel? \n 1. Skin pinch normal \n 2. Skin pinch slow \n\n"

""" Diagnosis Results """
no_dehydration = "No Dehydration"
some_dehydration = "Some Dehydration"
severe_dehydration = "Severe Dehydration"

""" List of patients and diagnoses """
patients_and_diagnoses = [
    ["John", "No Dehydration"],
    ["Mary", "Some Dehydration"],
    ["Bob", "Severe Dehydration"]
]

""" Error Messages """
error_message = "Could not save the diagnosis, due to invalid patient name"

# Function to list all patients and diagnoses stored in patients_and_diagnoses
def list_patients():
    for patient in patients_and_diagnoses:
        print(patient[0] + ": " + patient[1])

# Function to save a new diagnosis to the list of patients_and_diagnoses
def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    patients_and_diagnoses.append([name, diagnosis])
    print("Patient: " + name + "\nDiagnosis: " + diagnosis + "\nSaved to the list of patients and diagnoses")

# Function to assess skin pinch, returns a diagnosis
def assess_skin(skin):
    # Assess skin pinch
    if skin == "1":
        # Skin pinch normal
        return some_dehydration
    elif skin == "2":
        # Skin pinch slow
        return severe_dehydration
    else:
        # Invalid input
        print("Invalid input, please try again")
        return ""

# Function to assess eye appearance, returns a diagnosis
def assess_eye(eye):
    # Assess eye appearance
    if eye == "1":
        # Eyes normal or slightly sunken
        return no_dehydration
    elif eye == "2":
        # Eyes very sunken
        return severe_dehydration
    else:
        # Invalid input
        print("Invalid input, please try again")
        return ""
   
# Function to assess general appearance, continues to assess eye or skin pinch
def assess_appearance():
    # Assess general appearance
    appearance = input(appearance_prompt)
    if appearance == "1":
        # Normal Appearance
        eye = input(eye_prompt)
        return assess_eye(eye)
    elif appearance == "2":
        # Irritable or Lethargic
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        # Invalid input
        print("Invalid input, please try again")
        return ""

# Function to run a new diagnosis
def run_diagnosis():

    name = input(name_prompt)
    diagnosis = assess_appearance()

    # return name, diagnosis
    save_new_diagnosis(name, diagnosis)
    
# Main function
def main():
    
    while True:
        selection = input(welcome_prompt)
    
        if selection == "1":
            # List all patients
            list_patients()
        elif selection == "2":
            # Run a new diagnosis
            run_diagnosis()
        elif selection == "Q" or selection == "q":
            # Exit
            print("Goodbye")
            return # Exit the program
        else:
            # Invalid input
            print("Invalid input, please try again")
            

main()

""" Unit Tests """
    # Unit test for skin assessment
def test_assess_skin():
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("") == "")

#test_assess_skin()

    # Unit test for eye assessment
def test_assess_eye():
    print(assess_eye("1") == no_dehydration)
    print(assess_eye("2") == severe_dehydration)
    print(assess_eye("") == "")

#test_assess_eye()

    # Unit test for save new diagnosis
def test_save_new_diagnosis():
    print(save_new_diagnosis("John", "No Dehydration") == None)
    print(save_new_diagnosis("", "No Dehydration") == error_message)
    print(save_new_diagnosis("John", "") == error_message)
    print(save_new_diagnosis("", "") == error_message)

#test_save_new_diagnosis()


""" Integration Tests """
    # Integration test for appearance assessment
def test_assess_appearance():
    print(assess_appearance())

#test_assess_appearance()