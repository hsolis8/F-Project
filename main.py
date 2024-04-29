import sqlite3
#import cli_flask unable to dowload (0.0.1) not supporting PEP 517 builds
import click #second option
$ pip install Flask
conn = sqlite3.connect('example1.db')
c = conn.cursor()



def main():
#start of the program with user id and pin num 
  
  print("Welcome!")

  user_id = input("Please enter your account number('0' otherwise): ")
  pin_num = input("Please enter your pin('0' otherwise:) ")

  display_options();
  user_choice(user_id, pin_num);
  


def display_options():
  print("1. Check balance ")
  print("2. Deposit funds")
  print("3. Withdraw funds")
  print("4. Create a new account")
  print("5. Delete an account")
  print("6. Modify account details")
  print("7. Exit services")


#Give the user the choice to pick an option 

def user_choice(user_id, pin_num):
  in_use = True
  user_choice = int(input("\nEnter the number of your choice: "))
  if user_choice == 1:
      account_balance()
      #add a in_use = False if we want the program to end after picking an option other than 4
  elif user_choice == 2:
      deposit_funds(user_id, pin_num)
  elif user_choice == 3:
      withdraw_funds(user_id, pin_num)
  elif user_choice == 4:
      create_account(conn,c, user_id,  pin_num, name, balance)
  elif user_choice == 5:
       delete_account(user_id, pin_num)
  elif user_choice == 6:
     modify_account(user_id, pin_num)
  elif user_choice == 7:
      print(f"Goodbye, {user_name}! have a great day!")
      in_use = False 
  else:
    print("Invalid selection. Please try again.")
  return in_use


#Option 1 to check the balance
def account_balance(user_id, pin_num):
  print("\nYou have selected account balance checks ")
  insert_statement = "SELECT Balance FROM bank_account WHERE Id == ? AND Pin == ?"
  c.execute(insert_statement, (user_id, pin_num))
  conn.commit()
  if c.rowcount > 0: 
    balance = c.fetchal()[0][0]
    print(f"your current balance is: {balance}")
  else: 
    print("No account found with the provided ID and Pin")
  
  


#Opion 2 deposit funds
def deposit_funds(user_id, pin_num):
  print("\nYou have selected Deposet funds ")
  amount = float(input("\nHow much will you deposit?\n"))
  balance = account_balance + amount
  statement = "UPDATE bank_account SET Balance = ? WHERE Id = ?"
  c.execute(statement, (balance, user_id))
  conn.commit()
              
  


#Option 3 withdraw funds
def withdraw_funds()user_id, pin_num:
  print("\nYou have selected Withdraw Funds.\n")
  amount = float(input("\nHow much will you withdraw?\n"))
  balance = account_balance - amount
  statement = "UPDATE bank_account SET Balance = ? WHERE Id = ?"
  c.execute(statement, (balance, user_id))
  conn.commit()
  
#create an account

def create_account(conn,c, id,  pin, name, balance):
  print("\nYou have selected Create Account.\n")
  statement = ("INSERT INTO bank_account(Pin, Name, Balance) VALUES (?, ?, ?)")
  c.execute(statement,(pin, name, balance))
  conn.commit()
  
#delete account

def delete_account():
  print("\nYou have selected Delete Account.\n")
  statement = "DELETE FROM bank_account WHERE id = ?"
  c.execute(statement, (user_id))
  conn.commit()
  print("\nYour account has been deleted\n")

#modify account 

def modify_account(user_id, pin_num):
  print("\nYou have selected Modify Account.\n")
  update = input("\nWhat would you like to update?")
  new_value = input("\nWhat would be the new value?")
  if update == 'pin':
    statement_one = "UPDATE bank_account SET Pin = ? WHERE ID = ?"
    c.execute(statement_one, (new_value, user_id))
    conn.commit()
  if update == 'name':
    statement_two = "UPDATE bank_account SET Name = ? WHERE ID = ?"
    c.execute(statement_two, (new_value, user_id))
    conn.commit()

  print("You have successfully updated your information!")
  
if __name__ == '__main__':
  main()

