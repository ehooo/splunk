#!/usr/bin/env python

# https://docs.splunk.com/Splexicon:Streamingcommand

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib import six
from splunklib.searchcommands import (
    Configuration,
    dispatch,
    Option,
    StreamingCommand,
    validators
)


@Configuration()
class CustomStreamCommand(StreamingCommand):
    fieldname = Option(
        doc='''
        **Syntax:** **fieldname=***<fieldname>*
        **Description:** Name of the field that will hold the match count''',
        require=True, validate=validators.Fieldname())

    pattern = Option(
        doc='''
        **Syntax:** **pattern=***<regular-expression>*
        **Description:** Regular expression pattern to match''',
        require=True, validate=validators.RegularExpression())

    def stream(self, records):
        for record in records:
            count = 0
            for field_name in self.fieldnames:
                if field_name in record:
                    matches = self.pattern.findall(six.text_type(record[field_name].decode("utf-8")))
                    count += len(matches)
            record[self.fieldname] = count
            yield record


dispatch(CustomStreamCommand, sys.argv, sys.stdin, sys.stdout, __name__)
