# Задание 1

```
import matplotlib
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"Matplotlib location: {matplotlib.__file__}")
print(f"Matplotlib description: {matplotlib.__doc__}")
```
![image](https://github.com/user-attachments/assets/7b451023-5092-4c53-95d6-68c2db48d624)
![image](https://github.com/user-attachments/assets/33e088f3-39c7-4b4f-a18e-216707e8f83e)
![image](https://github.com/user-attachments/assets/3d0ca72c-996e-44d8-ba86-17aa2f522a01)
![image](https://github.com/user-attachments/assets/8bdea4fc-60d2-4961-b379-99a7dee410b0)

# Задание 2

```
const express = require('express');
console.log(`Express version: ${require('express/package.json').version}`);
console.log(`Express path: ${require.resolve('express')}`);
console.log(`Express description: ${require('express/package.json').description}`);
```
![image](https://github.com/user-attachments/assets/74a18c8f-e3e8-4b11-94b1-1eb2d5ff3c3f)

> Также можно использовать:

```
npm info express
```
![image](https://github.com/user-attachments/assets/70b9d370-2cac-4c3b-81ca-a43e9dc83431)

# Задание 3
```
digraph Exp {
    node [shape=box];

    subgraph cluster_matplotlib {
        label="matplotlib";
        matplotlib;
        python;
        freetype;
        libpng;
        numpy;
        setuptools;
        cycler;
        dateutil;
        kiwisolver;
        pyparsing;
        
        matplotlib -> python;
        matplotlib -> freetype;
        matplotlib -> libpng;
        matplotlib -> numpy;
        matplotlib -> setuptools;
        matplotlib -> cycler;
        matplotlib -> dateutil;
        matplotlib -> kiwisolver;
        matplotlib -> pyparsing;
    }

    subgraph cluster_express {
        label="express";
        express;
        accepts;
        body_parser;
        array_flatten;
        content_disposition;
        content_type;
        cookie_signature;
        cookie;
        debug;
        depd;
        encodeurl;
        escape_html;
        etag;
        finalhandler;
        fresh;
        http_errors;
        merge_descriptors;
        methods;
        on_finished;
        parseurl;
        path_to_regexp;
        proxy_addr;
        qs;
        range_parser;
        safe_buffer;
        
        express -> accepts;
        express -> body_parser;
        express -> array_flatten;
        express -> content_disposition;
        express -> content_type;
        express -> cookie_signature;
        express -> cookie;
        express -> debug;
        express -> depd;
        express -> encodeurl;
        express -> escape_html;
        express -> etag;
        express -> finalhandler;
        express -> fresh;
        express -> http_errors;
        express -> merge_descriptors;
        express -> methods;
        express -> on_finished;
        express -> parseurl;
        express -> path_to_regexp;
        express -> proxy_addr;
        express -> qs;
        express -> range_parser;
        express -> safe_buffer;
    }
}
```
```
dot -Tpng t3.dot -o t3.png
```
![image](https://github.com/user-attachments/assets/83953d44-16c0-4f93-a989-cae60603c0cd)

# Задание 4

```
include "globals.mzn";

var 0..9: n1;
var 0..9: n2;
var 0..9: n3;
var 0..9: n4;
var 0..9: n5;
var 0..9: n6;

constraint n1 + n2 + n3 == n4 + n5 + n6;
constraint all_different([n1, n2, n3, n4, n5, n6]);
solve minimize n1 + n2 + n3;
```
![image](https://github.com/user-attachments/assets/05abc4dc-41c8-43f1-9ec8-e24e3de6c380)

# Задание 5

```
int: mCount = 6;
int: dCount = 5;
int: iCount = 2;
var 1..mCount: m;
var 1..dCount: d;
var 1..iCount: i;

array[1..mCount] of tuple(int, int, int): mVersions = [(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,4,0), (1,5,0)];
array[1..dCount] of tuple(int, int, int): dVersions = [(1,8,0), (2,0,0), (2,1,0), (2,2,0), (2,3,0)];
array[1..iCount] of tuple(int, int, int): iVersions = [(1,0,0), (2,0,0)];

constraint (mVersions[m] == (1,0,0) \/ mVersions[m] == (1, 5, 0) /\ iVersions[i] == (1, 0, 0));
constraint (mVersions[m].2 >= 1 /\ mVersions[m].2 <= 5) -> (dVersions[d] == (2, 3, 0) \/ dVersions[d] == (2, 0, 0));
constraint mVersions[m] == (1, 0, 0) -> dVersions[d] == (1, 8, 0);
constraint (dVersions[d].2 >= 0 /\ dVersions[d].2 <= 3) -> iVersions[i] == (2, 0, 0);

solve satisfy;

output [
  "Menu version: ", show(mVersions[m]), "\n",
  "Dropdown version: ", show(dVersions[d]), "\n",
  "Icon version: ", show(iVersions[i]), "\n"
];
```
![image](https://github.com/user-attachments/assets/57c1d7ea-5654-4bf0-bbbc-ffcea06a7485)

# Задание 6

```
```

# Задание 7

