# Задание 1

cut -d: -f1 /etc/passwd|sort
- ![#1](https://github.com/user-attachments/assets/6d4ef45a-e63c-4cf2-ac3a-5ff4c253add4)

# Задание 2

cat /etc/protocols|sort -k 2,2nr|head -n 5|awk '{print $2, $1}'
- ![#2](https://github.com/user-attachments/assets/864a17f7-fffc-4134-8fcb-a640c742b487)

# Задание 3

