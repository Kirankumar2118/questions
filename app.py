from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)


# At the beginning of the file, add difficulty levels
DIFFICULTY_LEVELS = {
    'EASY': 1,
    'MEDIUM': 2,
    'HARD': 3
}



# Question bank for different programming languages
# Sample with difficulty added to Python questions
question_bank = {
    'Python': [
        {
            'question': 'What is a list comprehension in Python?',
            'options': [
                'A concise way to create lists based on existing lists',
                'A way to sort lists',
                'A type of function',
                'A loop structure'
            ],
            'correct_answer': 0,
            'explanation': 'List comprehension is a concise way to create lists based on existing lists or other iterables.',
            'difficulty': DIFFICULTY_LEVELS['EASY']
        },
        {
            'question': 'What is the difference between tuple and list in Python?',
            'options': [
                'Tuples are immutable while lists are mutable',
                'Tuples can only store numbers',
                'Lists can only store strings',
                'There is no difference'
            ],
            'correct_answer': 0,
            'explanation': 'The main difference is that tuples are immutable (cannot be modified after creation) while lists are mutable.',
            'difficulty': DIFFICULTY_LEVELS['EASY']
        },
        {
            'question': 'What is a decorator in Python?',
            'options': [
                'A function that modifies another function',
                'A type of loop',
                'A way to create classes',
                'A built-in data type'
            ],
            'correct_answer': 0,
            'explanation': 'A decorator is a function that takes another function as input and extends its behavior without explicitly modifying it.',
            'difficulty': DIFFICULTY_LEVELS['MEDIUM']
        },
        {
            'question': 'What is the purpose of __init__ method in Python?',
            'options': [
                'To initialize object attributes when creating an instance',
                'To delete an object',
                'To import modules',
                'To define static methods'
            ],
            'correct_answer': 0,
            'explanation': 'The __init__ method is a constructor that initializes object attributes when an instance is created.',
            'difficulty': DIFFICULTY_LEVELS['EASY']
        },
        {
            'question': 'What is a lambda function in Python?',
            'options': [
                'An anonymous function defined in a single line',
                'A built-in function',
                'A type of class',
                'A module'
            ],
            'correct_answer': 0,
            'explanation': 'Lambda functions are small anonymous functions that can be defined in a single line.',
            'difficulty': DIFFICULTY_LEVELS['MEDIUM']
        },
        {
            'question': 'What is the difference between "==" and "is" operators in Python?',
            'options': [
                '"==" compares values while "is" compares identity',
                'They are exactly the same',
                '"is" compares values while "==" compares identity',
                'Neither compares values'
            ],
            'correct_answer': 0,
            'explanation': '"==" compares the values of objects while "is" compares their identity (memory location).',
            'difficulty': DIFFICULTY_LEVELS['MEDIUM']
        },
        {
            'question': 'What is a generator in Python?',
            'options': [
                'A function that yields values one at a time',
                'A type of variable',
                'A built-in module',
                'A way to create classes'
            ],
            'correct_answer': 0,
            'explanation': 'A generator is a function that generates values on-the-fly and yields them one at a time.',
            'difficulty': DIFFICULTY_LEVELS['MEDIUM']
        },
        {
            'question': 'What is the purpose of the "self" parameter in Python classes?',
            'options': [
                'To refer to the instance of the class',
                'To create static methods',
                'To import modules',
                'To define class variables'
            ],
            'correct_answer': 0,
            'explanation': 'The self parameter refers to the instance of the class and is used to access instance variables and methods.',
            'difficulty': DIFFICULTY_LEVELS['EASY']
        },
        {
            'question': 'What is the Global Interpreter Lock (GIL) in Python?',
            'options': [
                'A mutex that allows only one thread to execute Python bytecode',
                'A type of variable scope',
                'A built-in function',
                'A way to handle exceptions'
            ],
            'correct_answer': 0,
            'explanation': 'The GIL is a mutex that prevents multiple native threads from executing Python bytecode simultaneously.',
            'difficulty': DIFFICULTY_LEVELS['HARD']
        },
        {
            'question': 'What are Python modules?',
            'options': [
                'Files containing Python code that can be imported and reused',
                'Built-in data types',
                'Special functions',
                'Class definitions'
            ],
            'correct_answer': 0,
            'explanation': 'Modules are files containing Python code that can be imported and reused in other Python programs.',
            'difficulty': DIFFICULTY_LEVELS['EASY']
        }
    ],
    'Java': [
    {
        'question': 'What is inheritance in Java?',
        'options': [
            'A mechanism that allows a class to inherit properties from another class',
            'A way to create objects',
            'A type of loop',
            'A data structure'
        ],
        'correct_answer': 0,
        'explanation': 'Inheritance is a fundamental OOP concept that allows a class to inherit attributes and methods from another class.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is the purpose of the "static" keyword in Java?',
        'options': [
            'To declare a class member that belongs to the class rather than instances',
            'To prevent class inheritance',
            'To create dynamic memory allocation',
            'To implement multiple inheritance'
        ],
        'correct_answer': 0,
        'explanation': 'The static keyword indicates that a member belongs to the class itself rather than to any specific instance of the class.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is method overloading in Java?',
        'options': [
            'Creating multiple methods with the same name but different parameters',
            'Overriding a parent class method',
            'Creating a copy of a method',
            'Implementing an interface method'
        ],
        'correct_answer': 0,
        'explanation': 'Method overloading allows creating multiple methods with the same name but different parameter lists in the same class.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is the purpose of the "final" keyword in Java?',
        'options': [
            'To prevent inheritance, method overriding, or variable reassignment',
            'To mark the end of a program',
            'To declare the main method',
            'To import external libraries'
        ],
        'correct_answer': 0,
        'explanation': 'The final keyword can be used to prevent inheritance of classes, overriding of methods, or reassignment of variables.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is a constructor in Java?',
        'options': [
            'A special method used to initialize objects',
            'A method to destroy objects',
            'A type of loop',
            'A way to implement interfaces'
        ],
        'correct_answer': 0,
        'explanation': 'A constructor is a special method that is called when an object is created and is used to initialize object state.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is the difference between ArrayList and LinkedList in Java?',
        'options': [
            'ArrayList uses dynamic array while LinkedList uses doubly linked list',
            'ArrayList is slower than LinkedList for all operations',
            'LinkedList uses less memory than ArrayList',
            'There is no difference between them'
        ],
        'correct_answer': 0,
        'explanation': 'ArrayList uses a dynamic array for storing elements while LinkedList uses a doubly linked list implementation.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is the purpose of the "super" keyword in Java?',
        'options': [
            'To call the parent class constructor or methods',
            'To create a new object',
            'To implement multiple inheritance',
            'To declare static methods'
        ],
        'correct_answer': 0,
        'explanation': 'The super keyword is used to call parent class methods or constructor and to access parent class variables.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is exception handling in Java?',
        'options': [
            'A mechanism to handle runtime errors using try-catch blocks',
            'A way to create custom objects',
            'A method to optimize code',
            'A type of loop structure'
        ],
        'correct_answer': 0,
        'explanation': 'Exception handling is a mechanism to handle runtime errors to maintain normal flow of program execution.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is the purpose of the "interface" in Java?',
        'options': [
            'To define a contract that classes must implement',
            'To create objects directly',
            'To handle exceptions',
            'To implement multiple inheritance of state'
        ],
        'correct_answer': 0,
        'explanation': 'An interface defines a contract of methods that implementing classes must provide.',
        'difficulty': DIFFICULTY_LEVELS['HARD']
    },
    {
        'question': 'What is the Java Virtual Machine (JVM)?',
        'options': [
            'A runtime environment that executes Java bytecode',
            'A text editor for Java',
            'A compiler for Java',
            'A database management system'
        ],
        'correct_answer': 0,
        'explanation': 'JVM is a runtime environment that provides a platform-independent way to execute Java bytecode.',
        'difficulty': DIFFICULTY_LEVELS['HARD']
    }
],
'C++': [
    {
        'question': 'What is a pointer in C++?',
        'options': [
            'A variable that stores memory address',
            'A type of loop',
            'A string variable',
            'A function'
        ],
        'correct_answer': 0,
        'explanation': 'A pointer is a variable that stores the memory address of another variable.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is operator overloading in C++?',
        'options': [
            'Defining how operators work with user-defined types',
            'Creating multiple functions with same name',
            'Overriding base class methods',
            'Creating new operators'
        ],
        'correct_answer': 0,
        'explanation': 'Operator overloading allows you to define how operators behave when used with user-defined types.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is the difference between struct and class in C++?',
        'options': [
            'Default access specifier is public in struct and private in class',
            'Struct cannot have member functions',
            'Class cannot have member variables',
            'There is no difference'
        ],
        'correct_answer': 0,
        'explanation': 'The main difference is that members are public by default in struct and private by default in class.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is virtual function in C++?',
        'options': [
            'A function that can be overridden in derived class',
            'A function without implementation',
            'A static function',
            'A private function'
        ],
        'correct_answer': 0,
        'explanation': 'Virtual functions enable runtime polymorphism by allowing function overriding in derived classes.',
        'difficulty': DIFFICULTY_LEVELS['HARD']
    },
    {
        'question': 'What is a reference in C++?',
        'options': [
            'An alias for an existing variable',
            'A pointer to a variable',
            'A copy of a variable',
            'A constant variable'
        ],
        'correct_answer': 0,
        'explanation': 'A reference is an alias for an existing variable and must be initialized when declared.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is the purpose of the "new" operator in C++?',
        'options': [
            'To allocate memory dynamically',
            'To create a new class',
            'To declare variables',
            'To implement inheritance'
        ],
        'correct_answer': 0,
        'explanation': 'The new operator allocates memory dynamically during runtime and returns a pointer to the allocated memory.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is a constructor in C++?',
        'options': [
            'A special member function that initializes objects',
            'A function to destroy objects',
            'A type of pointer',
            'A static member'
        ],
        'correct_answer': 0,
        'explanation': 'A constructor is a special member function that is called when an object is created.',
        'difficulty': DIFFICULTY_LEVELS['EASY']
    },
    {
        'question': 'What is function overloading in C++?',
        'options': [
            'Defining multiple functions with same name but different parameters',
            'Overriding base class functions',
            'Creating virtual functions',
            'Implementing operator overloading'
        ],
        'correct_answer': 0,
        'explanation': 'Function overloading allows you to define multiple functions with the same name but different parameter lists.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is the purpose of the "const" keyword in C++?',
        'options': [
            'To declare constants and prevent modifications',
            'To create static variables',
            'To implement inheritance',
            'To declare virtual functions'
        ],
        'correct_answer': 0,
        'explanation': 'The const keyword is used to declare constants and prevent modifications to variables or member functions.',
        'difficulty': DIFFICULTY_LEVELS['MEDIUM']
    },
    {
        'question': 'What is an STL container in C++?',
        'options': [
            'A template class that stores and manages collections of objects',
            'A type of pointer',
            'A member function',
            'A base class'
        ],
        'correct_answer': 0,
        'explanation': 'STL containers are template classes that provide different ways to store and manage collections of objects.',
        'difficulty': DIFFICULTY_LEVELS['HARD']
    }
]


}






