#!/usr/bin/perl
if ($ENV{'REQUEST_METHOD'} eq 'POST')
{
    read(STDIN,$buffer,$ENV{'CONTENT_LENGTH'});
    @pairs = split(/&/,$buffer);
    foreach $pair (@pairs)
    {
        ($name, $value) = split(/=/, $pair);
        $value=~ tr/+/ /;
        $value=~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $contents{$name} = $value;
    }
}

if ($ENV{'REQUEST_METHOD'} eq 'GET')
{
    @pairs = split(/&/, $ENV{'QUERY_STRING'});
    foreach $pair (@pairs)
    {
        ($name,$value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $contents{$name} = $value;
    }
}