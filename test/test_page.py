import unittest

from html5tagger import E, Document

from game.核心.基础数据类 import 字典
from game.核心.页面.构建 import 页面构建类, 创建页面


class TestPage(unittest.TestCase):
    def test_page(self):
        page = 创建页面("测试")
        page.段落("测试")
        page.段落().文本("测试文本", 样式=字典(字体颜色="红色")).文本(
            "绿色文本", 样式=字典(字体颜色="紫色")
        )

        with page.表单(
            表单提交类型="post", 表单提交地址="/", 样式=字典(左外边距="10px")
        ):
            page.段落("欢迎注册")
            page.段落.标签("用户名:").输入框(类型="文本")
            page.段落.标签("密码:").输入框(类型="文本")
            page.段落.输入框(类型="提交", 值="注册")
        page.模板_页头.JS脚本(资源="/test.js")
        print(page.渲染())

    def test_html_tagger(self):
        doc = Document(
            E.TitleText_,  # The first argument is for <title>, adding variable TitleText
            lang="en",  # Keyword arguments for <html> attributes
            # Just list the resources you need, no need to remember link/script tags
            _urls=["style.css", "favicon.png", "manifest.json"],
        )

        # Upper case names are template variables. You can modify them later.
        doc.Head_
        doc.h1.TitleText_("Demo")  # Goes inside <h1> and updates <title> as well

        # This has been a hard problem for DOM other such generators:
        doc.p("A paragraph with ").a("a link", href="/files")(" and ").em("formatting")

        # Use with for complex nesting (not often needed)
        with doc.table(id="data"):
            doc.tr.th("First").th("Second").th("Third")
            doc.TableRows_

        # Let's add something to the template variables
        doc.Head._script("console.log('</script> escaping is weird')")

        table = doc.TableRows
        for row in range(10):
            table.tr
            for col in range(3):
                table.td(row * col)

        # Or remove the table data we just added
        doc.TableRows = None
        print(doc)
