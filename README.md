# example-vulture

[![Build Status](https://travis-ci.org/RJ722/example-vulture.svg?branch=master)](https://travis-ci.org/RJ722/example-vulture)

How to add vulture to CI tests

## Adding vulture to CI tests

The following patch was added to enable testing for unused code through vulture:

```diff
+install:
+- pip install vulture
+
 script:
 - python factorial/factorial_test.py
+- vulture factorial/
```

The PR may be found [here](https://github.com/RJ722/example-vulture/pull/1/files?diff=split)

## References

The factorial example here has been taken from [pymbook](http://pymbook.readthedocs.io/en/latest/testing.html)
