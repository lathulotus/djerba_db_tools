# Untitled object in Clinical - Report Structure Schema Schema

```txt
Clinical.schema.json#/properties/case_overview/properties/results
```

Results covering case overview

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## results Type

`object` ([Details](clinical_shema-properties-case_overview-properties-results.md))

# results Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                  |
| :---------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay](#assay)                     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-assay.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/assay")                   |
| [primary\_cancer](#primary_cancer)  | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-primary_cancer.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/primary_cancer") |
| [site\_of\_biopsy](#site_of_biopsy) | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-site_of_biopsy.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/site_of_biopsy") |
| [study](#study)                     | `string` | Optional | cannot be null | [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-study.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/study")                   |

## assay

Type of assay used for sequencing (WGTS, WGS, TAR)

`assay`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-assay.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/assay")

### assay Type

`string`

### assay Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation                             |
| :------- | :-------------------------------------- |
| `"WGTS"` |Whole genome and transcriptome sequencing|
| `"WGS"`  |Whole genome sequencing|
| `"WES"`  |Whole exome sequencing|
| `"WTS"`  |Whole transcriptome sequencing|
| `"pWGS"` |Personalized whole genome sequencing|
| `"sWGS"` |Shallow whole genome sequencing|
| `"TAR"`  |Targeted sequencing|

## primary\_cancer

Cancer type.

`primary_cancer`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-primary_cancer.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/primary_cancer")

### primary\_cancer Type

`string`

### primary\_cancer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                         | Explanation |
| :---------------------------- | :---------- |
| `"Pancreatic adenocarcinoma"` |Pancreatic|
| `"Hepatobiliary Tumour"`      |Hepatobiliary|
| `"Multiple Myeloma"`          |Blood|
| `"Breast Cancer"`             |Breast|
| `"Invasive breast carcinoma"` |Breast|

## site\_of\_biopsy

Biopsy type/location (cfDNA)

`site_of_biopsy`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-site_of_biopsy.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/site_of_biopsy")

### site\_of\_biopsy Type

`string`

### site\_of\_biopsy Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                     | Explanation |
| :------------------------- | :---------- |
| `"Adipose"`                |             |
| `"Adnexa"`                 |             |
| `"Adrenal Gland"`          |             |
| `"Anus"`                   |             |
| `"Anorectal"`              |             |
| `"Appendix"`               |             |
| `"Ascites Fluid"`          |             |
| `"Astrocytoma"`            |             |
| `"Ampulla of Vater"`       |             |
| `"Axillary"`               |             |
| `"Back"`                   |             |
| `"Bile Duct"`              |             |
| `"Biliary"`                |             |
| `"Bladder"`                |             |
| `"Bone Marrow"`            |             |
| `"Brain"`                  |             |
| `"Bone"`                   |             |
| `"Breast"`                 |             |
| `"Buccal Cells"`           |             |
| `"Bowel"`                  |             |
| `"Carotid Artery"`         |             |
| `"Cord Blood"`             |             |
| `"Cecum"`                  |             |
| `"Cervix"`                 |             |
| `"cfDNA"`                  |             |
| `"Chest Wall"`             |             |
| `"Conjunctiva"`            |             |
| `"Cheek"`                  |             |
| `"Central Nervous System"`|             |
| `"Colon"`                  |             |
| `"Colorectal"`             |             |
| `"Cul-de-sac"`             |             |
| `"Circulating Tumour Cells"`|           |
| `"Diaphragm"`              |             |
| `"Duodenum"`               |             |
| `"Ear"`                    |             |
| `"Endometrial"`            |             |
| `"Epidural mass"`          |             |
| `"Esophagus"`              |             |
| `"Eye"`                    |             |
| `"Fallopian Tube"`         |             |
| `"Fibroid"`                |             |
| `"Fimbriae"`               |             |
| `"Fundus"`                 |             |
| `"Foreskin"`               |             |
| `"Foot"`                   |             |
| `"Gastric Margin"`         |             |
| `"Gallbladder"`            |             |
| `"Gastroesophageal Junction"`|          |
| `"Gastrointestinal stromal"`|           |
| `"Gastrojejunal"`          |             |
| `"Glomus"`                 |             |
| `"Gingiva"`                |             |
| `"Groin"`                  |             |
| `"Genital Tract"`          |             |
| `"Hypopharynx"`            |             |
| `"Heart"`                  |             |
| `"ileocecum"`              |             |
| `"Ileum"`                  |             |
| `"Iliac Crest"`            |             |
| `"Kidney"`                 |             |
| `"Lacrimal Sac"`           |             |
| `"Limb"`                   |             |
| `"Leukocyte"`              |             |
| `"Leg"`                    |             |
| `"Large Intestine"`        |             |
| `"Lymph Node"`             |             |
| `"Lymphoblast"`            |             |
| `"Lip"`                    |             |
| `"Placenta"`               |             |
| `"Lung"`                   |             |
| `"Liver"`                  |             |
| `"Larynx"`                 |             |
| `"Lymphocyte"`             |             |
| `"Mediastinum"`            |             |
| `"Mesenchyme"`             |             |
| `"Mandible"`               |             |
| `"Mouth"`                  |             |
| `"Mesentary"`              |             |
| `"Muscle"`                 |             |
| `"Maxilla"`                |             |
| `"Neck"`                   |             |
| `"Unknown"`                |             |
| `"Nose"`                   |             |
| `"Nasopharynx"`            |             |
| `"Oral Cavity"`            |             |
| `"Omentum"`                |             |
| `"Orbit"`                  |             |
| `"Ovary"`                  |             |
| `"Pancreas"`               |             |
| `"Peripheral Blood"`       |             |
| `"Pancreatobiliary"`       |             |
| `"Parathyroid"`            |             |
| `"Pelvic"`                 |             |
| `"Parotid gland"`          |             |
| `"Paratracheal"`           |             |
| `"Penis"`                  |             |
| `"Plasma"`                 |             |
| `"Perihepatic"`            |             |
| `"Peritoneum"`             |             |
| `"Peripheral Nerve"`      |             |
| `"Peri-aorta"`             |             |
| `"Prostate"`               |             |
| `"Platelet"`               |             |
| `"Palate"`                 |             |
| `"Pleura"`                 |             |
| `"Portocaval Space"`       |             |
| `"Pharynx"`                |             |
| `"periampullary"`          |             |
| `"Right Adnexa"`           |             |
| `"Rectosigmoid"`           |             |
| `"Rectum"`                 |             |
| `"Rib"`                    |             |
| `"Retroperitoneum"`        |             |
| `"Saliva"`                 |             |
| `"Small Bowel"`            |             |
| `"Scalp"`                  |             |
| `"Sigmoid Mass"`           |             |
| `"Serum"`                  |             |
| `"Salivary Gland"`         |             |
| `"Small Intestine"`        |             |
| `"Skin"`                   |             |
| `"Skull"`                  |             |
| `"Skeletal Muscle"`        |             |
| `"Spine"`                  |             |
| `"Soft Tissue"`            |             |
| `"Spleen"`                 |             |
| `"Serosa"`                 |             |
| `"Sinus"`                  |             |
| `"Stomach"`                |             |
| `"Sternum"`                |             |
| `"Subcutaneous Tissue"`    |             |
| `"Testes"`                 |             |
| `"Thymic Gland"`           |             |
| `"Thymus"`                 |             |
| `"Tonsil"`                 |             |
| `"Throat"`                 |             |
| `"Trachea"`                |             |
| `"Tongue"`                 |             |
| `"Thorax"`                 |             |
| `"Thyroid"`                |             |
| `"Urachus"`                |             |
| `"Ureter"`                 |             |
| `"Umbilical Cord"`         |             |
| `"Urine Pellet"`           |             |
| `"Urethra"`                |             |
| `"Urine Supernatant"`      |             |
| `"Uterus"`                 |             |
| `"Urine"`                  |             |
| `"Vagina"`                 |             |
| `"Vulva"`                  |             |

## study

Research study name

`study`

* is optional

* Type: `string`

* cannot be null

* defined in: [Clinical - Report Structure Schema](clinical_shema-properties-case_overview-properties-results-properties-study.md "Clinical.schema.json#/properties/case_overview/properties/results/properties/study")

### study Type

`string`
