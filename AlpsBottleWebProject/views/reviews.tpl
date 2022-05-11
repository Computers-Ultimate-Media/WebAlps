% rebase('layout.tpl', year=year, user_count=user_count)
<html style="font-size: 16px;">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css"/>
</head>
<body>

<div class="container-custom">
    <a href="/reviews/new">
        <button class="btn btn-primary">Post new review</button>
    </a>
    <div class="review-container">
        %for review in reviews:
        <div>
            <h3>
                {{review[0]}}
                <small class="text-muted">{{review[2]}}</small></h3>
            <h4 class="limited-width">{{review[1]}}</h4>
        </div>
        %end
    </div>
</div>

<footer></footer>
</body>
</html>