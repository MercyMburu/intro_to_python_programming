name="Mercy"
course="python"

print(f"My name is {name} and iam studying {course}")

with open(r"C:\Users\USER\Desktop\intro_to_programming\Week_2\quotes.txt","r") as file:
     content= file.readlines()
     print(content[0])
     
with open(r"C:\Users\USER\Desktop\intro_to_programming\Week_2\quotes.txt","a") as file:
     file.write("\nLife is for the living")
     
with open(r"C:\Users\USER\Desktop\intro_to_programming\Week_2\trial.txt","w") as file:
    file.write("Hello World")

     
     