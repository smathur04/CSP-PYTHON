from __future__ import print_function

''' Procedure '''

#1. N/A

#2. N/A

#3. N/A

''' Part I: Using Arrays of Pixels '''

'''
4. Arrays all contain the same data type, so they can be loaded and used faster,
while lists can contain all sorts of different datatypes. However, they both
are good ways to contain data and can be accesed using indexes (iterable).
'''

'''
5. 
the image height = the number of rows of pixels = print(len(img)) = 960
the image width = the number of columns = print(len(img[0])) = 584
the green intensity at (5,9) = img[5][9][1]
the red intensity at (4,10) = img[4][10][0] = 62
the red intensity of the 25th pixel in the 50th row = img[49][24][0] = 71
'''

import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img2 = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
###
# Change a region if condition is True
###
height = len(img2)
width = len(img2[0])
for r in range(155):
    for c in range(width):
        if sum(img2[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img2[r][c]=[255,0,255] # R + B = magenta
for row in range(415, 475):
    for column in range(130, 160):
        img2[row][column] = [200, 100, 100] # red + green = yellow
# Show the image data in a subplot
ax.imshow(img2, interpolation='none')
# Saves the figure
fig.savefig('women_sky_earing')


'''
print(type(img))
print(img)
print(len(img))
print(len(img[0]))
'''

''' Part II: Manipulating Pixels '''

'''
6. Code Above
'''

'''
7. 
a. The code replaces all the sky(add up to over 500) pixels within the
first 155 rows and all columns with magenta pixels.
b. and c. code above
'''

'''
8. Code Below
'''

'''
9. Code Below
'''

import PIL

columns = 500
rows = 500
stripe_width = 10
img = PIL.Image.new('RGBA', (columns, rows))
image = np.array(img)

for row in range(rows):
    for column in range(columns):
        
        if row/stripe_width % 2 == 0: 
            image[row][column] = [255, 0, 0, 255] 
            
        elif column/stripe_width % 3 == 0: 
            image[row][column] = [0, 255, 0, 255] 
            
        elif (row+column)/stripe_width % 4 == 0: 
            image[row][column] = [0, 0, 0, 255] 
        else:
            # Odd stripe
            image[row][column] = [255, 0, 255, 255]
            
fig, ax = plt.subplots(1, 1)
ax.imshow(image)
fig.savefig('mask')            
 
fig, ax = plt.subplots(1, 2)
ax[0].imshow(image)
ax[1].imshow(img2)
fig.savefig('women_and_mask')         

''' CONCLUSION '''

'''
1. An image is a multidimensional array that contains RGBA data for each pixel
for every corresponding column and row. To alter and image means that you change
some of the data of the pixels in an image.

2. They both might have the same RGB values, but their alpha values will differ.

3. 
a. Because they are the leftmost bits.
b. 8 bits are in a byte and 6 multiplied by 8 is 64. 
c. It would make lots of pixels blue. 

4. It might look for certain common formations or groupings of pixels with 
certain colors. 
'''
