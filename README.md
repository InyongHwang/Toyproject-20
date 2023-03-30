# 플바천국
개발 프로젝트를 함께할 팀원을 모집할 수 있는 사이트
<br></br>
<br></br>

# 프로젝트 사이트
http://myweb.eba-wmqnxdas.ap-northeast-2.elasticbeanstalk.com/
<br></br>
<br></br>

# 1. 제작 기간 및 팀 내 역할
### 기간 : 2023-03-27 ~ 2023-03-30

### 팀 구성
1. 황인용(팀장) : '로그인/회원가입' + '주최한 프로젝트' 페이지 구현
2. 김선민(부팀장) : '게시글 상세 페이지' + '신청한 프로젝트' 페이지 구현
3. 김채민 : '로그인/회원가입' 페이지 구현 + '프로젝트 로고' 제작
4. 김재형 : '메인 페이지' + '게시글 작성 페이지' 구현
<br></br>
<br></br>

# 2. 사용한 기술
`Back-end`
- flask
- mongodb
- jwt
- hashlib


`front-end`
- jquery
- bootstrap


`deploy`
- AWS Elastic Beanstalk
<br></br>
<br></br>

# 3. 주요 기능
`회원가입 및 로그인`
- 비밀번호는 hashlib으로 암호화하여 db에 저장했습니다.
- 정상 로그인 시 jwt를 발행해주어 다른 페이지에서도 로그인 상태를 유지할 수 있도록 하였습니다.

`게시글 CRUD`
- jwt를 이용하여 유저의 email과 게시글 작성자의 email이 일치할 경우에 한해서만 수정/삭제가 가능하도록 하였습니다.
