  # Coin Trade Market

  Flask 기반으로 만든 코인 트레이드 마켓 데모입니다.
  홈에서 여러 코인 마켓으로 바로 진입할 수 있고, 각 마켓 페이지에서 시세, 호가창, 주문 패널, 판매 게시글, 거래 히스토리
  를 확인할 수 있습니다.

  ## Features

  - 홈 대시보드
  - 다중 마켓 진입
    - `BTC`
    - `ETH`
    - `XRP`
  - 마켓별 상세 페이지
  - 실시간 거래소 스타일 UI
  - 주문 패널
    - 매수
    - 판매 등록
    - 입금 / 출금
  - 호가창 UI
  - 거래 히스토리 UI
  - 로그인 / 회원가입 페이지 라우팅

  ## Tech Stack

  - Python 3
  - Flask
  - HTML (Jinja2 Templates)
  - CSS
  - JavaScript

  ## Project Structure

  ```bash
  coin/
  ├── app.py
  ├── requirements.txt
  ├── package.json
  ├── templates/
  │   ├── base.html
  │   ├── home.html
  │   ├── market.html
  │   └── auth.html
  └── static/
      ├── styles.css
      └── app.js

  ## Installation

  가상환경 생성:

  python3 -m venv .venv

  가상환경에 패키지 설치:

  .venv/bin/python -m pip install -r requirements.txt

  ## Run

  npm start

  또는 직접 실행:

  .venv/bin/python app.py

  실행 후 접속:

  http://127.0.0.1:4173

  ## Routes

  - / : 홈
  - /markets/BTC : BTC 마켓
  - /markets/ETH : ETH 마켓
  - /markets/XRP : XRP 마켓
  - /signin : 로그인
  - /signup : 회원가입

  ## Notes

  - 현재 프로젝트는 데모 UI 중심입니다.
  - 실제 DB 저장은 연결되어 있지 않습니다.
  - 실제 인증, 주문 체결, 입출금 처리, 사용자 데이터 저장은 아직 구현되지 않았습니다.
  - 마켓 데이터는 app.py 내부 더미 데이터로 구성되어 있습니다.

  ## Future Improvements

  - 사용자 인증 기능 연동
  - DB 연동
  - 실제 주문 저장 / 체결 로직 추가
  - 입금 / 출금 처리 로직 추가
  - 관리자 페이지 추가
  - 차트 고도화
  - WebSocket 기반 실시간 데이터 반영

  ## License

  This project is for educational and demo purposes.
