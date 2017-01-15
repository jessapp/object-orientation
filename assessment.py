"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: Hides internal details about a method that we don't need to know. 

   Encapsulation: Data lives close to its functionality - classes keep everything
   "together."

   Polymorphism: Interchangability - it's easy to make different, interchangeable
   "types" of a class. 

2. What is a class?

    A class is a construct in Python that lets you structure your code in a
    particular way, using object orientation. 

3. What is an instance attribute?

    When you instantiate a class, each individual instace can have certain
    attributes that are unique, rather than inhereted from the class. These 
    instace attributes are not shared by all instances of the class. 

4. What is a method?

    A method is similar to a function, but defined on a class. They always take
    at least one parameter, "self." 

5. What is an instance in object orientation?

    An instance is a specific realization of a class. To create an object with
    the parameters defined in your class, you need to instantiate it. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute that applies to every instance of that
   class, whereas an instance attribute is unique to each instance. For example,
   a class attribute may be species = "cat", as it applies to all instances of
   the Cat class. Meanwhile, an instance attribute may be name = "Fluffy" for a
   specific cat named Fluffy.


"""

class Student(object):
    """Intitalizes Student class"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Initializes Question class"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prints question and evaluates user answer for accuracy"""

        print self.question

        user_answer = raw_input("> ")

        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Initializes Exam class"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds new question and answer to the exam"""

        new_question = Question(question, correct_answer)

        self.questions.append(new_question)

    def administer(self):
        """Administers exam and calculates total score as a float"""

        score = 0
        total = 0

        for question in self.questions:
            answer = question.ask_and_evaluate()

            if answer:
                score += 1
        
        # Note - I changed the total from a float to an int for the output
        # Of the example() function. To return a float, it would be:
        # total = float(score / (len(self.questions)))

        total = (score * 100) / len(self.questions)

        return total


class Quiz(Exam):
    """Subclass of exam which generates only pass or fail grades"""

    def administer(self):
        final_grade = super(Quiz, self).administer()

        # If I was returning the total as a float, here 60 would be .6
        if final_grade >= 60:
            return True
        else:
            return False


def take_test(exam, student):
    """Takes an exam and a student as parameters to administer an exam and 
    assign a final score."""

    score = exam.administer()

    print "%s %s, your score is %s." % (student.first_name, student.last_name,
        score)


def example():
    """Administers a test using data created within the function"""

    exam = Exam("midterm")

    first_question = exam.add_question("What is a group of pandas called?", 
        "An embarassment")

    second_question = exam.add_question("What is a group of crows called?",
        "A murder")

    third_question = exam.add_question("What is a group of owls called?", 
        "A parliament")

    new_student = Student("P", "Sherman", "42 Wallaby Way, Sydney")

    take_test(exam, new_student)




