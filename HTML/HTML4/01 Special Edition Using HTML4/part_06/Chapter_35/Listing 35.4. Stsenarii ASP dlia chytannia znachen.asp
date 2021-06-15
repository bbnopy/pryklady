<%@ Language = VBScript %>
<html>
    <head>
        <title>Laskavo prosymo</title>
    </head>
    <body>
        <h1>Laskavo prosymo</h1>
        <p>Vitaiu, <%=Request.QueryString("first") %> <%=Request.QueryString("last") %></p>
        <p>Laskovo prosymo na moiu storinku.</p>
        <p><% theNumberOfOccupations = Request.QueryString("Occupation").Count %>
            <% if theNumberOfOccupations = 0 %>
            Povynno buty, vy - bezrobitnyi
            <% else if theNumberOfOccupations = 1 %>
            Za profesiieiu vy - 
            <% Request.QueryString("Occupation")(1) %>
            <% else %>
            Vy poiednuiete taki posady:
            <% Request.QueryString("Occupation")(1) %>
            <% For i = 2 to the NumberOfOccupations - 1 %>
            ,<%Request.QueryString("Occupations")(i) %>
            <% Next %>
            and <% Request.QueryString("Occupation")(theNumberOfOccupations) %>
            <END IF>
        .</p>
        <p><a href="next.htm">Dali</a></p>
    </body>
</html>