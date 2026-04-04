# This script computes grades for CSE101 students based on projected test and HW grades. 

# 
# USAGE: python3 grading-for-students.py
# OUTPUT: projected grade, printed to console.
# 
# It will prompt the student to enter grades (through the console) for the tests and for the HWs.
# 
# The output grade is printed out to the console, and is computed based on a simple decision tree.
# 
# Niloofar Montazeri- May 2025

import sys
import os

test_str = input('Enter your raw test scores, with spaces between the scores: ') # get the string of test scores
hw_str = input('Enter your raw homework scores, with spaces between the scores: ') # get the string of HW scores
test_tokens = (test_str.strip()).split() # tokenize the test scores by whitespace
hw_tokens = (hw_str.strip()).split() # tokenize the HW scores by whitespace

test_scores = list() # initialize list of test scores
hw_scores = list() # initialize list of HW scores

num_tests = 5 # just setting the constants for number of tests and hws
num_hw = 4

# loop over test_tokens to get the test scores
for i in range(1,num_tests+1): # start loop from 1, to make indexing easier
    if (i > len(test_tokens)): # user did not provide score for this test
        print('You did not give a score for Test '+str(i)+', so setting score to zero\n')
        test_scores.append(0)
    else: # user did give score, so append
        test_scores.append(int(test_tokens[i-1])) # note the off by one, since i indexes the test number, which is one less than the array index. Also this line may throw exception if score provided is not integer


# loop over hw_tokens to get HW scores
for i in range(1,num_hw+1): # start loop from 1, to make indexing easier
    if (i > len(hw_tokens)): # user did not provide score for this HW
        print('You did not give a score for HW '+str(i)+', so setting score to zero\n')
        hw_scores.append(0)
    else: # user did give score, so append
        hw_scores.append(int(hw_tokens[i-1])) # note the off by one, since i is the HW number. Line may throw exception if score is not integer

test_total = sum(test_scores) - min(test_scores)# this is the normalized test score, obtained by removing the worst test. Total is out of 400
test_average=test_total/4  #test_average is out of 100

hw_average_after_downweight = float(4*sum(hw_scores) - 3*min(hw_scores))/float(4*num_hw - 3) # normalize hw scores, obtained by downweighting worst hw to one-fourth. Total is out of 100

# now for the decision tree




if test_average < 70:
    print('Sorry, you will not pass the course')
else: # student will pass the course. Now we determine the grade
    
    # low score on HW -> final grade is at least C 
    if hw_average_after_downweight < 30: 
        
        if test_average < 80: # pass-only test performance (70 -- 80)
            print('You will get at least a C.')
            
        elif test_average < 90: # ok test performance (80 -- 90) 
            print('You will get at least a C+.')
        
        else: #good test performance (90 or above)
            print('You will get at least a B-')
    
    
    # ok performance on HW (30--50)  -> final grade is at least B-
    elif hw_average_after_downweight < 50: 
        if test_average < 90: 
            print('You will get at least a B-.') 
        else:
            print('You will get at least a B.')
    
    # good HW performance ( 50 -- 75) -> final grade is B or B+
    elif hw_average_after_downweight < 75: 
        if test_average < 90: 
            print('You will get at least a B.') 
        else:
            print('You will get at least a B+.')
                
    # strong HW performance(75 or above) -> final grade is at least B+
    else: 
        
        # pass-only test performance (70 -- 80) -> final grade is B+
        if test_average <  80: 
            print('You will get a B+')
        
        # ok test performance (80 -- 90) -> final grade is A-
        elif test_average <  90: 
            print('You will get an A-')
        
        # good test performance (90 or above) -> final grade is at least A. 
        else: 
        	# great performance (100 or above) on BOTH test and HW -> A+ 
                if hw_average_after_downweight >= 100 and test_average >= 100:
                    print('You will get an A+')
                                
                else:
                    print('You will get at least an A.')