#!/usr/bin/perl
# dbbook.pl
use DB_File;
use Fcntl;
print "Content-type: text/html\n\n";
$file="addresses";
$database=tie(%db, 'DB_File', $file, O_READ, 0640) || die "can't";
print <<"html";
<html>
    <head>
        <title>Prosta adresna knyha dbm</title>
    </head>
    <body>
        <center>
        <h1>Prosta adresna knyha</h1>
        <table border=1></table>
        HTML

        while (($key,$value)= each(%db)) {
            @part = split(/:/,$value);

            if ($part[0]) {
                print "<tr><td><a href=\"mailto:$part[0]\">$key</a></td>";
            }
            else {
                print "<tr><td>$key</td>";
            }
            
            print "<td>$part[0]</td><td>$part[1]</td></tr>\n;
        }
print <<"html";
        </table>
        <p>
            <a href="/dbook.html">[Dodaty do adresnoi knyhy]</a>
        </p>
    </body>
</html>
HTML
unite(%db);
undef($database);
exit;