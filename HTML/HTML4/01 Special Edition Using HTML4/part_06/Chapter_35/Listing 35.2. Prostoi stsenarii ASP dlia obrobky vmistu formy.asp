<%@ Language = VBScript %>
<html>
    <head>
        <title>Laskavo prosymo</title>
    </head>
    <body>
        <h1>Laskavo Prosymo</h1>
        <p>Vitaiu, <%= Request.QueryString("first") %><%=Request.QueryString("last") %></p>
        <p>Laskavo prosymo na moiu storinku.</p>
        <p><a href="next.htm">Dali</a></p>
    </body>
</html>