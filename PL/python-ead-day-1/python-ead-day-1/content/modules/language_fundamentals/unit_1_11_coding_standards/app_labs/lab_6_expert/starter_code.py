"""
Lab 6: The Pythonic Auditor - Starter Code

Security auditing system for login attempts.
"""

# TODO: Define constants, functions, and proper script structure
FORBIDDEN_USERNAMES = ["admin", "root", "guest", "superuser"]

def audit_logins(login_list):
    """
    Apply forbidden username checks to a list of attempts.
    
    Args:
        login_list (list): List of usernames to audit.
    
    Returns:
        list: Flagged accounts that match forbidden usernames.
    """
    # TODO: Implement Pythonic membership check
    flagged_accounts = []
    for name in login_list:
        if name in FORBIDDEN_USERNAMES:
            flagged_accounts.append(name)
    return flagged_accounts

if __name__ == "__main__":
    # TODO: Test logic here
    test_list = ["user1", "admin", "user2"]
    flagged = audit_logins(test_list)
    if not flagged:
        print("No forbidden accounts detected.")
    else:
        print(f"Flagged: {flagged}")
