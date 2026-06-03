def validate_time(time_string):
    """Validate if the given time string is in the format HH:MM and represents a valid time."""

    # Step 1: Check if the string contains the colon separator
    if ':' not in time_string:
        print("Invalid format: Time should be in HH:MM format.")
        return False
    
    # Step 2: Split the string into hours and minutes
    time_parts = time_string.split(":")

    # A valid time must have exactly two parts: hours and minutes
    if len(time_parts) != 2:
        print("Invalid format: Time should contain exactly one colon.")
        return False
    
    hours_string = time_parts[0]
    minutes_string = time_parts[1]

    # --- FIX START: Validate that both parts are exactly two digits long ---
    if len(hours_string) != 2 or len(minutes_string) != 2:
        print("Invalid format: Both hours and minutes should be exactly two digits.")
        return False
    # --- FIX END ---

    # Validate that both parts are numeric
    if not hours_string.isdigit() or not minutes_string.isdigit():
        print("Invalid format: Both hours and minutes should be numeric.")
        return False
    
    # Step 4: Convert string to integers (Casting)
    hours = int(hours_string)
    minutes = int(minutes_string)

    # Step 5: Check logical time boundaries
    if hours < 0 or hours > 23:
        print("Invalid time: Hours should be between 0 and 23.")
        return False

    if minutes < 0 or minutes > 59:
        print("Invalid time: Minutes should be between 0 and 59.")
        return False

    # If all checks passed, the time is valid
    return True

# --- Main Application Loop ---
def main():
    print("Time Validation Application")
    print("Type 'exit' to quit the application.\n")

    while True:
        # Get input from the user via terminal
        user_input = input("Enter a time (HH:MM): ").strip()

        # Check if the user want to close the application
        if user_input.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break

        # Run the validation function
        is_valid = validate_time(user_input)

        if is_valid:
            print(f"'{user_input}' is a valid time.\n")
        else:
            print("Please try again with a valid time format.\n")

            # This ensures the script runs only if executed directly, not when imported as a module
if __name__ == "__main__":
    main()