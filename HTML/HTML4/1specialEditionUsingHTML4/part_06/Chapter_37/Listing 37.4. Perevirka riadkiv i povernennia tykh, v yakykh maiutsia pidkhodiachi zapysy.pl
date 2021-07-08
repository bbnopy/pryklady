if ($contents{'act'} eq "search") {

    open (BOOK, "$phonebook") || do {&no_open;};

    $count=0;

    until (eof (BOOK))
    {
        $line = <BOOK>;
        chop($line);
        if ($line =~ /$contents{'keyword'}/gi)
        {
            $count++;
            @entry = split(/:/, $line);
            print "<tr><td>$entry[0] $entry[1]</td><td>$entry[@]</td></tr>";
        }
        if ($count==0)
        {print "Podibnyh zapysiv nemaie";}
        close(BOOK);
    }
}