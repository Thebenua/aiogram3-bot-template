# Benua · Telegram Bot Template

Небольшой стартовый шаблон Telegram-бота на Python и aiogram 3. Бот работает через polling, отвечает на `/start`, `/help` и подсказывает доступные команды на другие сообщения.

## Локальный запуск

Нужны Python 3.11 и токен бота от [BotFather](https://t.me/BotFather).

```bash
python -m venv .venv
```

Активируйте окружение (`.venv\Scripts\Activate.ps1` в PowerShell или `source .venv/bin/activate` в Linux/macOS), затем:

```bash
python -m pip install -r requirements.txt
```

Скопируйте `.env.example` в `.env` и укажите `BOT_TOKEN`. Из корня проекта запустите `python main.py`, отправьте боту `/start` и завершите процесс сочетанием Ctrl+C. Для одного токена запускайте только один polling-процесс; активный webhook тоже может мешать polling.

`.env` и `.venv` исключены из Git. Не публикуйте токен; если он стал известен посторонним, перевыпустите его через BotFather.

## Docker

При установленном Docker Compose создайте `.env` как описано выше, затем выполните:

```bash
docker compose up --build -d
docker compose logs -f bot
docker compose down
```

Контейнер запускает только бота. PostgreSQL и Redis не настроены и для текущих команд не нужны.

## Проверки

```bash
python -m unittest discover -s tests -v
```

Тесты проверяют конфигурацию и ответы обработчиков без обращения к Telegram. Для проверки сети и токена отдельно запустите бота и отправьте команды.

## Структура

- `main.py` — создание бота и запуск polling.
- `config/config.py` — настройки из окружения и `.env`.
- `handlers/common.py` — команды и ответ на другие сообщения.
- `tests/` — модульные проверки.
- `Dockerfile` и `docker-compose.yml` — контейнерный запуск.
- [CONTRIBUTING.md](CONTRIBUTING.md) — рекомендации для разработки.

`DATABASE_URL` и `REDIS_URL` необязательны и пока не используются. Зависимости SQLAlchemy, asyncpg и Redis сохранены как задел для развития, но подключения и хранения данных в шаблоне нет. ИИ и внешние API также не подключены.

## Автор

[Benua](https://thebenua.online/) · [GitHub](https://github.com/Thebenua) · [Telegram](https://t.me/Thebenua)

Лицензия в репозитории пока не указана; условия использования кода следует уточнить у автора.
