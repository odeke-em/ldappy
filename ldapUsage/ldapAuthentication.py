#!/usr/bin/env python

# Author: Emmanuel Odeke <odeke@ualberta.ca>
# Module to aid with authentication with LDAP which is used
# by the University of Alberta, and affiliates

import re
import sys
import ldap

import constants # Local module

pyVersion = sys.hexversion/(1<<24)
stdinReader = raw_input if pyVersion < 3 else input

# CCID -- Campus Computing ID. Criteria for a valid ccid
#    ->Must consist entirely of alphanumeric characters
#    ->Max length: 7 characters
CCID_REGEX = "^([a-z0-9]{1,7})$"
ccidCompile = re.compile(CCID_REGEX,re.IGNORECASE|re.UNICODE)

def ccidValid(queryCCID):
  print("Validating ", queryCCID)
  # Arg: A ccid string to be validated
  # Returns: True if queryCCID passes the validation criteria
  return (queryCCID and ccidCompile.search(queryCCID))

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

def main():
  ccid = stdinReader("\033[93mCCID: \033[00m")
  password = stdinReader("\033[94mPassword: \033[00m") 
  # !!!Use actual tty settings to turn off character echoing!!!

  print(credentialsBind(ccid, password))
if __name__ == '__main__':
  main()
