# Python demo
---

Feel free to modify and play around with the code!
Please refer to [Documentation](https://docs.authlib.org/en/latest/) if you have any questions.

## Instructions

You will need to install `authlib`:
```console
jwt@demo:~$ pip install --user authlib
```

Then you can simply call the script:
```console
jwt@dome:~$ python3 main.py
```

Or if you wish to use python console:
```python
from main import issue_jwt,verify_jwt

s = issue_jwt()
time.sleep( 1 )
print( verify_jwt( s ) )
```
