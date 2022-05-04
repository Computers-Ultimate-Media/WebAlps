% rebase('layout.tpl', year=year)
<!DOCTYPE html>
<html style="font-size: 16px;">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css" /> 
</head>
<body>

<div class="container-custom">
	%for review in reviews:
    <div>
        <h5>{{review.author}}</h5>
        <h5/>{{review.date}}</h5>
        <h5/>{{review.text}}</h5> 
    </div>
</div>

<footer> </footer>
</body>
</html>