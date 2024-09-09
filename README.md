# Задание 1
```
cut -d: -f1 /etc/passwd|sort
```
- ![#1](https://github.com/user-attachments/assets/6d4ef45a-e63c-4cf2-ac3a-5ff4c253add4)

# Задание 2
```
cat /etc/protocols|sort -k 2,2nr|head -n 5|awk '{print $2, $1}'
```
- ![#2](https://github.com/user-attachments/assets/864a17f7-fffc-4134-8fcb-a640c742b487)

# Задание 3
```
x = input()
print('+' + '-' * (len(x)+2) + '+')
print(f'| {x} |')
print('+' + '-' * (len(x)+2) + '+')
```
- ![image](https://github.com/user-attachments/assets/ba1ecbbe-8625-4b99-b2ac-c11c67132b95)

# Задание 4
```
#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Используйте: $0 имя команды."
	exit 1
fi

command_name="$1"
command_path="./$command_name"

if [ ! -f "$command_path" ]; then
	echo "Ошибка: файл '$command_path' не найден."
	exit 1
fi

sudo chmod +x "$command_name"
sudo cp "$command_path" /usr/local/bin/

if [ $? -ne 0 ]; then
	echo "Ошибка: не удалось скопировать файл."
	exit 1
fi

sudo chmod 775 /usr/local/bin/"$command_name"

if [ $? -ne 0 ]; then
	echo "Ошибка: не удалось установить права для '$command_name'."
	exit 1
fi

echo "Команда '$command_name' успешно зарегестрирована."
```
