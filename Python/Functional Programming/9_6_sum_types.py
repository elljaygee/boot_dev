from enum import Enum

CSVExportStatus = Enum(
    "CSVExportStatus", ["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
)

def prepare(data):
    stringify_row = lambda one_row: list(map(str, one_row))
    return list(map (stringify_row, data))

def process(prepared_data):
    join_row = lambda one_row: ",".join(one_row)
    return "\n".join(map(join_row, prepared_data))
    

def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending...", prepare(data))
        case CSVExportStatus.PROCESSING:
            return ("Processing...", process(data))
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            return ("Unknown error, retrying...", process(prepare(data)))
        case _:
            raise Exception ("unknown export status")


# lambda explainer:

# lambda  n  :  n * 2
#   |     |      |
#   |     |      └── the return value (an expression)
#   |     └──────── the parameter(s)
#   └────────────── the keyword "lambda"