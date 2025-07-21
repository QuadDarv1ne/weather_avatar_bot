# 🐍 Полное руководство по Python-библиотекам с Poetry

## ~ ✨ Исчерпывающий справочник по основным зависимостям

## 📌 Содержание

1. [Основные рабочие зависимости](#-основные-рабочие-зависимости)
2. [Инструменты разработки](#-инструменты-разработки)
3. [Веб-фреймворки](#-веб-фреймворки)
4. [Data Science стэк](#-data-science-стэк)
5. [Работа с базами данных](#-работа-с-базами-данных)
6. [Боты и асинхронность](#-боты-и-асинхронность)
7. [API клиенты](#-api-клиенты)
8. [Практические примеры](#-практические-примеры)

## 📦 Основные рабочие зависимости

### 🌐 Сетевые запросы

```bash
poetry add requests       # Синхронные HTTP-запросы
poetry add httpx         # Асинхронные HTTP-запросы
poetry add aiohttp       # Альтернатива для asyncio
```

### 📊 Обработка данных

```bash
poetry add pandas        # Анализ табличных данных
poetry add numpy         # Математические операции
```

### ⏱ Работа с датами

```bash
poetry add pendulum      # Удобные временные зоны
poetry add arrow         # Облегченная альтернатива
```

### 🛠 Утилиты

```bash
poetry add python-dotenv # Загрузка .env переменных
poetry add pydantic      # Валидация данных
poetry add loguru        # Удобное логирование
```

## 🛠 Инструменты разработки

### 🧪 Тестирование

```bash
poetry add pytest pytest-cov --group dev  # Тесты + покрытие
```

### ✨ Форматирование кода

```bash
poetry add black isort --group dev  # Автоформатирование
```

### 🔍 Линтинг

```bash
poetry add flake8 pylint mypy --group dev  # Проверка кода
```

### 💻 REPL

```bash
poetry add ipython --group dev  # Улучшенная консоль
```

## 🌐 Веб-фреймворки

### 🚀 Современные

```bash
poetry add fastapi uvicorn  # Асинхронный API
```

### 🏗 Классические

```bash
poetry add flask           # Микрофреймворк
poetry add django          # Полноценный фреймворк
```

## 📊 Data Science стэк

### 📈 Визуализация

```bash
poetry add matplotlib seaborn  # Графики и визуализация
```

### 🤖 Машинное обучение

```bash
poetry add scikit-learn       # Классическое ML
poetry add tensorflow         # Глубокое обучение
```

### 📓 Ноутбуки

```bash
poetry add jupyter           # Интерактивные блокноты
```

## 🗃 Работа с базами данных

### 🗄 SQL

```bash
poetry add sqlalchemy        # ORM
poetry add psycopg2          # PostgreSQL драйвер
```

### 🚀 NoSQL

```bash
poetry add redis            # Ключ-значение хранилище
poetry add pymongo          # MongoDB драйвер
```

## 🤖 Боты и асинхронность

### 🤖 Telegram

```bash
poetry add aiogram          # Асинхронный фреймворк
poetry add telebot          # Синхронная альтернатива
```

### 🎮 Discord

```bash
poetry add discord.py       # Discord API
```

## 📡 API клиенты

### 🤖 ИИ сервисы

```bash
poetry add openai           # OpenAI API
```

### 🌐 Соцсети

```bash
poetry add tweepy           # Twitter/X API
```

### ☁️ Облачные платформы

```bash
poetry add google-api-python-client  # Google API
```

## 🛠 Практические примеры

### 🚀 Стартовый набор веб-разработчика

```bash
poetry add fastapi uvicorn sqlalchemy psycopg2 pydantic
poetry add pytest black mypy --group dev
```

### 📊 Набор для анализа данных

```bash
poetry add pandas numpy matplotlib jupyter
poetry add pytest ipython --group dev
```

## 💡 Советы по работе

1. Всегда фиксируйте версии в `pyproject.toml`
2. Разделяйте production и dev зависимости
3. Используйте `poetry show --tree` для анализа
4. Регулярно обновляйте зависимости (`poetry update`)

## 📚 Дополнительные ресурсы

- [Официальная документация Poetry](https://python-poetry.org/docs/)
- [PyPI - репозиторий пакетов](https://pypi.org/)
- [Awesome Python](https://github.com/vinta/awesome-python)

🎉 Теперь вы готовы к профессиональной разработке на Python.
