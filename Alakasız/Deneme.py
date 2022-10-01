def checkout():
    with open("book1.txt", "r+", encoding="utf-8") as file:
        with open("students1.txt", "r+", encoding="utf-8") as file2:
            liste = file.readlines()
            book = input("Enter the name of the book: ")
            liste2 = file2.readlines()
            studentNum = input("Enter student's number: ")
            file.seek(0)
            file2.seek(0)
            for i in liste:
                i = i.rstrip()
                a = i.split(",")
                if a[1] == book:
                    if a[3] == "F":
                        a[3] = "T"
                        a[4] = int(a[4])
                        a[4] += 1
                        a[4] = str(a[4])
                    else:
                        print("This book already checkouted.")
                        break
                a.insert(1, ",")
                a.insert(3, ",")
                a.insert(5, ",")
                a.insert(7, ",")
                file.writelines(a+["\n"])
            for b in liste2:
                if a[3] == "T":
                    break
                b = b.rstrip()
                x = b.split("/")
                if x[0] == studentNum:
                    x[2] = int(x[2])
                    x[2] += 1
                    x[2] = str(x[2])
                    x.append("\n"+book)
                x.insert(1, "/")
                x.insert(3, "/")
                file2.writelines(x+["\n"])

def top3books():
    with open("book1.txt", "r+", encoding="utf-8") as file:
        liste = file.readlines()
        books = []
        for i in liste:
            i = i.rstrip()
            books.append(i)
        books2 = []
        for a in books:
            a = a.split(",")
            a[4] = int(a[4])
            books2.append(a)
        a = (sorted(books2, key=lambda x: (x[4])))
        a.reverse()
        a[0] = a[0][0] + ","  + a[0][1]+ "," + a[0][2]+ "," + a[0][3]+ "," + str(a[0][4])
        a[1] = a[1][0] + "," + a[1][1] + "," + a[1][2] + "," + a[1][3] + "," + str(a[1][4])
        a[2] = a[2][0] + "," + a[2][1] + "," + a[2][2] + "," + a[2][3] + "," + str(a[2][4])
        print(f"{a[0]}\n{a[1]}\n{a[2]}")

def top3students():
    with open("students1.txt", "r+", encoding="utf-8") as file:
        liste = file.readlines()
        books = []
        for i in liste:
            i = i.rstrip()
            books.append(i)
        books2 = []
        for a in books:
            a = a.split("/")
            if len(a) == 3:
                if not a[2] == "":
                    a[2] = int(a[2])
                    books2.append(a)
        a = (sorted(books2, key=lambda x: (x[2])))
        a.reverse()
        a[0] = a[0][0] + "," + a[0][1] + "," + str(a[0][2])
        a[1] = a[1][0] + "," + a[1][1] + "," + str(a[1][2])
        a[2] = a[2][0] + "," + a[2][1] + "," + str(a[2][2])
        print(f"{a[0]}\n{a[1]}\n{a[2]}")
