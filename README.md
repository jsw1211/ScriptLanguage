# ScriptLanguage
 
반갑다 스크립트언어 텀프로젝트 시작한다.

메이플스토리 api를 만들것이다.

1. 경매장기능 (매물 검색, 시세 확인 등)
2. 캐릭터 검색 기능 (캐릭터에 대한 정보 및 이미지를 보여주고 레벨에 맞는 사냥터 추천)
3. 성형 및 헤어 미리보기 (코디 관련해서 미리 얼굴과 헤어를 조합해 볼 수 있다)

--------------------2020.05.20(수정)-------------------------

기능
1. 캐릭터 정보(이미지, 닉네임, 레밸, 서버 등)
2. 확률 정보(그래프 활용)
3. 랭킹 정보(레밸을 기준으로 서버별로 조회 가능)
4. 팝업스토어(이건 일단 팝업스토어만, pc방은 api에서 제공을 안해서 까다로움)

해야할 것
1. 팀프로젝트 제출란 형식에 따라 제출
2. 지도 기능 생각해보기
3. UI 만들고 json 파일 읽어보기

--------------------2020.05.25(수정)-------------------------

세부 설명
1. 캐릭터 정보(UI 구성한 대로)
   장비를 어떻게 보여줄 건지 정해야 함 (1. 장비들 이미지만
                                     2. 장비들 세부 정보 접근 가능 <- 상당히 어려울 것)
   Default 상태로 임시 캐릭터 이미지와 정보에 설명을 적어놓음 (예시: 닉네임, 레밸 등으로 표현)
2. 랭킹 정보
   서버가 일반서버(리부트 제외 전체) 랑 리부트서버(리부트서버만) 이 존재 어떻게 구성할 것인가?
   Default 상태는 일반서버 전체로 랭킹 보여줌

--------------------2020.05.29(수정)-------------------------

스타포스 관련
 넥슨 API 키를 입력하면 2023.12.27 부터 현재 날짜 까지의 정보를 전부 요청하고 저장함
 그렇게 저장한 정보를 활용해 얼마나 게임 재화를 사용 했는지
 표기된 강화 확률과 실제 나온 통계를 그래프를 통해 보여준다

오프라인 행사 관련
여러 오프라인 행사가 있지만 최근의 행사만 주목할 예정
1. 2023 여름 쇼케이스 (이 경우 CGV 정보도 포함 할 예정)
2. 2023 겨울 쇼케이스
3. 팝업스토어
지도 기능을 테스트 해보아야 함

검키우기 관련
 검 이미지를 사용하고 점점 강화시킬 수 있음
 강화 확률은 인게임 강화 확률과 동일하게
 미니게임 형식으로 스타포스 창을 띄워 맞추면 확률 UP
 지금까지 사용한 재화 보여주기

 --------------------2020.06.06(수정)-------------------------

추가 구현할 내용
1. C++ 모듈로 연결(즐겨찾기 내용 문자열로 저장할 예정)
2. 텔레그램 챗봇으로 간단한 캐릭터 정보조회, 랭킹 시스템 구현
   
