def studentscheckoutbooks(id,ISBN):
    with open("book1.txt", "r+", encoding="utf-8") as file1:
        with open("students1.txt", "r+", encoding="utf-8") as file2:
            liste1 = file1.readlines()
            liste2 = file2.readlines()
            for i in liste1:
                result1 = i.split(',')
                if result1[0] == ISBN:
                    for j in liste2:
                        result2 = j.split("/")
                        if result2[0] == id:
                            file2.write("\n" + i)


while True:
    islem = input("\n1- List all boooks.\n2- List checked out books.\n3- Add a new book.\n4- Search book by ISBN number.\n5- Search a book by name.\n6- Checking out a book.\n7- List all students.\n8- List top 3 books.\n9- List top 3 students.\n10- Exit.\n")

    if islem == "1":
        id = input("Lütfen öğrenci numaranızı giriniz: ")
        ISBN = input("Lütfen kiralamak istediğiniz kitabın ISBN numarasını giriniz: ")
        studentscheckoutbooks(id, ISBN)
    else:
        break