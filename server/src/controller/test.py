

def parseFile():
    # Open a file in read mode ('r')
    with open('data.txt', 'r') as file:
        # Read the entire content of the file into a string
        file_content = file.read()

    # Print or use the file content as needed
    return(file_content)

fileContent = parseFile()
fileContent = fileContent.split(";")
print(fileContent)
output = []
for bullet in fileContent:
    text = bullet.split("text:")[0].split("score:")[0]
    print(text)