from base_parser import BaseParser


class MatchParser(BaseParser):
    def parse(self, data):
        self.load_page()