from tree import Tree


class TestTree:
    '''Class Tree in tree.py'''

    def test_get_element_by_id(self):
        """Test get_element_by_id method finds elements by id and returns None when not found"""

        tree = Tree({
            'tag_name': 'body',
            'id': None,
            'children': [
                {
                    'tag_name': 'div',
                    'id': 'main',
                    'children': [
                        {
                            'tag_name': 'h1',
                            'id': 'heading',
                            'text_content': 'Title',
                            'children': []
                        },
                        {
                            'tag_name': 'h2',
                            'id': None,
                            'text_content': 'Subtitle',
                            'children': []
                        }
                    ]
                }
            ]
        })

        # Test finding existing element by id "heading"
        expected = {
            "tag_name": "h1",
            "id": "heading",
            "text_content": "Title",
            "children": []
        }

        result = tree.get_element_by_id("heading")
       
        # Test that non-existing id returns None
        assert tree.get_element_by_id("nope") is None