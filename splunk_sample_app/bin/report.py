#!/usr/bin/env python
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import (
    Configuration,
    dispatch,
    Option,
    ReportingCommand,
    validators
)


@Configuration()
class CustomReportCommand(ReportingCommand):
    total = Option(doc='''
        **Syntax:** **total=***<fieldname>*
        **Description:** Name of the field that will hold the computed sum''',
                   require=True, validate=validators.Fieldname())

    @Configuration()
    def map(self, records):
        try:
            response = {
                self.total: 0.0,
            }
            for field_name in self.fieldnames:
                response[field_name] = 0.0

            for record in records:
                if self.total in record:
                    try:
                        response[self.total] += float(record[self.total])
                    except (ValueError, TypeError):
                        pass
                for field_name in self.fieldnames:
                    if field_name in record:
                        try:
                            response[field_name] += float(record[field_name])
                        except (ValueError, TypeError):
                            pass
            response['_raw'] = json.dumps(response)
            yield response
        except Exception:
            self.logger.exception('Error during transform')
            raise

    def reduce(self, records):
        try:
            total = 0.0
            total_field = self.total
            for record in records:
                if total_field in record:
                    value = record[total_field]
                    try:
                        total += float(value)
                    except (ValueError, TypeError):
                        pass
            yield {self.total: total}
        except Exception:
            self.logger.exception('Error during transform')
            raise


dispatch(CustomReportCommand, sys.argv, sys.stdin, sys.stdout, __name__)
