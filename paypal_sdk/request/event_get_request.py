# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# event_get_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.get","Description":"Shows details for a webhook event notification, by ID.","Parameters":[{"Type":"string","VariableName":"event_id","Description":"The ID of the webhook event notification for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks-events/{event_id}","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class EventGetRequest (HttpRequest):
    """
    Shows details for a webhook event notification, by ID.
    """

    def __init__(self):
        super(EventGetRequest, self).__init__("/v1/notifications/webhooks-events/{event_id}", "GET")
        self.headers["Content-Type"] = "application/json"

    def eventId(self, eventId):
        self.url = self.path.replace("{event_id}", str(eventId))
        return self
    
