import re

html_doc = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()
# result = soup.title.parent
# result = soup.p.findChildren()

# for string in soup.stripped_strings:    # içerideki stringleri boşluksuz bu şekilde çekebilirsin.
#     print(repr(string))

# result = soup.a
# for parent in result.parents:
#     print(parent.name)

# result = soup.find_all(["a", "b"])       # listeleri şu şekilde çekebilirisin.

# for tag in soup.find_all(True):             # bütün tag' leri getirir.
#     print(tag.name)

# result = soup.find_all("p", "story")        # atanmış class' a göre tagleri çekme
# result = soup.find_all(id="link2")
# result = soup.find_all(string=re.compile("sisters"))  # bu string geçen satırı çekebilirsin.
# result = soup.find_all(id=True)
# result = soup.find_all("a", class_="sister")  # belirli classa sahip olanları çekme
# result = soup.find_all(string="Elsie")    # string var mı diye kontrol edebilirsin.

result = soup.get_text("|", strip=True)


print(result)