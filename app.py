from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)

# Конфигурация API Google Custom Search
API_KEY = 'AIzaSyDaE30UlvSu_pkRzUY_J2EWJmnoBY8UZZE'  # Вставь свой API ключ
CX_ID = '65020d36d904046cf'  # Вставь свой cx идентификатор


def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл data.json не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка в формате JSON")
        return []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/links')
def links():
    data = load_data()
    return render_template('links.html', links=data)


@app.route('/image')
def image():
    return render_template('image.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '').lower()

    # Запрос к Google Custom Search API
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX_ID}"
    response = requests.get(search_url)

    # Обработка ответа от API
    if response.status_code == 200:
        search_results = response.json().get('items', [])
        results = [{'title': item['title'], 'link': item['link']} for item in search_results]
    else:
        results = []

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
