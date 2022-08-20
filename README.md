# User Setting API
##    Пояснение к структуре:
    
    new_app (Папка с проектом)
       |---> dataclass (dataclass обьекты )
       |         |-> param.py 
       |        
       |---> models (Взаимодействие с sqlite)
       |         |-> __init__.py (создание и описание моделей)
       |         |-> param.py (запросы к бд параметры)
       |         |-> user.py (запросы к бд пользователи)
       |
       |---> routs (Обработчики запросов)
       |         |-> param.py (Параметров)
       |         |-> user.py (Пользователей)
       |         |-> visually_tests.py (Визуальная часть для наглядного тестирования)
       |
       |--> schemas (Схемы)
       |         |-> param.py (Параметров) 
       |         |-> user.py (Пользователей)
       |
       |--> static (Статические файлы)
       |         |-> style.css (Стили для роута /)
       |
       |--> templates (Шаблоны)
       |         |-> index.html (Страничка для роута /)
       |
       |--> tests (Тесты)
       |         |-> test.py (Тесты)
       |
       |--> main.py (Основной файл запуска)
       |--> requirements.txt (Файл с зависимостями)
       |--> TestServerUser.postman_collection.json (Запросы для postman)
       
       README.md (сейчас тут)
       Task.docx (Задание)

## Запуск
    1. cd new_app
    2. python3 main.py
    
## Тесты   
    pytest new_app/tests/test.py
    postman collection (TestServerUser.postman_collection.json)
    **Для тестов необходимо в main создать users-> model_user.create_test_users(n=10)