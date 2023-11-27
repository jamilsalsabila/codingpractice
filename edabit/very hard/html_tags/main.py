import re

opening_tags = "(<[^/]{1}[a-z=\"'.:\/ ]*>)"
closing_tags = "(</[a-z]+>)"
all_tags = "(</?[a-z=\"'.:\/ ]+>.*)"
