# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Bind the App Engine service endpoints."""

__author__ = 'John Orr (jorr@google.com)'

# Add the library location to the path
import sys
sys.path.insert(0, 'lib')

import webapp2

# The following import is needed in order to add third-party libraries
# before loading any other modules.
import appengine_config  # pylint: disable-msg=unused-import

import handlers
from oauth.handler import OAUTH_ROUTES

MAIN_ROUTES = [
    ('/handler/(\d*)/(.*)/', handlers.XBlockEndpointHandler),
    ('/display_xblock', handlers.DisplayXblockPageHandler),
    ('/rest/xblock', handlers.XblockRestHandler),
    ('/rest/xblock/(\d*)', handlers.XblockRestHandler),
    ('/.*', handlers.DefaultPageHandler),
]

ROUTES = OAUTH_ROUTES + MAIN_ROUTES

app = webapp2.WSGIApplication(ROUTES, debug=True)
