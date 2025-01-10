# import os

# # Path to rockyou.txt
# rockyou_path = "C:/Users/Manas/Desktop/Winter Projects/Password_Strength_Checker/rockyou.txt"

# # Check if the file exists
# if os.path.exists(rockyou_path):
#     print("rockyou.txt found! Displaying first 5 lines:")
    
#     # Open and read the first 5 lines of the file
#     with open(rockyou_path, 'r', encoding='latin-1') as file:
#         for i, line in enumerate(file):
#             if i < 5:  # Limit to first 5 lines
#                 print(line.strip())  # Print the line without extra newline characters
#             else:
#                 break
# else:
#     print("rockyou.txt not found! Please check the path.")













import os

# Change the current working directory
os.chdir("C:/Users/Manas/Desktop/Winter Projects/Password_Strength_Checker")

# Now, you can check if the file exists in this directory
rockyou_path = "rockyou.txt"
if os.path.exists(rockyou_path):
    print("rockyou.txt found!")
else:
    print("rockyou.txt not found!")
