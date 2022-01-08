# Loan Qualifier Application

The loan qualifier application is a command line interface application that efficiently matches up the borrower with the banks offering the loans meeting the borrower's profile and needs. It solves the issue of borrowers haphazardly submitting multiple loan applications to multiple banks and reduces the banks' loan application backlog by quickly identifying qualified borrowers. 


---

## Technologies

The loan qualifier application leverages Python 3.8+ and utilizes the following project dependencies:
- Fire
- Questionary
- Sys
- csv
- pathlib

---

## Installation Guide

The loan qualifer application is hosted on the following GitHub repository at: https://github.com/nguyenthuyt/loan_qualifier_app   

Before running the application, first install the following dependencies:

```python
pip install fire
pip install questionary
```



---

## Usage

Upon launching the loan qualifier application, you will be prompted with the following request to enter the location of bank data. Ensure the bank data file is formatted as a csv and enter the file path. 

```python
Enter a file path to a rate-sheet (.csv):
```

Next you will be prompted with a series of questions. Once a response has been inputted for each of the questions, the application will calculate and display the monthly debt to income ratio and loan to value ratio. Additionally, the application will return the number of qualifying loans found based on the responses provided. See below for example.

![Gitbash screen with loan qualifier application](images/LQapp.png)


---

## Contributors

The loan qualifier application was created as part of the Rice Fintech Bootcamp 2022 Program by:

Thuy Nguyen

Email: nguyen_thuyt@yahoo.com

LinkedIn: nguyenthuyt



---

## License

MIT
