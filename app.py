import psycopg2

# Подключаемся к базе данных PostgreSQL
connection = psycopg2.connect(
    dbname="your_surname",  # Название базы данных
    user="your_username",   # Имя пользователя
    password="your_password",  # Пароль
    host="db",  # Имя сервиса для контейнера db в docker-compose
    port="5432"
)

# Создаем курсор
cursor = connection.cursor()

# Выполняем запрос
cursor.execute("""
    SELECT name, age FROM test_table
    WHERE LENGTH(name) < 6
""")

# Получаем результаты
rows = cursor.fetchall()
ages = [row[1] for row in rows]

if ages:
    print(f"Максимальный возраст: {max(ages)}")
    print(f"Минимальный возраст: {min(ages)}")

# Закрываем соединение
cursor.close()
connection.close()
