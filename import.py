import requests
import os
import uuid

url = "http://localizacstudio.ads.autodesk.com:7860/api/v1/run/4b06762f-7329-454b-b4a0-fcd2dc702b55"
# The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Hello",
    "tweaks": {
        "Agent-9hWQI": {
            "format_instructions": "You are an AI that extracts structured JSON objects from unstructured text. Use a predefined schema with expected types (str, int, float, bool, dict). Extract ALL relevant instances that match the schema - if multiple patterns exist, capture them all. Fill missing or ambiguous values with defaults: None for missing values. Remove exact duplicates but keep variations that have different field values. Always return valid JSON in the expected format, never throw errors. If multiple objects can be extracted, return them all in the structured format.",
            "n_messages": 100,
            "output_schema": [],
            "system_prompt": "You are a helpful assistant that can use tools to answer questions and perform tasks."
        },
        "OllamaModel-F13V6": {
            "base_url": "http://localhost:11434/",
            "model_name": "gpt-oss:120b"
        },
        "MCPTools-qmP5R": {
            "mcp_server": {
                "name": "playwright_extension",
                "config": {
                    "command": "npx",
                    "args": ["@playwright/mcp@latest"]
                }
            },
            "tools_metadata": [
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
                    "args": {
                        "onlyErrors": {
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Only return error messages",
                            "title": "Onlyerrors"
                        }
                    }
                },
                {
                    "name": "browser_handle_dialog",
                    "description": "Handle a dialog",
                    "tags": ["browser_handle_dialog"],
                    "status": True,
                    "display_name": "browser_handle_dialog",
                    "display_description": "Handle a dialog",
                    "readonly": False,
                    "args": {
                        "accept": {
                            "description": "Whether to accept the dialog.",
                            "title": "Accept",
                            "type": "boolean"
                        },
                        "promptText": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "The text of the prompt in case of a prompt dialog.",
                            "title": "Prompttext"
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
                            "description": "() => { /* code */ } or (element) => { /* code */ } when element is provided",
                            "title": "Function",
                            "type": "string"
                        },
                        "element": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Human-readable element description used to obtain permission to interact with the element",
                            "title": "Element"
                        },
                        "ref": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Exact target element reference from the page snapshot",
                            "title": "Ref"
                        }
                    }
                },
                {
                    "name": "browser_file_upload",
                    "description": "Upload one or multiple files",
                    "tags": ["browser_file_upload"],
                    "status": True,
                    "display_name": "browser_file_upload",
                    "display_description": "Upload one or multiple files",
                    "readonly": False,
                    "args": {
                        "paths": {
                            "anyOf": [
                                {
                                    "items": {"type": "string"},
                                    "type": "array"
                                },
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "The absolute paths to the files to upload. Can be single file or multiple files. If omitted, file chooser is cancelled.",
                            "title": "Paths"
                        }
                    }
                },
                {
                    "name": "browser_fill_form",
                    "description": "Fill multiple form fields",
                    "tags": ["browser_fill_form"],
                    "status": True,
                    "display_name": "browser_fill_form",
                    "display_description": "Fill multiple form fields",
                    "readonly": False,
                    "args": {
                        "fields": {
                            "description": "Fields to fill in",
                            "items": {"$ref": "#/$defs/AnonModel0"},
                            "title": "Fields",
                            "type": "array"
                        }
                    }
                },
                {
                    "name": "browser_install",
                    "description": "Install the browser specified in the config. Call this if you get an error about the browser not being installed.",
                    "tags": ["browser_install"],
                    "status": True,
                    "display_name": "browser_install",
                    "display_description": "Install the browser specified in the config. Call this if you get an error about the browser not being installed.",
                    "readonly": False,
                    "args": {}
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
                            "description": "Human-readable element description used to obtain permission to interact with the element",
                            "title": "Element",
                            "type": "string"
                        },
                        "ref": {
                            "description": "Exact target element reference from the page snapshot",
                            "title": "Ref",
                            "type": "string"
                        },
                        "text": {
                            "description": "Text to type into the element",
                            "title": "Text",
                            "type": "string"
                        },
                        "submit": {
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Whether to submit entered text (press Enter after)",
                            "title": "Submit"
                        },
                        "slowly": {
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Whether to type one character at a time. Useful for triggering key handlers in the page. By default entire text is filled in at once.",
                            "title": "Slowly"
                        }
                    }
                },
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
                    "name": "browser_network_requests",
                    "description": "Returns all network requests since loading the page",
                    "tags": ["browser_network_requests"],
                    "status": True,
                    "display_name": "browser_network_requests",
                    "display_description": "Returns all network requests since loading the page",
                    "readonly": False,
                    "args": {}
                },
                {
                    "name": "browser_take_screenshot",
                    "description": "Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.",
                    "tags": ["browser_take_screenshot"],
                    "status": True,
                    "display_name": "browser_take_screenshot",
                    "display_description": "Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.",
                    "readonly": False,
                    "args": {
                        "type": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": "png",
                            "description": "Image format for the screenshot. Default is png.",
                            "title": "Type"
                        },
                        "filename": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "File name to save the screenshot to. Defaults to `page-{timestamp}.{png|jpeg}` if not specified. Prefer relative file names to stay within the output directory.",
                            "title": "Filename"
                        },
                        "element": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Human-readable element description used to obtain permission to screenshot the element. If not provided, the screenshot will be taken of viewport. If element is provided, ref must be provided too.",
                            "title": "Element"
                        },
                        "ref": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Exact target element reference from the page snapshot. If not provided, the screenshot will be taken of viewport. If ref is provided, element must be provided too.",
                            "title": "Ref"
                        },
                        "fullPage": {
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "When True, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Cannot be used with element screenshots.",
                            "title": "Fullpage"
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
                        },
                        "doubleClick": {
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Whether to perform a double click instead of a single click",
                            "title": "Doubleclick"
                        },
                        "button": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Button to click, defaults to left",
                            "title": "Button"
                        },
                        "modifiers": {
                            "anyOf": [
                                {
                                    "items": {"type": "string"},
                                    "type": "array"
                                },
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Modifier keys to press",
                            "title": "Modifiers"
                        }
                    }
                },
                {
                    "name": "browser_drag",
                    "description": "Perform drag and drop between two elements",
                    "tags": ["browser_drag"],
                    "status": True,
                    "display_name": "browser_drag",
                    "display_description": "Perform drag and drop between two elements",
                    "readonly": False,
                    "args": {
                        "startElement": {
                            "description": "Human-readable source element description used to obtain the permission to interact with the element",
                            "title": "Startelement",
                            "type": "string"
                        },
                        "startRef": {
                            "description": "Exact source element reference from the page snapshot",
                            "title": "Startref",
                            "type": "string"
                        },
                        "endElement": {
                            "description": "Human-readable target element description used to obtain the permission to interact with the element",
                            "title": "Endelement",
                            "type": "string"
                        },
                        "endRef": {
                            "description": "Exact target element reference from the page snapshot",
                            "title": "Endref",
                            "type": "string"
                        }
                    }
                },
                {
                    "name": "browser_hover",
                    "description": "Hover over element on page",
                    "tags": ["browser_hover"],
                    "status": True,
                    "display_name": "browser_hover",
                    "display_description": "Hover over element on page",
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
                    "name": "browser_select_option",
                    "description": "Select an option in a dropdown",
                    "tags": ["browser_select_option"],
                    "status": True,
                    "display_name": "browser_select_option",
                    "display_description": "Select an option in a dropdown",
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
                        },
                        "values": {
                            "description": "Array of values to select in the dropdown. This can be a single value or multiple values.",
                            "items": {"type": "string"},
                            "title": "Values",
                            "type": "array"
                        }
                    }
                },
                {
                    "name": "browser_tabs",
                    "description": "List, create, close, or select a browser tab.",
                    "tags": ["browser_tabs"],
                    "status": True,
                    "display_name": "browser_tabs",
                    "display_description": "List, create, close, or select a browser tab.",
                    "readonly": False,
                    "args": {
                        "action": {
                            "description": "Operation to perform",
                            "title": "Action",
                            "type": "string"
                        },
                        "index": {
                            "anyOf": [
                                {"type": "number"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Tab index, used for close/select. If omitted for close, current tab is closed.",
                            "title": "Index"
                        }
                    }
                },
                {
                    "name": "browser_wait_for",
                    "description": "Wait for text to appear or disappear or a specified time to pass",
                    "tags": ["browser_wait_for"],
                    "status": True,
                    "display_name": "browser_wait_for",
                    "display_description": "Wait for text to appear or disappear or a specified time to pass",
                    "readonly": False,
                    "args": {
                        "time": {
                            "anyOf": [
                                {"type": "number"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "The time to wait in seconds",
                            "title": "Time"
                        },
                        "text": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "The text to wait for",
                            "title": "Text"
                        },
                        "textGone": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "The text to wait for to disappear",
                            "title": "Textgone"
                        }
                    }
                }
            ]
        }
    }
}

payload["session_id"] = str(uuid.uuid4())

# Note: 'headers' variable is not defined in the original code
# You may need to add: headers = {"Content-Type": "application/json"}
headers = {}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes
    
    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")

except ValueError as e:
    print(f"Error parsing response: {e}")

