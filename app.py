# Hello World Flask 애플리케이션 예제

from flask import Flask # Flask 모듈 임포트
# Flask는 파이썬으로 작성된 웹 프레임워크로, 웹 애플리케이션을 쉽게 만들 수 있도록 도와줍니다.


app = Flask(__name__)  # Flask 애플리케이션 객체 생성

@app.route("/")         # 루트 URL에 대한 라우팅 설정
def hello():
    return "Hello, World!"  # 브라우저에 출력될 텍스트

@app.route("/challenge")  #라우트 추가
def challenge():
    return "Weekly Challenge"

@app.route("/user/<username>")
def show_user(username):
    return f"안녕하세요, {username}님"

if __name__ == "__main__":
    app.run(debug=True)  # 개발 서버 실행 (디버그 모드)
