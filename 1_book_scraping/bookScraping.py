from bs4 import BeautifulSoup
import requests
import textwrap
import time
import os

os.makedirs('books', exist_ok=True)

def get_books(page):
    response = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.find_all('article', class_='product_pod')

    if not books:
        return False

    book_list = []

    for book in books:
        five_star = book.find('p', class_='star-rating Five')
        if five_star:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            price = price.replace('Â', '')
            book_info = textwrap.dedent(f"""\
                Book Name: {title}
                Book Price: {price}
                {'-' * 50}
            """)
            book_list.append(book_info)

    filename = f'books/5_star_books_page_{page}.txt'

    total_books = len(book_list)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Total Books: {total_books}\n{'-' * 50}\n\n")
        for list in book_list:
            f.write(list)
    print(f'File Saved: {filename}')
    return True

if __name__ == '__main__':
    page = 1
    while True:
        success = get_books(page)
        if not success:
            print("No more pages. Scraping complete.")
            break
        time_wait = 1
        print(f'Waiting for {time_wait} minute before next page...')
        time.sleep(time_wait * 60)
        page += 1
