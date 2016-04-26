import urllib.request
from bs4 import BeautifulSoup


def walk_in_hidden(url, list_readme):
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    links = soup.findAll('a')
    for link in links:
        link = link['href']
        if link[-1] != '/':
            readme = urllib.request.urlopen(url+link).read().decode()
            list_readme.append((url, readme))
        elif link != '../':
            walk_in_hidden(url+link, list_readme)

if __name__ == '__main__':
    list_readme = []
    url = 'http://192.168.229.128/.hidden/'
    walk_in_hidden(url, list_readme)
    print("Walking...")
    printed = []
    for readme in list_readme:
        if readme[1] not in printed:
            print(readme[0])
            print(readme[1])
            printed.append(readme[1])
