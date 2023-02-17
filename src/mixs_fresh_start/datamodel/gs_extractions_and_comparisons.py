import csv
import logging

import click
import click_log

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

sheets_base_name = 'https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid='


def get_row_dicts(tsv_file):
    with open(tsv_file) as tsv_file:
        rows = []
        reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in reader:
            rows.append(row)
    return rows


class GsExtractionsAndComparison:

    def __init__(self, core_tsv, package_tsv):
        self.packages_row_list = get_row_dicts(package_tsv)
        self.core_row_list = get_row_dicts(core_tsv)

    def get_first_package_row(self):
        return self.packages_row_list[0]

    def get_first_core_row(self):
        return self.core_row_list[0]


@click.command()
@click.option('--package_file',
              default='assets/MIxS_6_term_updates-MIxS6_packages-Final_clean.tsv',
              help=f"TSV download of {sheets_base_name}750683809",
              required=True,
              type=str,
              )
@click.option('--core_file',
              default='assets/MIxS_6_term_updates-MIxS6_Core-Final_clean.tsv',
              help=f"TSV download of {sheets_base_name}178015749",
              required=True,
              type=str
              )
def cli(package_file: str, core_file: str):
    gs_extractions_and_comparison = GsExtractionsAndComparison(package_file, core_file)
    package_columns = list(gs_extractions_and_comparison.get_first_package_row().keys())
    core_columns = list(gs_extractions_and_comparison.get_first_core_row().keys())

    package_only_columns = set(package_columns) - set(core_columns)
    core_only_columns = set(core_columns) - set(package_columns)
    intersection_columns = set(package_columns) & set(core_columns)

    print(f"Package only columns: {package_only_columns}")
    print(f"Core only columns: {core_only_columns}")
    print(f"Intersection columns: {intersection_columns}")

    # schema_view = SchemaView(schema_file, merge_imports=True)
    #
    # comparisons = []
    #
    # schema_classes = schema_view.all_classes()
    # for ck, cv in schema_classes.items():
    #     if cv.slot_usage:
    #         for uk, uv in cv.slot_usage.items():
    #             uv_dict = json_dumper.to_dict(uv)
    #             for dk, dv in uv_dict.items():
    #                 if type(dv) == bool:
    #                     reference_slot = schema_view.get_slot(uk)
    #                     reference_attribute = reference_slot[dk]
    #                     comparison = {
    #                         "class": ck,
    #                         "slot": uk,
    #                         "attribute": dk,
    #                         "value": dv,
    #                         "reference_value": reference_attribute
    #                     }
    #                     comparisons.append(comparison)

    # with open(out_file, 'w') as f:
    #     writer = csv.DictWriter(f, fieldnames=comparisons[0].keys(), delimiter='\t')
    #     writer.writeheader()
    #     writer.writerows(comparisons)


if __name__ == '__main__':
    cli()
