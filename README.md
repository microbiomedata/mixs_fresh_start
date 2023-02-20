# mixs_fresh_start

This project requires the following system dependencies in addition to the Python libraties in pyproject.toml
- https://github.com/theZiz/aha
- https://github.com/aswinkarthik/csvdiff

## Website

* [https://microbiomedata.github.io/mixs_fresh_start](https://microbiomedata.github.io/mixs_fresh_start)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [mixs_fresh_start](src/mixs_fresh_start)
        * [schema](src/mixs_fresh_start/schema) -- LinkML schema (edit this)
* [datamodel](src/mixs_fresh_start/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)

## Where can we get MIxS specifications?

- Google Sheets (these aren't locked, so somebody could have altered them)
    - [MIxS 6 term updates, MIxS6 packages - Final_clean tab](https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=750683809)
    - [MIxS 6 term updates, MIxS6 Core- Final_clean](https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=178015749)
- Excel representation, recommend by Chris Hunter. Is there a single (or two) Excel sheets that correspond to the two
  Google Sheets? I see one sheet for each package/extension and one foreach checklist
    - https://github.com/GenomicsStandardsConsortium/mixs/tree/main/mixs/excel
- Chris
  Mungall's [automated LinkML conversion](https://github.com/GenomicsStandardsConsortium/mixs/tree/main/model/schema),
  based on https://github.com/GenomicsStandardsConsortium/mixs/blob/main/gsctools/mixs_converter.py
- [Incomplete schemasheets branch](https://github.com/GenomicsStandardsConsortium/mixs/tree/issue-511-tested-schemasheets/schemasheets)

### Advantages and disadvantages
