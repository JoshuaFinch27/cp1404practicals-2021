"""
CP1404 Practical - Email to name dictionary
"""


def main():
    """Create and populate the dictionary emails_to_names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_split_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/N) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_split_name_from_email(email):
    """Get persons possible name from split email address"""
    # Looked up the actual names for the parts of an email address (username@domain_name)
    username = email.split("@")[0]
    username_parts = username.split(".")
    name = " ".join(username_parts).title()
    return name


main()
