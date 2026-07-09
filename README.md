# Asynchronous Telegram Bot Boilerplate

![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11-blue?style=flat-square)
![Framework](https://img.shields.io/badge/framework-aiogram_3.x-red?style=flat-square)

Готовый к развертыванию (production-ready) шаблон асинхронного Telegram-бота корпоративного уровня. Спроектирован для работы под высокими нагрузками с изолированной бизнес-логикой.

---

### 🧠 Ключевые особенности (Features)

* **Asynchronous Core:** Полностью асинхронная архитектура на базе `aiogram 3.x`.
* **Data Layer:** Интеграция реляционной БД PostgreSQL через современную ORM `SQLAlchemy 2.0` и асинхронный драйвер `asyncpg`.
* **State Management:** Быстрое кэширование состояний (FSM) пользователей с помощью оперативной памяти `Redis`.
* **DevOps Ready:** Контейнеризация приложения через `Docker` и `Docker Compose` для мгновенного деплоя на любой VPS/VDS.

---

### 🚀 Быстрый запуск (Quick Start)

1. Клонируйте репозиторий и настройте переменные окружения в файле `.env`.
2. Запустите всю инфраструктуру одной командой:
```bash
docker-compose up --build -d
