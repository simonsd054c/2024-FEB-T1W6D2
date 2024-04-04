# Create email format using full name and string methods
# John Smith -> Dairy Farm
# john.smith@dairyfarm.com.au

full_name = input("enter your full name: ") # John Smith

company_name = input("enter your company name: ") # Dairy Farm

full_name_format = full_name.replace(" ", ".") # John.Smith

company_name_format = company_name.replace(" ", "") # DairyFarm

predicted_email = f"{full_name_format}@{company_name_format}.com.au".lower()

print(predicted_email)