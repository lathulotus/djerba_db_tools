# Project Overview
Djerba stores finalized genomic report outputs as JSON documents in a CouchDB database. While this design ensures traceability and archival integrity, downstream querying and cohort-level analysis are currently manual and not straightforward.

This project aims to:
- Enable structured querying of Djerba reports stored in CouchDB
- Aggregate biologically and clinically relevant variables
- Automatically publish up-to-date summary tables 
- Explore integration of CouchDB outputs into downstream tools

# Schema Documentation
For a better understanding on how data is stored in clinical reports (JSON files), visit [1_djerbaSchemas](./1_djerbaSchemas).

# Querying CouchDB
For querying through couchDB, visit [2_queryCouchDB](./2_queryCouchDB). This is your one-stop shop to the query scripts, usage guides, and documentation on how to use the pipeline.

# Data Analysis
For data analysis through interactive notebooks, visit [3_dataAnalysis](./3_dataAnalysis). This notebook allow for the automatic generation of weekly reports and filterable summary tables. This notebook also supports descriptive analysis by parameter and cumulative case trends between parameters.

# Case Studies
For examples of what couchDB can handle when it comes to data analysis and visualization, visit [4_caseStudies](./4_caseStudies). These are just a small handful of examples.
