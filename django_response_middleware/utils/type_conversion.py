
def query_list_to_list(query_list):
    """
    OrderedDict_list==>list
    OrderedDict_dict==>dict

    """

    if not query_list:
        return []

    if isinstance(query_list, dict):
        try:
            return dict(query_list)
        except:

            return query_list

    elif isinstance(query_list, list):
        try:
            return [dict(i) for i in query_list]
        except:
            return [i for i in query_list]
