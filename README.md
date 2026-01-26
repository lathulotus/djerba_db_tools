# Project Overview
Djerba stores finalized genomic report outputs as JSON documents in a CouchDB database. While this design ensures traceability and archival integrity, downstream querying and cohort-level analysis are currently manual and not straightforward.

This project aims to:
- Enable structured querying of Djerba reports stored in CouchDB
- Aggregate biologically and clinically relevant variables (e.g., cancer type, KRAS status, HRD/MSI-H, residual disease)
- Automatically publish up-to-date summary tables 
- Explore integration of CouchDB outputs into downstream tools (e.g., ShawK)
