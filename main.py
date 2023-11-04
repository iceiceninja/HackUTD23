from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv
#   uvicorn main:app --reload

app = FastAPI()

# Configure CORS settings
origins = [
    "http://127.0.0.1:3000",  # Replace with the actual address of your JavaScript code
    "http://localhost:3000",  # Add any other origins you want to allow
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    # Add any other origins you want to allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # You can specify specific HTTP methods (e.g., ["GET", "POST"])
    allow_methods=["GET", "POST"],
    allow_headers=["*"],  # You can specify specific headers
)
total = 0

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello():
    global total
    total += 1
    return {"message": str(total) + " hello"}

class LoanApplication(BaseModel):
    GrossMonthlyIncome: float
    CreditCardPayment: float
    CarPayment: float
    StudentLoanPayments: float
    AppraisedValue: float
    DownPayment: float
    LoanAmount: float
    MonthlyMortgagePayment: float
    CreditScore: int

@app.post("/loan-application")
async def submit_loan_application(data: LoanApplication):
    # Process the data here, for example, save it to a database or perform calculations.

    return {"message": "Loan application submitted successfully"}



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
    def isEligible(self):
        if(int(self.cScore) < 640):
            self.badCredit = True
        else:
            self.badCredit = False
        return self.badCredit

class LTV:  #have to be able to make a down payment that is at least 20% of the total mortgage they are trying to do
    def __init__(self, applicant):
        appraisal = applicant.value
        
# class Eligibility: 
#     def __init__(self,applicant):
#         if(int(applicant.cScore) < 640):
#             self.badCredit = True
#         else:
#             self.badCredit = False

@app.post("/upload")
async def file_upload(file: UploadFile):
    with open(file.filename, "r", newline='') as csv_file:
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
                
                if(person.isEligible() == True):
                    print("Declined for home purchase due to bad credit score")
                else:
                    print("Credit score is acceptable")


                # if(int(person.cScore) < 640):
                #     print("Denied for home purchase due to bad credit score")
            i += 1

# Step 4: File is automatically closed when exiting the 'with' block
    return {"message": "File uploaded successfully"}
