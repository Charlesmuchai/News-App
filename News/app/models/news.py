class News:
    '''
    News class to define News objects
    '''

    def __init__(self,author,title,description,url,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
