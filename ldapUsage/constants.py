# Author: Emmanuel Odeke <odeke@ualberta.ca>
# Resource file for constants

import sys

############################CONSTANTS####################################
ID_KEY = "id"
URL_KEY   = "url"
NAME_KEY  = "name"
EMAIL_KEY = "email"
PHONE_KEY = "phone"
CCID_KEY  = "ccid"
PASSWORD_KEY= "password"
OTHER_INFO_KEY = "other_info"
ATTACHMENT_KEY   = "attachmentLink"
REDIRECT_URL_KEY = "redirectUrl"
CREDENTIAL_VALIDITY_KEY = "credential_validity"

#Suffices
SET_SUFFIX = "_set"
ID_SUFFIX  = "_id"

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

#Short-form values of the different actor types
MANAGER   = "Manager"
REPORTER  = "Reporter"
REQUESTER = "Requester"
WORKER    = "Worker"

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

#Pagination keys
LONG_KEY = "long"
SHORT_KEY = "short"
LIMIT_KEY = "limit"
STATUS_KEY = "status"
FORMAT_KEY = "format"

#Thresholds here
THRESHOLD_LIMIT = 50
THRESHOLD_OFFSET = 0
THRESHOLD_TIME_LAPSE = 20

#JSON return form keys
META_KEY = "meta"
DATA_KEY = "data"

#Sort keys
SORT_KEY = "sort"
COUNT_KEY = "count"
OFFSET_KEY  = "offSet"
REVERSE_SUFFIX = "_r"

ALL_KEY = "all"
TIME_LAPSE_KEY = "timeLapse"
QUERY_TABLE_NAME_KEY = "queryTable"

SAVE_KEY = "save"
UNDERSCORE_KEY = "_"
NUMERICAL_DIV_ATTR = "__div__" #All number like objects accept division
LAST_EDIT_TIME_KEY = "lastEditTime"

CHANGES_MADE_KEY = "nChanges"
LAST_STATUS_EDIT_KEY = "lastStatusEditTime"
REQUESTER_PASSWORD_KEY = "requesterpass"

#GroupKeys
WORKER_GROUP_KEY = "WorkerGroup"
MANAGER_GROUP_KEY = "ManagerGroup"
REQUESTER_GROUP_KEY = "RequesterGroup"

#Redirect URLs
MANAGER_PAGE_URL = "/ece_resources_app/managerpage"
REQUESTER_PAGE_URL = "/ece_resources_app/requesterpage"
WORKER_PAGE_URL = "/ece_resources_app/mytasklist"
ERROR_PAGE_URL = "/?status=error"
INDEX_ROOT_URL = "/" #"index.html"
INVALID_LOGIN_ROLE_URL = "/?status=invalidloginrole"
INVALID_CREDENTIALS_PAGE_URL = "/?status=invalidcredentials"

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

#Extensions
CSV_EXTENSION = "csv"
JSON_EXTENSION = "json"
