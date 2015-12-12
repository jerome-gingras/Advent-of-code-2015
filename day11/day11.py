import re
illegal_letters = re.compile("[iol]")
double_char = re.compile(r"([a-z])\1")

def increment_string(string):
    lastchar = ord(string[-1]) + 1
    if (lastchar > 122):
        if len(string) == 1:
            print "Impossible"
            return ""
        return increment_string(string[:-1]) + "a"
    else:
        return string[:-1] + chr(lastchar)

def verify_string(string):
    global illegal_letters
    if len(illegal_letters.findall(string)) > 0:
        return False
    if len(set(double_char.findall(string))) < 2:
        return False
    if sum(map(lambda x, y, z: ord(z) == ord(y)+1 and ord(y) == ord(x)+1, string[:-2], string[1:-1], string[2:])) == 0:
        return False;
    return True
    
        
input = "hepxcrrq"        
temp = increment_string(input)
while not verify_string(temp):
    temp = increment_string(temp)
    if temp == "":
        print "Day 1: Impossible"
        break

print "Next password 1: " + temp
        
input = temp
temp = increment_string(input)
while not verify_string(temp):
    temp = increment_string(temp)
    if temp == "":
        print "Day 2: Impossible"
        break
        
print "Next password 2: " + temp