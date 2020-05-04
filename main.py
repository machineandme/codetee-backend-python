from io import StringIO, BytesIO

from PIL import Image, ImageFont, ImageDraw
from pygments.formatters.img import ImageFormatter, FontManager
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import find_lexer_class_for_filename as _find_lexer
from pygments.style import Style
from pygments.token import (Token, Keyword, Name, Comment, String)


class MegaSexyStyle(Style):
    default_style = "#dde1E6"
    background_color = "#00000000"
    styles = {
        Token: '#dde1E6',
        Comment: '#dde1E6',
        Keyword: '#dde1E6',
        Name.Function: '#dde1E6',
        Name.Class: '#dde1E6',
        String: '#dde1E6',
    }


# PATCH IN FONT MANAGER

def patch_init(self, *_):
    self.fonts = {}
    self.font_size = 80
    self.fonts['NORMAL'] = ImageFont.truetype("./IBM_Plex_Mono/IBMPlexMono-Regular.ttf", self.font_size)
    self.fonts['ITALIC'] = ImageFont.truetype("./IBM_Plex_Mono/IBMPlexMono-Italic.ttf", self.font_size)
    self.fonts['BOLD'] = ImageFont.truetype("./IBM_Plex_Mono/IBMPlexMono-Bold.ttf", self.font_size)
    self.fonts['BOLDITALIC'] = ImageFont.truetype("./IBM_Plex_Mono/IBMPlexMono-BoldItalic.ttf", self.font_size)


FontManager.__init__ = patch_init


# PATCH IMAGE

def get_image_size(self, maxcharno, maxlineno):
    return (self._get_char_x(maxcharno) + self.image_pad,
            self._get_line_y(maxlineno + 0) + (self.image_pad + (self.fonth // 2)))


def format_(self, tokensource, outfile):
    self._create_drawables(tokensource)
    self._draw_line_numbers()
    im = Image.new(
        'RGBA',
        self._get_image_size(self.maxcharno, self.maxlineno),
        self.background_color
    )
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
    lex = lex_class()
    return lex.get_tokens(code)


def show_cli(tokens):
    form = TerminalFormatter()
    text = StringIO()
    form.format(tokens, text)
    text.seek(0)
    return text.read()


def show_pic(tokens):
    form = ImageFormatter(line_numbers=False, image_pad=0, line_pad=10, style=MegaSexyStyle)
    file = BytesIO()
    form.format(tokens, file)
    file.seek(0)
    return Image.open(file)