@app.route('/')
def home():
    return render_template('index.html')




@app.route('/get_question', methods=['POST'])
def get_question():
    data = request.get_json()
    language = data.get('language', 'Python')
    current_difficulty = data.get('difficulty', DIFFICULTY_LEVELS['EASY'])
    last_correct = data.get('last_correct', None)
    
    if language in question_bank and question_bank[language]:
        questions = question_bank[language]
        
        # Filter questions based on difficulty
        if last_correct is not None:
            if last_correct:
                # If last answer was correct, increase difficulty
                current_difficulty = min(current_difficulty + 1, DIFFICULTY_LEVELS['HARD'])
            else:
                # If last answer was wrong, maintain current difficulty
                pass
        
        # Filter questions by current difficulty
        available_questions = [q for q in questions if q['difficulty'] == current_difficulty]
        
        if available_questions:
            # Randomly select a question from available questions
            question = dict(random.choice(available_questions))
            
            # Get the correct answer text
            correct_answer_text = question['options'][question['correct_answer']]
            
            # Shuffle the options
            shuffled_options = question['options'].copy()
            random.shuffle(shuffled_options)
            
            # Find the new index of the correct answer
            question['correct_answer'] = shuffled_options.index(correct_answer_text)
            question['options'] = shuffled_options
            
            return jsonify({
                'question': question,
                'total_questions': len(questions),
                'current_difficulty': current_difficulty
            })
    
    return jsonify({'error': 'Question not found'})

# ... existing code ...
@app.route('/evaluate_answers', methods=['POST'])
def evaluate_answers():
    data = request.get_json()
    answers = data.get('answers', [])
    language = data.get('language', 'Python')
    
    if language not in question_bank:
        return jsonify({'error': 'Language not found'})
    
    questions = question_bank[language]
    total_score = 0
    feedback = []
    
    for i, answer in enumerate(answers):
        if i < len(questions):
            question = questions[i]
            is_correct = answer == question['correct_answer']
            total_score += 100 if is_correct else 0
            feedback.append({
                'question_index': i,
                'is_correct': is_correct,
                'explanation': question['explanation'],
                'selected_answer': answer,
                'correct_answer': question['correct_answer'],
                'difficulty': question['difficulty']
            })
    
    average_score = total_score / len(questions) if questions else 0
    
    return jsonify({
        'feedback': feedback,
        'total_score': average_score
    })
if __name__ == '__main__':
    app.run(debug=True)