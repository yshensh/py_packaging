Recommend to use virtual environment and run the following steps

Step 1:
Specify package `some_package` from Python and make it usable via `pip`
```
cd ./py_packaging
pip install ./some_package_proj/
```

Step 2:
Specify package `some_package`
```
$python3
>>> from some_package import some_func
>>> some_func()
'some_func from some_package_proj'
>>> exit()
```

