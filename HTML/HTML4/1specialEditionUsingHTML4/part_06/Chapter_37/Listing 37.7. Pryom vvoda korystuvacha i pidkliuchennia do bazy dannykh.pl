#!/usr/bin/perl
# dbbooksearch.pl

use DB_File;
use Fcntl;
if ($ENV{'REQUEST_METHOD'} eq 'POST')
{
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eq;
        $form{$name} = $value;
    }
}
print "Content-type: text/html\n\n;

$file="addresses";
#database=tie(%db, "DB_File", $file, O_READ, 0640) || die "can't"
print <<"html";
<html>
    <head>
        <title>Rezultaty prostoi adresnoi knyhy dbm</title>
    </head>
    <body>
        <center>
            <h1>Rezultaty prostoi adresnoi knyhy</h1>
        </center>
        <table border=1>
        HTML

        while (($key,$value)=each(%db)) {
            if ($key =~ /$form{'name'}/i) {
                @part = split(/:/,$value);
                if ($part[0]) {
                    print "<tr><td><a href=\"mailto:$part[0]\">$key</a></td>";
                }
                else {
                    print "<tr><td>$key</td>";
                }
                print "<td>$part[0]</td><td>$part[1]</td></tr>\n";
            }
            }
print <<"html";
        </table>
        <p>
            <a href="/dbook.html">[Dodaty v adresnu knyhu]</a>
        </p>
    </body>
</html>

untie(%db);
undef($database);

exit;