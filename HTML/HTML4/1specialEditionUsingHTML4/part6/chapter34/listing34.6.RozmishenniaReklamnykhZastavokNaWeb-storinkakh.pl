#!/usr/bin/perl
#randpic.pl

@pics = ("pics/cgiad.gif", "pics/img2.gif");

@url = ("www.selah.net/rate.html", "www.in-command.com/");

@alt = ("The CGI Collection", "InCommand Internet Marketing");

@comment = ("Reklama v Web za dopomohoiu Kolektsii CGI", "Dodatok dlia biznesa v Intranet\/Internet");

# Teper my vyberaiemo vypadkove chyslo i prysvoiuiemo ioho zminnoiu $picnum

srand(time ^ $$);
$picnum = rand(@pics);
# Teper my pokazuiemo same oholoshennia.
# Ya vykorystovuval tablytsiu dlia formatuvannia vykhidnoi informatsii.

print "Content-type: text/html\n\n";
print "<table border=0>";
print "<tr><td align=center>";
print "<a href=\"http://$url[$picnum]\">"
print "<img src=\"$pics[$picnum]\" alt=\"$alt[$picnum]\" vorder=0>";
print "<\a>"
print "</td></tr>";
print "<tr><td align=center>";
print "<a href=\"http://$url[$picnum]\">$comment[$picnum]</a>";
print "</td></tr>";
print "</table>";
exit;