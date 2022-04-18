libraryDictionary = dict({
    "lev tolstoi": ["Anna Karenina", "War and Peace"],
    "charles dickens": ["Great Expectations", "Oliver Twist", "A Tale of Two Cities"],
    "alexandre dumas": "The Count of Monte Cristo",
    "emily bronte": "Wuthering Heights"
})

command = ""

while(command != "exit"):
    command = input("Enter an author: ")
    books = libraryDictionary.get(command.lower())
    if books != None:
        print(books)
    else: 
        print("Author not found")
    