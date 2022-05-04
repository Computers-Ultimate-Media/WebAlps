% rebase('layout.tpl', title=title, year=year, authors=authors)

<html style="font-size: 16px;">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css"/>
</head>
<body>
<div class="container-custom">
    <div class="tb lg">
        <!--Высочайшая вершина мира.!-->
    </div>
    <div class="sm"> Наши пользователи:</div>
    %for item in authors:
    <br>
    <div class="sm"> Логин: {{ item[0] }}</div>
    <div class="sm"> Почта: {{ item[1] }}</div>
    <br>
    %end
</div>
</body>
</html>


