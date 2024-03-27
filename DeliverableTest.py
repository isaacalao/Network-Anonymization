import subprocess

response = 1

while response != 0:
  response = 3
  print("0. Exit\n1. run ifconfig\n2. option 2")

  try:
    response = int(input("input your choice: "))
  except:
    print("\nNot a valid input\n")

  # switch statement for user response
  if response == 0:
    print("Exiting...")

  if response == 1:
    subprocess.check_call(['ifconfig'])