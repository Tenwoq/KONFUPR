# Практическое задание №3
 ИКБО-62-23 Саргсян Т.В.
## Задание №1
Код
```
{
  groups: std.map(function(i) 'ИКБО-' + (i + 1) + '-23', std.range(0, 62),
  students:
    [
      { age: 19, group: 'ИКБО-40-20', name: 'Иванов И.И.' },
      { age: 18, group: 'ИКБО-50-20', name: 'Петров П.П.' },
      { age: 18, group: 'ИКБО-51-20', name: 'Сидоров С.С.' },
      { age: 19, group: 'ИКБО-62-23', name: 'Саргсян Т.В.' },
    ],
  subject: 'Конфигурационное управление',
}
```
Вывод
```
{
  "groups": [
    "ИКБО-1-23",
    "ИКБО-2-23",
    "ИКБО-3-23",
    "ИКБО-4-23",
    "ИКБО-5-23",
    "ИКБО-6-23",
    "ИКБО-7-23",
    "ИКБО-8-23",
    "ИКБО-9-23",
    "ИКБО-10-23",
    "ИКБО-11-23",
    "ИКБО-12-23",
    "ИКБО-13-23",
    "ИКБО-14-23",
    "ИКБО-15-23",
    "ИКБО-16-23",
    "ИКБО-17-23",
    "ИКБО-18-23",
    "ИКБО-19-23",
    "ИКБО-20-23",
    "ИКБО-21-23",
    "ИКБО-22-23",
    "ИКБО-23-23",
    "ИКБО-24-23",
    "ИКБО-25-23",
    "ИКБО-26-23",
    "ИКБО-27-23",
    "ИКБО-28-23",
    "ИКБО-29-23",
    "ИКБО-30-23",
    "ИКБО-31-23",
    "ИКБО-32-23",
    "ИКБО-33-23",
    "ИКБО-34-23",
    "ИКБО-35-23",
    "ИКБО-36-23",
    "ИКБО-37-23",
    "ИКБО-38-23",
    "ИКБО-39-23",
    "ИКБО-40-23",
    "ИКБО-41-23",
    "ИКБО-42-23",
    "ИКБО-43-23",
    "ИКБО-44-23",
    "ИКБО-45-23",
    "ИКБО-46-23",
    "ИКБО-47-23",
    "ИКБО-48-23",
    "ИКБО-49-23",
    "ИКБО-50-23",
    "ИКБО-51-23",
    "ИКБО-52-23",
    "ИКБО-53-23",
    "ИКБО-54-23",
    "ИКБО-55-23",
    "ИКБО-56-23",
    "ИКБО-57-23",
    "ИКБО-58-23",
    "ИКБО-59-23",
    "ИКБО-60-23",
    "ИКБО-61-23",
    "ИКБО-62-23",
    "ИКБО-63-23"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-40-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-50-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-51-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 20,
      "group": "ИКБО-62-23",
      "name": "Саргсян Т.В."
    }
  ],
  "subject": "Конфигурационное управление"
}
```
## Задание №2
Код
```
let Student = { age : Natural, group : Text, name : Text }
let Group = Text
let groupPrefix = "ИКБО-"
let groupYear = "-23"
let makeGroup =
      λ(n : Natural) →
        groupPrefix ++ Natural/show n ++ groupYear

let groups =
      [ makeGroup 1, makeGroup 2, makeGroup 3, makeGroup 4, makeGroup 5
      , makeGroup 6, makeGroup 7, makeGroup 8, makeGroup 9, makeGroup 10
      , makeGroup 11, makeGroup 12, makeGroup 13, makeGroup 14, makeGroup 15
      , makeGroup 16, makeGroup 17, makeGroup 18, makeGroup 19, makeGroup 20
      , makeGroup 21, makeGroup 22, makeGroup 23, makeGroup 62
      ]

let students =
      [ { age = 19, group = makeGroup 4, name = "Иванов И.И." }
      , { age = 18, group = makeGroup 5, name = "Петров П.П." }
      , { age = 18, group = makeGroup 5, name = "Сидоров С.С." }
      , { age = 19, group = makeGroup 62, name = "Саргсян Т.В." }
      ]

let subject = "Конфигурационное управление"

in  { groups = groups, students = students, subject = subject }
```
Вывод
```
groups:
  - "ИКБО-1-23"
  - "ИКБО-2-23"
  - "ИКБО-3-23"
  - "ИКБО-4-23"
  - "ИКБО-5-23"
  - "ИКБО-6-23"
  - "ИКБО-7-23"
  - "ИКБО-8-23"
  - "ИКБО-9-23"
  - "ИКБО-10-23"
  - "ИКБО-11-23"
  - "ИКБО-12-23"
  - "ИКБО-13-23"
  - "ИКБО-14-23"
  - "ИКБО-15-23"
  - "ИКБО-16-23"
  - "ИКБО-17-23"
  - "ИКБО-18-23"
  - "ИКБО-19-23"
  - "ИКБО-20-23"
  - "ИКБО-21-23"
  - "ИКБО-22-23"
  - "ИКБО-23-23"
  - "ИКБО-62-23"
students:
  - age: 19
    group: "ИКБО-4-23"
    name: "Иванов И.И."
  - age: 18
    group: "ИКБО-5-23"
    name: "Петров П.П."
  - age: 18
    group: "ИКБО-5-23"
    name: "Сидоров С.С."
  - age: 19
    group: "ИКБО-62-23"
    name: "Саргсян Т.В."
subject: "Конфигурационное управление"
```
# Для решения последующих задач потребуется код на языке программирования Python, представленный ниже:
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
## Задание №3
Код
```
BNF = '''
E = A | A E
A = 0 | 1
'''
```
Вывод
![image](https://github.com/user-attachments/assets/e8bfb3f0-af9b-4a77-8e5c-2ef1ef98cd89)

## Задание №4
Код
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start, depth=0, max_depth=5, max_length=20):
    '''
    Сгенерировать случайную фразу с ограничением на глубину рекурсии и длину строки.
    '''
    if depth > max_depth:
        return ''
    if start in grammar:
        seq = random.choice(grammar[start])
        result = ''.join([generate_phrase(grammar, name, depth + 1, max_depth, max_length) for name in seq])
        if len(result) > max_length:
            return ''
        return result
    return str(start)

BNF = '''
S = ( S ) S | [ S ] S | ε
ε =
'''

grammar = parse_bnf(BNF)

# Генерируем несколько строк и выводим их через enter
for _ in range(10):
    print(generate_phrase(grammar, 'S'))
```
Вывод
![image](https://github.com/user-attachments/assets/36f386ee-5465-4995-b240-120807ec7f3c)

## Задание №5
Код
```
BNF = '''
E = T | E | T
T = F | T "&" F
F = "~" F | "(" E ")" | VAR
VAR = x | y | z
'''
```
Вывод
![image](https://github.com/user-attachments/assets/42549e4a-cb54-4858-826b-5988c816eb9b)

