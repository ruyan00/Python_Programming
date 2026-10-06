# 2. 패키지

# 여러 개의 모듈을 디렉터리 단위로 묶어놓은 것
# 패키지 -> 모듈 -> 함수/클래스/변수

# ===========================================================
# 1. 패키지 내 모듈 불러오기
#  - from 패키지명 import 모듈명
#  - from 패키지명.모듈명 import 함수명 (from 가져올 위치 import 가져올 대상)
# ===========================================================

from mypackage import mymath
from mypackage.mymath import PI, add

print(mymath.PI)
print(mymath.add(10, 20))

# ===========================================================
# 2. __init__에서 re-export한 것 사용하기
# ===========================================================

import mypackage as m

print(m.VERSION)
print(m.add(10, 20))


url = "https://httpbin.org/get"

# re-export하지 않은 경우 세부 모듈 경로를 알아야 함
from requests import api

response = api.get(url)

print(response.status_code)

from numpy import _core

print(_core.arange(5))

# re-export를 한 경우에는 세부 모듈 경로를 몰라도 됨
import requests

response = requests.get(url)
print(response.status_code)

import numpy as np

print(np.arange(5))
