# User Setting API
    Пояснение к структуре:
    
    new_app (Папка с проектом)
       |---> dataclass (dataclass обьекты )
       |         |-> param.py 
       |        
       |---> models (Взаимодействие с sqlite)
       |         |-> __init__.py (создание и описание моделей)
       |         |-> param.py (запросы к бд параметры)
       |         |-> user.py (запросы к бд пользователи)
       |---> routs (Обработчики запросов)
       |         |-> param.py (Параметров)
       |         |-> user.py (Пользователей)
       |         |-> visually_tests.py (Визуальная часть для наглядного тестирования)
       |--> schemas (Схемы)
       |         |-> param.py (Параметров) 
       |         |-> user.py (Пользователей)
       |--> static (Статические файлы)
       |         |-> style.css (Стили для роута /)
       |--> templates (Шаблоны)
       |         |-> index.html (Страничка для роута /)
       |--> main.py (Основной файл запуска)
       |--> requirements.txt (Файл с зависимостями)
       |--> TestServerUser.postman_collection.json (Запросы для postman)
       README.md (сейчас тут)
       Task.docx (Задание)
       
        