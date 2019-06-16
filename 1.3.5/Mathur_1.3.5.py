from __future__ import print_function

'''Procedure'''
#1. N/A
#2. N/A
#3. N/A
#4. N/A
#5. THe datatypes Int, Float, Long, String

'''
6. A string and integer are two different data types and therefore cannot be
added together because there is no data type for a combination of them while a
string and string added still is a string.
'''

'''
7.
slogan[0]: The first letter which starts counting at 0.
slogan[2]: The third letter due to the counting starting at 0.
slogan[8]: The seventh letter due to the counting starting at 0.
slogan[26]: Error due to there not being that many letters.
slogan[-2]: Starts counting from the right starting with -1 so it is s.
slogan[-7]: Starts counting from the right starting with -1 so it is h.
'''

'''
8 SLICING
slogan = 'My school is the best'
slogan[17:21]
'''

#9 print('DHS', slogan[10:21])

#10a. There are 7 letters in the word theater so that is what it returned.

#10b. The word 'theate' is returned because the slice is the same as [0:6]

'''
11. 'test goo'searches for the phrase 'goo' in the string and since it was 
there it returned true.
'''

'''
12. CODE BELOW
'''
def how_eligible(essay):
    '''
    Judges an essay using a four point system
    Input is always a string 
    Output is and integer value of the points you got.
    '''
    count = 0;
    if ',' in essay:
        count += 1;
    if '!' in essay:
        count += 1;
    if '?' in essay:
        count += 1;
    if '"' in essay:
        count += 1;
    return count;
    
''' ASSIGNMENT CHECK '''
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
