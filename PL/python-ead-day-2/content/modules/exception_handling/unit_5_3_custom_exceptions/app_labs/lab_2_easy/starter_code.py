class SecurityError(Exception):
    """
    TODO:
    1. override __init__(self, user, resource).
    2. Construct msg "User X denied access to Y".
    3. Call super().__init__(msg).
    4. Store nested attributes self.user, self.resource.
    """
    pass

def access_resource(user, resource):
    """
    TODO:
    If user == "guest", raise SecurityError(user, resource).
    Else return "Access Granted".
    """
    # WRITE CODE HERE
    pass

def main():
    try:
        access_resource("guest", "admin_panel")
    except SecurityError as e:
        print(f"Log: User={e.user} Resource={e.resource}")

if __name__ == "__main__":
    main()
