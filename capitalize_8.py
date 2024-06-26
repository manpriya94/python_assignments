first_name = input("enter first name: ")
last_name = input("enter last name: ")
company_name = input("enter your company name : ")

first_chars = first_name[:2].lower()
last_chars = last_name[-3:].lower()

email_aliases = (first_chars + last_chars + "@" + company_name + ".com")

print("My email is : ", email_aliases)
