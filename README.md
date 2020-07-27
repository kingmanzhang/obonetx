# obonetx: an intuitive way to use obonet for OBO-formatted ontologies

ObonetX is built on top of [obonet](https://github.com/dhimmel/obonet) and provides an intuitive way to use obo-formatted ontologies. Obonet parses an obo ontology into a [networkx](https://networkx.readthedocs.io/en/stable/overview.html) graph and expects users to call networkx functions to access ontology resources. While this approach takes full advantages of the power of networkx, it is not easy for users who are not familiar with networkx and not intuitive to manage an ontology. This package provides a wrapper of networkx graph models as an Ontology class and simplies the way to use an ontology. Many ideas are from [phenol](https://github.com/monarch-initiative/phenol), a java package for parsing and accessing ontologies.

## Usage
Parse and use the Human Phenotype Ontology
```python
from obonetx.ontology import Ontology

# use an url or file path
hpo_url = 'http://purl.obolibrary.org/obo/hp.obo'
hpo = Ontology(hpo_url)

# show root id
hpo.get_root_id()

# show all terms (term id as a set)
hpo.terms()

# show ancestor terms for HP:3000072 Abnormal levator palpebrae superioris morphology, excluding itself
hpo.ancestors(term_id='HP:3000072', include_self=False)

# show descendants of HP:0008050 Abnormality of the palpebral fissures, excluding itself
hpo.descendants(term_id='HP:0008050', include_self=False)

# show parents of HP:3000072 Abnormal levator palpebrae superioris morphology, excluding itself
hpo.parents(term_id='HP:3000072', include_self=False)

# show children of HP:3000072 Abnormal levator palpebrae superioris morphology, excluding itself
hpo.children(term_id='HP:3000072', include_self=False)

# check if there is a path between two terms
hpo.exists_path(src_id='HP:3000072', dest_id='HP:0000492')

# check if two terms are siblings
hpo.terms_are_siblings(t1='HP:3000072', t2='HP:0000492')

# retrieve a map from term_id to term_label
hpo.term_id_2_label_map()

# retrieve the underlying networkx graph model
hpo.nx_graph()

```

## Contributing

We welcome feature suggestions and community contributions.

## Installation

Install from pypi
```bash
pip install obonetx
```



