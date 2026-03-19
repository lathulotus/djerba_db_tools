# Usage Guide: Individual Scripts
Individual scripts support various purposes, as laid out in this table...
|                      Script                                |            Supports                                  |
|------------------------------------------------------------|------------------------------------------------------|
|**[couchDB_dynamic_query.py](../couchDB_dynamic_query.py)**  |Local report retrieval via string-based Mango querying|
|**[couchDB_variant_search.py](../couchDB_variant_search.py)**|Variant-based filtering (i.e., SNV, CNV, Fusions)     |
|**[couchDB_dynamic_query.py](../couchDB_dynamic_query.py)**  |Numeric-based filtering & plotting report accumulation|
|**[couchDB_summary.py](../couchDB_summary.py)**       |Generation of a thorough summary table                |

<br>

# Usage Guide: Dynamic Querying
Dynamic querying can be run without running the pipeline. This is done through directly accessing CouchDB, which requires login credentials. Such credentials can be saved in a text file, organized as follows:
```
host: url
port: 0000
db_name: database_name
username: username
password: password
```

Similarly, filters must  be defined in a separate YAML file. Use this simplified [filters template](../couchDB_dynamic_filters.yaml) to set filters. Supported filters can be found under the query type's [string-based filters section](#string-based-querying).

To simply download reports:
```
python3 couchDB_dynamic_query.py --login_file login.txt --filters_file couchDB_dynamic_filters.yaml --output_dir downloaded_reports/
```

To count filtered reports without downloading files:
```
python3 couchDB_dynamic_query.py --login_file login.txt --filters_file couchDB_dynamic_filters.yaml --count
```

<br>

# Usage Guide: Variant Search
Variant search can be done without running the entire pipeline, if a folder containing JSON reports exists. Use in-line flags to specify filters. Supported filter flags can be found under the query types's [variant search section](#variant-based-querying).

Sample variant filtering for reports containing TP53 SNVs:
```
python3 couchDB_variant_search.py --input_dir folder_containing_JSONs/ --snv_gene "TP53" --output_dir filtered_TP53_snvs/
```

<br>

# Usage Guide: Numeric Search
Numeric analysis (and plotting) can be done without running the entire pipeline, if a folder containing JSON reports exists. Use in-line flags to specify filters. Supported filter flags can be found under the query types's [numeric analysis section](#numeric-based-querying).

Sample numeric filtering for reports with failed purity scores:
```
python3 couchDB_numeric_analysis.py --input_dir folder_containing_JSONs/ --purity "<=0.3" --output_dir filtered_failed_purity/
```

To download a [plot](../../3_dataVisualization/accrual_by_coverage/coverage_over_time_greeq115.png), which can be applied with or without any other numeric filters:
```
python3 couchDB_numeric_analysis.py --input_dir folder_containing_JSONs/ --purity "<=0.3" --output_dir filtered_failed_purity/ --plot
```

<br>

# Usage Guide: Summary Table
Summary tables can be generated without running the entire pipeline, if a folders containing JSON reports exists. To download a summary table:
```
python3 couchDB_summary.py --input_dir folder_containing_JSONs/ --output_name summary_table
```

<br>
