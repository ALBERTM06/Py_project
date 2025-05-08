def reverse_string(s):
    if s == "":
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

input_string = "python"
reversed_str = reverse_string(input_string)
print(reversed_str)
#Expected output: nohtyp
