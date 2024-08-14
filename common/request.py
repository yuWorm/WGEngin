def request_parmas_to_dict(parmas: dict):
    """
    将sanic的请求参数转换为正常的字典
    :param parmas:
    :return:
    """
    res = {}
    for key, value in parmas.items():
        if len(value) == 0:
            res[key] = value
        elif len(value) == 1:
            res[key] = value[0]
        else:
            res[key] = value
    return res
