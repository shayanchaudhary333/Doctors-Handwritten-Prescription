#try:
 #   result = 10/0
#except ZeroDivisionError:
 #   print("Division by zero is not allowed.")

#try:
 #   value = int("123") 
  #  result = 10/0
#except:
 #   print("An error occured.")

##   value = int("abc")   
  #  result = 10/0
#except("ValueError,ZeroDivisionError ") :
 #   print("An error occured")
     
#try:
    #f1 = open("file4.txt","r")
    #content = f1.read()
    #print(content)
#except FileNotFoundError:
 #   print("File not found.")
#finally:
 #   if 'f' in locals():
  #   f1.close()        

#try:
 #  f = open("file4.txt","w")
  # f.write("asxdfcg")
   #f = open("file3.txt","r")
  # content = f.read()
   #print(content)
#except FileNotFoundError:
 #   print("file not found.")  
#finally:
 #   if 'f' in locals()   :
  #     f.close

customers = []
try:
    with open("customers.csv", "r") as file:
        for line in file:
            try:
                id, name, email = line.strip().split(",")
                customers.append({"id": id, "name": name, "email": email})
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
except FileNotFoundError:
    print("customers.csv not found.")
#EMPLOYEE RECORDS MANAGEMENT
try:
    with open("employees.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("Error: employees.txt file not found.")
except Exception as e:
    print(f"An error occurred: {e}")