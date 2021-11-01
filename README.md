# max_count_api_searchresults
Anytime when you implement API access to Splunk's search results, search results will be limitted to the maximum of 50K events.
For example, if a search produces 100K events, the API will only retunr 50K events regardless.

In order to fix this, increase two settings in Splunk configuration files.

1. Increase maxresultrows settings.

[restapi]
maxresultrows = <inMaximum result rows to be teger>
* returned by /events or /results getters from REST
  API.
* Default: 50000
https://docs.splunk.com/Documentation/Splunk/latest/Admin/Limitsconf

  
2. Pass max_count parameter along with the API call.
e.g.
max_count=50000
