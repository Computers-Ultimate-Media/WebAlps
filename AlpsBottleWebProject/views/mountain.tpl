% rebase('layout.tpl', year=year)

<!-- Шаблон страницы гор -->
<html style="font-size: 16px;">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/static/content/our_cute_style.css"/>
</head>
<body>
<div class="container-custom">
    <div class="tb lg">
        {{head}}
        <!--Высочайшая вершина мира.!-->
    </div>
    <div class="wrapper">
        <input type="radio" name="point" id="slide1" checked>
        <input type="radio" name="point" id="slide2">
        <input type="radio" name="point" id="slide3">
        <input type="radio" name="point" id="slide4">
        <input type="radio" name="point" id="slide5">
        <div class="slider">
            <div class="slides slide1"></div>
            <div class="slides slide2"></div>
            <div class="slides slide3"></div>
            <div class="slides slide4"></div>
            <div class="slides slide5"></div>
        </div>
        <div class="controls">
            <label for="slide1"></label>
            <label for="slide2"></label>
            <label for="slide3"></label>
            <label for="slide4"></label>
            <label for="slide5"></label>
        </div>
    </div>
    <div class="tb sm">
        {{description}}
        <br>
        <br>
        <br>
        <div class="lg"> {{climb_h}}</div>
        {{climb_text}}
        <div class="image-container">
            <img class="image-custom" src="{{img1}}">
        </div>

        <div class="lg"> Месторасположение и особенности</div>
        {{location_text}}
        <br>
        {{more_text}}
        <br>
        {{last_text}}
    </div>
</div>
</body>
</html>