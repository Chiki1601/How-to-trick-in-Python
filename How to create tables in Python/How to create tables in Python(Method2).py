from tabulate import tabulate


Heading = ["Name", "Age", "Occupation", "City"]

Data = [["Mansi", "21", "Computer Engineer", "Ahmedabad"], ["Mansi", "21", "Computer Engineer", "Ahmedabad"], [
    "Mansi", "21", "Computer Engineer", "Ahmedabad"], ["Mansi", "21", "Computer Engineer", "Ahmedabad"]]
print(tabulate(Data, headers=Heading,tablefmt="grid" ))
print("From tabulate")
