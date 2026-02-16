#first question
# show me how can you handle a error?
try:
   file=open("sample.txt","rt")
   file.read()
except TypeError:
   print("TypeError")

#second question
# show how can you append a new written file?

data = input("Enter some text to write in the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written to output.txt")

append_data = input("Enter additional text to append in the file: ")

with open("output.txt", "a") as file:
    file.write(append_data + "\n")

print("Additional data appended to output.txt")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)



