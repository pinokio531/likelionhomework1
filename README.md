# likelionhomework
2019 멋사 운영진 과제 페이지

- Languae : Python
- FrameWork : Django(Full-Stack FrameWork)
- Editor : VS_Code

# 내용
  - ## Python Setting
    ```
     - <https://www.python.org/downloads> 에서 자신의 OS 별 python 다운
     - $ python --version
          -> python 버전이 제대로 나온다면 설치완료
    ```
    
     ```
     * Mac OS의 경우 python 버전이 기본으로 깔려 있으므로 '$ python3 --version' 으로 확인해야함
     * python3 명령어가 쓰기 귀찮을 경우
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
           
     - $ python manage.py startapp myapp
           -> myapp 이라는 프론트작업 환경을 만들어줌
           -> myapp 은 편의상 설정한 이름으로, 개발자가 원하는 대로 이름을 지어주면 됨
        
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
 - ## Admin 등록하기
   ```
   - $ python manage.py createsuperuser
        -> 아이디, 이메일, 패스워드 입력해서 계정 등록
        -> /admin/ 들어갈 때 해당계정을 이용해서 접근가능
   ```
    
 - ## Model 다루기
   ```
   - models.py 에서 'class (모델명)' 을 선언하고 각종 파라미터들을 입력한다
   
   - $ python manage.py makemigrations
        -> db에 등록될 모델들을 확정한다.
        -> default는 'sqlite3' 이지만 settings.py 에서 변경가능
   - $ python manage.py migrate
        -> 확정된 모델들을 db에 반영한다
   - admin.py 에서 해당 모델을 'imort' 하고, 'admin.site.register(모델명)' 로 적용한다
   - 이후 부터 '/admin/' 라우터로 들어가 실제 내용을 작성할 수 있다.
   ```
   
 - ## 로그인 구현하기_1 (기본세팅)
    ```
   - html 파일
      <form method = "POST" action="{%url 'login'%}"> //http 통신형태 지정, 통신할 url 지정
      {% csrf_token %}                                //보안을 위해서 선언
        /~ 내용 ~/
      </form>
      
   - views.py
    -> 모듈 추가
        from .models import Blog //mirgration 한 model
        from .models import Score

        from django.shortcuts import redirect
        from django.contrib.auth.models import User
        from django.contrib import auth
   ```
 - ## 로그인 구현하기_2 (회원가입)
    ```
    def join(request):
    
    //html 에서 통신방법을 확인
    if request.method == 'POST':
    
        //password, password_confirm 으로 비밀번호 확인
        if request.POST['userpassword'] == request.POST['userpassword_confirm']
        
            //계정 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST["userpassword"])
            
            //로그인
            auth.login(request, user)
            return redirect('login')
    return render(request, 'join.html')
    ```
 - ## 로그인 구현하기_3 (로그인)
    ```
    def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpassword']
        
        //username과 password를 통해 계정확인
        user = auth.authenticate(request, username=username, password=password)
        
        //계정이 None이 아니면, 즉 계정이 존재하면 로그인 실행
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'home.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'home.html')
    ```
 - ## 로그인 구현하기_3 (로그아웃)
    ```
    def logout(request):
    if request.method == 'POST':
    
        //로그아웃 하기
        auth.logout(request)
        redirect('home')
    return render(request, 'home.html')
    ```
    
 - ## Paginator 구현하기
    ```
    - html
        <form>

        {% if posts.number != 1%}
            <a href="?page=1">처음</a>
        {% else %}
            <a> 처음 페이지 입니다.</a>
        {% endif %}

       {% if posts.number > 1 %}  //posts.number는 현재 페이지
           <a href="?page={{posts.previous_page_number}}">이전</a> //posts.previous_page_number는 (현재페이지 -1) 페이지 번호
       {% endif %}

        (
        <span>{{posts.number}}</span>
        /
        <span>{{posts.paginator.num_pages}}</span>
        )

       {% if posts.number < posts.paginator.num_pages %} //posts.paginator.num_pages는 전체페이지 수 = 마지막 페이지 번호
           <a href="?page={{posts.next_page_number}}">다음</a>
       {% endif %}
       
       {% if posts.number != posts.paginator.num_pages%}
           <a href="?page={{posts.paginator.num_pages}}">마지막</a>
       {% else %}
           <a> 마지막 페이지 입니다.</a>
       {% endif %}
       </form>
       
    - views.py
        - 모듈추가
            -> from django.core.paginator import Paginator
            
        blog_list = Blog.objects.all()      //db내 blog 모델에 해당하는 objects 전부 출력
        paginator = Paginator(blog_list, 2) //2개가 한페이지가 되도록 함
        page = request.GET.get('page')      //html에서 보여줄 페이지 번호를 get으로 수신
        posts = paginator.get_page(page)    //해당 paginator 적용
        return render(request, 'home.html', {'posts':posts})
    ```
    
 - ## 기타
   ```
    - cmd(ctrl) + c
       -> 서버 종료
     
   - $ pip uninstall django
       -> django 삭제
        
    - $ pip install django --(특정버전)
       -> 특정버전 django 설치 가능
        
    - $ deactivate
       -> 가상머신 종료
