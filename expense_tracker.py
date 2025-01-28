
import random 
from datetime import datetime, timedelta

# function to generate data to uplaod 
def generate_random_data(length=20): 

    generated_data = []

    #dictionary of possible categories and descriptions to generate 
    descriptions = {
    "Housing": ["Paid rent for January", "Electricity bill", "Internet service", "Water bill"],
    "Transportation": ["Filled gas tank", "Monthly bus pass", "Car repair", "Uber ride"],
    "Food": ["Grocery shopping", "Dinner at a restaurant", "Coffee and bagel", "Fast food drive-thru"],
    "Health": ["Doctor's appointment", "Monthly gym membership", "Prescription refill", "Therapy session"],
    "Personal Care": ["Haircut", "Bought skincare products", "Manicure appointment", "Toothpaste and shampoo"],
    "Entertainment": ["Netflix subscription", "Concert tickets", "Bought a video game", "Movie night"],
    "Savings": ["Transferred to emergency fund", "Invested in stocks", "Contributed to retirement fund"],
    "Debt": ["Credit card payment", "Student loan installment", "Car loan repayment"],
    "Insurance": ["Paid health insurance premium", "Car insurance renewal", "Life insurance payment"],
    "Education": ["Bought textbooks", "Online course subscription", "Paid tuition fees"],
    "Gifts & Donations": ["Charity donation", "Birthday gift for a friend", "Christmas present"],
    "Shopping": ["Bought new clothes", "Purchased a laptop", "Ordered new shoes"],
    "Travel": ["Booked a flight ticket", "Hotel stay payment", "Rented a car", "Bought travel insurance"],
    "Work Expenses": ["Office supplies", "Work conference fee", "Client lunch"],
    "Miscellaneous": ["Unexpected expense", "Bought a gift card", "Random Amazon purchase"]
}
    for i in range(length):
        data_point = {}
        #generate a random data within the past year.
        random_date = (datetime.now() - timedelta(days=random.randint(0,365))).date()
        data_point['Date'] = f"{random_date.month}/{random_date.day}/{str(random_date.year)[-2:]}"


        #generate a random category 
        random_catgory = random.choice(list(descriptions.keys()))
        data_point['Category'] = random_catgory

        #generate random cost 
        cost = round(random.uniform(0, 5000),2)
        data_point['Cost'] = cost
        
        #generate a random description from the chosen category
        random_description = random.choice(descriptions[random_catgory])
        data_point['Description'] = random_description

        generated_data.append(data_point)
    return generated_data

random_data = generate_random_data(1000)
#print(random_data)


# manually add an expense to any list of data inputted a parameter
def add_expense(date,category, cost, description, expense_list):
    expense = {
        'Date': date,
        'Category': category,
        'Cost': cost,
        'Description': description  
    }
    expense_list.append(expense)
    return expense_list
# caclculate the total of the expenses in the data set
get_total_expense = lambda expenses: sum(expense['cost'] for expense in expenses)


#get expense total based on the selected category 
get_total_expense_for_catagory = lambda expenses, catagory: sum(expense['Cost'] for expense in expenses if expense['Category'] == catagory)

def get_expenses(expenses):
    if not expenses: 
     return  "there is no data available"
    else:
     for expense in expenses:
       print(f"{expense['Date']} - {expense['Description']} - ${expense['Cost']} - {expense['Category']}\n")

print(get_expenses(random_data))





    









