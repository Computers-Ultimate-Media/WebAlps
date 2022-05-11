% rebase('layout.tpl', year=year, user_count=user_count)

<html style="font-size: 16px;">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css"/>
</head>
<body>

<form action="/reviews/new" method="post">
    <fieldset>
        <legend>New review</legend>
        <div class="form-group">
            <label for="loginText" class="form-label mt-4">Your username</label>
            <input class="form-control" id="loginText" name="AUTHOR" placeholder="Enter username" maxlength="120"
                   required>
        </div>
        <div class="form-group">
            <label for="textText" class="form-label mt-4">Your review</label>
            <textarea class="form-control" id="textText" name="TEXT" placeholder="Enter your review here"
                      maxlength="255" rows="5" required> </textarea>
        </div>
        <br>
        <button type="submit" value="Send" class="btn btn-primary">Post review</button>
    </fieldset>
</form>
</body>
</html>