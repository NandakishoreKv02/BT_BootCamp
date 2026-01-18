"""
Lab 4: Secure Access Validator - Starter Code
"""

def is_access_authorized(user_obj, user_role):
    """
    Check if a user is authorized to access patient records.
    
    Args:
        user_obj: The user object (can be None).
        user_role (str): The role string for the user.
        
    Returns:
        bool: True if authorized, False otherwise.
    """
    APPROVED_ROLES = ["Doctor", "Nurse", "Admin"]
    
    # TODO: Implement identity check (for user_obj) 
    # and membership check (for user_role)
    return user_obj is not None and user_role in APPROVED_ROLES

if __name__ == "__main__":
    # Mock user object
    class User: pass
    current_user = User()
    
    print(f"Authorized (Doctor): {is_access_authorized(current_user, 'Doctor')}")
    print(f"Authorized (Guest): {is_access_authorized(current_user, 'Guest')}")
    print(f"Authorized (No User): {is_access_authorized(None, 'Doctor')}")
