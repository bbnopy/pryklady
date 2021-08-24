#!/usr/bin/perl
$mailprog = "/usr/lib/sendmail";
$recipient = "user\@foo.bar.com";

if ($ENV{'REQUEST_METHOD'} eq 'POST')
{
    read(STDIN, $buffer, $ENV{"CONTENT_LENGTH'});
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-Fa-F0-9])/pack("C", hex($1))/eg;
        $contents{$name} = $value
    }
}

# Vidkryttia poshty
open(MAIL, "|$mailprog -t") || die "Ne mozhu vidkryty $mailprog!\n";
print MAIL "To: $recipient\n";
print MAIL "From: $contents{'email'} <$contents'realname'}>\n;
print MAIL "Subject: $#contents{'subject'}\n\n";
print MAIL "$contents{'comments'}\n\n";
close (MAIL);

print <<"HTML";
<html>
    <head>
        <title>Diakuiu Vam!</title>
    </head>
    <body bgcolor="#fff">
        <h1>Diakuiu Vam!</h1>
        <p>Diakuiu za Vashi lomentari!</p>
        <hr>
        <center>
            <a href="http://www.selah.net/cgi.html">[Povernennia na holovnu storinlu]</a>
        </center>
    </body>
</html>
exit;