from datetime import datetime

# Current year and month hard-coded
CURRENT_YEAR = 2024
CURRENT_MONTH = 6

def get_age(year, month, day):
    """Calculate age based on date of birth."""
    # Adjust year and month if the current month/day is before the birth month/day
    if CURRENT_MONTH < month or (CURRENT_MONTH == month and datetime.now().day < day):
        return CURRENT_YEAR - year - 1
    else:
        return CURRENT_YEAR - year

def can_retire(gender, date_of_birth):
    """Determine if a person can retire based on gender and age."""
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)
    
    if gender == 'm':
        return age >= 67
    elif gender == 'f':
        return age >= 62
    else:
        raise ValueError("Invalid gender input. Use 'm' for male or 'f' for female.")

def main():
    """Main function to interact with the user."""
    gender = input("Enter your gender ('m' for male, 'f' for female): ").strip().lower()
    date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ").strip()
    
    try:
        if can_retire(gender, date_of_birth):
            print("You can retire!")
        else:
            print("You cannot retire yet.")
    except ValueError as e:
        print(e)

# Run the main function
if __name__ == "__main__":
    main()
