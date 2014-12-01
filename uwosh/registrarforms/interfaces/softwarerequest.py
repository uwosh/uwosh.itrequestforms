from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from uwosh.registrarforms import registrarformsMessageFactory as _

class ISoftwareRequest(Interface):
    """a form to request a software purchase"""
    
    # -*- schema definition goes here -*-
