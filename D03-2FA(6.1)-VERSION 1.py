
from datetime import date

first_name = input("Enter first name: ").strip().title()
last_name = input("Enter last name: ").strip().title()
section = input("Enter section: ").strip().upper()
event_name = input("Enter event name: ").strip().title()

year = int(input("Enter event year: "))
month = int(input("Enter event month (1-12): "))
day = int(input("Enter event day: "))

full_name = first_name + " " + last_name
event_date = date(year, month, day)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_date.strftime("%B %d, %Y").replace(" 0", " "))
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")

