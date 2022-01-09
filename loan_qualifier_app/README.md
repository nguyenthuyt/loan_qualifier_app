# Loan Qualifier Application

The loan qualifier application is a command line interface application that efficiently matches up the borrower with the banks offering the loans meeting the borrower's profile and needs. It solves the issue of borrowers haphazardly submitting multiple loan applications to multiple banks and reduces the banks' loan application backlog by quickly identifying qualified borrowers. 


---

## Technologies

The loan qualifier application leverages Python 3.8+ and utilizes the following project dependencies:
* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs
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

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application, you will be prompted with the following request to enter the location of bank data. Ensure the bank data file is formatted as a csv and enter the file path. 

```python
Enter a file path to a rate-sheet (.csv):
```

Next you will be prompted with a series of questions. Once a response has been inputted for each of the questions, the application will calculate and display the monthly debt to income ratio and loan to value ratio. Additionally, the application will return the number of qualifying loans found based on the responses provided. See below for example.

![Gitbash screen with loan qualifier application](images/LQapp.png)

Once the results have been generated, the program will prompt the user with a choice to save the results or exit the application. If the user chooses yes, the user must enter a file path, file name and set the file as a CSV. See below for example.

![Gitbash screen requesting file output path](images/LQ_output_path.png)
---

## Contributors

The loan qualifier application was created as part of the Rice Fintech Bootcamp 2022 Program by:

Thuy Nguyen

Email: nguyen_thuyt@yahoo.com

LinkedIn: nguyenthuyt



---

## License

MIT
