% rebase('layout.tpl', title=title, year=year, user_count=user_count)

<html style="font-size: 16px;" lang="ru">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css"/>
    <title></title>
</head>
<body>
<form action="/registration" method="post" onsubmit="return validate_all();">
    <fieldset>
        <legend>Registration</legend>
        <div class="form-group">
            <label for="loginInput" class="form-label mt-4">Your login</label>
            <input class="form-control" id="loginInput" name="login" placeholder="Enter login" required>
        </div>
        <div class="form-group">
            <label for="emailInput" class="form-label mt-4">Your email</label>
            <input type="email" class="form-control" id="emailInput" name="email" aria-describedby="emailHelp"
                   placeholder="Enter email" required>
        </div>
        <div class="form-group">
            <label for="passwordInput" class="form-label mt-4">Password</label>
            <input type="password" class="form-control" id="passwordInput" name="password"
                   placeholder="Enter password" required>
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Sign up</button>
    </fieldset>
</form>
</body>
</html>