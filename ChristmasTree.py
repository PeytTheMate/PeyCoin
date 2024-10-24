
#      *      
#     ***     
#    *****    
#   *******   
#  *********  
# *********** 
#*************


def ChristmasTree(height):
    stars = 1
    maxColumns = height * 2 - 1
    for row in range(height):
        spaces = (maxColumns - stars) // 2
        print(spaces * " " + stars * "*" + spaces * " ")
        stars += 2



ChristmasTree(7)