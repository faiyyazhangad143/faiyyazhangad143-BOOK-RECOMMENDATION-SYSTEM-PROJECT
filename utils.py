import numpy as np

def recommend_books(selected_book,model,books_name,final_rating,book_pivot):
    book_list = []
    book_id = np.where(book_pivot.index == selected_book)[0][0]
    distance , suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=9)
    
    poster_url = fetch_poster_url(suggestion,book_pivot,final_rating)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list , poster_url

def fetch_poster_url(suggestion,book_pivot,final_rating):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url
