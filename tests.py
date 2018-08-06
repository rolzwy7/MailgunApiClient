import unittest
from mgapi.mgapi import Api as MailgunApi

# Tests configuration - Start
config_file           = "C:\\Users\\Account\\Desktop\\config.json"
existing_domain       = "sandbox9f1a26d223824cbab4beeba8ff46a577.mailgun.org"
existing_tag          = "DevTest"
existing_mailing_list = "test@sandbox9f1a26d223824cbab4beeba8ff46a577.mailgun.org"

non_existent_domain   = "nonexistent.com.eu"
non_existent_tag      = "NON_EXISTENT_TAG"

test_event            = "accepted"
test_aggregate        = "devices"

_verbose_responses    = False
_api_builtin_debug    = False
# Tests configuration - Stop

_v = _verbose_responses
api = MailgunApi(config_file=config_file, debug=_api_builtin_debug)

### Convention
# - class:   class <RequestType>_<TestCaseName>_TestCase
# - method:  def test__<MethodName>__<StateUnderTest>_<ExpectedBehavior>
class GET_JustificationSuccess_TestCase(unittest.TestCase):

    def test__get_domains__CorrectParams_True(self):
        des, ser = api.get_domains()
        self.assertTrue(des["justify"]["success"])

        des, ser = api.get_domains(domain=existing_domain)
        self.assertTrue(des["justify"]["success"])

    def test__get_bounces__CorrectParams_True(self):
        des, ser = api.get_bounces()
        self.assertTrue(des["justify"]["success"])

    def test__get_unsubscribes__CorrectParams_True(self):
        des, ser = api.get_unsubscribes()
        self.assertTrue(des["justify"]["success"])

    def test__get_complaints__CorrectParams_True(self):
        des, ser = api.get_complaints()
        self.assertTrue(des["justify"]["success"])

    def test__get_lists__CorrectParams_True(self):
        des, ser = api.get_lists()
        self.assertTrue(des["justify"]["success"])

    def test__get_members__CorrectParams_True(self):
        des, ser = api.get_members(address=existing_mailing_list)
        self.assertTrue(des["justify"]["success"])

    def test__get_events__CorrectParams_True(self):
        des, ser = api.get_events()
        self.assertTrue(des["justify"]["success"])

    def test__get_stats_total__CorrectParams_True(self):
        des, ser = api.get_stats_total(event=test_event)
        self.assertTrue(des["justify"]["success"])

    def test__get_tags__CorrectParams_True(self):
        des, ser = api.get_tags()
        self.assertTrue(des["justify"]["success"])

    def test__get_tag_stats__CorrectParams_True(self):
        des, ser = api.get_tag_stats(existing_tag, test_event)
        self.assertTrue(des["justify"]["success"])

    def test__get_tag_aggregates__CorrectParams_True(self):
        des, ser = api.get_tag_aggregates(existing_tag, test_aggregate)
        self.assertTrue(des["justify"]["success"])


if __name__ == "__main__":
    unittest.main()
