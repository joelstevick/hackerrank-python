import unittest
from code import html_parse, State

class TestHtmlParser(unittest.TestCase):
    def setUp(self):
        self.initial_context = {
            "state": State.NULL,
            "tags": [],
            "tag_name": '',
            "attributes": []
        }
        print("")

    # can parse a single tag
    def test_parse_single_tag(self):
        html = '<hello>World</hello>'
               
        context = html_parse(html, self.initial_context)
        
        self.assertEqual(len(context["tags"]), 1)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
        
    # can parse multiple tags
    def test_parse_multiple_tags(self):
        html = '<hello>World</hello><foo>bar</foo>'
               
        context = html_parse(html, self.initial_context)

        self.assertEqual(len(context["tags"]), 2)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
        
        self.assertEqual(context["tags"][1]["name"], "foo")

    # can parse a single attribute
    def test_parse_single_attribute(self):
        html = '<hello foo="bar">World</hello>'
               
        context = html_parse(html, self.initial_context)
        
        self.assertEqual(len(context["tags"]), 1)
        
        self.assertEqual(len(context["tags"][0]["attributes"]), 1)
        
    # can parse nested tags
    def test_parse_nested_tags(self):
        html = '<hello>World<foo>bar</foo></hello>'
               
        context = html_parse(html, self.initial_context)

        self.assertEqual(len(context["tags"]), 2)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
        
        self.assertEqual(context["tags"][1]["name"], "foo")

    # can parse attribute from nested tag
    def test_parse_nested_attribute(self):
        html = '<hello>World<foo foo2="bar2">bar</foo></hello>'
               
        context = html_parse(html, self.initial_context)

        self.assertEqual(len(context["tags"][1]["attributes"]), 1)

if __name__ == '__main__':
    unittest.main()