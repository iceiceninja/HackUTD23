import csv

class Applicant:
    def __init__(self,ID,gross,cCard,car,student,value,down,loan,mortgage,cScore):
        self.ID = ID
        self.gross = gross
        self.cCard = cCard
        self.car = car
        self.student = student
        self.value = value
        self.down = down
        self.loan = loan
        self.mortgage = mortgage
        self.cScore = cScore
class LTV:  #have to be able to make a down payment that is at least 20% of the total mortgage they are trying to do
    #LTV = 
    def __init__(self, applicant):
        appraisal = applicant.value
        down = applicant.down

class Eligibility: 
    def __init__(self,applicant):
        if(int(applicant.cScore) < 640):
            self.badCredit = True
        else:
            self.badCredit = False

        

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
            print("Card Payment: ", person.car)
            print("Student Loan Payments: ", person.student)
            print("Appraised Value: ", person.value)
            print("Down Payment: ", person.down)
            print("Loan Amount: ", person.loan)
            print("Monthly Mortgage Payment: ", person.mortgage)
            print("Credit Score: ", person.cScore)
            
            if(Eligibility(person).badCredit == True):
                print("Declined for home purchase due to bad credit score")
            else:
                print("Credit score is acceptable")


            # if(int(person.cScore) < 640):
            #     print("Denied for home purchase due to bad credit score")
        i += 1

# Step 4: File is automatically closed when exiting the 'with' block
