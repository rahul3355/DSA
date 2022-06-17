def bonAppetit(bill, k, b):
    # Write your code here
    total_anna = sum(bill) - bill[k]
    split = total_anna // 2
    anna_actual = b - split
    if anna_actual == 0:
        print("Bon Appetit")
    else:
        print(anna_actual)