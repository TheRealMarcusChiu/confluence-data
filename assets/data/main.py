from bs4 import BeautifulSoup
import json


def parse(s):
    n = {
        'name': s.li.label.a.string,
        'href': s.li.label.a['href'],
        'children': []}

    lu_tags = s.li.findAll('ul', recursive=False)
    for lu_tag in lu_tags:
        n['children'].append(parse(lu_tag))

    if len(n['children']) == 0:
        n['value'] = 1

    return n


with open('confluence-data.xml', 'r') as file:
    data = file.read().replace('\n', '')
    soup = BeautifulSoup(data, 'html.parser')
    node = parse(soup)

    with open('confluence-data.json', 'w') as fp:
        json.dump(node, fp)