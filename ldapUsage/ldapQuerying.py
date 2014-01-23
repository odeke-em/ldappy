#!/usr/bin/env python

# Author: Emmanuel Odeke <odeke@ualberta.ca>
# Utility to aid you in looking up information about
# a user logged from an LDAP tree
import ldap
import copy
import constants # Local module

# Helper function
def mergeDicts(toDict, fromDict):
  #Copy items from 'fromDict' to 'toDict'
  if not (isinstance(fromDict, dict) and isinstance(toDict,dict)):
    return None

  for key in fromDict:
    keyCopy = copy.copy(key)
    valueCopy = copy.copy(fromDict[key])
    toDict[keyCopy] = valueCopy

def getLDAPInfo(searchParamDict):
  # Return results of a query on an ldap directory, given queryParameters 
  # and/or searchFilters eg 
  # To get users' phone numbers and emails whose 
  #   username is 'konradOno'
  #     results = getLDAPInfo(
  #       {
  #         constants.SEARCH_KEY_WORD:'(uid=*konradOno)', 
  #         constants.SEARCH_FILTERS_KEY:[constants.LDAP_MAIL_KEY, 
  #         constants.LDAP_PHONE_KEY]
  #     })
  #The results with have a meta section and a data section
  dataArray = list()
  metaDict = dict()
  resultsDict = dict()

  resultsDict[constants.DATA_KEY] = dataArray 
  resultsDict[constants.META_KEY] = metaDict
  
  #metaDict[constants.SEARCH_PARAMS_KEY] = None
  #metaDict[constants.SEARCH_FILTERS_KEY] = None 
  metaDict[constants.SUCCESS_STATUS_KEY] = False

  searchKeyWord = searchParamDict.get(constants.SEARCH_KEYWORD_KEY)
  print(searchParamDict, constants.SEARCH_KEYWORD_KEY)
  if hasattr(searchKeyWord, '__iter__'):
    searchKeyWord = "&".join(filter(lambda s: s, searchKeyWord))

  if not (isinstance(searchParamDict, dict) and searchKeyWord): return resultsDict

  print("srPD ", searchParamDict)

  # !!! Once you are ready to deploy and have made your certificate signed
  #  and recognized by the UOFA, set the last argument to True !!
  ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, False)
  uofa_ldapObject = ldap.initialize(constants.UOFA_LDAP_URI)
  defaultQueryParams = [constants.LDAP_SURNAME_KEY, constants.LDAP_PHONE_KEY, 
                        constants.LDAP_GIVEN_NAME_KEY, constants.LDAP_UID_KEY]
  givenFilters = searchParamDict.get(constants.SEARCH_FILTERS_KEY, defaultQueryParams)
  searchFilters = list()
  for aFilter in givenFilters:
    if ',' in aFilter:
      delimitedFilters = aFilter.split(',')
      searchFilters += map(lambda s: str(s), filter(lambda a:a, delimitedFilters))
    else: searchFilters.append(str(aFilter))
  print("searchFs ", searchFilters)
  #metaDict[constants.SEARCH_PARAMS_KEY] = searchKeyWord
  #metaDict[constants.SEARCH_FILTERS_KEY] = searchFilters
  try:
    searchResults = uofa_ldapObject.search_s(
     constants.UALBERTA_PEOPLE_TREE_SEARCH, ldap.SCOPE_SUBTREE,searchKeyWord,searchFilters
    )
  except Exception, e:
    #An unhandled exception occured here, implement handling later
    print(e)
  else:  
    metaDict[constants.SUCCESS_STATUS_KEY] = True
    resultsLen = len(searchResults)
    metaDict[constants.COUNT_KEY] = resultsLen
    dataArray = map(lambda tup: tup[1], searchResults)
    mergedDict = dict() 
    for eachDict in dataArray:
      mergeDicts(mergedDict, eachDict)
    resultsDict[constants.DATA_KEY] =mergedDict 

  return resultsDict

def main():
  results = getLDAPInfo(
    {
      constants.SEARCH_KEYWORD_KEY:'(uid=*klindenb)', 
      constants.SEARCH_FILTERS_KEY:[constants.LDAP_EMAIL_KEY, 
    constants.LDAP_PHONE_KEY]
    }
  )

  print(results)

if __name__ == '__main__':
  main()
