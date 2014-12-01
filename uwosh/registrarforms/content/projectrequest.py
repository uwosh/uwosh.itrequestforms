"""Definition of the projectrequest content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base, schemata

from uwosh.registrarforms.content.request_base import RequestSchema

from uwosh.registrarforms import registrarformsMessageFactory as _
from uwosh.registrarforms.interfaces import IProjectRequest
from uwosh.registrarforms.config import PROJECTNAME

ProjectRequestSchema = RequestSchema.copy() + atapi.Schema((
    
    atapi.StringField(
        'requires_identifiable_information',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Does your request require the use or storage of personally identifiable information covered by FERPA, HIPPA, PCL, etc.?"),
            description=_(u"What is FERPA? For information on the UWO FERPA and other policies, please refer to the portlet on this page"),
        ),
        vocabulary=['Yes','No'],
        required=True,
    ),

    atapi.StringField(
        'requires_existing_data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Do you need data from existing systems?"), 
            format='radio',
        ),
        vocabulary=['Yes','No'],
        required=True,
    ),

    atapi.StringField(
        'existing_data_needed',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Please specify the data needed from existing systems."),
            description=_(u"If you answered \"Yes\" above, please indicate which of the following data is needed from the existing Student Information System (PeopleSoft) or other campus systems"),
            format='checkbox',
        ),        
        vocabulary=['none needed',
                    'Student Demographic Data',
                    'Student Academic Data (GPA, major, etc.)',
                    'Enrollment Data',                   
                    'Course Catalog/Class Listing data', 
                    'Student Course Schedule data', 
                    'Admissions data', 
                    'Financial Aid data', 
                    'Student Account data', 
                    'Employee data', 
                    'Student/Employee Login data', 
                    'Other - please specify below'],
        required=True,
    ),
    
    atapi.TextField(
        'existing_data_needed_comments',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Data Comments"),
            description=_(u"Please provde details if you selected Other above"),
            rows=3,
        ),
    ),
    
    atapi.StringField(
        'data_users',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Who will be using the data?"),
            format='checkbox',
        ),        
        vocabulary=['Faculty/Instructors',
                    'Academic Staff',
                    'Classified Staff',
                    'Student Employees',
                    'Third Party - please explain below',
                    'Other - please explain below'],
        required=True,
    ),
    
    atapi.TextField(
        'data_users_comments',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Data User Comments"),
            description=_(u"Please explain who will use the data if you chose 'Third Party' or 'Other' above"),
            rows=3,
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ProjectRequestSchema['title'].storage = atapi.AnnotationStorage()
ProjectRequestSchema['description'].storage = atapi.AnnotationStorage()

ProjectRequestSchema['title'].widget.label = 'Project Request Title'
ProjectRequestSchema['description'].widget.description = 'Please describe the project'
ProjectRequestSchema['description'].required = True

schemata.finalizeATCTSchema(ProjectRequestSchema, moveDiscussion=False)
ProjectRequestSchema.changeSchemataForField('relatedItems', 'default')

class ProjectRequest(base.ATCTContent):
    """Project Request Form"""
    implements(IProjectRequest)

    meta_type = "ProjectRequest"
    schema = ProjectRequestSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    from uwosh.registrarforms.content.utils import getLoggedInUserEmail
    from uwosh.registrarforms.content.utils import getLoggedInUserFullname

atapi.registerType(ProjectRequest, PROJECTNAME)
