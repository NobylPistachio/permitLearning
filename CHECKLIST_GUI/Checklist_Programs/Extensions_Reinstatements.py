
#this is to help follow along for a more on hands approach for reinstating/extensions

import datetime

def leave_alone():
    print("They need to pay the fees first")

def clone():
    print("You might need to clone this permit")

def reinstate():
    print("You are going to need to reinstate")

def extend():
    print("They still have time to Extend")

def handle_permit_expiration(permit) -> bool:
    """
    Check the Balance, Issue Date, and Expiration Date of the Permit
    """
    balance:float = permit.balance
    issue_date:int = permit.first_issue_date #should use a date object really
    expiration_date:int = permit.permit_expires #should use a date object

    today = datetime.date.today()

    if balance > 0:
        leave_alone()
        return False
    if issue_date < 2020:
        clone()
    if (expiration_date+10) >= today:
        extend()
        return True
    else:
        reinstate()
        return True