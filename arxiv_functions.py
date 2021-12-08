"""CSC108/A08: Fall 2021 -- Assignment 3: arxiv.org

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Anya Tafliovich.

"""

import copy  # needed in examples of functions that modify input dict
from typing import Dict, List, TextIO

# remove unused constants from this import statement when you are
# finished your assignment
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS,
                       ABSTRACT, END, SEPARATOR, NameType,
                       ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_ARXIV2 = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_ARXIV3 = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya'), ('Pancer', 'Richard')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_ARXIV4 = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_ARXIV5 = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Tafliovich', 'Anya Y.')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Tafliovich', 'Anya Y.')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [('Tafliovich', 'Anya Y.')],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}
EXAMPLE_BY_AUTHOR2 = {
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067'],
    ('Bretscher', 'Anna'): ['827'],
    ('Ponce', 'Marcelo'): ['827']
}
EXAMPLE_BY_AUTHOR3 = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Breuss', 'Nataliya'): ['031', '042'],
    ('Pancer', 'Richard'): ['031', '067'],
    ('Bretscher', 'Anna'): ['067', '827']
}

EXAMPLE_CO = [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]
EXAMPLE_CO2 = [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]
EXAMPLE_CO3 = [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]

EXAMPLE_MOST_PUBLISHED = [('Bretscher', 'Anna'), ('Ponce', 'Marcelo'),
                          ('Tafliovich', 'Anya Y.')]
EXAMPLE_MOST_PUBLISHED2 = [('Tafliovich', 'Anya Y.')]
EXAMPLE_MOST_PUBLISHED3 = [('Bretscher', 'Anna'), ('Breuss', 'Nataliya'),
                           ('Pancer', 'Richard'), ('Ponce', 'Marcelo'),
                           ('Tafliovich', 'Anya Y.')]

