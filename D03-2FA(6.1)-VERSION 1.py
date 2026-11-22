
first_name = input("Enter first name: ").strip().title()
last_name = input("Enter last name: ").strip().title()
section = input("Enter section: ").strip().upper()
event_name = input("Enter event name: ").strip().title()
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

full_name = first_name + " " + last_name

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Year:", year)
print("Event Month:", month)
print("Event Day:", day)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
