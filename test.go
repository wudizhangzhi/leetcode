package main

import (
	"fmt"
	"regexp"
	"strings"
)

var pattern = `^(INFO|WARNING|ERROR)`
var negate = true

var content = `
ERROR:bdzh.pipelines(2021-09-08 14:00:05; pipelines.py:913): status_code:200,monitor_change:1,change_ratio:None 
ERROR:bdzh.pipelines(2021-09-08 14:00:05; pipelines.py:213): es存储失败,Traceback (most recent call last):
  File "/data/projects/bdzh-spiders/bdzh/pipelines.py", line 174, in _process_item
    response = s.execute()
  File "/usr/local/python38/lib/python3.8/site-packages/elasticsearch_dsl/search.py", line 695, in execute
    es.search(
  File "/usr/local/python38/lib/python3.8/site-packages/elasticsearch/client/utils.py", line 84, in _wrapped
    return func(*args, params=params, **kwargs)
  File "/usr/local/python38/lib/python3.8/site-packages/elasticsearch/client/__init__.py", line 810, in search
    return self.transport.perform_request(
  File "/usr/local/python38/lib/python3.8/site-packages/elasticsearch/transport.py", line 318, in perform_request
    status, headers_response, data = connection.perform_request(method, url, params, body, headers=headers, ignore=ignore, timeout=timeout)
  File "/usr/local/python38/lib/python3.8/site-packages/elasticsearch/connection/http_urllib3.py", line 239, in perform_request
    self._raise_error(response.status, raw_data)
  File "/usr/local/python38/lib/python3.8/site-packages/elasticsearch/connection/base.py", line 131, in _raise_error
    raise HTTP_EXCEPTIONS.get(status_code, TransportError)(status_code, error_message, additional_info)
elasticsearch.exceptions.NotFoundError: NotFoundError(404, 'index_not_found_exception', 'no such index [bdzh_spider]', bdzh_spider, index_or_alias)
 
ERROR:bdzh.pipelines(2021-09-08 14:00:08; pipelines.py:913): status_code:200,monitor_change:1,change_ratio:None 

`

func main() {
	regex, err := regexp.Compile(pattern)
	if err != nil {
		fmt.Println("Failed to compile pattern: ", err)
		return
	}

	lines := strings.Split(content, "\n")
	fmt.Printf("matches\tline\n")
	for _, line := range lines {
		matches := regex.MatchString(line)
		if negate {
			matches = !matches
		}
		fmt.Printf("%v\t%v\n", matches, line)
	}
}
