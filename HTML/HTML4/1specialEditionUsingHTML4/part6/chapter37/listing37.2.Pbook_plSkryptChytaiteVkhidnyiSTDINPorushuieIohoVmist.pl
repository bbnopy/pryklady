if ($ENV {'REQUEST_METHOD'} eq 'POST')
{
    read (STDIN, $buffer, $ENV{ 'CONTENT_LENGTH' });
    @pairs = split(/&/, $buffer);
    foreach $pair (@paris) {
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $contents{$name} = $value;
}
}
print "Content-type: text/html\n\n;
$phonebook = "phonebk.txt";
if ($contents{'act'} eq "add") {
    open (BOOK, ">>$phonebook") || do {&no_open;};
    print book
    "$contents{'fname'}:$contents{'lname'}:$contents{'phone'}\n";
    close(BOOK);
    print <<"HTML";
    <html>
    <head>
        <title>Dodana informatsiia</title>
    </head>
    <body>
        <h1>Dodana informatsiia</h1>
        Vvedena informatsiia bula dodana v telefonu knyhu.
        <hr>
        <center>
            <a href="/pbook.html">{Povernutysia do telefonnoi knyhy}</a>
        </center>
    </body>
    </html>
    HTML
    exit;
}
sub no_open {
    print <<"HTML";
    <html>
    <head>
        <title>Pomylka!</title>
    </head>
    <body>
        <h1>Pomylka! Ne mozhu vidkryty bazu dannykh!</h1>
        <center>
            <a href="/pbook.html">[Povernennia do telefonnoi knyhy]</a>
        </center>
    </body>
    </html>
    HTML
    exit;
}