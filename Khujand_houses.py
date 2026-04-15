import tkinter as tk
from tkinter import scrolledtext
import requests 
from bs4 import BeautifulSoup
import webbrowser # Импортируем для открытия браузера

def open_link(event):
    # Эта функция определяет, на какую ссылку нажали
    try:
        # Получаем индекс текста под курсором
        index = display.index(f"@{event.x},{event.y}")
        # Ищем тег 'link', который мы добавим ниже
        tags = display.tag_names(index)
        for tag in tags:
            if tag.startswith("http"):
                webbrowser.open(tag) # Открываем ссылку в браузере
    except Exception as e:
        print(f"Ошибка при открытии ссылки: {e}")

def start():
    display.delete(1.0, tk.END)
    display.insert(tk.END, "⏳ Загрузка ссылок...\n\n")
    root.update()

    url = "https://somon.tj/nedvizhimost/prodazha-kvartir/hudzhand/"  
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', class_='advert')

        display.delete(1.0, tk.END)

        for card in cards:
            title_el = card.find('a', class_='advert__content-title')
            price_el = card.find('div', class_='advert__content-header')
            
            if title_el and price_el:
                title = title_el.text.strip().replace('\n', ' ')
                price = price_el.text.strip().replace('\n', ' ')
                full_link = "https://somon.tj" + title_el.get('href')
                
                # Вывод заголовка и цены
                display.insert(tk.END, f"🏠 {title}\n", "title_style")
                display.insert(tk.END, f"💰 Цена: {price}\n", "price_style")
                
                # СОЗДАЕМ КЛИКАБЕЛЬНУЮ ССЫЛКУ
                # Мы создаем уникальный тэг для каждой ссылки, равный самому URL
                display.insert(tk.END, "🔗 Открыть объявление\n", full_link)
                display.tag_config(full_link, foreground="#00d2ff", underline=1)
                
                # Привязываем событие клика (левая кнопка мыши) к этой ссылке
                display.tag_bind(full_link, "<Button-1>", open_link)
                
                display.insert(tk.END, f"{'-'*35}\n")
    except Exception as e:
        display.insert(tk.END, f"❌ Ошибка: {e}")

# --- Интерфейс ---
root = tk.Tk()
root.title("Somon Interactive Scanner")
root.geometry("650x600")
root.configure(bg="#17172b")

header = tk.Label(root, text="SOMON INTERACTIVE", font=("Segoe UI", 18, "bold"), bg="#1a1a2e", fg="#00d2ff")
header.pack(pady=15)

btn = tk.Button(root, text="ОБНОВИТЬ И НАЙТИ ССЫЛКИ", command=start, 
                bg="#4ecca3", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=20, pady=10)
btn.pack(pady=10)

display = scrolledtext.ScrolledText(root, width=70, height=25, bg="#142041", fg="#c2b5b5", font=("Consolas", 10), padx=10, pady=10)
display.pack(padx=20, pady=10)

# Стили
display.tag_config("title_style", foreground="#ffffff", font=("Consolas", 10, "bold"))
display.tag_config("price_style", foreground="#4ecca3")

root.mainloop()