# likelionhomework1
2019 멋사 운영진 과제 1차

Languae : Python
FrameWork : Django(Full-Stack FrameWork)
Editor : VS_Code

# 내용
  - ## Python Setting
    ```
     - <https://www.python.org/downloads> 에서 자신의 OS 별 python 다운
     - $ python --version
          -> python 버전이 제대로 나온다면 설치완료
    ```
    
    * Mac OS의 경우 python 버전이 기본으로 깔려 있으므로 '$ python3 --version' 으로 확인해야함
    * python3 명령어가 쓰기 귀찮을 경우
     ```
      - /user/ 위치에서 '$ ls -a'
      
      - 숨김 파일 중 .bash_profile 을 찾은 후
          -> $ vi .bash_profile
          
      - alias python="python3" 로 변경 후
          -> 'esc' -> ':' -> 'w' -> 'q' -> 'enter' 순서대로 진행
          
      - $ source ~/.bash_profile
          -> 변경사항 수동으로 실행
          
      - $ python --version
          -> python3 버전이 잘 나오면 성공
     ```
     
  - ## VS_Code Setting
    ```
     - Preference 탭에서 Extension 클릭
     
     - Python 설치
     
     - Django 설치
     
     - Django Template 설치(선택사항)
        -> html에서 Django template 문법 사용시 보기 좋게 표현됨
    ```
     
  - ## Django Setting
    ```
     - VS_Code로 들어와 Terminal을 연다
     
     - $ python --version
        -> python 버전 다시 확인
        
     - $ pip install django
        -> python 프레임워크인 django 설치
    ```
        
  - ## Django Project Setting
    ```
     - $ python -m venv (가상환경이름)
        -> 가상환경 생성
        
     - $ source (가상환경이름)/bin/activate
        -> 가상환경 실행, Window의 경우에는 '$ source (가상환경이름)/scripts/activate'
        
     - $ django-admin startproject (프로젝트이름)
        -> 프로젝트 생성
        
     - $ cd (프로젝트이름)
        -> 해당 프로젝트로 들어감
        
     - myapp 폴더에 'templates' 폴더 생성
        -> html 파일을 만드는 폴더가 됨
        
     - myproject 폴더로 들어가 Installed_App에 'myapp.apps.MyappConfig' 추가
        -> django에 내가 만들 app을 등록하는 것임
        
     - $ python manage.py runserver
        -> 서버 시작, 이상없이 페이지가 열리면 셋팅완료.
    ```
    
  - ## Django 내 주요 폴더 및 파일 설명
    ```
    - myapp/templates
      -> html 파일을 작성하는 폴더
      
    - myapp/view.py
      -> python을 이용하여 각종 함수 작성하는 파일
      ex) return render(request, 'xxx.html')
            -> 'xxx.html' 을 렌더링 하는 함수
            
    - myapp/models.py
      -> model을 정의하는 곳(추후 진행 예정)
      
    - myproject/settings.py
      -> myapp, database 등을 등록하는 파일
      
    - myproject/urls.py
      -> router를 등록하는 파일
      
    - manage.py
      -> 브라우저에서 작동하는 파일
    ```
    
 *기타*
  ```
  - cmd(ctrl) + c
     -> 서버 종료
     
  - $ pip uninstall django
        -> django 삭제
        
  - $ pip install django --(특정버전)
        -> 특정버전 django 설치 가능
        
  - $ deactivate
        -> 가상머신 종료
  ```
