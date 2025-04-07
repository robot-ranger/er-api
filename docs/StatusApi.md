# er.StatusApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](StatusApi.md#status_get) | **GET** /status | 
[**status_put**](StatusApi.md#status_put) | **PUT** /status | 

# **status_get**
> Status status_get()



Get the current status of the robot

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.StatusApi()

try:
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_put**
> Status status_put(body)



Change the state of the robot

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.StatusApi()
body = er.StatusBody() # StatusBody | 

try:
    api_response = api_instance.status_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusBody**](StatusBody.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

