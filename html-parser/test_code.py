import unittest
import pytest
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
    
    # can parse a self terminating tag
    def test_parse_self_terminating_tag(self):
        html = '<hello/>'
               
        context = html_parse(html, self.initial_context)
        
        self.assertEqual(len(context["tags"]), 1)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
        
    # can parse a self terminating tag with a space
    def test_parse_self_terminating_tag(self):
        html = '<hello />'
               
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
        self.assertEqual(context["tags"][0]["attributes"][0]["name"], "foo")
        self.assertEqual(context["tags"][0]["attributes"][0]["value"], "bar")

    # can parse multiple attributes
    def test_parse_multiple_attributes(self):
        html = '<hello foo="bar" foo2="bar2">World</hello>'
               
        context = html_parse(html, self.initial_context)
        
        self.assertEqual(len(context["tags"]), 1)
        
        self.assertEqual(len(context["tags"][0]["attributes"]), 2)
        self.assertEqual(context["tags"][0]["attributes"][0]["name"], "foo")
        self.assertEqual(context["tags"][0]["attributes"][0]["value"], "bar")
        self.assertEqual(context["tags"][0]["attributes"][1]["name"], "foo2")
        self.assertEqual(context["tags"][0]["attributes"][1]["value"], "bar2")

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
        self.assertEqual(context["tags"][1]["attributes"][0]["value"], "bar2")

    # can parse comment
    def test_parse_comment(self):
        html = '<!-- <hello>World<foo foo2="bar2">bar</foo></hello> -->'
               
        context = html_parse(html, self.initial_context)

        self.assertEqual(len(context["tags"]), 0)

    # can parse comment
    def test_parse_comment_with_tag(self):
        html = '<!-- <hello>World</hello> --><foo foo2="bar2">bar</foo>'
               
        context = html_parse(html, self.initial_context)

        self.assertEqual(len(context["tags"]), 1)

    # can pass hackerrank sample test
    def test_hackerrank_sample(self):
        html = '''  <head>
                    <title>HTML</title>
                    </head>
                    <object type="application/x-flash"
                    data="your-file.swf"
                    width="0" height="0">
                    <!-- <param name="movie" value="your-file.swf" /> -->
                    <param name="quality" value="high"/>
                    </object>
                '''
        context = html_parse(html, self.initial_context)
            
        self.assertEqual(len(context["tags"]), 4)
        self.assertEqual(context["tags"][0]["name"], "head")
        self.assertEqual(context["tags"][1]["name"], "title")

        self.assertEqual(context["tags"][2]["name"], "object")
        self.assertEqual(context["tags"][2]["attributes"][0]['name'], "type")
        self.assertEqual(context["tags"][2]["attributes"][0]['value'], "application/x-flash")
        self.assertEqual(context["tags"][2]["attributes"][1]['name'], "data")
        self.assertEqual(context["tags"][2]["attributes"][1]['value'], "your-file.swf")
        self.assertEqual(context["tags"][2]["attributes"][2]['name'], "width")
        self.assertEqual(context["tags"][2]["attributes"][2]['value'], "0")
        self.assertEqual(context["tags"][2]["attributes"][3]['name'], "height")
        self.assertEqual(context["tags"][2]["attributes"][3]['value'], "0")

        self.assertEqual(context["tags"][3]["name"], "param")
        self.assertEqual(context["tags"][3]["attributes"][0]['name'], "name")
        self.assertEqual(context["tags"][3]["attributes"][0]['value'], "quality")
        self.assertEqual(context["tags"][3]["attributes"][1]['name'], "value")
        self.assertEqual(context["tags"][3]["attributes"][1]['value'], "high")


 
if __name__ == '__main__':
    unittest.main()