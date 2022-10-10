# Дипломный проект для курса автоматизации тестирования на платформе teachmeskills.by
Для запуска тестов:
                    1. Cкопируйте репозитой через SSH
                    2. Создайте виртуальное окружение и выполните в него вход (python -m venv venv, venv/Scripts/activate)
                    3. Скачайте все модули на виртуальное окружение (pip3 install -r requirements.txt)
                    4. Тесты запускаются коммандой pytest -v --alluredir=reports
                    но если необходимо ускорить прохождение тестов, то можно выполнить 2 последовательные комманды:
                    pytest -s -v -n=2 -m  "multiple_CPUs_run" --alluredir=reports
                    pytest -s -v -n=2 -m  "non_multiple_CPUs_run" --alluredir=reports
                    5. Посмотреть аллюр репорт allure serve reports 
