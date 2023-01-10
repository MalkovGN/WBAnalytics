class JsonParser:
    """
    Subcategories json parser class
    Getting unique urls
    """
    def __init__(self, data):
        self.data = data
        self.urls = []

    def start(self):
        if 'childs' in self.data.keys():
            self.unpack(self.data['childs'])
        else:
            if self.data['url'].startswith('/'):
                self.urls.append('https://www.wildberries.ru' + self.data['url'])
            else:
                self.urls.append(self.data['url'])

    def unpack(self, sub_category):
        for element in sub_category:
            if 'childs' in element.keys():
                element = element['childs']
                self.unpack(element)
            else:
                if element['url'].startswith('/'):
                    self.urls.append('https://www.wildberries.ru' + element['url'])
                else:
                    self.urls.append(element['url'])
