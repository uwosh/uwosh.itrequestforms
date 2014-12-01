from Products.CMFCore.utils import getToolByName

def getLoggedInUserEmail(self):
    pm = getToolByName(self, 'portal_membership')
    if pm.isAnonymousUser():
        return ''
    else:
        member = pm.getAuthenticatedMember()
        return member.email 

def getLoggedInUserFullname(self):
    pm = getToolByName(self, 'portal_membership')
    if pm.isAnonymousUser():
        return ''
    else:
        member = pm.getAuthenticatedMember()
        return member.fullname 

