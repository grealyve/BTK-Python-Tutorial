import mod

result = help(mod)
result = help(mod.func)
result = mod.numbers
result = mod.person["name"]
result = mod.func(10)
p = mod.Person()

p.speak()

print(result)
import sys
print(sys.path)