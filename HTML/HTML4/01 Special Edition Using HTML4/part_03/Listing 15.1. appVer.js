var theNavigatorResult = navigator.appVersion.indexOf("\(Win");
var theExplorerResult = navigator.appVersion.indexOf("windows");

// Zapudhcheni na tsomu kompiuteri Netscape i  Windows
if (theNavigatorResult != -1)
{
    document.write("<p>Shchob zminyty shryft v Netscape Navigator, vyberit Edit, Preference. Potim vyberit Appearance, Fonts. Vstanovit potribni rozmiry shryftiv i vyberit \"Use my default fonts, overriding document specific fonts.\"</p>");
}
else
if (theExplorerResult != -1)
{
    if (navigator.appVersion.indexOf("MSIE 4") == -1)
    {
        document.write("<p>Shchob zminyty rozmir shryftu v Microsoft Internet Explorer, vyberit View, Fonts i vstanovit potribni rozmiry shryftiv.</p>");
    }
}