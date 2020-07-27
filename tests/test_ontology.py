import os
from obonetx import ontology

directory = os.path.dirname(os.path.abspath(__file__))


class TestOntologyClass:

    def setup(self):
        self.onto = ontology.Ontology(path=os.path.join(
            directory, 'data/taxrank.obo'))
        self.root = 'TAXRANK:0000000'

    def test_constructor(self):
        assert(self.onto is not None)

    def test_root_id(self):
        assert(self.onto.get_root_id() == self.root)

    def test_ancestors(self):

        assert(len(self.onto.ancestors(self.root)) == 0)
        assert(len(self.onto.ancestors(self.root, include_self=True)) == 1)

        term_id = 'TAXRANK:0000003'
        assert(self.onto.ancestors(term_id) == {'TAXRANK:0000000'})
        assert (self.onto.ancestors(term_id, include_self=True) == {
            'TAXRANK:0000000', term_id})

    def test_descendants(self):
        assert(len(self.onto.descendants(self.root)) > 0)
        assert(len(self.onto.descendants(self.root, include_self=True)) -
               len(self.onto.descendants(self.root, include_self=False)) == 1)

    def test_parents(self):
        term_id = 'TAXRANK:0000004'
        assert(self.onto.parents(term_id) == {'TAXRANK:0000000'})
        assert (self.onto.parents(term_id, include_self=True) == {
            'TAXRANK:0000000', term_id})

    def test_children(self):
        assert(len(self.onto.children(self.root)) > 0)
        assert (len(self.onto.children(self.root, include_self=True)) -
                len(self.onto.children(self.root, include_self=False)) == 1)

    def test_term_id2label_map(self):
        assert(len(self.onto.term_id_2_label_map()) > 0)
        assert(self.onto.term_id_2_label_map()[self.root] == 'taxonomic_rank')
        assert (self.onto.term_id_2_label_map()['TAXRANK:0000001'] == 'phylum')

    def test_graph(self):
        shallowcopy = self.onto.nx_graph()
        deepcopy = self.onto.nx_graph(deepcopy=True)

        shallowcopy.remove_node('TAXRANK:0000004')
        assert(len(shallowcopy.nodes) == len(self.onto.graph.nodes))
        assert(len(deepcopy.nodes) != len(self.onto.graph.nodes))

    def test_exists_path(self):
        t1 = 'TAXRANK:0000000'
        t2 = 'TAXRANK:0000004'
        t3 = 'TAXRANK:0000005'
        assert(self.onto.exists_path(t1, t2))
        assert(self.onto.exists_path(t1, t3))
        assert(not self.onto.exists_path(t2, t1))
        assert(not self.onto.exists_path(t2, t3))

    def test_terms_are_siblings(self):
        t1 = 'TAXRANK:0000000'
        t2 = 'TAXRANK:0000004'
        t3 = 'TAXRANK:0000005'
        assert (self.onto.terms_are_siblings(t2, t3))
        assert (not self.onto.terms_are_siblings(t1, t2))
        assert (not self.onto.terms_are_siblings(t1, t3))

    # def test_terms_are_related(self):
    #     t1 = 'TAXRANK:0000000'
    #     t2 = 'TAXRANK:0000004'
    #     t3 = 'TAXRANK:0000005'
    #     assert (self.onto.terms_are_related(t2, t3))
    #     assert (not self.onto.terms_are_related(t1, t2))