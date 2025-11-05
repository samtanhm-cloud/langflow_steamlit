"""
Simplified MCP Tools metadata compatible with Gemini API
Removes problematic schema definitions that cause validation errors
"""

MCP_TOOLS_METADATA = [
    {
        "name": "browser_navigate",
        "description": "Navigate to a URL",
        "tags": ["browser_navigate"],
        "status": True,
        "display_name": "browser_navigate",
        "display_description": "Navigate to a URL",
        "readonly": False,
        "args": {
            "url": {
                "description": "The URL to navigate to",
                "title": "Url",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_snapshot",
        "description": "Capture accessibility snapshot of the current page, this is better than screenshot",
        "tags": ["browser_snapshot"],
        "status": True,
        "display_name": "browser_snapshot",
        "display_description": "Capture accessibility snapshot of the current page, this is better than screenshot",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_click",
        "description": "Perform click on a web page",
        "tags": ["browser_click"],
        "status": True,
        "display_name": "browser_click",
        "display_description": "Perform click on a web page",
        "readonly": False,
        "args": {
            "element": {
                "description": "Human-readable element description used to obtain permission to interact with the element",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Exact target element reference from the page snapshot",
                "title": "Ref",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_type",
        "description": "Type text into editable element",
        "tags": ["browser_type"],
        "status": True,
        "display_name": "browser_type",
        "display_description": "Type text into editable element",
        "readonly": False,
        "args": {
            "element": {
                "description": "Human-readable element description",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Exact target element reference",
                "title": "Ref",
                "type": "string"
            },
            "text": {
                "description": "Text to type into the element",
                "title": "Text",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_take_screenshot",
        "description": "Take a screenshot of the current page",
        "tags": ["browser_take_screenshot"],
        "status": True,
        "display_name": "browser_take_screenshot",
        "display_description": "Take a screenshot of the current page",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_navigate_back",
        "description": "Go back to the previous page",
        "tags": ["browser_navigate_back"],
        "status": True,
        "display_name": "browser_navigate_back",
        "display_description": "Go back to the previous page",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_close",
        "description": "Close the page",
        "tags": ["browser_close"],
        "status": True,
        "display_name": "browser_close",
        "display_description": "Close the page",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_console_messages",
        "description": "Returns all console messages",
        "tags": ["browser_console_messages"],
        "status": True,
        "display_name": "browser_console_messages",
        "display_description": "Returns all console messages",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_resize",
        "description": "Resize the browser window",
        "tags": ["browser_resize"],
        "status": True,
        "display_name": "browser_resize",
        "display_description": "Resize the browser window",
        "readonly": False,
        "args": {
            "width": {
                "description": "Width of the browser window",
                "title": "Width",
                "type": "number"
            },
            "height": {
                "description": "Height of the browser window",
                "title": "Height",
                "type": "number"
            }
        }
    },
    {
        "name": "browser_press_key",
        "description": "Press a key on the keyboard",
        "tags": ["browser_press_key"],
        "status": True,
        "display_name": "browser_press_key",
        "display_description": "Press a key on the keyboard",
        "readonly": False,
        "args": {
            "key": {
                "description": "Name of the key to press or a character to generate, such as `ArrowLeft` or `a`",
                "title": "Key",
                "type": "string"
            }
        }
    }
]

