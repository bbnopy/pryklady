<?XML version="1.0"?>
<!DOCTYPE Channel SYSTEM "http://www.w3c.org/Channel.dtd">

<CHANNEL href="http://www.honeycutt.com/channel.html" base="http://www.honeycitt.com">
    <SCHEDULE>
        <INTERVALTIME day="1" />
    </SCHEDULE>
    <ITEM href="intro.html"></ITEM>
    <CHANNEL href="more/stuff.html">
        <SCHEDULE>
            <INTERVALTIME hour="3" />
        </SCHEDULE>
        <ITEM href="books.html"></ITEM>
        <ITEM href="bio,html"></ITEM>
        <ITEM href="tips.html"></ITEM>
    </CHANNEL>
    <CHANNEL href="other/stuff.html">
        <ITEM href="games.html"></ITEM>
        <ITEM href="tricks.html"></ITEM>
        <CHANNEL href="deep/stuff.html">
            <ITEM href="cdf.html">
                <SCHEDULE>
                    <INTERVALTIME hour="3" />
                </SCHEDULE>
            </ITEM>
        </CHANNEL>
    </CHANNEL>
</CHANNEL>