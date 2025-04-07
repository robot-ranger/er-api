# er.FilesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file**](FilesApi.md#download_file) | **GET** /download/{folder}/{file_name} | 
[**upload_file**](FilesApi.md#upload_file) | **PUT** /upload | 

# **download_file**
> InlineResponse200 download_file(folder, file_name)



Downloads a file

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.FilesApi()
folder = 'folder_example' # str | Name of the folder where the file is located
file_name = 'file_name_example' # str | Name of the file to download

try:
    api_response = api_instance.download_file(folder, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Name of the folder where the file is located | 
 **file_name** | **str**| Name of the file to download | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> InlineResponse2001 upload_file(file=file)



Uploads a file

### Example
```python
from __future__ import print_function
import time
import er
from er.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = er.FilesApi()
file = 'file_example' # str |  (optional)

try:
    api_response = api_instance.upload_file(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

