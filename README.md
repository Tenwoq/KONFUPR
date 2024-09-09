# Задание 1

cut -d: -f1 /etc/passwd|sort
- (https://github.com/Tenwoq/KONFUPR/blob/Pract1/%231.jpg)
# Задание 2

cat /etc/protocols|sort -k 2,2nr|head -n 5|awk '{print $2, $1}'
# Задание 3

