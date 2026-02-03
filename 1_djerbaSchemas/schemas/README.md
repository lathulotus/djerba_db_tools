# JSON File Structure Breakdown:

This document outlines the hierarchical structure of the clinical report, showing its components and associated contents. The tree format effectively visualizes the hierarchy and data within the JSON, and highlights the differences between the structure of a passing report and a failed report.
## Passing Clinical Report hierarchy 
```
MOHCCNO-2308-v1_report.clinical.json
├── _id: string, report unique identifier (e.g., "MOHCCNO-2308-v1")
│
├── _rev: string, revision token used for version control (e.g., "4-9fff255e183af139035bc5c36285e444")
│
├── last_updated: string timestamp (e.g., "24/12/2025_16:04:30Z")
│
├── core: object, containing fundamental information about the report
│       ├── author: string, name of CGI member who authored the report.
│       ├── document_config: string, reference to the config file.
│       ├── report_id: string, report main identifier 
│       ├── core_version: string, version of the core reporting software.
│       └── extract_time: string, timestamp.
│
├── plugins: object, holds detailed results.
│       ├── wgts.cnv_purple: object, Copy Number Variation results.
│       │       ├── plugin_name: string 
│       │       ├── version: string 
│       │       ├── priorities: object, defines plugin execution order
│       │       │   ├── configure: integer
│       │       │   ├── extract: integer
│       │       │   └── render: integer
│       │       ├── attributes: array of strings (e.g., ["research"])
│       │       ├── merge_inputs: object, inputs used for merging data
│       │       │   ├── gene_information_merger: array of objects
│       │       │   │       └── { Gene: str, Gene_URL: str, Summary: str}
│       │       │   └── treatment_options_merger: array.
│       │       └── results: object, CNV analysis results.
│       │               ├── percent genome altered: integer
│       │               ├── total variants: integer 
│       │               ├── clinically relevant variants: integer 
│       │               ├── cnv plot: string, base64 encoded SVG 
│       │               ├── has expression data: boolean
│       │               └── body: array of objects
│       │                       └── { "Expression Percentile", "Gene", "Gene_URL", "Alteration", "Chromosome", "OncoKB" }
│       │
│       ├── wgts.snv_indel: object, Single Nucleotide Variants and Indels results.
│       │       ├── plugin_name
│       │       ├── version
│       │       ├── priorities
│       │       ├── attributes
│       │       ├── merge_inputs
│       │       │   ├── gene_information_merger
│       │       │   └── treatment_options_merger
│       │       └── results: object
│       │               ├── somatic mutations: integer
│       │               ├── coding sequence mutations: integer
│       │               ├── oncogenic mutations: integer
│       │               ├── vaf_plot: string (base64 encoded)
│       │               ├── has loh data: boolean
│       │               ├── has expression data: boolean
│       │               └── Body: array of objects
│       │                       └── { "Expression percentile", "Gene", "Gene URL", "protein", "type", "vaf", "LOH", "Chromosome", "OncoKB" }
│       │
│       ├── fusion: object, gene fusions results.
│       │       ├── plugin_name: string 
│       │       ├── version: string
│       │       ├── priorities: object
│       │       ├── attributes: array of strings
│       │       ├── merge_inputs: object
│       │       └── results: object
│       │               ├── Clinically relevant variants: integer
│       │               ├── NCCN relevant variants: integer
│       │               ├── Total variants: integer
│       │               └── body: array of objects 
│       │
│       ├── genomic_landscape: object, high-level genomic biomarker info.
│       │       ├── plugin_name: string 
│       │       ├── version: string 
│       │       ├── priorities: object
│       │       ├── attributes: array of strings
│       │       ├── merge_inputs: object
│       │       └── results: object
│       │               ├── genomic_landscape_info: object (Summary info like TMB, percentiles)
│       │               │   ├── Tumour Mutation Burden: integer
│       │               │   ├── TMB per megabase: integer
│       │               │   ├── Cancer-specific Percentile: integer
│       │               │   ├── Cancer-specific Cohort: string
│       │               │   ├── Pan-cancer Percentile: integer
│       │               │   └── Pan-cancer Cohort: string
│       │               ├── genomic_biomarkers: object (Specific biomarker details)
│       │               │   ├── TMB: object
│       │               │   │   └── { Alteration, Alteration_URL, "Genomic biomarker value", "Genomic alteration actionable", "Genomic biomarker text", "Genomic biomarker plot" }
│       │               │   ├── HRD: object (Homologous Recombination Deficiency details)
│       │               │   └── MSI: object (Microsatellite Instability details)
│       │               ├── can_report_hrd: boolean
│       │               ├── can_report_msi: boolean
│       │               ├── cant_report_hrd_reason: string
│       │               └── ctDNA: object 
│       │                   ├── ctDNA_candidate_sites: integer
│       │                   └── ctDNA_eligibility: string
│       │
│       └── supplement.body: object
│               ├── plugin_name: string
│               ├── priorities: object
│               ├── attributes: array of strings
│               ├── merge_inputs: object
│               └── results: object
│                   ├── assay: string (e.g., "WGTS")
│                   ├── components: object (Versions and URLs of sub-components)
│                   │   └── core, expression_helper, fusion, genomic_landscape, ... (each with url and version)
│                   ├── failed: boolean
│                   ├── author: string
│                   ├── extract_date: string
│                   ├── include_signoffs: boolean
│                   ├── url: string
│                   ├── version: boolean
│                   └── template_dir: string
│
├── mergers: object
│       ├── treatment_options_merger: object
│       │       ├── render_priority: integer
│       │       └── attributes: array of strings
│       └── gene_information_merger: object
│               ├── render_priority: integer
│               └── attributes: array of strings
│
├── config: object, contains the full set of input parameters for all plugins used in generating the report.
│       ├── input_params_helper: object
│       ├── provenance_helper: object
│       ├── wgts.cnv_purple: object
│       └── ... (configurations for all other plugins)
│
└── html_cache: object, stores pre-rendered HTML content for quick display of the report.
        └── MOHCCNO-2308-v1_report: string, the actual cached HTML report in base64 format.
```
## Failed Clinical Report hierarchy 

