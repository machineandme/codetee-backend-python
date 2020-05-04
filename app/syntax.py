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

FONT_SIZE = 20


class MegaSexyStyle(Style):
    default_style = "#dde1E6"
    background_color = "#000000"
    styles = {
        Token: ibmcolors.Cool_Gray_20,
        Text: ibmcolors.Cool_Gray_20,
        Whitespace: ibmcolors.Cool_Gray_20,
        Escape: ibmcolors.Cool_Gray_20,
        Error: ibmcolors.Cool_Gray_20,
        Other: ibmcolors.Cool_Gray_20,

        Keyword: ibmcolors.Purple_50,
        Keyword.Constant: ibmcolors.Purple_50,
        Keyword.Declaration: ibmcolors.Blue_50,
        Keyword.Namespace: ibmcolors.Blue_50,
        Keyword.Pseudo: ibmcolors.Purple_50,
        Keyword.Reserved: ibmcolors.Purple_50,
        Keyword.Type: ibmcolors.Blue_50,
        
        Name: ibmcolors.Cool_Gray_20,
        Name.Attribute: ibmcolors.Yellow_30,
        Name.Builtin: ibmcolors.Cyan_50,
        Name.Builtin.Pseudo: ibmcolors.Cyan_50,
        Name.Class: ibmcolors.Blue_50,
        Name.Constant: ibmcolors.Blue_50,
        Name.Decorator: ibmcolors.Yellow_30,
        Name.Entity: ibmcolors.Yellow_30,
        Name.Exception: ibmcolors.Cyan_50,
        Name.Function: ibmcolors.Blue_50,
        Name.Function.Magic: ibmcolors.Blue_60,
        Name.Property: ibmcolors.Yellow_30,
        Name.Label: ibmcolors.Blue_50,
        Name.Namespace: ibmcolors.Blue_50,
        Name.Other: ibmcolors.Cool_Gray_30,
        Name.Tag: ibmcolors.Red_50,
        Name.Variable: ibmcolors.Blue_50,
        Name.Variable.Class: ibmcolors.Blue_40,
        Name.Variable.Global: ibmcolors.Blue_50,
        Name.Variable.Instance: ibmcolors.Cyan_30,
        Name.Variable.Magic: ibmcolors.Cyan_40,
        
        Literal: ibmcolors.Green_50,
        Literal.Date: ibmcolors.Green_50,
        
        String: ibmcolors.Green_30,
        # String.Affix: "#fff",
        # String.Backtick: "#fff",
        # String.Char: "#fff",
        # String.Delimiter: "#fff",
        # String.Doc: "#fff",
        # String.Double: "#fff",
        String.Escape: ibmcolors.Magenta_30,
        # String.Heredoc: "#fff",
        # String.Interpol: "#fff",
        # String.Other: "#fff",
        String.Regex: ibmcolors.Magenta_30,
        # String.Single: "#fff",
        # String.Symbol: "#fff",
        
        Number: ibmcolors.Orange_40,
        # Number.Bin: "#fff",
        # Number.Float: "#fff",
        # Number.Hex: "#fff",
        # Number.Integer: "#fff",
        # Number.Integer.Long: "#fff",
        # Number.Oct: "#fff",
        
        Operator: ibmcolors.Red_50,
        # Operator.Word: "#fff",
        
        Punctuation: ibmcolors.Red_50,
        
        Comment: ibmcolors.Cool_Gray_60,
        # Comment.Hashbang: "#fff",
        # Comment.Multiline: "#fff",
        # Comment.Preproc: "#fff",
        # Comment.PreprocFile: "#fff",
        # Comment.Single: "#fff",
        Comment.Special: ibmcolors.Yellow_30,
        
        # Generic: "#fff",
        # Generic.Deleted: "#fff",
        # Generic.Emph: "#fff",
        # Generic.Error: "#fff",
        # Generic.Heading: "#fff",
        # Generic.Inserted: "#fff",
        # Generic.Output: "#fff",
        # Generic.Prompt: "#fff",
        # Generic.Strong: "#fff",
        # Generic.Subheading: "#fff",
        # Generic.Traceback: "#fff",
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
                          line_pad=10,
                          style=MegaSexyStyle)
    file = BytesIO()
    form.format(tokens, file)
    file.seek(0)
    return Image.open(file)
