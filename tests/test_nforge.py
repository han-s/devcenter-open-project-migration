import hashlib
import unittest

from nforge import InvalidProjectError
from nforge import Nforge


class TestNforge(unittest.TestCase):
    valid_pr_name = 'd2coding'
    test_d2coding = Nforge(project_name=valid_pr_name, dev_code=False)
    # sha1 hash file
    d2coding_wiki_docs = {'FrontPage': 'fc1ede112bc7f117dc5d4f89db6478a2d13c06a8',
                          'OpenFontLicense': 'e4575441fb9b826e243d7a76622686d7923835cb'}
    invalid_name = '!245sad'

    def test_invalid_project_error(self):
        with self.assertRaises(InvalidProjectError):
            invalid_pr = Nforge(project_name=self.invalid_name, dev_code=False)
            self.assertIsNone(invalid_pr)

        self.assertIsInstance(self.test_d2coding, cls=Nforge)

    def test_wiki(self):
        wiki = self.test_d2coding.wiki()

        for name, doc in self.d2coding_wiki_docs.items():
            wiki_doc = wiki[name]

            self.assertTrue(type(wiki_doc) is str)
            self.assertEqual(hashlib.sha1(wiki_doc.encode('utf-8')).hexdigest(), doc)

if __name__ == '__main__':
    unittest.main()
