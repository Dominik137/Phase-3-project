from sqlalchemy.orm import Session as SQLAlchemySession
from models import create_user, authenticate_user, get_user_subscriptions, create_subscription, Session

if __name__ == '__main__':
    exit_program = False
    authenticated_user = None

    while not exit_program:

            if not authenticated_user:
                first_prompt = input("""
Welcome:
1) Create Profile
2) Log in
3) Exit
""")
                
                if first_prompt == "1":
                    # Create a new profile
                    username = input("Create Username: ")
                    password = input('Create Password: ')
                    create_user(username, password)
                    print("User created successfully.")

                elif first_prompt == "2":
                    # Log in
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    authenticated_user = authenticate_user(username, password)

                    if not authenticated_user:
                        print("Login failed. Invalid username or password.")
                        
                elif first_prompt == "3":
                    # Exit program
                    print("Exiting program.")
                    exit_program = True
            else:
                second_prompt = input('''
1) See all Subscriptions
2) Add new Subscription
3) Logout
''')

                if second_prompt == "1":
                    # Show all subscriptions
                    subscriptions = get_user_subscriptions(authenticated_user)
                    if not subscriptions:
                        print("No subscriptions saved.")

                elif second_prompt == "2":
                    # Add new subscription
                    Service_Name = input("Enter Service name: ")
                    Cost = float(input("Enter cost: "))  # Assuming cost is a float field
                    Bill_date = int(input("Enter the day of the month you will be billed: "))
                    create_subscription(authenticated_user, Service_Name, Cost, Bill_date)

                elif second_prompt == "3":
                    # Logout
                    authenticated_user = None
                    print("Logged out successfully.")

                elif second_prompt == "4":
                    # Exit program
                    print("Exiting program.")
                    exit_program = True

                else:
                    print("Invalid choice. Please try again.")