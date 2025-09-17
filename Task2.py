user_input= input("Enter text to write to the file:")
with open("output.txt","w") as file:
    file.write(f"{user_input}\n")
    file.close()
    print('\n')
print("Data successfully written to output.txt.")
user_input1=input("Enter additional teext to append:")
with open("output.txt",'a') as file:
     file.write(f"{user_input1}\n")
     file.close()
print("Data successfully appended.\n")

print("Final content of output.txt:")
with open("output.txt","r") as file:
    file_read=file.read()
    print(file_read)

     
