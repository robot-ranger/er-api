# er.ReferencesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ref_get**](ReferencesApi.md#ref_get) | **GET** /transform/{ref_id} | 
[**references_get**](ReferencesApi.md#references_get) | **GET** /references | 

# **ref_get**
> Transform ref_get(ref_id, _from=_from)



Get transform to a specific reference (XYZRPY) (Meters and Radians)

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.ReferencesApi()
ref_id = 'ref_id_example' # str | UID of target reference
_from = '_from_example' # str | UID of base reference (default=World) (optional)

try:
    api_response = api_instance.ref_get(ref_id, _from=_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencesApi->ref_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_id** | **str**| UID of target reference | 
 **_from** | **str**| UID of base reference (default&#x3D;World) | [optional] 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **references_get**
> ReferenceArray references_get()



Get all defined references on the system

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.ReferencesApi()

try:
    api_response = api_instance.references_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencesApi->references_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReferenceArray**](ReferenceArray.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

