# er.ProgramsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**programs_current_get**](ProgramsApi.md#programs_current_get) | **GET** /programs/current | 
[**programs_current_put**](ProgramsApi.md#programs_current_put) | **PUT** /programs/current | 
[**programs_get**](ProgramsApi.md#programs_get) | **GET** /programs | 

# **programs_current_get**
> Program programs_current_get()



Get the currently loaded program

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.ProgramsApi()

try:
    api_response = api_instance.programs_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramsApi->programs_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Program**](Program.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **programs_current_put**
> programs_current_put(body)



Load a new program

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.ProgramsApi()
body = er.Program() # Program | Program name

try:
    api_instance.programs_current_put(body)
except ApiException as e:
    print("Exception when calling ProgramsApi->programs_current_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Program**](Program.md)| Program name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **programs_get**
> ProgramArray programs_get()



Get all available programs on the robot

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.ProgramsApi()

try:
    api_response = api_instance.programs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramsApi->programs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProgramArray**](ProgramArray.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

