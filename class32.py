# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

phone_number = input('Enter a U.S. phone number: ').strip()

for ch in ["-","(",")","."]:
    phone_number = phone_number.replace(ch, " ")

cleaned_number = "".join(phone_number.split())

if len(cleaned_number) == 10 and cleaned_number.isdigit():
    formatted_number = (
        f"({cleaned_number[:3]}) "
        f"{cleaned_number[3:6]}-"
        f"{cleaned_number[6:]}"
    )
    print("Formatted number:", formatted_number)
else:
    print("Please enter exactly 10 digits.")