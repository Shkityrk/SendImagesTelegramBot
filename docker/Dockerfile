# Используем официальный образ Python как базовый
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в рабочую директорию
COPY src/ .

# Команда для запуска приложения
CMD ["python", "-m", "src"]
