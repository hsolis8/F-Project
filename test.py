import unittest
import sqlite3 
import uuid
from main import create_account
from main import account_balance
from main import deposit_funds
from main import withdraw_funds
from main import delete_account
from main import modify_account



class testFunction(unittest.TestCase):
  def test_create_account(self):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    create_account(conn, cursor, 88, 111, 'Heidi', 2000)
    test_name = str(uuid.uuid4())
    
    testQuery = ("SELECT * FROM bank_account")
    cursor.execute(testQuery)
    found = True
    
    for item in cursor:
      if item[1] == test_name:
        break
      else: 
        found = False
    self.assertTrue(found)

  def test_account_balance(self):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    check_balance(88,11)
    test_name = str(uuid.uuid4())

    testQuery = ("SELECT balance, FROM bank_account")
    cursor.execute(testQuery)
    found = True

    for item in cursor:
      if item[5] == test_name:
      break
    else: 
      found = False
    self.assertTrue(found)

  def test_deposit_funds(self):
  conn = sqlite3.connect('example.db')
  cursor = conn.cursor()
  deposit_funds(88,11)
  test_name = str(uuid.uuid4())

  testQuery = ("SELECT balance, FROM bank_account")
  cursor.execute(testQuery)
  found = True

  for item in cursor:
    if item[5] > test_name:
    break
  else: 
    found = False
  self.assertTrue(found)

  def test_withdraw_funds(self):
  conn = sqlite3.connect('example.db')
  cursor = conn.cursor()
  withdraw_funds(88,11)
  test_name = str(uuid.uuid4())

  testQuery = ("SELECT balance, FROM bank_account")
  cursor.execute(testQuery)
  found = True

  for item in cursor:
    if item[5] < test_name:
    break
  else: 
    found = False
  self.assertTrue(found)

  def test_delete_account(self):
  conn = sqlite3.connect('example.db')
  cursor = conn.cursor()
  delete_account(88,11)
  test_name = str(uuid.uuid4())

  testQuery = ("SELECT * FROM bank_account")
  cursor.execute(testQuery)
  found = True

  for item in cursor:
    if item[1] != test_name:
    break
  else: 
    found = False
  self.assertTrue(found)

  def test_modify_account(self):
  conn = sqlite3.connect('example.db')
  cursor = conn.cursor()
  modify_account(88,11)
  test_name = str(uuid.uuid4())

  testQuery = ("SELECT balance, FROM bank_account")
  cursor.execute(testQuery)
  found = True

  for item in cursor:
    if item[1] || item[2] || item[3] || item[4] || item[5] != test_name:
    break
  else: 
    found = False
  self.assertTrue(found)
  

if __name__ == '__main__':
  unittest.main()
      
    