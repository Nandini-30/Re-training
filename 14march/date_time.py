import datetime


def check_age_difference(date1, date2):
    date_format = "%d.%m.%Y"
    birthdate = datetime.datetime.strptime(date1, date_format)
    joining_date = datetime.datetime.strptime(date2, date_format)
    age_diff = joining_date - birthdate
    min_age_diff = datetime.timedelta(days=365*18)
    
    if age_diff >= min_age_diff:
        print("Age difference is at least 18 years")
    
    else:
        print("Age difference is less than 18 years")
        
date1 = input("Enter birthdate in dd.mm.yyyy format: ")
date2 = input("Enter joining date in dd.mm.yyyy format: ")
check_age_difference(date1, date2)