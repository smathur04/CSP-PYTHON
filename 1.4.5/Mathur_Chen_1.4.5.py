from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right

    plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  
  
    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
round_corners_of_all_images()
 
    
''' PROCEDURE '''
#1: N/A
#2: N/A
#3: N/A
#4: N/A

'''
5. The three functions are round_corners_of_all_images(), get_images(), and
round_corners_one_image().
'''

'''
6. It rounded the corners of all the images in the images folder and then placed
all the new modified images in a folder name modified. It also tallyed in the
ipython terminal as it modified each image.
''' 

'''
7.

a. 
Argument 1: original_image is a PIL.image

Argument  2: percent_of_side is a float

Return value: result is also a PIL.image 

b. It is a dark magenta.

c. 
Object created in line 26: rounded_mask

Object created in line 27: drawing_layer

d.  To make an image transparent in the corners, the alpha value should be 255 

e.
Horizontal Rect: 36-38
Vertical Rect: 33-35
Top Left Circ: 41-42
Top Right Circ: 43-44
Bottom Left Circ: 45-46
Bottom Right Circ: 47-48

f. 
The color is white. This is because the color is originally black but it is
transparent so it became white. 

g. (0,0,0,0)
'''

'''
8.

a.Because a default value is specified for directory, that argument is optional,
so get_images() can be passed either 0 or 1 arguments.

b. Returns two 2 tuples, image_list and file_list.

c.
os.getcwd() 
os.listdir() 
os.path.join()

d. Return a list containing the names of the entries in the directory given by 
path.

e. It uses a try-except on every image so it can test for errors individually,
the doenside is it might take the program longer to run.

f. Lines 80 and 81 check to see if there is a specific type of error, and if
there is they allow the code to still keep running. 
'''

'''
9. 
a. It is in the try-except statement so it the code will still run if the 
modified directory already exists.

b. The amount of imaages that are in the directory.

c. It means number and is used to iterate through all the images.
'''

''' CONCLUSION '''
'''
1. This was created by using a mask to make everything that is not part of the
icon transparent.

2. The round_corners_of_all_images functions worked by using the other two 
functions. This made the code neater, simpler, and broke things up into 
easy to understand pieces.

3. I think both Barb and Alice are right in certain ways. In a sense, all images
are manipulations because of how complex the way we see things is, but it all
depends on your definition of manipulation. If you think manipulaations only
count if they are done after a picture is created, then Barb is right there is
a "real image".

4. An image or picture that you draw, take, or creat in any way is officially 
yours to use. Also, so are free images online or images that you must use with
watermarks or credits. As long as you follow all specified rules, most pictures
can be used in many ways by you. However, selling should only be done with your
own photos and images.

5. We work well together, but need to work on staying on topic and not getting
distracted. Next time, we need to focuse more and try to get things done faster.
'''