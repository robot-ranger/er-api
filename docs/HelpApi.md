# er.HelpApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datatypes**](HelpApi.md#get_datatypes) | **GET** /help/datatypes | 

# **get_datatypes**
> DatatypeDictionary get_datatypes()



Get a dictionary from supported datatypes to IDs

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.HelpApi()

try:
    api_response = api_instance.get_datatypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelpApi->get_datatypes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatatypeDictionary**](DatatypeDictionary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

