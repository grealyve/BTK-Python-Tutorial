html_doc = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>


    <h1 id="header">
        Python Kursu
    </h1>

    <div class="gruop1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
        </ul>
    </div>

    <div class="gruop2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
        </ul>
    </div>

    <img src="cirilla.jpg" alt="">

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

# result = soup.prettify()    # düzeltilmiş bir şekilde gelicek.
# result = soup.title         # title kısmını çevirir
# result = soup.body          # body kısmını çevirir
# result = soup.head          # head kısmını çevirir.

# result = soup.title.name    # sadece etiket ismini verir
# result = soup.title.string  # title içindeki stringi çeker
# result = soup.h1            # ilk h1 i çeker
# result = soup.h2.name       # sadece etiket ismini verir

# result = soup.find_all("h2")  # bütün h2'leri çeker
# result = soup.find_all("h2")[1] # belirlediğin h2'yi çeker.

# result = soup.div   # ilk div'i çeker
# result = soup.find_all("div")   # bütün div'leri çeker
# result = soup.find_all("div")[1].ul.find_all("li")

# result = soup.div.findChildren()
#
# result = soup.div.findNextSibling()

# result = soup.find_all("a")       # linkleri çekme
# for i in result:
#     print(i.get("href"))
#
# print(result)