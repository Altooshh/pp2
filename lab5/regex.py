import re

pattern1 = r"ab*"

pattern2= r"ab{2,3}"

pattern3= r"\b[a-z]+(?:_[a-z]+)*\b"

pattern4= r"\b[A-Z][a-z]*\b"

pattern5= r"a.*b"

pattern6= r"[ ,. ]"
def task6(text):
    return re.sub(pattern6, ":", text)

pattern7= r"_[a-z]"
def task7(text):
    return re.sub(pattern7, lambda match: match.group(0)[1].upper(),text)

pattern8= r"(?=[A-Z])"
def task8(text):
    return re.split(pattern8, text)

pattern9= r"([A-Z])"
def task9(text):
    return re.sub(pattern9, r' \1', text).strip()

pattern10 =r"([a-z])([A-Z])"
def task10(text):
    return re.sub(pattern10, lambda match: match.group(1) + "_"+ match.group(2).lower(),text)

print(re.findall(pattern1, "asdbbbabbabbbbababbbba"))  

print(re.findall(pattern2, "asdbbbabbabbbbababbbba"))  

print(re.findall(pattern3, "today i_have a worn_der_ful_ _day ah__yes"))  

print(re.findall(pattern4, "I believe we Are going to visit Astana with IoT Infrastracture"))  

print(re.findall(pattern5, "I believe we are going to visit Astana with IoT Infrastracture but we have some troubles"))  

print(task6("Hello, world. This is a Python program to replace spaces, commas, and dots."))  

print(re.findall(pattern7, "this_is_a_test_string"))  

print(task7("this_is_a_test_string"))  

print(task8("HelloWorldTest"))  

print(task9("HelloWorldTest"))  

print(task10("HelloWorldTest"))