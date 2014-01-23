#!/usr/bin/env python

# Author: Emmanuel Odeke <odeke@ualberta.ca>
# Module to aid with authentication with LDAP which is used
# by the University of Alberta, and affiliates

import re
import constants # Local module

# CCID -- Campus Computing ID. Criteria for a valid ccid
#    ->Must consist entirely of alphanumeric characters
#    ->Max length: 7 characters
CCID_REGEX = "^([a-z0-9]{1,7})$"
ccidCompile = re.compile(CCID_REGEX,re.IGNORECASE|re.UNICODE)

def emailValid(queryEmail):
  # Input: A potential email string
  # Returns: 0 on success, else the error description

  return False

def ccidValid(queryCCID):
  print("Validating ", queryCCID)
  # Arg: A ccid string to be validated
  # Returns: True if queryCCID passes the validation criteria
  return (queryCCID and ccidCompile.search(queryCCID))

def nonSerializable(obj):
  # Input: An arbitrary Python object
  # An object is serializable only iff an iterator can be created from it.
  # Returns True iff an object is non serializable, else False
  # print("OBJ ",obj)
  try:
    iterator = iter(obj)
  except TypeError:
    return True 
  else: 
    return False 

def credentialsBind(ccid, password):
  # Args: ccid, password. Both non-empty strings
  # Returns: True iff the ccid and password bind with the UofA LDAP service

  if not (ccid and password): # Empty credentials not allowed
    return False

  if not ccidValid(ccid): 
    print("invalid ccid")
    return False

  ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, False)
  uofa_ldapObject = ldap.initialize(constants.UOFA_LDAP_URI)

  # The authentication attempt here
  # Note: DN in full: Distinct Name
  LOGIN_DN = "uid=%s,%s"%(ccid, constants.UALBERTA_PEOPLE_TREE_SEARCH)

  try:
    uofa_ldapObject.bind_s(LOGIN_DN, password)
  except ldap.INVALID_CREDENTIALS, e: # Failed to authenticate
    return False
  except Exception, e:
    # An unhandled exception occured here, implement handling later
    return False
  else:  return True
