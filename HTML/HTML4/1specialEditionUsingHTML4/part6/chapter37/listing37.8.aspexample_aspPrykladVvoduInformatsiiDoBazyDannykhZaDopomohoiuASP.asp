<% datasource="PBOOK" tblNames="NAMES" tblAddr="ADDRESSES" if request ("ACT")="add" and request("OK") <> "" then
    on error resume next
    sql ="INSERT INTO NAMES (FNAME,LNAME) VALUES ('" +request ("FNAME") + "','"+
    request ("LNAME") + "')"
    set conn = Server.CreateObject("ADODB.Connection")
    set rs = Server.CreateObject("ADDODB.RecordSet")
    conn.Open datasource
    rs.Open sql, conn

    if err.number = 0 then response.redirect("pbook.asp")
    quit
    end if
    if request ("CANCEL") <> "" then
        response.redirect("pbook.asp")
        end if
        %>
        <html>

        <head>
            <meta name="GENERATOR" content="InCommand Interactive">
            <title>Shablon</title>
        </head>

        <body>
            <h1>Dodaty robotu</h1>
            <% if err.number> 0 then
                response.write("Pry dodanni tsoho imeni vyishla pomylka")
                end if
                %>
                <form method="post" action="addname.asp">
                    <input type="hidden" name="act" value="add">
                    <table>
                        <tr bgcolor="#cccccc">
                            <td id="fname">Imia #: </td>
                            <td>
                                <input name="fname" value="<%=request('FNAME')%>">
                            </td>
                        </tr>
                        <tr>
                            <td id="fname1" valign="top">Prizvyshie: </td>
                            <td><input name="lname" value="<%request('LNAME')%>"></td>
                        </tr>
                        <tr>
                            <td></td><input type="submit" name="ok" value="ok">&nbsp<input type="submit" name="ok"
                                value="ok">&nbsp
                            <input type="submit" name="cancel" value="Cancel"></td>
                        </tr>
                    </table>
                </form>
                <hr>
                <a href="main.asp">Holovne meniu</a>
        </body>

        </html>