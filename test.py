# # # import pandas as pd
# # # import statsmodels.api as sm

# # # # Load dataset (Replace 'data.csv' with your actual file path)
# # # data = pd.read_csv('HW3_Data.csv')

# # # # Define the dependent variable (Income)
# # # Y = data['INCOME']

# # # # Model 1: Income = β0 + β1 * MF_DUMMY + ε
# # # X1 = sm.add_constant(data['MF_DUMMY'])
# # # model1 = sm.OLS(Y, X1).fit()
# # # print(model1.summary())

# # # # Model 2: Income = β0 + β1 * MF_DUMMY + β2 * Years_Experience + ε
# # # X2 = sm.add_constant(data[['MF_DUMMY', 'Years_Experience']])
# # # model2 = sm.OLS(Y, X2).fit()
# # # print(model2.summary())

# # # # Model 3: Income = β0 + β1 * MF_DUMMY + β2 * Years_Experience + β3 * (Years_Experience * MF_DUMMY) + ε
# # # data['Interaction'] = data['Years_Experience'] * data['MF_DUMMY']
# # # X3 = sm.add_constant(data[['MF_DUMMY', 'Years_Experience', 'Interaction']])
# # # model3 = sm.OLS(Y, X3).fit()
# # # print(model3.summary())

# # # # Model 4: Income = β0 + β1 * MF_DUMMY + β2 * Years_Experience + β3 * (Years_Experience * MF_DUMMY) + β4 * (Years_Experience^2) + ε
# # # data['Years_Exp_Squared'] = data['Years_Experience'] ** 2
# # # X4 = sm.add_constant(data[['MF_DUMMY', 'Years_Experience', 'Interaction', 'Years_Exp_Squared']])
# # # model4 = sm.OLS(Y, X4).fit()
# # # print(model4.summary())

# # # # Arbitrary
# # # X5 = sm.add_constant(data[['Years_Experience','Interaction']])
# # # model5 = sm.OLS(Y,X5).fit()
# # # print(model5.summary())

# # import numpy as np
# # import matplotlib.pyplot as plt
# # from sklearn.linear_model import LinearRegression

# # # Generate sample data (house size in square feet vs. price)
# # X = np.array([600, 800, 1000, 1200, 1400, 1600, 1800]).reshape(-1, 1)  # Square footage
# # y = np.array([150000, 180000, 210000, 240000, 270000, 300000, 330000])  # House price

# # # Create and train the model
# # model = LinearRegression()
# # model.fit(X, y)

# # # Predict prices for new house sizes
# # X_test = np.array([900, 1500, 1700]).reshape(-1, 1)
# # y_pred = model.predict(X_test)

# # # Plot the results
# # plt.scatter(X, y, color='blue', label="Training Data")
# # plt.plot(X, model.predict(X), color='red', label="Regression Line")
# # plt.scatter(X_test, y_pred, color='green', marker='x', s=100, label="Predicted Prices")
# # plt.xlabel("Square Footage")
# # plt.ylabel("House Price")
# # plt.legend()
# # plt.show()

# def is_valid(board, row, col, num):
#     """Check if placing 'num' at board[row][col] is valid according to Sudoku rules."""
    
#     # Check row
#     if num in board[row]:
#         return False
    
#     # Check column
#     if num in board[:][col]:
#         return False

#     # Check 3x3 subgrid
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(start_row, start_row + 3):
#         for j in range(start_col, start_col + 3):
#             if board[i][j] == num:
#                 return False
    
#     return True

# def find_empty_cell(board):
#     """Find an empty cell in the Sudoku board (returns row, col)."""
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:  # Empty cell
#                 return i, j
#     return None  # No empty cells

# def solve_sudoku(board):
#     """Solve the Sudoku puzzle using Backtracking."""
#     empty = find_empty_cell(board)
#     if not empty:
#         return True  # No empty cells → Sudoku solved!
    
#     row, col = empty
    
#     for num in range(1, 10):  # Try numbers 1-9
#         if is_valid(board, row, col, num):
#             board[row][col] = num  # Place number
            
#             if solve_sudoku(board):  # Recursively solve the next cell
#                 return True
            
#             board[row][col] = 0  # Undo placement (backtrack)
    
#     return False  # No solution found

# def print_board(board):
#     """Print the Sudoku board in a readable format."""
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - -")
#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")
#             print(board[i][j], end=" ")
#         print()

# # Example Sudoku puzzle (0 represents empty cells)
# sudoku_board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# print("Original Sudoku Puzzle:")
# print_board(sudoku_board)

# if solve_sudoku(sudoku_board):
#     print("\nSolved Sudoku:")
#     print_board(sudoku_board)
# else:
#     print("\nNo solution exists.")
print(int("a"))