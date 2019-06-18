from django.test import TestCase
import json
# Create your tests here.
a = {
    "专业实训":['假条1','假条2','假条3'],
    "数字电路":['假条1','假条2','假条3'],
}
print(type(a))

b = json.dumps(a)
print(b)
print(type(b))