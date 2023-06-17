#program : calculate the average, and letter grade
#author: Avey
#date : 4/4/2023

'''
    Problem : Finding the letter grade of a student using their three test scores
        Input : The test scores
        Processing : Calculating the average of the three test scores
        Output: Using the average, print out a letter grade

        Pseudocode:
            1. Prompt the user to enter the three test scores gotten by student
            2. Read user input and store it into a variable
            3. Find the average of all three test scores, and kill the program if the socre is out of range(0-100)
            4. If the average of all three test scores is >= 90:
                    letter grade = A
                If the average of all three scores is >= 70 and <90:
                    if
                    Look at the third score, if it is >= 90:
                    letter grade = 'A'
                else:
                    letter grade = 'B'
                If the average of all three test score is >=50 and <70:
                    Look at the average of the second and third test score, if it is >= 70:
                    Letter grade = 'C'
                else;
                    Letter grade = 'D'
                If the average score < 50:
                    Letter grade = 'F'
            5. variable : test_score1 , test_score2 , test_score3, average ,average2

'''

def main():
    #grade input
    
    for i in range (1,4):
        if i == 1:
            test_score1 = grade_input(1)
        elif i == 2:
            test_score2 = grade_input(2)
        else:
            test_score3 = grade_input(3)
    
    #processing average
    average = average_3scores(test_score1, test_score2 , test_score3)
    average2 = average_2scores (test_score2 , test_score3)

    #get letter grade
    letter_grade = get_letter_grade(average,average2,test_score3)

    #display letter grade
    display_letter_grade(average,letter_grade)
    
def grade_input(test_score):
    #prompt user to enter the three test scores
    test_score = int(input("Enter the score for test" + str(test_score) + ":"))
    while test_score < 0 or test_score > 100:
        test_score = int(input("Invalid.The test score has to be between 0-100:"))
    return test_score

def average_3scores(test_score1,test_score2,test_score3):
    #get the average of the 3 test scores
    average_3scores = float(test_score1 + test_score2 + test_score3) / 3
    average = int(average_3scores + 0.5)
    return average

def average_2scores(test_score2,test_score3):
    #get the average of the 2 test scores
    average_2scores = float(test_score2 + test_score3) / 2
    average = int(average_2scores + 0.5)
    return average
    
def get_letter_grade(average,average2,test_score3):
    #get letter grade
    if average > 90:
        letter_grade = "A"
    elif average > 70 or average2 < 90:
        if test_score3 >= 90:
            letter_grade = 'A'
        else:
            letter_grade = 'B'

    elif average >= 50 and average <70:
        if average2 >= 70:
            letter_grade = 'C'
        else:
            letter_grade = 'D'
       
    else:
        average >=0 and average < 50
        letter_grade = 'F'
        
    return letter_grade
        
def display_letter_grade(average,letter_grade):
    #display letter grade
    print()
    print("Your final average is :" , format (average,".2f"))
    print("Your final grade is :" , letter_grade)



#call main()
main()
    
