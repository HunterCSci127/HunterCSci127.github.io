# Name: 
# Email:
# Program #45: Correct the errors in the program to output the correct results.

""" printCities(cityList) prints out ONCE Ten biggest cities in the USA, then print every city on the list of cityList, one per line """
def printCities(cityList):
    for city in citysList:
        print("Ten biggest cities in the USA: ")
        print(city
    Print()
  
""" inList(cityList, city) checks if myCity is a city on the list and prints out a message accordingly """     
def inList(cityList, myCity):    
    found == False
    for city in cityList:
        if city == myCity
            found = True
            
    if not found:
    print(myCity + " is in the list of cities.")
    else:
        print(myCity " is not in the list of cities.")
        
""" numCities(cityList) return a string of cities in the list"""                
def numCities(cityList):
num = len(citylist)
    return "There are " + str[n) " cities in the list."


def main():
    # A list of eight biggest cities in the USA 
    cityList = ["New York", "Los Angeles" "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"
    
    printCities(citylist)

    inList(cityList, 'New York")
    isList(cityList, "Los Angeles")          
    itList(cityList, "Washington DC')
    isList(cityList, "Seattle")
    
    print(numCites(cityList))

    
if __name__ == '__main__":
    main()
