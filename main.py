#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from caesar import encrypt
import webapp2

inputFields = """
<form action="/secret" method="post">
	<label>
		I want to encrypt
		<input type="text" name="msg2crypt"/>
		<br /> with 
		<input type="number" name="numberOfTimes" value="1" min="1" max = "99"/> iterations
	</label>

	<input type="submit" value="Encrypt"/>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(inputFields)


class Secret(webapp2.RequestHandler):
	def post(self):
		msg = self.request.get("msg2crypt")
		numOTimes = self.request.get("numberOfTimes")
		reply = encrypt(msg, int(numOTimes))
		self.response.write(inputFields + '<hr />' + reply)
        


#         answer = encrypt("Hello, Zach!", 2)
# print(answer)
# # => prints Jgnnq, Bcej!

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/secret', Secret)
], debug=True)
