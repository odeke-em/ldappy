# Author: Emmanuel Odeke <odeke@ualberta.ca>
# Resource file for constants

import sys

############################CONSTANTS####################################
UALBERTA_DOMAIN_KEY = "ualberta.ca"

DATE_KEY    = "date"
LAST_NAME_KEY  = "lastname"
FIRST_NAME_KEY = "firstname"
SPEED_CODE_KEY = "speedCode" #code for account purposes
DESCRIPTION_KEY = "description"
DEADLINE_DATE_KEY = "deadlineDate"
TYPEOF_REQUEST_KEY = "typeOfRequest" #To be takenout in favour of 'requestType'
REQUEST_TYPE_KEY   = "requestType"
NAMEOF_REQUEST_KEY = "nameOfRequest"
REQUESTER_CCID_KEY ="requesterCCID"
SUBMISSION_DATE_KEY = "submissionDate"

#Credential and connection-related keys
UOFA_LDAP_URI = "ldaps://directory.srv.ualberta.ca"
CREDENTIAL_VALIDITY_KEY = "credential_validity"

#Return values 
ERROR_ID = -1
SAVE_SUCCESS = 1
SAVE_FAILURE = 0
LOGIN_SUCCESS = 0xfff
LOGIN_FAILURE = ~LOGIN_SUCCESS
UNKNOWN_OBJECT = -1

#Thresholds here
THRESHOLD_LIMIT = 50
THRESHOLD_OFFSET = 0
THRESHOLD_TIME_LAPSE = 20

#JSON return form keys
META_KEY = "meta"
DATA_KEY = "data"
COUNT_KEY = "count"

#Sort keys
NUMERICAL_DIV_ATTR = "__div__" #All number like objects accept division
LAST_EDIT_TIME_KEY = "lastEditTime"

#LDAP SEARCH FIELDS
LDAP_UID_KEY = "uid"
LDAP_CITY_KEY = "l"
LDAP_TITLE_KEY = "title"
LDAP_EMAIL_KEY = "mail"
LDAP_PHONE_KEY = "telephoneNumber"
LDAP_STREET_KEY = "street"
LDAP_SURNAME_KEY = "sn"
LDAP_DISPLAY_NAME = "displayName"
LDAP_GIVEN_NAME_KEY = "givenName"
LDAP_COMMON_NAME_KEY = "cn"
LDAP_POSTAL_CODE_KEY = "postalCode"
LDAP_ROOM_NUMBER_KEY = "roomNumber"
LDAP_DISTINCT_NAME_KEY = "dn"
LDAP_PROVINCE_STATE_KEY = "st"
UALBERTA_PEOPLE_TREE_SEARCH = "ou=people,dc=ualberta,dc=ca"

QUERY_ARGS_KEY = "queryArgs"
SEARCH_PARAMS_KEY = "searchParameters"
SEARCH_FILTERS_KEY = "searchFilters"
SEARCH_KEYWORD_KEY = "searchKeyWord"
SUCCESS_STATUS_KEY = "success"
