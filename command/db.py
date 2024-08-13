import graphlib
from aerich.migrate import Migrate
from aerich import utils


def get_models_describe_by_order(app: str) -> dict:
    """
    实现根据关联的字段对模型进行排序，防止在生成一对多sql的时候出现关联表后创建的问题
    :param app: orm配置里面的App
    :return:
    """
    ret = utils.get_models_describe(app=app)
    result = {}
    # 生成对应的图
    graph = {}
    for k, v in ret.items():
        graph[k] = []
        # 获取关联字段
        fk_fields = v.get("fk_fields", "")
        # 没有关联直接跳过
        if len(fk_fields) == 0:
            continue
        # 便利一对多关联，解析关联的顺序
        for fk_field in fk_fields:
            # 获取模型名称
            python_type = fk_field.get("python_type")
            if python_type:
                graph[k].append(python_type)
    # 生成图数据排序对象
    ts = graphlib.TopologicalSorter(graph)
    order_res = tuple(ts.static_order())
    for name in order_res:
        result[name] = ret[name]
    return result


async def migrate(cls, name) -> str:
    """
    diff old models and new models to generate diff content
    :param cls:
    :param name:
    :return:
    """
    new_version_content = get_models_describe_by_order(cls.app)
    cls.diff_models(cls._last_version_content, new_version_content)
    cls.diff_models(new_version_content, cls._last_version_content, False)

    cls._merge_operators()

    if not cls.upgrade_operators:
        return ""

    return await cls._generate_diff_py(name)


# 重写迁移函数
Migrate.migrate = classmethod(migrate)


# 防止变量修改失效，所以后导入cli
def get_cli():
    from aerich.cli import cli

    return cli


cli = get_cli()

__all__ = ["cli"]
