from ast import Try
from calendar import month
from datetime import date


def get_dob():
    # write code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))
	
	return date(year,month,day)
	
def get_age(dob):
    # write code here

	today = date.today()
	age = int(today.year - dob.year)

	return age

def main():
	# write code here
	
	dob = get_dob()
	if dob.year > date.today().year :
		print ("Invalid date of birth!")
	else:
		age = get_age(dob)
		print(f"You are {age} years old.")


if __name__ == '__main__':
    main()
