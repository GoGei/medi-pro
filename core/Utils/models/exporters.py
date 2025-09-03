import json
import csv
import io
from abc import abstractmethod, ABC


class ExportModes(object):
    JSON = 'json'
    CSV = 'csv'


class BaseExport(ABC):
    def __init__(self, queryset, fields: tuple, obj_to_dict_func: callable = None, delimiter: str = ';'):
        self.queryset = queryset
        self.fields = fields
        self.obj_to_dict_func = obj_to_dict_func
        self.delimiter = delimiter

    def prepare_data(self) -> list[dict]:
        return [self.obj_to_dict(item) for item in self.queryset]

    def obj_to_dict(self, item) -> dict:
        if self.obj_to_dict_func:
            return self.obj_to_dict_func(item)
        return {field: getattr(item, field) for field in self.fields}

    @abstractmethod
    def export(self):
        ...


class JSONExport(BaseExport):
    def export(self) -> str:
        return json.dumps(self.prepare_data(), ensure_ascii=False, indent=2)


class CSVExport(BaseExport):
    def export(self) -> str:
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=self.fields, delimiter=self.delimiter, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in self.prepare_data():
            writer.writerow(row)
        return buffer.getvalue()


class QuerysetExporter(object):
    def __init__(self, mode: str, *args, **kwargs):
        mapping = {
            ExportModes.JSON: JSONExport,
            ExportModes.CSV: CSVExport,
        }

        self.exporter = mapping[mode](*args, **kwargs)
        self.mode = mode

    def get_content(self):
        return self.exporter.export()

    def get_content_type(self):
        mapping = {
            ExportModes.JSON: 'application/json',
            ExportModes.CSV: 'text/csv',
        }
        return mapping[self.mode]

    def get_extension(self):
        mapping = {
            ExportModes.JSON: 'json',
            ExportModes.CSV: 'csv',
        }
        return mapping[self.mode]
