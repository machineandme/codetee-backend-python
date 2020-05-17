from io import BytesIO, StringIO

from PIL import Image, ImageDraw, ImageFont
from pygments.formatters.img import FontManager, ImageFormatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import find_lexer_class_for_filename as _find_lexer
from pygments.token import Text

from app.stylez import FirstStyle

FONT_SIZE = 30


# PATCH IN FONT MANAGER


def patch_init(self, *_):
    self.fonts = {}
    self.font_size = FONT_SIZE
    self.fonts['NORMAL'] = ImageFont. truetype(
        "./DharmaTypeCodeSaverBold.ttf", self.font_size)
    self.fonts['ITALIC'] = ImageFont.truetype(
        "./DharmaTypeCodeSaverBold.ttf", self.font_size)
    self.fonts['BOLD'] = ImageFont.truetype(
        "./DharmaTypeCodeSaverBold.ttf", self.font_size)
    self.fonts['BOLDITALIC'] = ImageFont.truetype(
        "./DharmaTypeCodeSaverBold.ttf", self.font_size)


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


def show_pic(tokens, s=FirstStyle):
    form = ImageFormatter(line_numbers=False,
                          image_pad=0,
                          line_pad=6,
                          style=s)
    form.style.background_color = "#ffffff00"
    file = BytesIO()
    form.format(tokens, file)
    file.seek(0)
    return Image.open(file)
