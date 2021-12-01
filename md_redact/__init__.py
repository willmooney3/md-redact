import os

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


redacted_replacement = os.getenv('MD_REDACT_REPLACEMENT', '(redacted)')


class RedactProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        redact_content = os.getenv('MD_REDACT_CONTENT', False)
        attrs = {}
        if redact_content:
            attrs = {"class": "redacted"}
        el = etree.Element('span', attrib=attrs)
        el.text = redacted_replacement if redact_content else m.group(1)
        return el, m.start(0), m.end(0)


class RedactExtension(Extension):
    def extendMarkdown(self, md):
        REDACT_PATTERN = r'\$(.*?)\$'
        md.inlinePatterns.register(RedactProcessor(REDACT_PATTERN, md), 'redact', 175)
        md.registerExtension(self)


def makeExtension(**kwargs):  # pragma: no cover
    return RedactExtension(**kwargs)


makeExtension()
