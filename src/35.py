def greet_user(name):
    """
    This function greets the user by name.
    
    Parameters:
    - name: The name of the user to greet.
    
    Returns:
    - A greeting message personalized for the given name.
    """
    return f"Hello, {name}! How are you today?"

# Example usage:
user_name = "Alice"
greeting = greet_user(user_name)
print(greeting)
