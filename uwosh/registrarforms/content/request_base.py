"""Defines the base schema for the request types
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base, schemata
from uwosh.registrarforms import registrarformsMessageFactory as _

import time

RequestSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField(
        'name',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Your Name"),
            description='',
        ),
        required=True,
        default_method='getLoggedInUserFullname',
    ),

    atapi.StringField(
        'email',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Your Email"),
            description='',
        ),
        required=True,
        default_method='getLoggedInUserEmail',
        validators=('isEmail',),
    ),    

    atapi.StringField(
        'department',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Your Department"),
            description='',
        ),
        required=True,
        default='',
    ),    

    atapi.StringField(
        'phone_number',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Your Phone Number"),
            description='',
        ),
        required=True,
        default='',
    ),    

    atapi.TextField(
        'consequences',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"What are the consequences if this project is not completed?"),
            rows=5,
        ),
    ),
    
    atapi.DateTimeField(
        'ideal_date',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u'Project Needed By'),
            format='%Y-%b-%d',
            show_hm=False,
            starting_year=time.localtime()[0],
        ),
        required=True,
    ),

    atapi.StringField(
        'mandated_by',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"The above date is"),
            format='radio',
        ),
        vocabulary=['Mandated by an agency outside of the University',
                    'Mandated by UW System policy',
                    'Mandated by UW Oshkosh Administration or Faculty policy',
                    'Preferred date for optimal implementation',
                    'Other - please comment below'],
        required=True,
    ),

    atapi.TextField(
        'date_comments',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Date Comments"),
            description=_(u"Please provide detail about your date requirements"),
            rows=3,
        ),
        required=True,
    ),

    

))


