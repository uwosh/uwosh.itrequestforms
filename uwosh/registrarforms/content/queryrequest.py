"""Definition of the QueryRequest content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.registrarforms.content.request_base import RequestSchema

from uwosh.registrarforms import registrarformsMessageFactory as _
from uwosh.registrarforms.interfaces import IQueryRequest
from uwosh.registrarforms.config import PROJECTNAME

QueryRequestSchema = RequestSchema.copy() + atapi.Schema((
    atapi.StringField(
        'requestedbefore',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Is this a new list or have you requested it before?"),
        ),
        vocabulary=['New','Previously requested'],
        required=True,
    ),
    
    atapi.StringField(
        'havequeryname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"If it was previously requested, do you have the name of the query?"),
        ),
        vocabulary=['Yes','No'],
    ),

    atapi.StringField(
        'queryname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"If you answered yes above, what is the query name?"),
        ),
    ),

    atapi.StringField(
        'infousers',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Who will be using or viewing this information?"),
        ),
        required=True,
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

QueryRequestSchema['title'].storage = atapi.AnnotationStorage()
QueryRequestSchema['description'].storage = atapi.AnnotationStorage()

QueryRequestSchema['title'].widget.label = 'Query Request Title'
QueryRequestSchema['description'].widget.description = 'Please describe the query'
QueryRequestSchema['description'].required = True

schemata.finalizeATCTSchema(QueryRequestSchema, moveDiscussion=False)
QueryRequestSchema.changeSchemataForField('relatedItems', 'default')

class QueryRequest(base.ATCTContent):
    """Query Request Form"""
    implements(IQueryRequest)

    meta_type = "QueryRequest"
    schema = QueryRequestSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    from uwosh.registrarforms.content.utils import getLoggedInUserEmail
    from uwosh.registrarforms.content.utils import getLoggedInUserFullname

atapi.registerType(QueryRequest, PROJECTNAME)
