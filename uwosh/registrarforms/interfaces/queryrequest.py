from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from uwosh.registrarforms import registrarformsMessageFactory as _

class IQueryRequest(Interface):
    """a form to request a query"""
    
    # -*- schema definition goes here -*-
