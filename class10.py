msg = "welcome to Python 101: Strings"
# new_string = (
#     msg[20] + " " +      # 1
#     msg[:7] + " " +      # Welcome
#     msg[25:29] + " " +   # Ring
#     msg[8:10] + " " +    # to
#     msg[13] + msg[12] + msg[2] + msg[1] + msg[25]  # Tyler
# )
new_string = f"{msg[20]} {msg[:7]} {msg[25:29]} {msg[8:10]} {msg[13]}{msg[12]}{msg[2]}{msg[1]}{msg[25]}"
print(new_string.title())

print(new_string[::-1].title())