if ($contents{'act'} eq "display") {

    open (BOOK, $phonebook) || do {&no_open;};
    until (eof(BOOK))
    {
        $line = <BOOK>;
        @entry = split(/:/, $line);
        print "<tr><td>$entry[0] $entry[1]</td><td> $entry[2]</td></tr>";
    }

    close(BOOK);
}