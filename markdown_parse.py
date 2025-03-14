import sys
import io
import re
import markdown # pip install markdown
from bs4 import BeautifulSoup # pip install beautifulsoup4
from numpy.core.defchararray import isnumeric


def md_to_text():
    with open('CHANGELOG.md', 'r', encoding='utf-8') as fileobj:
        text = fileobj.read()  # или читайте по строке
        # print(text)

    # for line in text.split('\n'):
    #     # if line.startswith('#'):
    #     #     print(line)
    #     # print(line[3:4])
    #     if line.startswith('#') and isnumeric(line[4:5]):
    #         print(line)

    # with open('CHANGELOG.md', 'r') as md:
    html = markdown.markdown(text)

    # markdown.markdownFromFile(input = 'CHANGELOG.md', output=)
    # html = sys.stdout
    # print(html)

    soup = BeautifulSoup(html, features="html.parser")
    print(soup)

    for prev_siblings in soup.find("h1", string=re.compile("Released")).find_previous_siblings():
        prev_siblings.decompose()
    print(soup)
    with open('CHANGELOG-2.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    # references = soup.find("h1", string=re.compile("Released"))
    # previous = references.fetchPreviousSiblings()
    # print(previous)

    # references.name = "h4"

    # print(references.contents)
    # references.contents.append("История релизов")
    # new_html = references.find_next_siblings()
    # print(new_html[1])

    # print(references.contents)
    # print(len(references))
    # print(references)
    # print(references.find_next_siblings())



def example():
    md = '**A** [B](http://example.com) <!-- C -->'
    text = md_to_text(md)
    print(text)
    # Output: A B

def main():
    md_to_text()

    # with open('CHANGELOG.md', 'r') as f:
    #     markdown_data = f.readline()
    # text = md_to_text(markdown_data)
    # print(text)

if __name__ == '__main__':
    main()
