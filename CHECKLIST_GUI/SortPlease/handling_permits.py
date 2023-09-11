
#will need to query Accela Database in order to get info of the permit
def query_Accela(permit_num) -> dict:
    
    ...

class Permit:
    def __init__(self,permit_num) -> None:
        self.record_num = permit_num

        self.data:dict = query_Accela(self.record_num)
        
        self.address:str = self.data["Summary"]["Site Address"]
        self.parcel:str = self.data["Summary"]["Parcel No"]

        self.status:str = self.data["Summary"]["Application Status"]
        self.application_name:str = self.data["Summary"]["Application Name"]
        self.description:str = self.data["Summary"]["Description of Work"]

        self.balance:float = self.data["Summary"]["Balance"]
        self.first_issued:str = self.data["Summary"]["First Issue Date"] or self.data["Custom1_Fields"]["First Issue Date"] #should be a date object
        self.expiration:str = self.data["Summary"]["Permit Expires"] or self.data["Custom1_Fields"]["Permit Expires"]
    
    def __str__(self) -> str:
        return self.record_num