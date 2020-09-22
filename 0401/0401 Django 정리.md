# 0401 Django 정리

> style.css, img 파일 등 가져다 쓸 때

- articles폴더 안에 static 폴더 만들고 style.css 파일 만들어서 css 기능 추가
- static 파일을 쓸 때는 항상`html파일` 두 번째 줄에 `{% load static %}` 을 추가할 것 !! {% extends 'base.html'%} 이 <u>항상 최상단</u>에 위치 !

```html
# base.html

<!-- 맨 앞에 넣어주고 -->
{% load static %}

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
</head>

<body>
    <h1>게시판</h1>
    <!-- 이미지 넣기 -->
    <img src="{% static 'images/parts.jpg' %}">
    {% block body %}
    {% endblock %}
</body>
</html>
```



```html
# new.html

{% extends 'base.html' %}
{% load static %}

{%block css %}
<link rel="stylesheet" href="{% static 'stylesheets/form.css' %}">
{% endblock% }
{% block body %}

    <form action="/articles/create/">
        <label for="title">제목 : </label>
        <input type="text" name="title">
        <label for="content">내용 : </label>
        <textarea name="content" id="content">

        </textarea>
        <!-- <input type="text" name="content"> -->
        <input type="submit" value="작성완료"> 
    </form>
{% endblock %}
```



> models.py 에서 변경사항이 있을 때

- db file, migration 이력을 삭제 한 후 (init.py 는 삭제 ㄴㄴ)

- python manage.py makemigraitions , migrate 2개의 명령어를 통해 다시 마이그레이션을 만든다.



> Django는 기본적으로 sqlite3 를 쓰지만 다른 DB를 쓰려고 할 때

![image-20200922002458069](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200922002458069.png)

https://docs.djangoproject.com/en/3.0/ref/settings 참고



<hr>

### Bootstrap 가져다 쓰기

1. `base.html` 의 head 부분에 cdn 을 복사한다.

2. JS 부분은 body 태그 바로 위에 붙여넣는다.



