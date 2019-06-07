import cookielib
import urllib2
import mechanize

# Browser
br = mechanize.Browser()

cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar(cookiejar)

br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

# authenticate
response = br.open( "https://websim.worldquantchallenge.com/simulate" )
print response.read()
for form in br.form.controls:
    print form
br.select_form( name="EmailAddress" )
# these two come from the code you posted
# where you would normally put in your username and password
br["EmailAddress" ] = "qiao.xu@stonybrook.edu"
br[ "Password" ] = "yourleave@"
res = br.submit()

print "Success!\n"