COL = [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
COL2 = [('Pancer', 'Richard')]
COL3 = [('Pancer', 'Richard')]

# We provide this PARTIAL docstring to show the use of examples.
def make_author_to_articles(id_to_article: ArxivType) -> Dict[NameType,
                                                              List[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True
    >>> make_author_to_articles(EXAMPLE_ARXIV2) == EXAMPLE_BY_AUTHOR2
    True
    >>> make_author_to_articles(EXAMPLE_ARXIV3) == EXAMPLE_BY_AUTHOR3
    True

    """

    authors_to_articles = {}

    for ids in id_to_article:
        for authors in id_to_article[ids][AUTHORS]:
            if authors not in authors_to_articles:
                authors_to_articles[authors] = [id_to_article[ids][ID]]
            else:
                authors_to_articles[authors].append(id_to_article[ids][ID])

    for authors in authors_to_articles:
        authors_to_articles[authors].sort()

    return authors_to_articles

def get_coauthors(id_to_article: ArxivType,
                  author_name: NameType) -> List[NameType]:
    """Return a list of coauthors of the author specified by the second
    argument. Two people are coauthors if they are authors of the same article.
    The list should be sorted in lexicographic order.

    >>> get_coauthors(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.')) == EXAMPLE_CO
    True
    >>> get_coauthors(EXAMPLE_ARXIV2, ('Tafliovich', 'Anya Y.')) == EXAMPLE_CO2
    True
    >>> get_coauthors(EXAMPLE_ARXIV3, ('Tafliovich', 'Anya Y.')) == EXAMPLE_CO3
    True

    """

    coauthors = []

    for id1 in make_author_to_articles(id_to_article)[author_name]:
        for authors in make_author_to_articles(id_to_article):
            for id2 in make_author_to_articles(id_to_article)[authors]:
                if id1 == id2:
                    if authors not in coauthors and authors != author_name:
                        coauthors.append(authors)
    coauthors.sort()

    return coauthors

def get_most_published_authors(id_to_article: ArxivType) -> List[NameType]:
    """Return a list of authors who published the most articles. List only
    contains more than one author in case of a tie. The list should be sorted
    in lexicographic order.

    >>> get_most_published_authors(EXAMPLE_ARXIV) == EXAMPLE_MOST_PUBLISHED
    True
    >>> get_most_published_authors(EXAMPLE_ARXIV2) == EXAMPLE_MOST_PUBLISHED2
    True
    >>> get_most_published_authors(EXAMPLE_ARXIV3) == EXAMPLE_MOST_PUBLISHED3
    True

    """

    most_publisheds = []
    most_article = 0

    for authors in make_author_to_articles(id_to_article):
        if len(make_author_to_articles(id_to_article)[authors]) > most_article:
            most_article = len(make_author_to_articles(id_to_article)[authors])

    for authors in make_author_to_articles(id_to_article):
        if len(make_author_to_articles(id_to_article)[authors]) == most_article:
            most_publisheds.append(authors)
    most_publisheds.sort()

    return most_publisheds

def suggest_collaborators(id_to_article: ArxivType,
                          author_name: NameType) -> List[NameType]:
    """Return a list of authors with whom the author specified by the second
    argument is encouraged to collablerate. The list should be sorted in
    lexicographic order. The list of suggested collaborators should include all
    authors who are coauthors of this author's coauthors.

    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Pancer', 'Richard')) == COL
    True
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.')) == COL2
    True
    >>> suggest_collaborators(EXAMPLE_ARXIV3, ('Tafliovich', 'Anya Y.')) == COL3
    True

    """

    collaborators = []

    first_degree_coauthors = get_coauthors(id_to_article, author_name)

    for authors1 in first_degree_coauthors:
        for author2 in get_coauthors(id_to_article, authors1):
            if author2 not in first_degree_coauthors and author2 != author_name:
                collaborators.append(author2)
    collaborators.sort()

    return collaborators

def has_prolific_authors(article_dict: Dict[NameType, List[str]],
                         id_article: ArticleType,
                         lowest: int) -> bool:
    """Return True iff the article (second argument) has atleasat one author
    who is considered prolific. The first parameter is a dictionary that maps
    author name to a list of IDs of articles published by that author, the
    second parameter represents the information on a single article, and the
    third argument represents the minimum number of publications for an author
    to be considered prolific.

    >>> has_prolific_authors(make_author_to_articles(EXAMPLE_ARXIV), '008', 2)
    True
    >>> has_prolific_authors(make_author_to_articles(EXAMPLE_ARXIV), '031', 2)
    False
    >>> has_prolific_authors(make_author_to_articles(EXAMPLE_ARXIV2), '008', 2)
    True
    """

    for authors in article_dict:
        for articles in article_dict[authors]:
            if articles == id_article and len(article_dict[authors]) >= lowest:
                return True
    return False

# We provide this PARTIAL docstring to show use of copy.deepcopy.
def keep_prolific_authors(id_to_article: ArxivType,
                          lowest: int) -> None:
    """Update id_to_article so that it contains only articles published by
    authors with min_publications or more articles published. As long
    as at least one of the authors has min_publications, the article
    is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    """

    authors_to_articles = make_author_to_articles(id_to_article)
    non_prolific_articles = []

    for authors in authors_to_articles:
        for articles in authors_to_articles[authors]:
            if not has_prolific_authors(authors_to_articles, articles, lowest):
                non_prolific_articles.append(articles)

    for articles in id_to_article:
        if id_to_article[articles][AUTHORS] == []:
            non_prolific_articles.append(articles)

    non_prolific_remover(id_to_article, non_prolific_articles)

def non_prolific_remover(id_to_article: ArxivType,
                         non_prolific_articles: List) -> None:
    """Remove all articles from id_to_article that are present in the
    non_prolific_articles list

    """

    for articles in non_prolific_articles:
        id_to_article.pop(articles)

# Note that we do not include example calls since the function works
# on an input file.
def read_arxiv_file(afile: TextIO) -> ArxivType:
    """Return a dict containing all arxiv information in afile.

    Precondition: afile is open for reading
                  afile is in the format described in the handout
    """

    arxiv_lines = afile.read().split('\n')

    arxiv_list = arxiv_list_creator(arxiv_lines)

    arxiv_dict = {}
    for i in range(len(arxiv_list)):
        arxiv_dict[arxiv_list[i][0]] = {ID: arxiv_list[i][0],
                                        TITLE: arxiv_list[i][1],
                                        CREATED: arxiv_list[i][2],
                                        MODIFIED: arxiv_list[i][3],
                                        AUTHORS: list_of_authors(arxiv_list, i),
                                        ABSTRACT: abstract_sum(arxiv_list, i)}

    for articles in arxiv_dict:
        arxiv_dict[articles][AUTHORS].sort()

    return arxiv_dict_none(arxiv_dict)

def arxiv_dict_none(arxiv_dict: List[list]) -> List[list]:
    """Return list with all values of "" replaced with None.

    """

    for articles in arxiv_dict:
        for keys in arxiv_dict[articles]:
            if arxiv_dict[articles][keys] == '':
                arxiv_dict[articles][keys] = None
    return arxiv_dict

def arxiv_list_creator(arxiv_lines: List) -> List[list]:
    """Return list with elements from first index to the index of 'END' at
    each occurance of 'END'.

    """

    arxiv_list = []
    temp_list = []
    for elements in arxiv_lines:
        if elements != END:
            temp_list.append(elements)
        else:
            arxiv_list.append(temp_list)
            temp_list = []

    return arxiv_list

def list_of_authors(arxiv_list: List[list], list_num: int) -> List:
    """Return list of authors as a tuple from given list and sublist number.

    """

    professors = []
    for i in range(4, arxiv_list[list_num].index("", 4)):
        professors.append(tuple(arxiv_list[list_num][i].split(SEPARATOR)))

    return professors

def abstract_sum(arxiv_list: List[list], list_num: int) -> str:
    """Return string consisting of all lines of abstract from given list and
    sublist number.

    """

    abstract = ""
    for i in range(arxiv_list[list_num].index("", 4) + 1,
                   len(arxiv_list[list_num])):
        abstract += arxiv_list[list_num][i] + '\n'

    return abstract[:-1]

if __name__ == '__main__':

    import doctest
    doctest.testmod()

    with open('example_data.txt') as example_data:
        example_arxiv = read_arxiv_file(example_data)
        print('Did we produce a correct dict? ',
              example_arxiv == EXAMPLE_ARXIV)

    # uncomment to work with a larger data set
    with open('data.txt') as data:
        arxiv = read_arxiv_file(data)

    author_to_articles = make_author_to_articles(arxiv)
    most_published = get_most_published_authors(arxiv)
    print(most_published)
    print(get_coauthors(arxiv, ('Varanasi', 'Mahesh K.')))  # one
    print(get_coauthors(arxiv, ('Chablat', 'Damien')))  # many
