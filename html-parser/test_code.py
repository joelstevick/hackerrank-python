import unittest
from code import html_parse, State

class TestHtmlParser(unittest.TestCase):
    # can parse <hello>World</hello>
    def test_parse_simple_tag(self):
        html = '<hello>World</hello>'
               
        context = html_parse(html, {
            "state": State.NULL,
            "tags": [],
            "tag_name": ''
        })
        
        self.assertEqual(len(context["tags"]), 1)
        
        self.assertEqual(context["tags"][0]["name"], "hello")
    
if __name__ == '__main__':
    unittest.main()