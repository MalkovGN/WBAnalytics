urls_list = []


def check_childs(data):
    if 'childs' in data.keys():
        data = data['childs']
        # print(data)
        return data
    else:
        urls_list.append(data['url'])


def unpack(data):
    for elem in data:
        if 'childs' in elem.keys():
            elem = elem['childs']
            print(elem)
        else:
            # print(elem)
            urls_list.append(elem['url'])


child_data = check_childs(data_json)
# print(child_data)
unpack(child_data)

for url in urls_list:
    print(url)