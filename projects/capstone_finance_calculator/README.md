# Financial Calculator

This Python program is a financial calculator that allows users to calculate the amount of interest on their investment or the monthly bond repayment for a home loan.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)
- [Acknowledgements](#acknowledgements)


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CharuKes/finalCapstone.git
   ```
3. Install python
   go to: https://www.python.org/downloads/
   download and install

4. Open the terminal or command prompt and navigate to the project directory.
5. Run the following command to execute the program
    ```shell
    python financial_calculator.py
    ```

## Usage

When the program is executed, it will present the user with two options: 'investment' or 'bond'. The user can select the desired option by entering either 'investment' or 'bond' from the menu.

### Investment Calculation

If the user selects 'investment', they will be prompted to enter the following information:

1. Amount of deposit (positive integer or float)
2. Yearly rate of interest (positive integer or float)
3. Number of years for the investment (positive integer or float)
4. Type of interest calculation ('simple' or 'compound')

The program will calculate the investment amount based on the provided information and display the result.

### Bond Repayment Calculation

If the user selects 'bond', they will be prompted to enter the following information:

1. Present value of the house (positive integer or float)
2. Yearly interest rate (positive integer or float)
3. Number of months for the loan (positive integer or float)

The program will calculate the monthly bond repayment amount based on the provided information and display the result.

### Error Handling

The program includes error handling to ensure that the user enters valid input. If the user enters negative values or invalid input, they will be prompted to re-enter the correct information.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to create a pull request or submit an issue in the project repository.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

## Acknowledgements

This financial calculator was developed by [Charu Kesarwani](https://github.com/CharuKes) as a part of HyperionDev Capstone project 1.
