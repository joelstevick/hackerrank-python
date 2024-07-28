import unittest
from code import html_parse, State

class TestHtmlParser(unittest.TestCase):
    # can parse a single tag
    def test_parse_single_tag(self):
        html = '<hello>World</hello>'
               
        context = html_parse(html, {
            "state": State.NULL,
            "tags": [],
            "tag_name": ''
        })
        
        self.assertEqual(len(context["tags"]), 1)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
        
    # can parse multiple tags
    def test_parse_multiple_tags(self):
        html = '<hello>World</hello><foo>bar</foo>'
               
        context = html_parse(html, {
            "state": State.NULL,
            "tags": [],
            "tag_name": ''
        })
        
        self.assertEqual(len(context["tags"]), 2)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
        
        self.assertEqual(context["tags"][1]["name"], "foo")


if __name__ == '__main__':
    unittest.main()