
# row=int(input("請輸入行數"))
# for i in range(row):
#     for j in range(i + 1):
#         print(" "*row-i-1+'*'*j, end='')
#     print()


row=int(input("請輸入行數:"))

# for i in range(row):
#     print("*"*(int(i)+1))
# *
# **
# ***
# ****
# *****

# for i in range(row,0,-1):
#     print(" "*(i)+"*"*((row-i)*2+1))
#      *
#     ***
#    *****
#   *******
#  *********

# for i in range(row,0,-1):
#     print(" "*(i)+"*"*(row-i+1))
#      *
#     **
#    ***
#   ****
#  *****

# for i in range(row,0,-1):
#     print("*"*i)
# *****
# ****
# ***
# **
# *

# for i in range(row):
#     print(" "*i+"*"*(row-i))
# *****
#  ****
#   ***
#    **
#     *

# for i in range(row,0,-1):
#     print(" "*i+"*"*((row-i)*2+1))
# for i in range(row+1):
#     print(" "*i+"*"*((row-i)*2+1))
#經簡化後 變成下方的程式

# for i in range(row,-row-1,-1):
#     print(" "*abs(i)+"*"*((row-abs(i))*2+1))
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

# for i in range(row):
#     print(" "*i+"* "*row)
# * * * * * 
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *

# for i in range(row,0,-1):
#     print(" "*i+"* "*row)
#      * * * * * 
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *

# for i in range(row-2+1):
#     print(" "*i+"*"*(row-i)*2)

for i in range(row-1,0,-1):
    print(" "*i+"*"*(row-i)*2)
# **********
#  ********
#   ******
#    ****

