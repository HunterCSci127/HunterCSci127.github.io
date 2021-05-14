# Uses a specified semester as a template to create files for a new specified semester
# Created By: Owen Kunhardt

import shutil
import sys
import replacer
    
print("Example Input Format: Fall 2020")
oldSemesterName = input("Enter Name of Template Semester: ")
newSemesterName = input("Enter Name of New Semester: ")

# Checks if input is valid
words = oldSemesterName.split()

if words[0] not in ["Fall", "Spring", "Summer"] or len(words[1]) != 4:
    print("Invaild input for template semester.")
    sys.exit()

words = newSemesterName.split()

if words[0] not in ["Fall", "Spring", "Summer"] or len(words[1]) != 4:
    print("Invaild input for new semester.")
    sys.exit()



# Changes semester names to match file path format
if oldSemesterName.find("Summer") > -1:
    oldName = "summer" + oldSemesterName[-2] + oldSemesterName[-1]

else:
    oldName = oldSemesterName[0].lower() + oldSemesterName[-2] + oldSemesterName[-1]

if newSemesterName.find("Summer") > -1:
    newName = "summer" + newSemesterName[-2] + newSemesterName[-1]

else:
    newName = newSemesterName[0].lower() + newSemesterName[-2] + newSemesterName[-1]

# Stores file paths in variables
oldNamePath = "../" + oldName
newNamePath = "../" + newName
oldHtml = "../" + oldName + ".html"
newHtml = "../" + newName + ".html"

# Copies template semester files
shutil.copytree(oldNamePath, newNamePath)
shutil.copy(oldHtml, newHtml)

# Changes semester in main file
replacer.replace(newHtml, oldSemesterName, newSemesterName)
replacer.replace(newHtml, oldName, newName)

# Changes semester in labs
# Assumes there are exactly 13 labs
for i in range(1,14):
    labFile = "../" + newName + "/lab" + str(i) + ".html"
    replacer.replace(labFile, oldSemesterName, newSemesterName)

# Changes semester in all other files
replacer.replace("../" + newName + "/ps.html", oldSemesterName, newSemesterName)
replacer.replace("../" + newName + "/psHC.html", oldSemesterName, newSemesterName)
replacer.replace("../" + newName + "/quizzes.html", oldSemesterName, newSemesterName)
replacer.replace("../" + newName + "/syl.html", oldSemesterName, newSemesterName)
replacer.replace("../" + newName + "/sylHC.html", oldSemesterName, newSemesterName)
replacer.replace("../" + newName + "/honors.html", oldSemesterName, newSemesterName)
replacer.replace("../" + newName + "/final/final.html", oldSemesterName, newSemesterName)

# Changes month assignment is due based in on whether new semester is fall or spring or summer
if newName[0] == 'f':
    replacer.replace("../" + newName + "/ps.html", "February", "September")
    replacer.replace("../" + newName + "/ps.html", "March", "October")
    replacer.replace("../" + newName + "/ps.html", "April", "November")
    replacer.replace("../" + newName + "/ps.html", "May", "December")

elif newName.find("summer") > -1:
    replacer.replace("../" + newName + "/ps.html", "February", "June")
    replacer.replace("../" + newName + "/ps.html", "March", "June")
    replacer.replace("../" + newName + "/ps.html", "April", "June")
    replacer.replace("../" + newName + "/ps.html", "May", "July")

else:
    replacer.replace("../" + newName + "/ps.html", "September", "February")
    replacer.replace("../" + newName + "/ps.html", "October", "March")
    replacer.replace("../" + newName + "/ps.html", "November", "April")
    replacer.replace("../" + newName + "/ps.html", "December", "May")

# Changes month lecture occurs based on whether new semester is fall or spring or summer
if newName[0] == 'f':
    replacer.replace(newHtml, "January", "August")
    replacer.replace(newHtml, "February", "September")
    replacer.replace(newHtml, "March", "October")
    replacer.replace(newHtml, "April", "November")
    replacer.replace(newHtml, "May", "December")

elif newName.find("summer") > -1:

    replacer.replace(newHtml, "January", "May")
    replacer.replace(newHtml, "February", "June")
    replacer.replace(newHtml, "March", "June")
    replacer.replace(newHtml, "April", "June")
    replacer.replace(newHtml, "May", "July")

else:
    replacer.replace(newHtml, "August", "January")
    replacer.replace(newHtml, "September", "February")
    replacer.replace(newHtml, "October", "March")
    replacer.replace(newHtml, "November", "April")
    replacer.replace(newHtml, "December", "May")


# Changes month quiz occurs based in on whether new semester is fall or spring or summer
if newName[0] == 'f':
    replacer.replace("../" + newName + "/quizzes.html", "February", "September")
    replacer.replace("../" + newName + "/quizzes.html", "March", "October")
    replacer.replace("../" + newName + "/quizzes.html", "April", "November")
    replacer.replace("../" + newName + "/quizzes.html", "May", "December")

elif newName.find("summer") > -1:

    replacer.replace("../" + newName + "/quizzes.html", "February", "June")
    replacer.replace("../" + newName + "/quizzes.html", "March", "June")
    replacer.replace("../" + newName + "/quizzes.html", "April", "June")
    replacer.replace("../" + newName + "/quizzes.html", "May", "July")

else:
    replacer.replace("../" + newName + "/quizzes.html", "September", "February")
    replacer.replace("../" + newName + "/quizzes.html", "October", "March")
    replacer.replace("../" + newName + "/quizzes.html", "November", "April")
    replacer.replace("../" + newName + "/quizzes.html", "December", "May")


