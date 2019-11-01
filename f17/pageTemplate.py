#CSci 127 Teaching Staff
#October 2017
#A template for a program that produces customized html pages.
#Modified by:  ADD YOUR NAME HERE

def customizePage(name, color, imageName):
     """
     Takes as input a name, a color, and the name of an image,
     and returns a string customized with these values
     """
     
     templateString = '<html><head><title>Webpage of NAME</title></head><body style ="background-color:COLOR"><h1>NAME</h1><img src="IMAGE"> NAME</body></html>'

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(customizedString)

def main():
     n = input('Enter the name: ')
     mString = monthString(n)
     print('The month is', mString)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
