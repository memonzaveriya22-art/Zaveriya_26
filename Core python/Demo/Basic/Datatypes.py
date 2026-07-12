### Numeric
## Numeric is not datatype it is categoery

#1. int
num = 20
print(type(num))

#2. float
num = 2.18
print(type(num))

#3.complex
num = 9 + 8j         #Real+Imaginary
print(type(num))


###Text

#1. str
var = 'firstbut solution'
var = "firstbit's solution"
var = '''firstbit solution.
firstbit solution.'''

###Sequential

#1. list
var = [10,20,30,40,50]
print(type(var))


#2. tuple
var = (10,20,30,40,50)
var = 10,20,30,40,50  #tuple
print(type(var))

#3. range
var =range(1,10000)
print(type(var))



###set type
#1. set
var = {10,20,30,40}
print(type(var))


#2. frozenset
var = frozenset({10,20,30,40,})
print(type(var))



###Mapping
#1. dictionary
var = {'id':101, 'name':'apurava', 'sal':30000}
print(type(var))



###Other
#!. boolean
var = True
print(type(var))



#2. Nonetypes
var = None
print(type(var))
