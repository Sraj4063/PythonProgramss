from Loan import Loan

def main():
    annualInterestRAte = eval(input("enter yearly interet rate, eg 7.25"))
    numberOfYears = eval(input("enter the no. of years"))
    loanAmount = eval(input("enter loan amount eg 100000.95"))
    borrower = input("enter the borrowers name")
    loan = Loan(annualInterestRAte,numberOfYears, loanAmount,borrower)

    #display loan date , monthly payment and total payment
    print("the loan is for",loan.getBorrower())
    print("the monthly payment is ",format(loan.getMonthlyPayment(),".2f"))
    print("the total payment is", format(loan.getTotalPayment(), ".2f"))
main()