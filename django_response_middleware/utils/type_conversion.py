
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


def list_str(error_list):
    error_list_ = []
    if isinstance(error_list, dict):
        error_list = [error_list]
    for ii in error_list:
        for k, v in ii.items():
            error_list_.append({k: v})
    return error_list_
