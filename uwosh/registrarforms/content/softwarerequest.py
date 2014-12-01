"""Definition of the SoftwareRequest content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.registrarforms.content.request_base import RequestSchema

from uwosh.registrarforms import registrarformsMessageFactory as _
from uwosh.registrarforms.interfaces import ISoftwareRequest
from uwosh.registrarforms.config import PROJECTNAME

SoftwareRequestSchema = RequestSchema.copy() + atapi.Schema((
    
    atapi.StringField(
        'install_location',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Installation Location"),
            description=_(u"Where will the software be installed?"),
            format='radio',
        ),
        vocabulary=['On a single computer',
                    'On a campus network server',
                    'Hosted off compus',
                    'Don\'t know/not sure where software will be installed'],
        required=True,
    ),

    atapi.StringField(
        'login_type',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Login Required"),
            description=_(u"Will the software require a login?"),
            format='radio',
        ),
        vocabulary=['Uses the university email login',
                    'Uses its own unique login',
                    'Does not require a login',
                    'Don\'t know/not sure of login process'],
        required=True,
    ),

    atapi.StringField(
        'individual_data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Will you enter or use data about individuals (students, faculty, staff)?"),
            description=_(u""),
            format='radio',
        ),
        vocabulary=['Yes','No'],
        required=True,
    ),

    atapi.StringField(
        'university_data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Do you need access to any university data?"),
            description=_(u"If 'Yes' you must also fill out a Project Request Form"),
            format='radio',
        ),
        vocabulary=['Yes','No'],
        required=True,
    ),

    atapi.StringField(
        'responsible_data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Will you use data the university is responsible for, even if the software does not access an existing system for it?"),
            description=_(u"For details on what sort of data the university is responsible for, please see the portlet on this page"),
            format='radio',
        ),
        vocabulary=['Yes','No'],
        required=True,
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SoftwareRequestSchema['title'].storage = atapi.AnnotationStorage()
SoftwareRequestSchema['description'].storage = atapi.AnnotationStorage()

SoftwareRequestSchema['title'].widget.label = 'Software Request Title'
SoftwareRequestSchema['description'].widget.description = 'Please describe the software'
SoftwareRequestSchema['description'].required = True

schemata.finalizeATCTSchema(SoftwareRequestSchema, moveDiscussion=False)
SoftwareRequestSchema.changeSchemataForField('relatedItems', 'default')

class SoftwareRequest(base.ATCTContent):
    """Software Request Form"""
    implements(ISoftwareRequest)

    meta_type = "SoftwareRequest"
    schema = SoftwareRequestSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    from uwosh.registrarforms.content.utils import getLoggedInUserEmail
    from uwosh.registrarforms.content.utils import getLoggedInUserFullname

atapi.registerType(SoftwareRequest, PROJECTNAME)
