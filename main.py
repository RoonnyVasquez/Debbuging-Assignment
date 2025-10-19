db = open("output.txt", "a")
a = "Hello" + str(1)  # Corrected line
b = "How do you do?"
db.write(a + ", " + b + "\n")
db.close()  # Added to ensure file is closed