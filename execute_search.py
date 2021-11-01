###############################################

  # Execute search on remote Search Head instance

  def execute_search(self):

    #
    #
    cmdurl = '/services/search/jobs'
    #
    # Pass the search (contained in searchStr) with the
    #   REST API endpoint.
    #
    self.serverResponse = myhttp.request(baseurl + cmdurl, 'POST',
                                    headers={'Authorization': 'Splunk %s' % self.sessionKey},
                                    body=urllib.parse.urlencode(
                                      {'output_mode': 'json',
                                       'search': self.searchStr,
                                       'max_count': max_count}))[1]  # max_count paramter for the number events
    #
