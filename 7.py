import dominate
from dominate.tags import *

table_headers = ['Column 1', 'Another One', 'Ehmmmm']

def create_page():
    doc = dominate.document(title='Example Table')

    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(cls='container'):
            h1('Welcome to adams site!')
            a(href="https://www.google.com/")
            img(src="dita.jpg")
            button(onclick="document.location='https://www.google.com/'")
            with table(id='main', cls='table table-striped'):
                caption(h3('A table to show data'))
                with thead():
                    with tr():
                        for table_head in table_headers:
                            th(table_head)
                with tbody():
                    for i in range(10):
                        with tr():
                            td('click this')
                            td('Another one')
                            td('You played yourself')

    print(doc)


create_page()

#python 7.py >> test.html
# open index.html
