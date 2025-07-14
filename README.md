# QA Samples by Alexander Savin

📌 Репозиторий с примерами тестовой документации и API-тестов. Содержит тест-кейсы, баг-репорты, Postman-коллекции и примеры автотестов.

## 📑 Содержание

- [Документация](#документация)
- [Автотесты (Python + pytest)](#автотесты-python--pytest)

## 🧪 Стек
- Postman (REST, SOAP)
- Python + PyTest (в планах)
- JSON-схемы, чек-листы, тест-кейсы
- BrowserStack, Figma, SQL, Git (в процессе освоения)

## 📁 Структура
- `/api-tests` — Postman-коллекции, автотесты
- `/docs` — тест-кейсы, чек-листы, баг-репорты
- `/json-schemas` — схемы валидаторов
- `/mindmaps` — карты процессов и UI-потоков

## 🔧 Автотесты (Python + pytest)

Примеры автотестов находятся в `api-tests/mock_api`:

- `claimer_api.py` — функция-заглушка для API POST /cases  
- `test_create_case.py` — тест на успешное создание записи  
- `conftest.py` — pytest‑фикстуры

### 🚀 Запуск автотестов:

```bash
cd api-tests/mock_api
pip install pytest requests
pytest
```

## 🛠 О себе
QA-инженер с опытом более 3 лет. Тестирую веб и десктоп-приложения, API, разрабатываю тестовую документацию, участвую в интеграционных и регрессионных тестах. Работал с высоконагруженными системами, корпоративными порталами и внутренними сервисами.

---

📫 [Написать](mailto:savinkrokodil@mail.ru) | 🔗 [GitHub](https://github.com/savinkrokodil)
