#Data Structures
def main():
     my_dictionary = { 'Key':'Value',('K','E','Y'):5 }
     my_dictionary1 =  { x: x + 1 for x in range (10) }
     my_dictionary1[1] = 17
     print(my_dictionary1)
     del my_dictionary1[1]         ## del takes out the specific point in the dictionary so at this point, Dictionary key 1 does not Exist now
     print("After i took out key number 1, we have : ",my_dictionary1)
     '''
     print(my_dictionary)
    print(my_dictionary['Key'])
    print(my_dictionary1)
     '''
## when it comes to the numbering aspect you have to run a try and except method
## of doing things
     try:
          valueEntered = int(input("Enter your number:  "))    ## Very Important user must specify Type in this Case int or float would work
          print("Your number is ", my_dictionary1[valueEntered])
     except Exception as e:
          print("Fail Buddy, out of reach: ",e)
## to print only Keys and values
     print(my_dictionary.keys()) ## or in the first columns called keys
     print(my_dictionary.values())## or the secound after the columns called values

## 11.27.2016. --- We are at 1:35:15/ 2:39:58
         
main()
