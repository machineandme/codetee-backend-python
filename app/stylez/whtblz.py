from pygments.style import Style as _Style
from pygments.token import (Comment, Error, Escape, Generic, Keyword, Literal,
                            Name, Number, Operator, Other, Punctuation, String,
                            Text, Token, Whitespace)

from app import ibmcolors


class Style(_Style):
    default_style = ibmcolors.Black
    background_color = ibmcolors.White
    styles = {
        Token: "bold " + ibmcolors.Cool_Gray_90,
        # Text: "bold " + ibmcolors.Cool_Gray_20,
        # Whitespace: "bold " + ibmcolors.Cool_Gray_20,
        # Escape: "bold " + ibmcolors.Cool_Gray_20,
        # Error: "bold " + ibmcolors.Cool_Gray_20,
        # Other: "bold " + ibmcolors.Cool_Gray_20,
        #
        # Keyword: "bold " + ibmcolors.Purple_50,
        # Keyword.Constant: "bold " + ibmcolors.Purple_50,
        # Keyword.Declaration: "bold " + ibmcolors.Blue_50,
        # Keyword.Namespace: "bold " + ibmcolors.Blue_50,
        # Keyword.Pseudo: "bold " + ibmcolors.Purple_50,
        # Keyword.Reserved: "bold " + ibmcolors.Purple_50,
        # Keyword.Type: "bold " + ibmcolors.Blue_50,
        #
        # Name: "bold " + ibmcolors.Cool_Gray_20,
        # Name.Attribute: "bold " + ibmcolors.Yellow_30,
        # Name.Builtin: "bold " + ibmcolors.Cyan_50,
        # Name.Builtin.Pseudo: "bold " + ibmcolors.Cyan_50,
        # Name.Class: "bold " + ibmcolors.Blue_50,
        # Name.Constant: "bold " + ibmcolors.Blue_50,
        # Name.Decorator: "bold " + ibmcolors.Yellow_30,
        # Name.Entity: "bold " + ibmcolors.Yellow_30,
        # Name.Exception: "bold " + ibmcolors.Cyan_50,
        # Name.Function: "bold " + ibmcolors.Blue_50,
        # Name.Function.Magic: "bold " + ibmcolors.Blue_60,
        # Name.Property: "bold " + ibmcolors.Yellow_30,
        # Name.Label: "bold " + ibmcolors.Cool_Gray_20,
        # Name.Namespace: "bold " + ibmcolors.Cool_Gray_20,
        # Name.Other: "bold " + ibmcolors.Cool_Gray_30,
        # Name.Tag: "bold " + ibmcolors.Red_50,
        # Name.Variable: "bold " + ibmcolors.Blue_50,
        # Name.Variable.Class: "bold " + ibmcolors.Blue_40,
        # Name.Variable.Global: "bold " + ibmcolors.Blue_50,
        # Name.Variable.Instance: "bold " + ibmcolors.Cyan_30,
        # Name.Variable.Magic: "bold " + ibmcolors.Cyan_40,
        #
        # Literal: "bold " + ibmcolors.Green_50,
        # Literal.Date: "bold " + ibmcolors.Green_50,
        #
        # String: "bold " + ibmcolors.Green_30,
        # # String.Affix: "bold " + "#fff",
        # # String.Backtick: "bold " + "#fff",
        # # String.Char: "bold " + "#fff",
        # # String.Delimiter: "bold " + "#fff",
        # # String.Doc: "bold " + "#fff",
        # # String.Double: "bold " + "#fff",
        # String.Escape: "bold " + ibmcolors.Magenta_30,
        # # String.Heredoc: "bold " + "#fff",
        # # String.Interpol: "bold " + "#fff",
        # # String.Other: "bold " + "#fff",
        # String.Regex: "bold " + ibmcolors.Magenta_30,
        # # String.Single: "bold " + "#fff",
        # # String.Symbol: "bold " + "#fff",
        #
        # Number: "bold " + ibmcolors.Orange_40,
        # # Number.Bin: "bold " + "#fff",
        # # Number.Float: "bold " + "#fff",
        # # Number.Hex: "bold " + "#fff",
        # # Number.Integer: "bold " + "#fff",
        # # Number.Integer.Long: "bold " + "#fff",
        # # Number.Oct: "bold " + "#fff",
        #
        # Operator: "bold " + ibmcolors.Red_50,
        # # Operator.Word: "bold " + "#fff",
        #
        # Punctuation: "bold " + ibmcolors.Red_50,
        #
        # Comment: "bold " + ibmcolors.Cool_Gray_60,
        # # Comment.Hashbang: "bold " + "#fff",
        # # Comment.Multiline: "bold " + "#fff",
        # # Comment.Preproc: "bold " + "#fff",
        # # Comment.PreprocFile: "bold " + "#fff",
        # # Comment.Single: "bold " + "#fff",
        # Comment.Special: "bold " + ibmcolors.Yellow_30,
        #
        # # Generic: "bold " + "#fff",
        # # Generic.Deleted: "bold " + "#fff",
        # # Generic.Emph: "bold " + "#fff",
        # # Generic.Error: "bold " + "#fff",
        # # Generic.Heading: "bold " + "#fff",
        # # Generic.Inserted: "bold " + "#fff",
        # # Generic.Output: "bold " + "#fff",
        # # Generic.Prompt: "bold " + "#fff",
        # # Generic.Strong: "bold " + "#fff",
        # # Generic.Subheading: "bold " + "#fff",
        # # Generic.Traceback: "bold " + "#fff",
    }
