"""
Complete MCP Tools metadata for Playwright browser automation (21 tools)
Fixed for Gemini API compatibility - all schemas validated
"""

MCP_TOOLS_METADATA = [
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
        "name": "browser_handle_dialog",
        "description": "Handle a dialog (alert, confirm, or prompt)",
        "tags": ["browser_handle_dialog"],
        "status": True,
        "display_name": "browser_handle_dialog",
        "display_description": "Handle a dialog",
        "readonly": False,
        "args": {
            "accept": {
                "description": "Whether to accept the dialog",
                "title": "Accept",
                "type": "boolean"
            },
            "promptText": {
                "description": "The text to enter in a prompt dialog (optional, only for prompts)",
                "title": "PromptText",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_evaluate",
        "description": "Evaluate JavaScript expression on page or element",
        "tags": ["browser_evaluate"],
        "status": True,
        "display_name": "browser_evaluate",
        "display_description": "Evaluate JavaScript expression on page or element",
        "readonly": False,
        "args": {
            "function": {
                "description": "JavaScript function to evaluate: () => { code } or (element) => { code }",
                "title": "Function",
                "type": "string"
            },
            "element": {
                "description": "Human-readable element description (optional)",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Element reference from snapshot (optional)",
                "title": "Ref",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_file_upload",
        "description": "Upload one or multiple files to a file input",
        "tags": ["browser_file_upload"],
        "status": True,
        "display_name": "browser_file_upload",
        "display_description": "Upload files",
        "readonly": False,
        "args": {
            "paths": {
                "description": "Array of absolute file paths to upload",
                "title": "Paths",
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        }
    },
    {
        "name": "browser_fill_form",
        "description": "Fill multiple form fields at once",
        "tags": ["browser_fill_form"],
        "status": True,
        "display_name": "browser_fill_form",
        "display_description": "Fill multiple form fields",
        "readonly": False,
        "args": {
            "fields": {
                "description": "Array of form fields to fill with name, ref, type, and value",
                "title": "Fields",
                "type": "array",
                "items": {
                    "type": "object"
                }
            }
        }
    },
    {
        "name": "browser_install",
        "description": "Install the browser. Call this if you get an error about browser not being installed",
        "tags": ["browser_install"],
        "status": True,
        "display_name": "browser_install",
        "display_description": "Install browser",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_press_key",
        "description": "Press a key on the keyboard",
        "tags": ["browser_press_key"],
        "status": True,
        "display_name": "browser_press_key",
        "display_description": "Press a key",
        "readonly": False,
        "args": {
            "key": {
                "description": "Key name or character: ArrowLeft, Enter, a, etc.",
                "title": "Key",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_type",
        "description": "Type text into an editable element",
        "tags": ["browser_type"],
        "status": True,
        "display_name": "browser_type",
        "display_description": "Type text",
        "readonly": False,
        "args": {
            "element": {
                "description": "Human-readable element description",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Exact element reference from snapshot",
                "title": "Ref",
                "type": "string"
            },
            "text": {
                "description": "Text to type",
                "title": "Text",
                "type": "string"
            },
            "submit": {
                "description": "Press Enter after typing (true/false)",
                "title": "Submit",
                "type": "boolean"
            },
            "slowly": {
                "description": "Type one character at a time (true/false)",
                "title": "Slowly",
                "type": "boolean"
            }
        }
    },
    {
        "name": "browser_navigate",
        "description": "Navigate to a URL",
        "tags": ["browser_navigate"],
        "status": True,
        "display_name": "browser_navigate",
        "display_description": "Navigate to URL",
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
        "name": "browser_navigate_back",
        "description": "Go back to the previous page",
        "tags": ["browser_navigate_back"],
        "status": True,
        "display_name": "browser_navigate_back",
        "display_description": "Navigate back",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_network_requests",
        "description": "Returns all network requests since loading the page",
        "tags": ["browser_network_requests"],
        "status": True,
        "display_name": "browser_network_requests",
        "display_description": "Get network requests",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_take_screenshot",
        "description": "Take a screenshot of the current page",
        "tags": ["browser_take_screenshot"],
        "status": True,
        "display_name": "browser_take_screenshot",
        "display_description": "Take screenshot",
        "readonly": False,
        "args": {
            "type": {
                "description": "Image format: png or jpeg (default: png)",
                "title": "Type",
                "type": "string"
            },
            "filename": {
                "description": "Filename to save as (optional)",
                "title": "Filename",
                "type": "string"
            },
            "fullPage": {
                "description": "Capture full scrollable page (true/false)",
                "title": "FullPage",
                "type": "boolean"
            }
        }
    },
    {
        "name": "browser_snapshot",
        "description": "Capture accessibility snapshot of the current page - better than screenshot for element interaction",
        "tags": ["browser_snapshot"],
        "status": True,
        "display_name": "browser_snapshot",
        "display_description": "Capture page snapshot",
        "readonly": False,
        "args": {}
    },
    {
        "name": "browser_click",
        "description": "Perform click on a web page element",
        "tags": ["browser_click"],
        "status": True,
        "display_name": "browser_click",
        "display_description": "Click element",
        "readonly": False,
        "args": {
            "element": {
                "description": "Human-readable element description",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Exact element reference from snapshot",
                "title": "Ref",
                "type": "string"
            },
            "doubleClick": {
                "description": "Perform double-click instead of single (true/false)",
                "title": "DoubleClick",
                "type": "boolean"
            },
            "button": {
                "description": "Mouse button: left, right, or middle (default: left)",
                "title": "Button",
                "type": "string"
            },
            "modifiers": {
                "description": "Modifier keys to press during click (array of strings)",
                "title": "Modifiers",
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        }
    },
    {
        "name": "browser_drag",
        "description": "Perform drag and drop between two elements",
        "tags": ["browser_drag"],
        "status": True,
        "display_name": "browser_drag",
        "display_description": "Drag and drop",
        "readonly": False,
        "args": {
            "startElement": {
                "description": "Source element description",
                "title": "StartElement",
                "type": "string"
            },
            "startRef": {
                "description": "Source element reference",
                "title": "StartRef",
                "type": "string"
            },
            "endElement": {
                "description": "Target element description",
                "title": "EndElement",
                "type": "string"
            },
            "endRef": {
                "description": "Target element reference",
                "title": "EndRef",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_hover",
        "description": "Hover over an element on the page",
        "tags": ["browser_hover"],
        "status": True,
        "display_name": "browser_hover",
        "display_description": "Hover over element",
        "readonly": False,
        "args": {
            "element": {
                "description": "Human-readable element description",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Exact element reference",
                "title": "Ref",
                "type": "string"
            }
        }
    },
    {
        "name": "browser_select_option",
        "description": "Select an option in a dropdown",
        "tags": ["browser_select_option"],
        "status": True,
        "display_name": "browser_select_option",
        "display_description": "Select dropdown option",
        "readonly": False,
        "args": {
            "element": {
                "description": "Human-readable dropdown description",
                "title": "Element",
                "type": "string"
            },
            "ref": {
                "description": "Dropdown element reference",
                "title": "Ref",
                "type": "string"
            },
            "values": {
                "description": "Array of values to select",
                "title": "Values",
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        }
    },
    {
        "name": "browser_tabs",
        "description": "List, create, close, or select browser tabs",
        "tags": ["browser_tabs"],
        "status": True,
        "display_name": "browser_tabs",
        "display_description": "Manage browser tabs",
        "readonly": False,
        "args": {
            "action": {
                "description": "Action to perform: list, new, close, or select",
                "title": "Action",
                "type": "string"
            },
            "index": {
                "description": "Tab index for close/select actions (optional)",
                "title": "Index",
                "type": "number"
            }
        }
    },
    {
        "name": "browser_wait_for",
        "description": "Wait for text to appear/disappear or time to pass",
        "tags": ["browser_wait_for"],
        "status": True,
        "display_name": "browser_wait_for",
        "display_description": "Wait for condition",
        "readonly": False,
        "args": {
            "time": {
                "description": "Time to wait in seconds (optional)",
                "title": "Time",
                "type": "number"
            },
            "text": {
                "description": "Text to wait for to appear (optional)",
                "title": "Text",
                "type": "string"
            },
            "textGone": {
                "description": "Text to wait for to disappear (optional)",
                "title": "TextGone",
                "type": "string"
            }
        }
    }
]
