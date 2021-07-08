#!/usr/bin/perl

#Copyright 1996, Robert Niles

$logfile = "redirect.log";

if ($ENV{'REQUEST_METHOD'} eq 'POST")
{
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
        ($name, $value) = split(/=/,$pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $contents{$name} = $value;
    }
}

chop($date = 'date');
&logit if $contents{'location'};
print "Content-type: text/html\n\n";
print <<"html";
<html>
    <head>
        <title>Whatever</title>
    </head>
    <body>
        <h1>Whatever</h1>
        <form action="/cgi-bin/redirect.pl" method="POST">
            <input type="submit" name="location" value="Infoseek"><br>
            <input type="submit" name="location" value="AltaVista"><br>
            <input type="submit" name="location" value="WebCrawler"><br>
        </form>
    </body>
</html>
html

exit;

sub logit {

    if ($contents{'location'} eq "Infoseek")
    {
        $location = "http://www.infoseek.com";
    }
    if ($contents{'location'} eq "AltaVista")
    {
        $location = "http://www.altavista.com";
    }
    if ($contents{'location'} eq "WebCrawler")
    {
        $location = "http://www.webcrawler.com";
    }

    open(LOG, ">>$logfile");
    print LOG "$date User clicked on: $contents{'location'}\n";
    close(LOG);
    print "Location: $location\n\n";
    exit;
}