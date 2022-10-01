import re

# re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall()

# result = re.findall("Python", str)
# result = len(result)

# re.split()

# result = re.split(" ",str)

# re.sub()

# result = re.sub(" ", "-", str)
# result = re.sub("\s", "-", str)  # seçilen karakteri başka karakterle değiştirme

# re.search()

# result = re.search("Python", str)
# result = result.span()           # başlangıç ve bitiş indexlerini alırsın
# result = result.start()          # başlangıç indexi
# result = result.end()            # bitiş indexi
# result = result.group()            # bulduğu ifadeyi gönderir
# result = result.string              # hangi stringde arıyor onu yazar


# REGULAR EXPRESSION

"""

        [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.
        
            [abc] => a      : 1 match
                     ac     : 2 match
                     Python : No matches
                     
            [a-e] => [abcde]
            [1-5] => [12345]
            [0-39]=> [01239]  # Burada 9 sabit kalır 0123 döner
            
            [^abc] => abc dışındaki karakterler.
            [^0-9] => rakam olmayan karakterler.
            
"""

# result = re.findall("[sat]", str)
# result = re.findall("[a-e]", str)

"""
        . - Herhangi bir tek karakteri belirtir.
        
            .. => a     : No match
                  ab    : 1 match
                  abc   : 1 match
                  abcd  : 2 matches
                  
"""

# result = re.findall("...", str)     # Her üçlü karakteri ayırır.
# result = re.findall("Py..on", str)  # Python yazılarını geri çevirir.

"""
        ^ - Belirtilen karakterlerle başlıyor mu bütün string ifade?
        
        ^a => a:    1 match
              abc:  1 match
              bac:  No match

"""

# result = re.findall("^P", str)

"""
        $ - Belirtilen karakterle string ifade bitiyor mu?
        
            a$ => a     : 1 match
                  lamba : 1 match
                  Python: No match

"""

# result = re.findall("t$", str)
# result = re.findall("saat$", str)       # saat geri döner

"""
        a* - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
        
        
            ma*n => mn      : 1 match
                    man     : 1 match
                    maaan   : 1 match
                    main    : No match (a'nın arkasından n gelmiyor.)
                                
"""

# result = re.findall("sa*t", str)

"""
        a+ - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
        
            ma+n => mn      : No match
                    man     : 1 match
                    maaan   : 1 match
                    main    : No match (a'nın arkasına n gelmiyor.)

"""

# result = re.findall("sa+t", str)

"""
        ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
            
            ma?n => mn      : No match
                    man     : 1 match
                    maaan   : 1 match
                    main    : No match (a'nın arkasına n gelmiyor.)

"""

# result = re.findall("sa?t", str)

"""
        {} - Karakter sayısını kontrol eder.
        
            a1{2} => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
            a1{2,3}=>a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı.
            [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
            
"""

# result = re.findall("a{2}", str)
# result = re.findall("[0-9]{2}", str)

"""
        | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
            
            a|b => a ya da b
                
                cde =>      no match
                ade =>      1 match
                acdbea =>   3 match

"""

"""
        () - gruplandırmak için kullanılır.
        
            (a|b|c)xy => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

# result = re.findall("\APython", str)
# result = re.findall("saat\Z", str)

"""
        \ - Özel karakterleri aramamızı sağlar 
            \$a => $ karakterinin arkasına a karakterini arar. Yani $ regular exp. engine tarafından yorumlanmaz

        \A - Belirtilen karakter stringin başında mı?
            \Athe => the string in başında mı
        
        \Z - Belirtilen karakter stringin sonunda mı?
            the\Z => the string in sonunda mı
            
        \b - Belirtilen karakter kelimenin başında ya da sonunda mı?
            \bthe => the kelimenin başında mı?
            the\b => the kelimenin sonunda mı?
            
        \B - Belirtilen karakter kelimenin başında ya da sonunda değil mı?
            \Bthe => the kelimenin başında değil mı?
            the\B => the kelimenin sonunda değil mı?
        
        \d - [0-9] ile aynı anlama gelir yani rakamları arar.
            \d => 123abc34
            
        \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
            \D => 1ab44_50
            
        \s - Boşluk karakterlerini arar.
        \S - Boşluk karakterleri dışındakiler.
        \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
        \W - w nin tam tersi.


"""

print(result)