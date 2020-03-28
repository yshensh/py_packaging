Recommend to use virtual environment and run the following steps

Step 1:
create a source distribution and a wheel
```
cd ./py_packaging/some_wheel_proj/
python setup.py sdist bdist_wheel
```

Step 2:
copy source distribution and wheel to seperate directory
```
mkdir -p packages
cp some_wheel_proj/dist/some_wheel-1.0* packages
```

Step 3:
use `pip` to install
```
pip install --no-index --find-link=./packages some_wheel==1.0
```

Step 4:
Specify package `some_wheel_package`

1)
```
$python3
>>> import some_wheel
>>> some_wheel_package.some_func()
'some_func from some_wheel_proj'
```

2)
```
$python3
>>> from some_wheel_package import some_func
>>> some_func()
'some_func from some_wheel_proj'
```