```
MOHPC1_2-2682-v1_report.json
├── core: object
│   ├── author: string
│   ├── document_config: string
│   ├── report_id: string
│   ├── core_version: string
│   └── extract_time: string
│
├── plugins: object
│   ├── report_title: object
│   │   ├── plugin_name: string
│   │   ├── version: string
│   │   ├── priorities: object
│   │   │   ├── configure: integer
│   │   │   ├── extract: integer
│   │   │   └── render: integer
│   │   ├── attributes: array of strings
│   │   └── results: object
│   │       └── header_type: string
│   │
│   ├── patient_info: object
│   │   ├── plugin_name: string
│   │   ├── version: string
│   │   ├── priorities: object
│   │   ├── attributes: array of strings
│   │   └── results: object
│   │       ├── patient_name: string
│   │       ├── patient_dob: string
│   │       ├── patient_genetic_sex: string
│   │       ├── requisitioner_email: string
│   │       ├── physician_licence_number: string
│   │       ├── physician_name: string
│   │       ├── physician_phone_number: string
│   │       └── hospital_name_and_address: string
│   │
│   ├── case_overview: object
│   │   ├── plugin_name: string
│   │   ├── version: string
│   │   ├── priorities: object
│   │   ├── attributes: array of strings
│   │   └── results: object
│   │       ├── assay: string
│   │       ├── assay_description: string
│   │       ├── primary_cancer: string
│   │       ├── site_of_biopsy: string
│   │       ├── donor: string
│   │       ├── study: string
│   │       ├── patient_study_id: string
│   │       ├── tumour_id: string
│   │       ├── normal_id: string
│   │       ├── report_id: string
│   │       └── requisition_approved: string
│   │
│   ├── summary: object
│   │   ├── plugin_name: string
│   │   ├── version: string
│   │   ├── priorities: object
│   │   ├── attributes: array of strings
│   │   └── results: object
│   │       ├── summary_text: string
│   │       └── failed: boolean
│   │
│   ├── sample: object
│   │   ├── plugin_name: string
│   │   ├── version: string
│   │   ├── priorities: object
│   │   ├── attributes: array of strings
│   │   └── results: object
│   │       ├── OncoTree code: string
│   │       ├── Sample Type: string
│   │       ├── Estimated Cancer Cell Content (%): integer
│   │       ├── Estimated Ploidy: string
│   │       ├── Callability (%): string
│   │       └── Coverage (mean): string
│   │
│   └── supplement.body: object
│       ├── plugin_name: string
│       ├── priorities: object
│       ├── attributes: array of strings
│       ├── merge_inputs: object
│       ├── results: object
│       │   ├── assay: string
│       │   ├── components: object
│       │   │   ├── case_overview: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   ├── core: object
│       │   │   │   ├── url: string
│       │   │   │   └── version: string
│       │   │   ├── input_params_helper: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   ├── patient_info: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   ├── provenance_helper: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   ├── report_title: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   ├── sample: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   ├── summary: object
│       │   │   │   ├── url: null
│       │   │   │   └── version: string
│       │   │   └── supplement.body: object
│       │   │       ├── url: string
│       │   │       └── version: string
│       │   ├── failed: boolean
│       │   ├── author: string
│       │   ├── extract_date: string
│       │   ├── include_signoffs: boolean
│       │   ├── template_dir: string
│       │   ├── report_signoff_date: string
│       │   ├── clinical_geneticist_name: string
│       │   └── clinical_geneticist_licence: string
│       ├── url: string
│       └── version: string
│
├── mergers: object (empty)
│
└── config: object
    ├── input_params_helper: object
    │   ├── assay: string
    │   ├── donor: string
    │   ├── oncotree_code: string
    │   ├── primary_cancer: string
    │   ├── project: string
    │   ├── requisition_approved: string
    │   ├── requisition_id: string
    │   ├── sample_type: string
    │   ├── site_of_biopsy: string
    │   ├── study: string
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   └── tcga_code: string
    │
    ├── report_title: object
    │   ├── failed: string
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   └── render_priority: string
    │
    ├── provenance_helper: object
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   ├── provenance_input_path: string
    │   ├── project: string
    │   ├── donor: string
    │   ├── assay: string
    │   ├── sample_name_normal: string
    │   ├── sample_name_tumour: string
    │   ├── sample_name_aux: string
    │   ├── tumour_id: string
    │   └── normal_id: string
    │
    ├── core: object
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   ├── render_priority: string
    │   ├── author: string
    │   ├── report_id: string
    │   ├── report_version: string
    │   ├── input_params: string
    │   └── document_config: string
    │
    ├── patient_info: object
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   ├── render_priority: string
    │   ├── patient_name: string
    │   ├── patient_dob: string
    │   ├── patient_genetic_sex: string
    │   ├── requisitioner_email: string
    │   ├── physician_licence_number: string
    │   ├── physician_name: string
    │   ├── physician_phone_number: string
    │   └── hospital_name_and_address: string
    │
    ├── sample: object
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   ├── render_priority: string
    │   ├── oncotree_code: string
    │   ├── sample_type: string
    │   ├── callability: string
    │   ├── mean_coverage: string
    │   ├── donor: string
    │   ├── purity: string
    │   ├── ploidy: string
    │   └── tumour_id: string
    │
    ├── case_overview: object
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   ├── render_priority: string
    │   ├── assay: string
    │   ├── assay_description: string
    │   ├── primary_cancer: string
    │   ├── site_of_biopsy: string
    │   ├── donor: string
    │   ├── study: string
    │   ├── patient_study_id: string
    │   ├── tumour_id: string
    │   ├── normal_id: string
    │   ├── report_id: string
    │   └── requisition_approved: string
    │
    ├── summary: object
    │   ├── failed: string
    │   ├── attributes: string
    │   ├── depends_configure: string
    │   ├── depends_extract: string
    │   ├── configure_priority: string
    │   ├── extract_priority: string
    │   ├── render_priority: string
    │   └── summary_file: string
    │
    └── supplement.body: object
        ├── failed: string
        ├── attributes: string
        ├── depends_configure: string
        ├── depends_extract: string
        ├── configure_priority: string
        ├── extract_priority: string
        ├── render_priority: string
        ├── assay: string
        ├── report_signoff_date: string
        ├── user_supplied_draft_date: string
        ├── clinical_geneticist_name: string
        ├── clinical_geneticist_licence: string
        └── template_dir: string
│
└── html_cache: object
    └── MOHPC1_2-2682-v1_report.clinical: string
```
As shown in the above structures, The top-level plugins (`core`, `plugins`, `config`) are similar, but the key differences between a passing report and a failed report are:

### 1. Different Set of Plugins

- **Passing Report** contains plugins for detailed genomic analysis:
  - `wgts.cnv_purple`
  - `wgts.snv_indel`
  - `fusion`
  - `genomic_landscape`

- **Failed Clinical Report** contains plugins to structure a basic case summary and failure notice:
  - `report_title` to generate a "failed report" title
  - `patient_info`
  - `case_overview`
  - `summary` to explicitly states the reason for failure
  - `sample`

### 2. Purpose of the Content
- **The Passing Report:** data-rich, containing arrays of genomic variants, plots, and biomarker information.  
- **The Failed Report:** lacks analytical results and provides only enough information to identify the case and the reason for quality control failure. The `summary` plugin is solely used to convey the failure text.
