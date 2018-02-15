<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <link href="./static/main.css" rel="stylesheet" type="text/css">
        <title>Title</title>
    </head>
    <body>
        {% for x in baekur %}
        <a href="/book"><h1>{{x}}</h1></a>
        {% endfor %}
    </body>
</html>