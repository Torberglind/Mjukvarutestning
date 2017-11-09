def extract_author(author):

    if ',' in author:
        new_auth = author.split(',')
        return new_auth[0], new_auth[1].strip(' ')

    new_auth = author.split(' ')
    if len(new_auth) == 1:
        return new_auth[0], ''
    if len(new_auth) == 2:
        return new_auth[1], new_auth[0]
    return new_auth[2], " ".join([new_auth[0], new_auth[1]])


def extract_authors(authors):
    new_authors = authors.split(' and ')
    for i in range(len(new_authors)):
        new_authors[i] = new_authors[i].split(', ')
    return [(new_authors[0][0],new_authors[0][1]), (new_authors[1][0], new_authors[1][1])]