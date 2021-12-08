import csv
phone = input("phonenum: ")
phone = phone.replace('0', '+84', 1)
with open('noname.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Phone'])
    writer.writerow([phone])
    f.close()