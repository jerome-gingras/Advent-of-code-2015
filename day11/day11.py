import re
illegal_letters = re.compile("[iol]")

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
        return false
    
        
input = "hepxcrrq"        
temp = increment_string(input)
while(not verify_string(temp):
    temp = increment_string(temp)

print "Next password: " + temp