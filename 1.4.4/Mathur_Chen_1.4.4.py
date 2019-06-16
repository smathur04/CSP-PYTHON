'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')

''' PROCEDURE '''
#9. N/A
#10. N/A
#11. N/A
#12. N/A

'''
13. 
matplotlib.pyplot (plt) - an object oriented plotting library that is good for 
simple image manipulations and plotting and graphing.

numpy (np) - a library that is a math extension for the plotting features of
plt.

PIL - another object oriented library that is great for more advanced image
manipulations. 

'''

#14. N/A

'''
15.  

a. Line 19 calls the function subplots() from the matplotlib.pyplot library. 
The function is being called with 2 argument(s): 1 and 2. The function returns 1
object(s), which is/are being assigned to fig, ax.

b. In line 20 the imshow() method is called on the object ax[0]. 
Recite to your partner the methods called on each object in lines 20-27:
Line 20 calls imshow() on ax[0]
Line 23 calls imshow() on ax[1]
Line 24 calls set_xticks() on ax[1]
Line 25 calls set_xlim() on ax[1]
Line 26 calls set_ylim() on ax[1]
Line 27 calls savefig() on fig

c. (1162, 966)
'''

'''
16. X limits: 700 - 800 ; Range: 100
    Y Limits: 940 - 1025; Range: 85
'''

'''
17.

a. Line 30 uses the join() method from the os.path module. It is being passed
2 arguments. The value it returns is being assigned to the variable earth_file.

b.
In line 31 the open() function of the PIL.Image module returns a new PIL.Image 
object, which is being assigned to the variable earth_img.

c. Because a tuple is enclosed in parenthesis and the tuple is within the 
parenthesis of the method call.

d. It resizes the Earth to the size of the girl's iris.

e. 
Line 33 calls the method subplots() on the object fig2, axes2 with 2 
argument(s): (1,2). 

Line 34 calls the method imshow() on the object axes2[0] with 1 
argument(s): earth_img. 

Line 35 calls the method imshow()  on the object axes2[1] with 1 
argument(s): earth_small. 

Line 36 calls the method savefig() on the object fig2 with 1 
argument(s): 'resize_earth'. 

f. type; jpg; thumbnail

g. Width and Height

h. Prints the width and height of earth_img an earth_small, and the height of 
earth_img.

i. The image with more pixels has much better quality than the one with less.
'''

print(earth_img.size)
print(earth_small.size)
print(earth_img.size[1])

'''
18. Resize() looks at a few pixels in an image at a time and estimates what
color would best fit a new pixel in the resized image, it does this multiple
times until the entire image has been resized.
'''

'''
19.
a. student_img bytes = 15,667,200
   earth_small bytes = 30,972
   
b. earth_small.save('smallEarth.png')

c. 
student.jpg bytes = 211,546

smallEarth.png bytes = 18,774

d. When the files are downloaded, the are compressed and therefore, their size
is reduced.

e. Then that specific color will fill the indicated region. 

f. If the modes are different then the pasted image is converted to match the 
same mode of the image it is being pasted on to.

g. The first argument tells what needs to be pasted on to the object student_img
   The second argument is a two tuple defining the coordinates of the upper left
   corner on which the image will be pasted. The third argument uses the alpha
   from the mask of earth_small.
'''

#20. CODE BELOW
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
student_img.paste(earth_small, (700, 940), mask=earth_small) 
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earths_as_eyes')

''' CONCLUSION '''

'''
1. 
Classes:
Image - An important class of PIL
pyplot - An important class of Matplotlib

Methods:
open() - Opens up a new file 
paste() - Pastes color or image 
subplots() - Creates an array
imshow() - Saves the image
resize() - Changes image size

Attributes:
Color(RGB); Type of file; Name; Coordinates

2. We did a lot of image manipulations by using prewritten code from the PIL
library. The thing abstracted was all the code that goes into the library,
classes, and modules.
'''