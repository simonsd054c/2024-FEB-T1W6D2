# Create email format using full name and string methods
# John Smith -> Dairy Farm
# john.smith@dairyfarm.com.au

full_name = input("enter your full name: ") # John Smith

company_name = input("enter your company name: ") # Dairy Farm

splitted_full_name = full_name.split() # ['John', 'Smith']
joined_full_name_with_dot = ".".join(splitted_full_name) # John.Smith

splitted_company_name = company_name.split() # ['Dairy', 'Farm']
joined_company_name_with_nothing = "".join(splitted_company_name) # DairyFarm

predicted_email = f"{joined_full_name_with_dot}@{joined_company_name_with_nothing}.com.au".lower()

print(predicted_email)