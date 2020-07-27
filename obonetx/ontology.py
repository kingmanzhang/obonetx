from obonet.read import read_obo
import networkx as nx
import copy


class Ontology:
    """
    Class to represent an ontology. The underlying data structure is a
    networkx MultiDiGraph. The class simplies some commonly used functions
    in a similar way to the Java phenol library.
    phenol: https://github.com/monarch-initiative/phenol/blob/master/phenol-core/src/main/java/org/monarchinitiative/phenol/ontology/algo/OntologyAlgorithm.java
    """
    def __init__(self, path):
        """
        Initialize an ontology class by providing the path.
        :param path:
        """
        self.graph = read_obo(path)
        self.root_id = self._find_root_id()

    def _find_root_id(self):
        """
        Find the root id
        :return: root id
        """
        for node in self.graph.nodes:
            if len(self.graph[node]) == 0:
                return node
        raise RuntimeError("root term not found")

    def nx_graph(self, deepcopy=False):
        """
        Return the networkx graph to the user to use functionalities
        supported by networkx. Note that the directions are opposite
        in networkx compare to ontologies. An edge in networkx graph is from a
        specific term to a generic term. So successors are more specific terms,
        for example, "red wine" is a successor of "wine".
        :param deepcopy: whether to create a deep copy
        :return: a copy of the ontology graph
        """
        if deepcopy:
            return copy.deepcopy(self.graph)
        else:
            return self.graph

    def get_root_id(self):
        """
        Returns the root id
        :return: root id
        """
        return self.root_id

    def ancestors(self, term_id, include_self=False):
        """
        Returns all the ancestor ontology terms (more generic terms). Note
        "ancestor" here is opposite to networkx "ancestor".
        :param term_id: query term
        :param include_self: whether to include the term itself
        :return: all ancestors
        """
        ancestor_set = nx.descendants(self.graph, term_id)
        if include_self:
            ancestor_set.add(term_id)
        return ancestor_set

    def descendants(self, term_id, include_self=False):
        """
        Returns all the descendant ontology terms (more specific terms). Note
        "descendant" here is opposite to networkx "descendant".
        :param term_id: query term
        :param include_self: whether to include the term itself
        :return: all descendants
        """
        descendant_set = nx.ancestors(self.graph, term_id)
        if include_self:
            descendant_set.add(term_id)
        return descendant_set

    def parents(self, term_id, include_self=False):
        """
        Returns the immediate parents of a term
        :param term_id: query term
        :param include_self: whether to include the term itself
        :return: parents
        """
        parent_set = set(self.graph[term_id].keys())
        if include_self:
            parent_set.add(term_id)
        return parent_set

    def children(self, term_id, include_self=False):
        """
        Returns the immediate children of a term
        :param term_id: query term
        :return: children terms
        :param include_self: whether to include the term itself
        """
        child_set = set(self.graph.predecessors(term_id))
        if include_self:
            child_set.add(term_id)
        return child_set

    def terms(self):
        """
        Return all ontology terms as a set
        :return:
        """
        all_terms = copy.deepcopy(self.graph.nodes)
        return all_terms

    def term_id_2_label_map(self):
        """
        Returns a map from term id to term label
        :return: an id => label map
        """
        id_2_label = copy.deepcopy(nx.get_node_attributes(self.graph, 'name'))
        return id_2_label

    def exists_path(self, src_id, dest_id):
        """
        Checks whether there is a path from the source node to the
        destination node on the ontology tree (from most generic to most
        specific)
        :param src_id: source term id
        :param dest_id: destination term id
        :return: true iff src_id is an ancestor of dest_id. It throws a
        runtime error if two terms are identical.
        """
        if src_id == dest_id:
            raise RuntimeError("cannot decide whether there is path to itself")
        return src_id in self.ancestors(dest_id, include_self=False)

    def terms_are_siblings(self, t1, t2):
        """
        Checks whether two terms are the siblings.
        :param t1:
        :param t2:
        :return:
        """
        if t1 == t2:
            raise RuntimeError("cannot decide a term is its own sibling")
        parent1 = self.parents(t1, include_self=False)
        parent2 = self.parents(t2, include_self=False)
        return len(parent1.intersection(parent2)) > 0

    def terms_are_related(self, t1, t2):
        """
        Checks whether two terms are related.
        :param t1: term id 1
        :param t2: term id 2
        :return: true iff t1 and t2 have a common ancestor that is not the
        root of the ontology. It throws a runtime error if two terms are
        identical.
        """
        # TODO: waiting for resource to be fully tested
        raise NotImplementedError()
        # if t1 == t2:
        #     raise RuntimeError("cannot decide a terms is related to itself")
        # aces1 = self.ancestors(t1, include_self=False)
        # aces2 = self.ancestors(t2, include_self=False)
        # inst = aces1.interset(aces2)
        # for t in inst:
        #     if t != self.root_id:
        #         return True
        # return False
