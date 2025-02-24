import requests
url = "https://zenquotes.io/api/random"
try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        quote = data[0].get("q", "Цитата не знайдена.")
        author = data[0].get("a", "Невідомий автор")
        print(f'"{quote}" - {author}')
        with open("quote.txt", "w", encoding="utf-8") as file:
            file.write(f'"{quote}" - {author}')
    else:
        print("Не вдалося отримати цитату.")
except requests.exceptions.RequestException as e:
    print("Помилка підключення:", e)



