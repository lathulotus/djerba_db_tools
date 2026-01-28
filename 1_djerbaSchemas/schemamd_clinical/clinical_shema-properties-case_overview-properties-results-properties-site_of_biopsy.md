# Clinical Report Structure: Case Overview - Site of Biopsy

```txt
Clinical.schema.json#/properties/case_overview/properties/results/properties/site_of_biopsy
```

Biopsy type/location (cfDNA)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [clinical\_shema.json\*](../../../../../../cygwin64/home/wwwla/out/clinical_shema.json "open original schema") |

## site\_of\_biopsy Type

`string`

## site\_of\_biopsy Constraints

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
