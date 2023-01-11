class JsonParser:
    """
    Subcategories json parser class
    Getting unique subcategory_info
    """
    def __init__(self, data):
        self.data = data
        self.subcategory_info = []

    def start(self):
        if 'childs' in self.data.keys():
            self.unpack(self.data['childs'])
        else:
            if self.data['url'].startswith('/'):
                try:
                    self.subcategory_info.append(
                        {
                            'name': self.data['name'],
                            'url': 'https://www.wildberries.ru' + self.data['url'],
                            'shard': self.data['shard'],
                            'query': self.data['query'],
                        }
                    )
                except KeyError:
                    self.subcategory_info.append(
                        {
                            'name': self.data['name'],
                            'url': 'https://www.wildberries.ru' + self.data['url'],
                        }
                    )
            else:
                self.subcategory_info.append(
                    {
                        'name': self.data['name'],
                        'url':  self.data['url'],
                    }
                )

    def unpack(self, sub_category):
        for element in sub_category:
            if 'childs' in element.keys():
                element = element['childs']
                self.unpack(element)
            else:
                if element['url'].startswith('/'):
                    try:
                        self.subcategory_info.append(
                            {
                                'name': element['name'],
                                'url': 'https://www.wildberries.ru' + element['url'],
                                'shard': element['shard'],
                                'query': element['query'],
                            }
                        )
                    except KeyError:
                        self.subcategory_info.append(
                            {
                                'name': element['name'],
                                'url': 'https://www.wildberries.ru' + element['url'],
                            }
                        )
                else:
                    self.subcategory_info.append(
                        {
                            'name': element['name'],
                            'url': element['url'],
                        }
                    )
