#practice python code for coursera github intro

while True:
  balance=100000
  print("     ATM     ")
  print("""
  1)        Balance
  2)        Withdraw
  3)        Deposit
  4)        Quit
  """)
  
  try:
    Option=int(input("Enter Transaction Option: "))
  except Exception as e:
    print("Error:", e)
    print("Enter 1, 2, 3, or 4 only")
    continue
  if Option == 1:
    print("Balance $ ",balance)
  if Option == 2:
    print("Balance $ ",balance)
    Withdraw = float(input("Enter Withdraw Amount $ "))
    if Withdraw > 0:
      forwardbalance = (balance - Withdraw)
      print("Remaining Balance $ ", forwardbalance)
    elif Withdraw > balance:
      print("Insufficient Funds in Account")
    else:
      print("No Withdrawl Completed")
  if Option == 3:
    print("Balance $ ",balance)
    Deposit=float(input("Enter Deposit Amount $ "))
    if Deposit > 0:
      forwardbalance = (balance + Deposit)
      print("Remaining Balance $ ", forwardbalance)
    else:
      print("No Deposit Completed")
  if Option == 4:
   exit()
