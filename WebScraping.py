
# import library that can fatch the whole website data
from urllib.request import urlopen

# variable that has assign the website link
my_Url = "https://www.olx.com.pk/property-for-sale_c2"
# make a object and by using the urllib open packger that open the file
#html = urlopen(my_Url)
html2 = urlopen("https://www.olx.com.pk/property-for-sale_c2")
# by using read() function we can read all material of the data
print(html2.read())
