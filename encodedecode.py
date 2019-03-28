string1 = 'message'.encode('utf16')   #also utf32 & utf8 are available. utf8 is not much of use.
print(string1)
string1 = string1.decode('utf16')
print(string1)

