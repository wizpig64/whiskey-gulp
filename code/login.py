#!/usr/bin/env python
import os

from tools import wget, searchinfile, COOKIEFILE, HTMLFILE

def amiloggedin(f, u):
    return bool(searchinfile(f, '<a href="/accounts/" class="user">%s' % u))

def gettoken():
    return searchinfile(COOKIEFILE, 'csrftoken\t(.+)').group(1)

def cleanup():
    os.remove(HTMLFILE)
    return

def logout():
    os.remove(COOKIEFILE)
    return

def login(userdict, verbose=False):
    username = userdict['username']
    password = userdict['password']
    #check login status
    if verbose: print "CHECKING LOGIN STATUS"
    wget('https://auth.whiskeymedia.com/accounts/', args='-q')
    if amiloggedin(HTMLFILE, username):
        if verbose: print "LOGGED IN AS %s" % username
        #done
    else:
        if verbose: print "NOT LOGGED IN, ATTEMPTING TO NOW..."
        #then try logging in now
        postdata = 'csrfmiddlewaretoken=%s&username=%s&password=%s' % (gettoken(), username, password)
        wget('https://auth.whiskeymedia.com/login/', args='-q --post-data \'%s\'' % postdata)
        if amiloggedin(HTMLFILE, username):
            if verbose: print 'LOGGED IN SUCCESSFULLY. YOU MAY NOW DOWNLOAD STUFF.'
        else:
            print 'Login failed! Check your info it conf/user.py'
            cleanup()
            return False
    
    cleanup()
    return True
