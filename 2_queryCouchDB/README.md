# Querying CouchDB
Querying CouchDB database to assess reports stored by Djerba. Supported queries include specific report IDs for single and bulk data retrieval. Querying by metadata fields (i.e., report type, date, cancer type) further allows for bulk data retrieval by data type. This supports downstream assessment of variables production of summary tables and assessment of relationships and/or trends.

Query script found under **[query_couchdb](./query_couchdb.py)**.

### Clinical vs Research
CouchDB contains a vast amount of clinical reports along with research reports resulting from failed clinical reports. RUO reports generated on request are not archived on the database. Briefly, differences in metadata fields are as follows:
- **Clinical reports** are patient-oriented and support metadata fields such as ```primary_cancer``` and associated ```OncoTree Code```. As such, downstream ```treatment_options``` plugins are supported. Further fields include ```site_of_biopsy```, ```sample type``` and ```percent genome altered```.
- **Research reports** are data-oriented and do not support metadata fields such as ```primary_cancer``` and associated ```OncoTree Code```. As such, reports do not support the treatment options subheading. Further fields specific to the clinical reports appear as ```NA```.

<br>

# Query Types
Major queries include fetching single or bulk reports by report ID(s). Metadata filtering supports searching by general fields such as report types and date. Extensive metadata filtering supports searching by specific fields such as cancer type and biomarker value, useful for trend assessment. Query types can be viewed under **[query_types](./query_types.md)**.

<br>

# Usage Guide
Documentation on how to query CouchDB can be found under **[query_usage_guide](./query_usage_guide.md)**.

