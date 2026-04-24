import random 
import os


print(""" 
============================
        Python Quiz
============================""")



bf_random= [
    {
        "id": 1,
        "question": "What happens if you access a missing key using my_dict['key']?",
        "options": {
            "A": "It returns None",
            "B": "It returns False",
            "C": "It raises a KeyError",
            "D": "It creates the key with value 0"
        },
        "answer": "C"
    },
    {
        "id": 2,
        "question": "As of Python 3.7+, which statement is true about dictionaries?",
        "options": {
            "A": "They are unordered collections",
            "B": "They maintain insertion order",
            "C": "They allow duplicate keys",
            "D": "Keys must be mutable (like lists)"
        },
        "answer": "B"
    },
    {
        "id": 3,
        "question": "What is the result of: {'a': 1}.get('b', 3)?",
        "options": {
            "A": "None",
            "B": "KeyError",
            "C": "2",
            "D": "3"
        },
        "answer": "D"
    },
    {
        "id": 4,
        "question": "Which method removes a key and returns its value?",
        "options": {
            "A": ".remove()",
            "B": ".pop()",
            "C": ".delete()",
            "D": ".discard()"
        },
        "answer": "B"
    },
    {
        "id": 5,
        "question": "What is the output of {x: x**2 for x in [1, 2]}?",
        "options": {
            "A": "{1, 4}",
            "B": "[1: 1, 2: 4]",
            "C": "{1: 1, 2: 4}",
            "D": "(1: 1, 2: 4)"
        },
        "answer": "C"
    }
]

##randomize questions in the list and assign it to questions
random.shuffle(bf_random)
questions = bf_random
def main():

    score = 0 #stores score 
    i=0
    while i<len(questions):
        print(f"""
Question {i+1}/{len(questions)}
-----------------------------------""")
        print(questions[i]["question"])
        for x in questions[i]["options"].items():
            print(f"{x[0]} : {x[1]}")
        user = input("Your Answer? (A/B/C/D): ")
        ##os.system("clear")
        if user.upper()== questions[i]["answer"]:
            print("Correct")
            score +=1
        else:
            print("Wrong")
    
        i = i+1
    
    os.system("clear")
    
    print(f""" 
============================
       Final Result
============================

You scored {score} out of {len(questions)}
Not bad, but there is room to improve
        
    """)

    p = input("Play Again? (y/n)  : ")
    

    if p.lower() == "y":
        main()
    else:
        print("Thank you for playing the game. Have a nice day!!")
        pass
main()
