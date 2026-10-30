# Open API 기본

# ===========================================================
#  1. Open API란?
#  - ( API, Application Programming Interface ): 프로그램 간에 기능 또는 데이터를 주고받기 위한 인터페이스
#  - ( Open API ): 다른 프로그램에서 사용할 수 있도록 공개된 API
#
#  [Open API 사용 순서]
#  1) Open API 제공 서비스 확인
#  2) API 사용 신청
#  3) API 인증키 발급
#  4) API 요청(Request)
#  5) 서버로부터 데이터 응답(Response): 대부분 XML, JSON 형식
# ===========================================================

import requests
import webbrowser

# ===========================================================
# 1. 랜덤 강아지 사진 가져오기
# - https://dog.ceo
# ===========================================================


def get_dog_image():
    try:
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패 (상태 코드: {response.status_code})")
            return

        data = response.json()
        print(data)
        webbrowser.open(data["message"])

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


# get_dog_image()


# ===========================================================
#  2. 랜덤 고양이 사진 가져오기
#  - https://thecatapi.com/
# ===========================================================


def get_cat_image():
    try:
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패 (상태 코드: {response.status_code})")
            return

        data = response.json()
        print(data)
        webbrowser.open(data[0]["url"])

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


# get_cat_image()


# ===========================================================
#  3. 대학 검색하기
#  - https://github.com/Hipo/university-domains-list
# ===========================================================


def get_univ_list(country="Korea, Republic of"):
    try:
        url = "http://universities.hipolabs.com/search"
        params = {"country": country}
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패 (상태 코드: {response.status_code})")
            return

        data = response.json()
        # print(data)

        # 대학 수: 000개
        # 앞의 5개만 출력: 대학명 (홈페이지 주소)
        print(f"대학 수: {len(data)}개")
        for univ in data[:5]:
            print(f"{univ["name"]} ({univ["web_pages"][0]})")

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


# get_univ_list()
# get_univ_list("United States")


# ===========================================================
#  4. 날씨 조회하기
#  - https://open-meteo.com/
# ===========================================================


def get_weather(lat, lon):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "precipitation", "wind_speed_10m"],
        }
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패 (상태 코드: {response.status_code})")
            return

        data = response.json()
        print(data)
        # 측정 일시: XX
        # 기온: XX
        # 풍속: XX
        print(f"측정 일시: {data['current']['time']}")
        print(
            f"기온: {data['current']['temperature_2m']}{data['current_units']['temperature_2m']}"
        )
        print(
            f"풍속: {data['current']['wind_speed_10m']}{data['current_units']['wind_speed_10m']}"
        )

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


get_weather(lat=37.3416467, lon=126.8310305)
