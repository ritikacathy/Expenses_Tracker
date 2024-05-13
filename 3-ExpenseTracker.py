# an expense tracker using Lambda functions
# Lambda functions give you a concise way to write small, throwaway functions in your code.
def add_expenses(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
expenses = []
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses) # filters will apply the function (arg 1) on list (arg 2)
# the comparison is between the user input and the iterations in the categories, then returns the expenses of that category
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expenses(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break
if __name__ == '__main__':
    main()