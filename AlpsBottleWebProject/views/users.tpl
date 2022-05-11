% rebase('layout.tpl', title=title, year=year, authors=authors, user_count=user_count)

<html style="font-size: 16px;">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css"/>
</head>
<body>
<div class="container-custom">
    <div class="user-container">
        <div class="sm"> Наши пользователи:</div>
        %for item in authors:
        <h3>
            {{ item[0] }}
            <small class="text-muted">{{ item[1] }}</small>
        </h3>
        %end
    </div>
</div>
</body>
</html>


