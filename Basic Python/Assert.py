assert "Selenium" in "Selenium web automation","Validation failed"
print("validation passed")

# assert "Selenium" in "zelenium web automation","Validation failed"
# print("validation passed")

str1 = "Python"
str2 = "Python"
assert str1==str2 ,"Validation 2 failed"
print("Validation 2 passed")

# str1 = "Python"
# str2 = "python"
# assert str1==str2 ,"Validation 2 failed"
# print("Validation 2 passed")

assert "Selenium" in ["Selenium","Java","Python"], "Validation 3 failed"
print("Validation 3 passed")

# assert "Selenium" in ["C","Java","Python"], "Validation 3 failed"
# print("Validation 3 passed")

import math
assert math.sqrt(4)==2 ,"Incorrect"
print("correct")