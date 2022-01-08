def html():
    # To use this routine the Media folder must be used for your output and picture files
    myHTML =  getMediaPath("myHTML.html")
    pictureFile = getMediaPath("barbara.jpg")
    eol=chr(11) # End-of-line character

    # The following line builds a literal string that includes both single and double quotes
    buildSpecial = "<IMG SRC= ̈"+ pictureFile + ’" ALT= "I am oneheck of a programmer!">’+eol
    outFile = open(myHTML,’w’)
    outFile.write( ’<HTML>’+eol)
    outFile.write(’<HEAD>’+eol)
    outFile.write(’<TITLE>Homepage of Georgia P. Burdell</TITLE>’+eol)
    outFile.write(’<LINK REL=STYLESHEET TYPE="text/css" HREF="style.css">’)
    outFile.write(’</HEAD>’+eol)
    outFile.write(’<BODY>’+eol)
    outFile.write(’<CENTER><H2>Welcome to the home page of GeorgiaP. Burdell!</H2></CENTER>’+eol)
    outFile.write(’<BR>’+eol)
    outFile.write(’<P> Hello, and welcome to my home page! As you should have already’+eol)
    outFile.write(’ guessed, my name is Georgia, and I am a <AHREF=http://www.cc.gatech.edu><B>’+eol)
    outFile.write(’Computer Science</B></A> major at <A HREF=http://www.gatecoutFile.write(’Georgia Tech</B> </A>’+eol)
    outFile.write(’<BR>’+eol)
    outFile.write(’Here is a picture of me in case you were wondering what I looked like.’+eol)
    outFile.write(’</P>’+eol)
    outFile.write(buildSpecial)
    # Write the special line we built up near the top
    outFile.write(’<P><H4> Well, welcome to my web page. The majority of it is still under construction, so I doń thave a lot to show you right now. ’+eol)
    outFile.write(’I am in my 75th year at Georgia Tech but am taking CS 1315 so I don ́thave a lot of spare time to update the page.’+eol)
    outFile.write(’I promise to start real soon!’+eol)
    outFile.write(’--Georgia P. Burdell</P></H4>’+eol)
    outFile.write(’<HR>’+eol)
    outFile.write(’<PIf you want to send me e-mail, click <><A HREF = "mailto:name@ece.gatech.edu">name@ece.gatech.edu</A>’+eol)
    outFile.write(’<HR></P>’+eol)
    outFile.write(’<CENTER><A HREF="http://www.cc.gatech.edu/">’+eol)
    outFile.write(’<IMG SRC="http://www.cc.gatech.edu/newhome_images/CoC_logo" ALT= "To my school"></CENTER>’+eol)
    outFile.write(’</A>’+eol)
    outFile.write(’</BODY>’+eol)
    outFile.write(’</HTML>’+eol)
    outFile.close()
