from io import BytesIO, StringIO

from PIL import Image, ImageDraw, ImageFont
from pygments.formatters.img import FontManager, ImageFormatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import find_lexer_class_for_filename as _find_lexer
from pygments import lexers
from pygments.style import Style
from pygments.token import (Comment, Error, Escape, Generic, Keyword, Literal,
                            Name, Number, Operator, Other, Punctuation, String,
                            Text, Token, Whitespace)

from app import ibmcolors

FONT_SIZE = 24


class MegaSexyStyle(Style):
    default_style = "#dde1E6"
    background_color = ibmcolors.Warm_Gray_100
    styles = {
        Token: "bold " + ibmcolors.Cool_Gray_20,
        Text: "bold " + ibmcolors.Cool_Gray_20,
        Whitespace: "bold " + ibmcolors.Cool_Gray_20,
        Escape: "bold " + ibmcolors.Cool_Gray_20,
        Error: "bold " + ibmcolors.Cool_Gray_20,
        Other: "bold " + ibmcolors.Cool_Gray_20,

        Keyword: "bold " + ibmcolors.Purple_50,
        Keyword.Constant: "bold " + ibmcolors.Purple_50,
        Keyword.Declaration: "bold " + ibmcolors.Blue_50,
        Keyword.Namespace: "bold " + ibmcolors.Blue_50,
        Keyword.Pseudo: "bold " + ibmcolors.Purple_50,
        Keyword.Reserved: "bold " + ibmcolors.Purple_50,
        Keyword.Type: "bold " + ibmcolors.Blue_50,
        
        Name: "bold " + ibmcolors.Cool_Gray_20,
        Name.Attribute: "bold " + ibmcolors.Yellow_30,
        Name.Builtin: "bold " + ibmcolors.Cyan_50,
        Name.Builtin.Pseudo: "bold " + ibmcolors.Cyan_50,
        Name.Class: "bold " + ibmcolors.Blue_50,
        Name.Constant: "bold " + ibmcolors.Blue_50,
        Name.Decorator: "bold " + ibmcolors.Yellow_30,
        Name.Entity: "bold " + ibmcolors.Yellow_30,
        Name.Exception: "bold " + ibmcolors.Cyan_50,
        Name.Function: "bold " + ibmcolors.Blue_50,
        Name.Function.Magic: "bold " + ibmcolors.Blue_60,
        Name.Property: "bold " + ibmcolors.Yellow_30,
        Name.Label: "bold " + ibmcolors.Cool_Gray_20,
        Name.Namespace: "bold " + ibmcolors.Cool_Gray_20,
        Name.Other: "bold " + ibmcolors.Cool_Gray_30,
        Name.Tag: "bold " + ibmcolors.Red_50,
        Name.Variable: "bold " + ibmcolors.Blue_50,
        Name.Variable.Class: "bold " + ibmcolors.Blue_40,
        Name.Variable.Global: "bold " + ibmcolors.Blue_50,
        Name.Variable.Instance: "bold " + ibmcolors.Cyan_30,
        Name.Variable.Magic: "bold " + ibmcolors.Cyan_40,
        
        Literal: "bold " + ibmcolors.Green_50,
        Literal.Date: "bold " + ibmcolors.Green_50,
        
        String: "bold " + ibmcolors.Green_30,
        # String.Affix: "bold " + "#fff",
        # String.Backtick: "bold " + "#fff",
        # String.Char: "bold " + "#fff",
        # String.Delimiter: "bold " + "#fff",
        # String.Doc: "bold " + "#fff",
        # String.Double: "bold " + "#fff",
        String.Escape: "bold " + ibmcolors.Magenta_30,
        # String.Heredoc: "bold " + "#fff",
        # String.Interpol: "bold " + "#fff",
        # String.Other: "bold " + "#fff",
        String.Regex: "bold " + ibmcolors.Magenta_30,
        # String.Single: "bold " + "#fff",
        # String.Symbol: "bold " + "#fff",
        
        Number: "bold " + ibmcolors.Orange_40,
        # Number.Bin: "bold " + "#fff",
        # Number.Float: "bold " + "#fff",
        # Number.Hex: "bold " + "#fff",
        # Number.Integer: "bold " + "#fff",
        # Number.Integer.Long: "bold " + "#fff",
        # Number.Oct: "bold " + "#fff",
        
        Operator: "bold " + ibmcolors.Red_50,
        # Operator.Word: "bold " + "#fff",
        
        Punctuation: "bold " + ibmcolors.Red_50,
        
        Comment: "bold " + ibmcolors.Cool_Gray_60,
        # Comment.Hashbang: "bold " + "#fff",
        # Comment.Multiline: "bold " + "#fff",
        # Comment.Preproc: "bold " + "#fff",
        # Comment.PreprocFile: "bold " + "#fff",
        # Comment.Single: "bold " + "#fff",
        Comment.Special: "bold " + ibmcolors.Yellow_30,
        
        # Generic: "bold " + "#fff",
        # Generic.Deleted: "bold " + "#fff",
        # Generic.Emph: "bold " + "#fff",
        # Generic.Error: "bold " + "#fff",
        # Generic.Heading: "bold " + "#fff",
        # Generic.Inserted: "bold " + "#fff",
        # Generic.Output: "bold " + "#fff",
        # Generic.Prompt: "bold " + "#fff",
        # Generic.Strong: "bold " + "#fff",
        # Generic.Subheading: "bold " + "#fff",
        # Generic.Traceback: "bold " + "#fff",
    }


