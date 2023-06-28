
#customer actions
def request_customer(*args) -> None:
    ...






def PCPAO(a):
    ...

def Check_Jurisdiction(address):
    municipal_subprocess = ["Safety Harbor","Bellair Bluffs",""]
    if PCPAO(address) == "Unincorporated" or PCPAO(address) in municipal_subprocess:
        return True
    else:
        return False

permit_statuses = ["Waiting for Applicant","Finaled","Closed","Administrative Close","Void","Issued"]

def check_for_duplicate_permits():
    #do at same time with checking for violations, and checking for open permits on Accela via the parcel number.(saves time)
    ...

def check_for_violations():
    #do at same time with check for duplicate permits, and checking for open permits on Accela via the parcel number.(saves time)
    ...

def check_for_open_permits():
    #do at same time with checking for violations, and check for duplicate permits on Accela via the parcel number.(saves time)
    ...

def check_sublist():
    ...

def check_licensed_professionals_attached():
    PPL_Pros: int = 0
    if PPL_Pros == 1:
        sublist = None
        return True
    #if there is more than 1 pro then we need sublist
    elif PPL_Pros > 1:
        sublist = check_sublist()
    # if 0 pros then we need sublist & CPF if there is more than one trade
    elif PPL_Pros == 0:
        sublist = check_sublist()
        if sublist == None:
            CPF = None #check for CPF
            request_customer(sublist,CPF)
    ...

def check_submitted_documents():
    ...

def check_NOC_requirement():
    ...

def verify_Standard_Description_and_use_established_naming_convention():
    ...

def deem_complete():
    #for safety purposes this will stay empty
    ...

def move_to_distribution():
    ...

def BR_RMR():
    Check_Jurisdiction("1569 S Prescott Ave")