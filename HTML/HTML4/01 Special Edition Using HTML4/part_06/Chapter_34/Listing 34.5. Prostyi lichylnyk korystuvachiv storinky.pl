#!/usr/bin/perl
# simplecount 1.0
# count.pl

$uri = $ENV{'DOCUMENT_URI'};

$countfile = "count";

print "Content-type: text/html\n\n";

open(COUNT, "+<$countfile") || do{
    print "Ne mozhu vidkryty fail-rakhivnyk";
    die; };
flock(COUNT, 2);

while (<COUNT>) {
    chop;
    ($file, $count) = split(/:/,$_);
    $counts{$dile} = $count;
}

$counts{$uri}++;

seek(COUNT, 0, 0);

foreach $file (keys %counts) {
    print COUNT $file, ":", $counts{$file}, "\n";
}

flock(COUNT, 8);
close(COUNT);

print $counts{uri};

exit;