# PATCH IN FONT MANAGER


def patch_init(self, *_):
    self.fonts = {}
    self.font_size = FONT_SIZE
    self.fonts['NORMAL'] = ImageFont.truetype(
        "./IBM_Plex_Mono/IBMPlexMono-Regular.ttf", self.font_size)
    self.fonts['ITALIC'] = ImageFont.truetype(
        "./IBM_Plex_Mono/IBMPlexMono-Italic.ttf", self.font_size)
    self.fonts['BOLD'] = ImageFont.truetype(
        "./IBM_Plex_Mono/IBMPlexMono-Bold.ttf", self.font_size)
    self.fonts['BOLDITALIC'] = ImageFont.truetype(
        "./IBM_Plex_Mono/IBMPlexMono-BoldItalic.ttf", self.font_size)


FontManager.__init__ = patch_init

# PATCH IMAGE


def get_image_size(self, maxcharno, maxlineno):
    return (self._get_char_x(maxcharno) + self.image_pad,
            self._get_line_y(maxlineno + 0) + (self.image_pad +
                                               (self.fonth // 2)))


def format_(self, tokensource, outfile):
    self._create_drawables(tokensource)
    self._draw_line_numbers()
    im = Image.new('RGBA', self._get_image_size(self.maxcharno,
                                                self.maxlineno),
                   self.background_color)
    self._paint_line_number_bg(im)
    draw = ImageDraw.Draw(im)
    # Highlight
    if self.hl_lines:
        x = self.image_pad + self.line_number_width - self.line_number_pad + 1
        recth = self._get_line_height()
        rectw = im.size[0] - x
        for linenumber in self.hl_lines:
            y = self._get_line_y(linenumber - 1)
            draw.rectangle([(x, y), (x + rectw, y + recth)],
                           fill=self.hl_color)
    for pos, value, font, kw in self.drawables:
        draw.text(pos, value, font=font, **kw)
    im.save(outfile, self.image_format.upper())


ImageFormatter._get_image_size = get_image_size
ImageFormatter.format = format_


def tokenize(file_name, code):
    lex_class = _find_lexer(file_name, code)
    if lex_class is not None:
        lex = lex_class()
        return lex.get_tokens(code)
    else:
        return [(Text, code,)]


def show_cli(tokens):
    form = TerminalFormatter()
    text = StringIO()
    form.format(tokens, text)
    text.seek(0)
    return text.read()


def show_pic(tokens):
    form = ImageFormatter(line_numbers=False,
                          image_pad=0,
                          line_pad=6,
                          style=MegaSexyStyle)
    file = BytesIO()
    form.format(tokens, file)
    file.seek(0)
    return Image.open(file)
