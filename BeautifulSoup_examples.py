from bs4 import BeautifulSoup

html = "<a><table></table></a>"
res1 = BeautifulSoup(html, "html.parser")
# res2 = BeautifulSoup(html, "lxml")
# res3 = BeautifulSoup(html, "html5lib")

print(res1)
# print(res2)
# print(res3)
