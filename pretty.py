from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name","Age", "City"]
table.add_row(["A","12","CC"])
table.add_row(["A","12","CC"])
table.add_row(["A","12","CC"])

print(table)