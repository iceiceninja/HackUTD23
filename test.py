import csv

class Applicant:
    def __init__(self,ID,gross,cCard,car,student,value,down,loan,mortgage,cScore):
        self.ID = int(ID)
        self.gross = float(gross)
        self.cCard = float(cCard)
        self.car = float(car)
        self.student = float(student)
        self.value = float(value)
        self.down = float(down)
        self.loan = float(loan)
        self.mortgage = float(mortgage)
        self.cScore = float(cScore)

class LTV:  #have to be able to make a down payment that is at least 20% of the total mortgage they are trying to do
    #LTV = 
    def __init__(self, applicant):
        self.LTV = round((applicant.loan / applicant.value)*100, 2)

class DTI:
    def __init__(self, applicant):
        gross = applicant.gross
        creditCard = applicant.cCard
        carPayment = applicant.car
        studentLoan = applicant.student
        mortgage = applicant.mortgage

        self.overallDTI = round((creditCard + carPayment + studentLoan + mortgage) / gross * 100, 2)
        self.mortgageDTI = round(mortgage/(creditCard + carPayment + studentLoan), 2) 
class FEDTI:
    def __init__(self, applicant):
        self.FEDTI = round(applicant.mortgage/applicant.gross,2)

class Eligibility: 

# valueLTV == 1 means pass, 0 means fail
    def __init__(self,applicant):
        if(applicant.cScore < 640): 
            self.valueCredit = 0
        else:
            self.valueCredit = 1

# valueLTV == 1 means pass, 0 means fail, 2 means warning
        if(LTV(applicant).LTV > 80):    
            self.valueLTV = 1
        elif(LTV(applicant).LTV >= 80 & LTV(applicant).LTV <= 95):
            self.valueLTV = 2
        else:
            self.valueLTV = 0

# valueDTI == 1 means pass, 0 means fail, 2 means warning
        if(DTI(applicant).overallDTI > 43):
            self.valueDTI = 0
        elif(DTI(applicant).overallDTI < 43 & DTI(applicant).mortgageDTI > 36):
            self.valueDTI = 2
        elif(DTI(applicant).overallDTI < 36 & DTI(applicant).mortgageDTI > 28):
            self.valueDTI = 2
        elif(DTI(applicant).overallDTI < 36 & DTI(applicant).mortgageDTI < 28):
            self.valueDTI = 1

# valueFEDIT == 1 means pass, 0 means fail
        if(FEDTI(applicant).FEDTI <= 28):
            self.valueFEDTI = 1
        else:
            self.valueFEDTI = 0

            
        


        

# Step 1: Open the CSV file
file_path = "HackUTD-2023-HomeBuyerInfo.csv"  # Replace with your file path
with open(file_path, 'r', newline='') as csv_file:
    # Step 2: Create a CSV reader
    csv_reader = csv.reader(csv_file)

    i = 0
    # Step 3: Parse the content
    for row in csv_reader:
        # Process each row as needed
        if( i == 2 ):


            person = Applicant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]);

            line = row
            print("ID: ", person.ID)
            print("Gross Monthly Income: ", person.gross)
            print("Credit Card Payment: ", person.cCard)
            print("Car Payment: ", person.car)
            print("Student Loan Payments: ", person.student)
            print("Appraised Value: ", person.value)
            print("Down Payment: ", person.down)
            print("Loan Amount: ", person.loan)
            print("Monthly Mortgage Payment: ", person.mortgage)
            print("Credit Score: ", person.cScore)

            elegible = Eligibility(person)



                
            if(elegible.valueCredit == 0):
                print("Credit rating is below 640, which is too low")
            else:
                print("Credit rating is acceptable")

            if(elegible.valueLTV == 0):
                print("LTV is above 95%, which is too high")
            elif(elegible.valueLTV == 1):
                print("LTV is acceptable")
            else:
                print("LTV is between 80 and 95 percent, which means you will need to purchase Private Mortgage Insurance")

            if(elegible.valueDTI == 0):
                print("DTI is above 43%, which is too high")
            elif(elegible.valueDti == 1):
                print("DTI is acceptable")
            elif(elegible.valueDTI == 2):
                print("DTI warning")

            if(elegible.valueFEDTI == 0):
                print("FEDTI is greater than 28%, which is too high")
            else:
                print("FEDTI is acceptable")

            if(elegible.valueCredit == 1 & elegible.valueDTI == 1 & elegible.valueFEDTI == 1 & elegible.valueLTV == 1):
                print("Able to purchase a home")
            else: 
                print("Not able to purchase a home")


        i += 1

# Step 4: File is automatically closed when exiting the 'with' block
