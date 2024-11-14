""" 
blocklist.py

this file just contains the blocklist of jwt tokens. 
it will be imported by app and the logout resource so 
that tokend=s can be added to the blocklist when the user logs out.

"""

BLOCKLIST = set()
