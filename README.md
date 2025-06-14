# 🎮 Player Inventory API (FastAPI + PostgreSQL)

## 📌 Описание

API для управления инвентарём игроков: создание персонажей, добавление предметов, просмотр экипировки и отслеживание ресурсов. Реализован на FastAPI и PostgreSQL с документацией через Swagger.

## 🚀 Функции

- 📦 Добавление и просмотр предметов в инвентаре
- 🧙‍♂️ Создание и просмотр игроков
- ⚔ Привязка предметов к конкретным игрокам
- 💰 Отслеживание золота и других ресурсов

## ⚙️ Стек

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## 🛠 Установка и запуск

### 1. Клонируй или скачай проект

```bash
git clone https://github.com/yourname/player-inventory-api.git
cd player-inventory-api
```

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Настрой PostgreSQL

Создай базу данных `inventory_db`:

```sql
CREATE DATABASE inventory_db;
```

Проверь строку подключения в `database.py`:

```python
DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/inventory_db"
```

### 4. Запусти сервер

```bash
uvicorn main:app --reload
```

API будет доступно по адресу:  
📎 http://localhost:8000

Swagger UI:  
📎 http://localhost:8000/docs

ReDoc:  
📎 http://localhost:8000/redoc

## 🔗 Эндпоинты

| Метод | URL                                | Описание                       |
|-------|-------------------------------------|--------------------------------|
| POST  | /players/                          | Создать нового игрока          |
| GET   | /players/                          | Получить список всех игроков   |
| POST  | /players/{id}/items/               | Добавить предмет игроку        |
| GET   | /players/{id}/items/               | Получить все предметы игрока   |

## 🧪 Тестирование через Postman

1. Импортируй коллекцию Postman (если есть)
2. Протестируй эндпоинты: `POST /players/`, `POST /players/{id}/items/`, `GET /players/1/items/`
3. Добавь скрипт во вкладке **Tests**:

```javascript
pm.test("Успешный ответ", function () {
    pm.response.to.have.status(200);
});
```

## 📄 Swagger-документация

Swagger UI автоматически доступен по адресу:  
http://localhost:8000/docs

## 👨‍💻 Автор

Практическая работа №8 — Тема №92: API для инвентаря игроков  
МИРЭА, Институт перспективных технологий и индустриального программирования  
Кафедра Индустриального программирования