import csv

def write_info(infolist):
    with open('Info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact no", "E-Mail ID"])
        
        writer.writerow(infolist)

if _name_ == '_main_':
    while True:
        Info = input("Enter student info (separated by spaces, e.g., Name Age ContactNo Email): ")
        print(Info)
  
        Info_list = Info.split(' ')
        print(str(Info_list))
  
        write_info(Info_list)
  
        condition_check = input("Enter Yes or No for another student: ")
        if condition_check.lower() != "yes":
            break
  
