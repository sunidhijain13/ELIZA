import re

# Define the pattern-response pairs
patterns = [
    # Case for "I'm/I am depressed/sad"
    (r'.*\b(I\'?m|I am)\b (depressed|sad).*', 
     lambda m: f'I AM SORRY TO HEAR YOU ARE {m.group(2).upper()}'),

    # Replace "my boyfriend made me"
    (r'\bmy boyfriend made me\b(.*)', r'YOUR BOYFRIEND MADE YOU\1'),

    # Replace "my" with "YOUR" 
    (r'\bmy\b', r'YOUR'),
    
    # Replace "me" with "YOU" 
    (r'\bme\b', r'YOU'),

    # Replace "I'm" or "I am" with "YOU ARE" 
    (r'\b(I\'?m|I am)\b', r'YOU ARE'),

    # Replace "I" with "YOU"
    (r'\bI\b', r'YOU'),

    # Full response triggered when "all" is detected in the sentence
    (r'.*\ball\b.*', r'IN WHAT WAY?'),

    # Full response triggered when "always" is detected in the sentence
    (r'.*\balways\b.*', r'CAN YOU THINK OF A SPECIFIC EXAMPLE?')
]

# Default response if no pattern matches
fallback_response = "I SEE. PLEASE TELL ME MORE."

def eliza_response(user_input):
    """
    Process the user's input and return an appropriate ELIZA-like response.
    """
    # Remove filler words
    user_input = re.sub(r'^(well|so|like|um|uh)\W+', '', user_input, flags=re.IGNORECASE)

    # Loop to pattern match
    for pattern, response in patterns:
        # Check if the input matches the current pattern
        if re.search(pattern, user_input, flags=re.IGNORECASE):
            # Return the response 
            return re.sub(pattern, response, user_input, flags=re.IGNORECASE).upper()
    
    # Return the fallback response 
    return fallback_response.upper()

# Main dialogue loop
while True:
    user_input = input("USER: ")
    
    # Exit loop if the user types 'quit'
    if user_input.lower() == 'quit':
        print("ELIZA: GOODBYE!".upper())
        break
    
    # ELIZA's response
    response = eliza_response(user_input)
    
    # Print ELIZA's response
    print(f"ELIZA: {response}")
