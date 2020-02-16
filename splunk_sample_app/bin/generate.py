#!/usr/bin/env python
import json
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import (
    Configuration,
    dispatch,
    GeneratingCommand,
    Option,
    validators
)


@Configuration()
class CustomGenerateCommand(GeneratingCommand):
    def get_base_row(self, obj):
        row = {
            'type': '',
            'obj_type': str(type(obj)),
            'dir': dir(obj),
            'str': str(obj),
        }
        row['_raw'] = json.dumps(row)
        return row

    def generate(self):
        row = self.get_base_row(self.fieldnames)
        row['type'] = 'fieldnames'
        yield row
        for item in self.fieldnames:
            row = self.get_base_row(item)
            row['type'] = 'fieldnames.item'
            yield row

        row = self.get_base_row(self.metadata)
        row['type'] = 'metadata'
        yield row

        row = self.get_base_row(self.metadata.searchinfo)
        row['type'] = 'metadata.searchinfo'
        yield row


dispatch(CustomGenerateCommand, sys.argv, sys.stdin, sys.stdout, __name__)
