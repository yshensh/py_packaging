Recommend to use virtual environment and run the following steps

Step 1:
Specify one directory with one module to make it installable via pip
```
cd ./py_packaging
pip install ./some_module_proj/
```

Step 2:
Specify package `some_module`
```
$python3
>>> from some_module import some_func
>>> some_func()
'some_func from some_module_proj'
>>> exit()
```
