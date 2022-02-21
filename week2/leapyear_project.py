#week two project: this algorithm calssifies user inputs as leap or not leap years

#Input an year to check leap or not leap
user_input = input("Enter an year to check whether leap or not leap: ")


#check whether the input is a leap year or leap century
leap_year = int(user_input) % 4
leap_century = int(user_input) % 400
unleap_century = int(user_input) % 100


# if the year is divisible by 4 and its not a century year, then it is leap
if (leap_year == 0 and unleap_century != 0):
    print(user_input + " is a leap year")

#if its a century year and divisible by 400 then its also a leap year.
elif (leap_century == 0 and unleap_century == 0):
    print( user_input + " is a leap year")

else:
    print(user_input + " is not a leap year")