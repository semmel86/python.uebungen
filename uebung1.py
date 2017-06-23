'''
ALP2 - Uebung1
Created on 25.04.2017
@author: Sebastian Selmke
'''

'''
@note: 1 - weekday
'''

# control if a given Date (int,int,int) is a real Date,
# if so, returns true else false
def isDate(day,month,year):
    # first check Month between 0 and 12
    if(month<=12 or month>=0): 
        
        # define possible values for day depending on the specific month
        lengthOfMonthInDays=[31,28,31,30,31,31,30,31,30,31,30,31]
        # calculate if it is a leap year-> February days +1 
        # for performance, first check if month = February, if not the condition is not useful
        if(month==2 and year % 4 == 0 and not(year % 100 ==0 and year % 400!=0)):
            lengthOfMonthInDays[1]=29 #lang February
        # check if day into possible day range
        if(day>=1 and day <=lengthOfMonthInDays[month-1]):
            return True
    else:
        # date not valid
        return False

# returns the weekday as String if the given date is valid
def weekday(day,month,year):
    
    # check date
    if(isDate(day,month,year)):
        
        # calculate number of weekday
        
        y=year-(14-month)//12
        x=y+ (y//4) -(y//100) + (y//400)
        m= month + 12 *((14-month)//12) -2
        result2=(day+x+(31*m)//12)%7
        #print ("result2 :", result2)
        # convert weekday number to readable String 
        return getDayAsString(int(result2))
    else:
        return "The given Date is not valid"
    
# convert a given number(0-6) into a String representing a Weekday
# or Error Message if the number is out of range
def getDayAsString(day):
    if(day>=0 and day<=6):
        days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return days[day-1]
    else:
        return "An Error occured while formatting Integer to the Day, Number "+str(day)+" out of range"
    
#TESTs
#print(weekday(31,1,2017),"= Dienstag")
#print(weekday(14,7,1789),"= Dienstag")
#print(weekday(23,5,1949),"= Montag")
#print(weekday(18,1,1892),"= Montag")
#print(weekday(9,11,1989),"= Donnerstag")
#print(weekday(29,4,2017),"= Samstag")
#print(weekday(30,3,2017),"= Donnerstag")


'''
@note: 2 - Summenberechnung
'''
  
   
# return the result for the given function and number of iterations n, for negative n result=0
# if no function is given f(n)=n will be used
def getSum(n,function =lambda n:n):
    # initialize result as float
    result=0.0
    # iterate over n
    try:
         for i in range(n):
        # summerize current and previous results, except n=0 
       
            if(i!=0):
                result=result+function(i)
            #print("current result:",result,"for n:",i)
    except OverflowError:
        print("Overflow Error for n=",n," please type in smaller values for this function with n <",i)
        return # empty result, as it could not be calculated completely
    else:
        return result

fct1 = lambda n:n
fct2 = lambda n: 1.0/n
fct3 = lambda n: 1.0/n*n
fct4 = lambda n: 1.0/fac(n)

# factorial
def fac(n):
    result=1
    for i in range(n):
        #except n=0 
        if(i!=0):
            result=result*i
    return result
  
# TEST
#print ("fct1:",getSum(100,fct1))
#print ("fct2:",getSum(10000,fct1))
#print ("fct3:",getSum(100,fct2))
#print ("fct4:",getSum(100000,fct2))
#print ("fct5:",getSum(100,fct3))
#print ("fct6:",getSum(100000,fct3))
#print ("fct7:",getSum(20,fct4))
#print ("fct8:",getSum(1000,fct4))   #-> too large for float   
        
        


'''
@note: 3 - Product
'''
def product():
    # start with 1 (neutral element of multiplication)
    product=1;
    # stop the loop if product equals 0
    while product !=0:
        try:
            num=int(input("Type in an integer value:")) # read in next int
            # catch Errors and print Message 
        except NameError: # occurs for Strings
            print("You have to type in integer values!")
        except SyntaxError: # occurs for mixed int-char Strings
            print("You have to type in integer values!") 
        except ValueError:
            print("Invalid literal!")    
        else: # if no error occurs proceed
            if(num==0):
                print("Goodbye") 
                return # terminate   
            product*=num    # calculate and print product
            if(num>0):
                print("Product:",product)
       
# RUN TEST        
#product()