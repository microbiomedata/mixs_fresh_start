## Add your own custom Makefile targets here

RUN=poetry run

tsvs_all: tsvs_cleanup pre_col_diff_report management_all post_col_diff_report assets/mixs_combined.tsv report_id_scn_multi_pairings

tsvs_cleanup:
	rm -rf \
assets/mixs_combined.tsv \
assets/mixs_v6.xlsx \
assets/mixs_v6_MIxS.tsv \
assets/mixs_v6_MIxS_managed_keys.tsv \
assets/mixs_v6_environmental_packages.tsv \
assets/mixs_v6_environmental_packages_managed_keys.tsv

# Chris Mungall and Chris Hunter prefer not to the MIxS Google Sheets in
#   https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o
#   - They have already been converted into Mungall's https://github.com/GenomicsStandardsConsortium/mixs/tree/main/model/schema by mixs_converter.py
#   - They could have theoretically been changed since the MIxS 6.1 release was made

assets/mixs_v6.xlsx:
	curl -L "https://github.com/GenomicsStandardsConsortium/mixs/raw/main/mixs/excel/mixs_v6.xlsx" > $@


pre_col_diff_report: assets/mixs_v6_MIxS.tsv assets/mixs_v6_environmental_packages.tsv
	$(RUN) compare_headers \
		--file1 $(word 1, $^) \
		--file2  $(word 2, $^)

# Define a list of sheet names to extract.
SHEET_NAMES := MIxS environmental_packages

# Define a pattern rule to generate TSV files for all sheets in the XLSX file.
assets/mixs_v6_%.tsv: assets/mixs_v6.xlsx
	$(RUN) xlsx_tab_to_tsv \
		--log_level INFO \
		--sheet $* \
		--tsv_output $@ \
		--xlsx_input $<

# Define a phony target to generate TSV files for all sheets in the XLSX file.
.PHONY: extract_all_sheets
extract_all_sheets: $(patsubst %,assets/mixs_v6_%.tsv,$(SHEET_NAMES))


assets/mixs_v6_MIxS_managed_keys.tsv: assets/mixs_v6_MIxS.tsv
	$(RUN) tsv_key_management \
		--input-tsv $< \
		--output-tsv $@ \
		--key-to-remove migs_ba \
		--key-to-remove migs_eu \
		--key-to-remove migs_org \
		--key-to-remove migs_pl \
		--key-to-remove migs_vi \
		--key-to-remove mimag \
		--key-to-remove mimarks_c \
		--key-to-remove mimarks_s \
		--key-to-remove mims \
		--key-to-remove misag \
		--key-to-remove miuvig \
		--rename-column "Item (rdfs:label)" Item \
		--rename-column Occurence Occurrence


assets/mixs_v6_environmental_packages_managed_keys.tsv: assets/mixs_v6_environmental_packages.tsv
	$(RUN) tsv_key_management \
		--input-tsv $< \
		--output-tsv $@ \
		--key-to-remove Requirement \
		--rename-column "Package item" Item

management_cleanup:
	rm -rf assets/mixs_v6_MIxS_managed_keys.tsv assets/mixs_v6_environmental_packages_managed_keys.tsv

management_all: management_cleanup assets/mixs_v6_MIxS_managed_keys.tsv assets/mixs_v6_environmental_packages_managed_keys.tsv

post_col_diff_report: assets/mixs_v6_MIxS_managed_keys.tsv assets/mixs_v6_environmental_packages_managed_keys.tsv
	$(RUN) compare_headers \
		--file1 $(word 1, $^) \
		--file2  $(word 2, $^)


assets/mixs_combined.tsv: assets/mixs_v6_MIxS_managed_keys.tsv assets/mixs_v6_environmental_packages_managed_keys.tsv
	$(RUN) combine_any_tsvs \
	  --input-tsv1 $(word 1, $^) \
	  --input-tsv2 $(word 2, $^) \
	  --column-order "MIXS ID","Structured comment name","Item","Environmental package","Section","Expected value","Value syntax","Occurrence","Preferred unit","Example","Definition" \
	  --output-tsv $@

report_id_scn_multi_pairings: assets/mixs_combined_modified.tsv
	$(RUN) find_multi_pairings \
		--input_tsv $< \
		--column_a "Structured comment name" \
		--column_b "Item"


		-#-column_b "Structured comment name"
		-#-column_b "Item"
		-#-column_b "MIXS ID"

assets/mixs_uniform_terms.tsv: assets/mixs_combined_modified.tsv
	$(RUN) drop_then_remove_dupes \
		--input-tsv $< \
		--uniform-terms-out $@ \
		--conflicting-terms-out $(subst uniform,conflicting, $@) \
		--drop-field "Environmental package" \
		--drop-field "Section" \
		--drop-field "Example"

assets/mixs_combined_original_no_752.tsv: assets/mixs_combined_original.tsv
	grep -v "MIXS:0000752"  $< > $@


assets/mixs_combined_modified_no_752.tsv: assets/mixs_combined_modified.tsv
	grep -v "MIXS:0000752" $< > $@

assets/mixs_combined_diff.html: assets/mixs_combined_original_no_752.tsv assets/mixs_combined_modified_no_752.tsv
	script -q -c "csvdiff --separator '\t'  --primary-key 0,3,4 --format word-diff  $^" | aha > $@

diff_cleanup:
	rm -rf assets/mixs_combined_original_no_752.tsv assets/mixs_combined_modified_no_752.tsv assets/mixs_combined_diff.html

diff_all: diff_cleanup assets/mixs_combined_diff.html


# denoters
  #MIXS ID
  #Structured comment name
  #Item

# context
  #Environmental package
  #Section

  #Expected value
  #Value syntax
  #Occurrence
  #Preferred unit
  #Definition

# package specific
  #Example