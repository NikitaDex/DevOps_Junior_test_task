1. Создание inventory файла:
    Прописать в терминале  "python3 make_inv/script.py"

2. Подготовка mysql сервера:
    Прописать в терминале  "ansible-playbook -i inventory side.yml"

3. Добавление необходим баз и пользователей:
    Прописать в терминале  "ansible-playbook -i inventory --extra-vars "mysql_root_password=XXX" mysql.yml"
    Вместо XXX указать пароль от root пользователя mysql.