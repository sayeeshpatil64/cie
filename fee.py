import sys

if len(sys.argv) != 5:
    print("Usage: python student_fees.py <name> <branch> <fees_paid> <balance>")
    sys.exit(1)

name = sys.argv[1]
branch = sys.argv[2]
fees_paid = float(sys.argv[3])
balance = float(sys.argv[4])

print("----- Student Fee Status Report -----")
print(f"Student Name : {name}")
print(f"Branch       : {branch}")
print(f"Fees Paid    : {fees_paid}")
print(f"Balance      : {balance}")

if balance == 0:
    print("Status       : All fees cleared ")
else:
    print("Status       : Pending fees ")

print("-------------------------------------")