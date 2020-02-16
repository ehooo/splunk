#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import (
    Configuration,
    dispatch,
    EventingCommand,
    Option, validators)


@Configuration()
class CustomFilterCommand(EventingCommand):
    fieldname = Option(
        doc='''
        **Syntax:** **fieldname=***<fieldname>*
        **Description:** Name of the field that will hold the match count''',
        require=False, validate=validators.Fieldname())

    def check_item(self, item):
        option = self.options.get('fieldname')
        check = True
        if option.value is not None:
            check = item.get(option.value, None)

        if check:
            if not self.fieldnames:
                return item
            for key in self.fieldnames:
                for val in item.values():
                    if key in val:
                        return item

    def transform(self, events):
        try:
            for event in events:
                item = self.check_item(event)
                if item:
                    yield item
        except Exception:
            self.logger.exception('Error during transform')
            raise


dispatch(CustomFilterCommand, sys.argv, sys.stdin, sys.stdout, __name__)
