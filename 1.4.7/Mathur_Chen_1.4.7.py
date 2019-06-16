################################################################################

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import PIL
import PIL.ImageDraw            
import numpy as np

################################################################################

def get_images(directory=None):
    
    """ 
    Returns PIL.Image objects for all the images in directory.
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

################################################################################

def add_background_one_image(original_image, background_color, color, theme):
    
    '''
    Returns a PIL.image that is either a plain colored background or a polka
    dotted background behind original_image(must be .png)
    Original_image is just the .png image you want to add the background too
    Color is 4-tuple RGBA value for the polka dot's color
    Background color is 4-tuple RGBA value for the background's color
    Theme chooses whether there will be polka dots or not
    '''
    
    #this code only runs if the theme chosen is plain
    if theme == 'plain':
        #make colored background and paste image on top then return pasted image
        background = PIL.Image.new('RGBA', original_image.size, color)
        background.paste(original_image, (0,0), mask=original_image)
        return background
    
    #this code runs if the plain theme is not chosen(polka dots will be chosen)   
    else:
        #create a polka dot mask
        polka_dot_mask = PIL.Image.new('RGBA', (500,500), (0,0,0,0))
        #create a drawing layer
        drawing_layer = PIL.ImageDraw.Draw(polka_dot_mask)
        #draw a ton or varying sized circles all over the mask
        drawing_layer.ellipse([(10,10),(60,60)], fill = color)
        drawing_layer.ellipse([(80,80),(130,130)], fill = color)
        drawing_layer.ellipse([(150,200),(200,250)], fill = color)
        drawing_layer.ellipse([(280,280),(330,330)], fill = color)
        drawing_layer.ellipse([(400,400),(450,450)], fill = color)
        drawing_layer.ellipse([(350,350),(400,400)], fill = color)
        drawing_layer.ellipse([(100,440),(150,490)], fill = color)
        drawing_layer.ellipse([(100,250),(150,300)], fill = color)
        drawing_layer.ellipse([(400,10),(450,60)], fill = color)
        drawing_layer.ellipse([(250,120),(300,170)], fill = color)
        drawing_layer.ellipse([(250,50),(300,100)], fill = color)
        drawing_layer.ellipse([(155,50),(195,90)], fill = color)
        drawing_layer.ellipse([(40,180),(80,220)], fill = color)
        drawing_layer.ellipse([(35,350),(75,390)], fill = color)
        drawing_layer.ellipse([(205,185),(245,225)], fill = color)
        drawing_layer.ellipse([(150,140),(190,180)], fill = color)
        drawing_layer.ellipse([(340,100),(380,140)], fill = color)
        drawing_layer.ellipse([(415,140),(455,180)], fill = color)
        drawing_layer.ellipse([(310,185),(380,255)], fill = color)
        drawing_layer.ellipse([(160,325),(240,405)], fill = color)
        drawing_layer.ellipse([(410,270),(460,320)], fill = color)
        #save the mask
        plt.imshow(polka_dot_mask)
        #resize the mask to fit the original image
        final_dots = polka_dot_mask.resize(original_image.size)
        #create a plain background and past the original image and polka dots
        background = PIL.Image.new('RGBA', original_image.size,background_color)
        background.paste(final_dots, (0,0), mask=final_dots)
        background.paste(original_image, (0,0), mask=original_image)
        #return the new background
        return background

################################################################################

def make_border_one_image(original_image, color, border_thickness):
    
    """
    Adds a rectangular border to a PIL.Image that is .png
    original_image must be a PIL.Image and a .png
    
    Returns a new PIL.Image that is .png with a rectangular border and of the
    size of the original_image plus the border. Also border is of the color 
    chosen in the terminal.
    
    Original image is the image you want add the border to.
    Border_thickness is an integer that decides how big the border will be
    Color is a 4-tuple that represents the RGBA value of the border
    """
    #Adds the size of the border to the image
    width, height = original_image.size
    width += border_thickness * 2
    height += border_thickness * 2
    
    ###
    #create a mask
    ###
    
    #start with a mask based on chosen color
    border_mask = PIL.Image.new('RGBA', (width, height), color)
    
    #add a drawing layer
    drawing_layer = PIL.ImageDraw.Draw(border_mask)
    
    #draw transparent rectangle in the center depending on the border thickness
    drawing_layer.rectangle([(border_thickness, border_thickness), 
    (width-border_thickness, height-border_thickness)],fill=(0,0,0,0))

    #save the mask
    plt.imshow(border_mask)
    
    #paste the image and return
    result = PIL.Image.new('RGBA', (width,height), (color))
    result.paste(border_mask, (0,0), mask=border_mask)
    result.paste(original_image,(border_thickness, border_thickness))
    return result
    
################################################################################

def add_logo_one_image(original_image, logo_size, placement):
    
    '''
    Adds a small logo(image) into one of the corners of the original_image
    
    Returns the original_image with the logo pasted in one of the corners
    
    original_image is a .png PIL image that you want to paste the logo on to
    logo_size is an integer value of how big the logo will be 
    placement is a 2-tuple representing the (x,y) value for the logo's left
    corner
    '''
    
    #get images from the 1.4.7 folder
    image_list, file_list = get_images('../../..')
    
    #Choose logo.png
    curr_image = image_list[0]
    
    #Resize logo.png
    small_logo = curr_image.resize((logo_size,logo_size))
    
    #paste the small logo onto the original_image
    original_image.paste(small_logo, placement)
    
    #return the final product
    return original_image
    
################################################################################

def image_manipulations():
    
    '''
    Takes no input
    
    Returns several versions of the image(s) being modified each with certain
    additional manipulations being done to it. Returns a version with just the
    background, one with the background and border, one with the background,
    border and logo, and one with the background, border, logo, and message.
    
    This function runs the user-input based automated process for applying image
    manipulations to whatever .png images are in Project_Images. It gives the
    user instructions and prompts them to enter certain values so they can end
    up with an image that they desire.
    
    '''
    
    #Introduction & Instructions
    print('Welcome! Let\'s start manipulating some images and saving some \
gorillas!')
    print('Make sure you are only using .png images or else the program will \
not work.')
    print ('''Also, when choosing certain aspects of your image to be 
manipulated(color, border, logo, etc.) please choose all your inputs carefully,
follow all directions, and do your best to pick options that work well with
your image! If you are using a very small or large image pick sizes of things
accordingly. Remember, if things don't look good the first time, just run the 
program again and try to change things up. Have fun!''')
    print('')
    print('First, you should pick the color you want the background to be \
behind the gorillas.')
    print('')
    print('')
    
 
    directory = os.getcwd() # Use current working directory
        
    # Create a new directory 'background_added'
    new_directory = os.path.join(directory, 'background_added')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  
  
    # Go through the images and save modified versions
    for n in range(len(image_list)):

        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
            
        #Prints the specific image you are currently modifying
        print('You are on', filename + '.png')
        print('')
        
        #Prompts you to choose a plain or polk-dotted background
        theme = raw_input('What theme would you like, enter the letter A for \
polka dot or the letter B for plain: ')
        
        #This runs if the polka dot theme was chosen
        if theme in ['A', 'a', 'polka dots', 'Polka Dots', 'polka dot']:
            
            #Prompts you to pick the rgba color of the background
            red = raw_input('Please enter the numeric red value you want your \
background to have: ')
            green = raw_input('Please enter the numeric green value you want \
your background to have: ')
            blue = raw_input('Please enter the numeric blue value you want your\
background to have: ')
            alpha = raw_input('Please enter the numeric alpha value you want \
your background to have: ')
            print('')
            print('')
        
            #save the background color as RGBA 4-tuple
            back_color_choice = (int(red), int(green), int(blue), int(alpha))
            
            #prompts you to pick the polka dot rgba color values
            red = raw_input('Please enter the numeric red value you want your \
dots to have: ')
            green = raw_input('Please enter the numeric green value you want \
your dots to have: ')
            blue = raw_input('Please enter the numeric blue value you want \
your dots to have: ')
            alpha = raw_input('Please enter the numeric alpha value you want \
your dots to have: ')
            print('')
            print('')
        
            #save the dot color as RGBA 4-tuple
            dot_color_choice = (int(red), int(green), int(blue), int(alpha))
        
            #adds the background with the users choices by running a function
            new_image = add_background_one_image(curr_image, back_color_choice,
            dot_color_choice, 'polka')
            
            # Save the altered image, suing PNG to retain transparency
            new_image_filename = os.path.join(new_directory, filename + 
            '_background.png')
            new_image.save(new_image_filename)
        
        #this code runs if the plain them was chosen   
        if theme in ['B', 'b','plain', 'Plain']:
            
            #prompts you to pick the rgba color of the background
            red = raw_input('Please enter the numeric red value you want your \
background to have: ')
            green = raw_input('Please enter the numeric green value you want \
your background to have: ')
            blue = raw_input('Please enter the numeric blue value you want your\
background to have: ')
            alpha = raw_input('Please enter the numeric alpha value you want \
your background to have: ')
            print('')
            print('')
            
            #save the color as RGBA 4-tuple
            color_choice = (int(red), int(green), int(blue), int(alpha))
            
            #adds the background with the users choices by running a function
            new_image = add_background_one_image(curr_image, color_choice, 
            color_choice, 'plain')
            
            # Save the altered image, suing PNG to retain transparency
            new_image_filename = os.path.join(new_directory, filename + 
            '_background.png')
            new_image.save(new_image_filename)
            
    #Enter a new working directory
    path = '../Project_Images/background_added'
    os.chdir(path)
    directory = os.getcwd()
    
    #Instructions
    print('''Now, you should pick the color and thickness you want the border 
to have. Remember to consider the size of your image and what size border will
work best with it''')
    print('') 
    
    # Create a new directory 'bordered'
    new_directory = os.path.join(directory, 'bordered')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  
  
    # Go through the images and save modified versions
    for n in range(len(image_list)):

        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
        
        #Prompts you to pick the border color values individually
        print('You are on', filename +  '.png')
        print('')
        
        red = raw_input('Please enter the numeric red value you want your \
border to have: ')
        green = raw_input('Please enter the numeric green value you want your \
border to have: ')
        blue = raw_input('Please enter the numeric blue value you want your \
border to have: ')
        alpha = raw_input('Please enter the numeric alpha value you want your \
border to have: ')
        print('')
        
        #Saves color as RGBA 4-tuple
        color_choice = (int(red), int(green), int(blue), int(alpha))
        
        #Prompts you to pick the border thickness/size
        border_thickness = int(raw_input('Please enter the integer value of \
the size you want your border to be: '))
        print('')
        
        #add borders to the images by calling a function
        new_image = make_border_one_image(curr_image, color_choice,
        border_thickness) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename 
        + '_bordered.png')
        new_image.save(new_image_filename)
    
    #Change working directory   
    path = '../background_added/bordered'
    os.chdir(path)
    directory = os.getcwd()
    
    # Create a new directory 'logo'
    new_directory = os.path.join(directory, 'logo')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  
    
    print('Now let\'s add a logo!')
    print('')
    
    for n in range(len(image_list)):

        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
        width, height = curr_image.size
        
        #Tells you what image you are currently manipulating
        print('You are on', filename +  '.png')
        print('')
        
        #prompts you to pick the size of the logo
        logo_size_prompt=raw_input('Please enter the intger value you want the \
size of the logo to be: ')
        print('')
        
        #prompts you to pick which corner to put the logo
        logo_placement=raw_input('Which corner would you like to add your logo \
(top-right; top-left; bottom-right; bottom-left): ')
        print('')
        
        #the size of the logo
        logo_size = int(logo_size_prompt)
        
        #Calls a function and uses arguments to paste in the top-right
        if logo_placement == 'top-right':
            new_image = add_logo_one_image(curr_image, logo_size, 
            (width - logo_size,0))
             # Save the altered image, suing PNG to retain transparency
            new_image_filename = os.path.join(new_directory, filename +
            '_logo.png')
            new_image.save(new_image_filename)

        #Calls a function and uses arguments to paste in the top-left            
        if logo_placement == 'top-left':
            new_image = add_logo_one_image(curr_image, logo_size,
            (0,0))
            new_image_filename = os.path.join(new_directory, filename +
            '_logo.png')
            new_image.save(new_image_filename)
        
        #Calls a function and uses arguments to paste in the bottom-right   
        if logo_placement == 'bottom-right':
            new_image = add_logo_one_image(curr_image, logo_size,
            (width - logo_size, height - logo_size))
            new_image_filename = os.path.join(new_directory, filename +
            '_logo.png')
            new_image.save(new_image_filename)
        
        #Calls a function and uses arguments to paste in the bottom-left    
        if logo_placement == 'bottom-left':
            new_image = add_logo_one_image(curr_image, logo_size,
            (0, height - logo_size))
            new_image_filename = os.path.join(new_directory, filename +
            '_logo.png')
            new_image.save(new_image_filename)
    
    print('All Done! Enjoy your new images!')
    
    #Return to Project_Images so the progam can run easily again   
    path = '../..'
    os.chdir(path)
    
################################################################################

image_manipulations()

################################################################################