空标签 = set(
    "area base br col embed hr img input keygen link menuitem meta param source track wbr".split()
)
可选标签 = set(
    "html head body p colgroup thead tbody tfoot tr th td li dt dd optgroup option".split()
)
无需闭合标签 = 空标签 | 可选标签
标签表 = {
    "链接": "a",
    "段落": "p",
    "一级标题": "h1",
    "二级标题": "h2",
    "三级标题": "h3",
    "四级标题": "h4",
    "五级标题": "h5",
    "六级标题": "h6",
    "文本": "span",
    "容器": "div",
    "换行": "br",
    "分割线": "dr",
    "图片": "img",
    "加粗": "b",
    "删除": "del",
    "内嵌网页": "frame",
    "输入框": "input",
    "标签": "label",
    "多行输入框": "textarea",
    "表单": "form",
    "音频": "audio",
    "视频": "video",
    "表格": "table",
    "表头": "thead",
    "表格内容": "tbody",
    "表头元素": "th",
    "表行": "tr",
    "表列": "td",
    "下拉框": "select",
    "下拉项": "option",
    "列表": "ul",
    "列表项": "li",
    "引入资源": "link",
    "JS脚本": "script",
    "标题": "title",
    "按钮": "button",
}
样式表 = {
    "宽": "width",
    "高": "height",
    "行高": "line-height",
    "边框": "border",
    "边框宽度": "border-width",
    "边框颜色": "border-color",
    "边框样式": "border-style",
    "边框半径": "border-radius",
    "外边距": "margin",
    "上外边距": "margin-top",
    "下外边距": "margin-bottom",
    "左外边距": "margin-left",
    "右外边距": "margin-right",
    "内边距": "padding",
    "上内边距": "padding-top",
    "下内边距": "padding-bottom",
    "左内边距": "padding-left",
    "右内边距": "padding-right",
    "字体颜色": "color",
    "背景颜色": "background-color",
    "字体": "font",
    "字体大小": "font-size",
    "字体粗度": "font-weight",
    "字体样式": "font-style",
    "字体系列": "font-family",
    "文本对齐": "text-align",
    "文本装饰": "text-decoration",
    "文本缩进": "text-indent",
    "文本溢出": "text-overflow",
    "显示": "display",
    "位置": "position",
    "顶部": "top",
    "底部": "bottom",
    "左边": "left",
    "右边": "right",
    "浮动": "float",
    "清除浮动": "clear",
    "透明度": "opacity",
    "可见性": "visibility",
    "溢出": "overflow",
    "换行": "word-wrap",
    "Z轴索引": "z-index",
    "最大宽度": "max-width",
    "最小宽度": "min-width",
    "最大高度": "max-height",
    "最小高度": "min-height",
    "阴影": "box-shadow",
    "过渡": "transition",
    "动画": "animation",
}
颜色映射表 = {
    "黑色": "#000000",
    "白色": "#FFFFFF",
    "红色": "#FF0000",
    "绿色": "#008000",
    "蓝色": "#0000FF",
    "黄色": "#FFFF00",
    "青色": "#00FFFF",
    "紫色": "#800080",
    "橙色": "#FFA500",
    "粉色": "#FFC0CB",
    "灰色": "#808080",
    "浅灰色": "#D3D3D3",
    "深灰色": "#A9A9A9",
    "棕色": "#A52A2A",
    "金色": "#FFD700",
    "银色": "#C0C0C0",
    "天蓝色": "#87CEEB",
    "深蓝色": "#00008B",
    "橄榄色": "#808000",
    "暗红色": "#8B0000",
    "紫罗兰": "#EE82EE",
    "靛蓝": "#4B0082",
    "藏青色": "#000080",
    "亮绿色": "#00FF00",
    "海军蓝": "#4682B4",
    "深绿": "#006400",
    "珊瑚色": "#FF7F50",
    "巧克力色": "#D2691E",
    "淡紫色": "#DDA0DD",
    "淡黄色": "#FFFFE0",
    "亮蓝色": "#ADD8E6",
    "亮青色": "#E0FFFF",
    "亮粉色": "#FFB6C1",
}
样式值表 = {
    # display 属性相关
    "块级": "block",  # 块级元素
    "内联": "inline",  # 内联元素
    "内联块": "inline-block",  # 内联块元素
    "无": "none",  # 隐藏元素
    # position 属性相关
    "静态": "static",  # 静态定位
    "相对": "relative",  # 相对定位
    "绝对": "absolute",  # 绝对定位
    "固定": "fixed",  # 固定定位
    "粘性": "sticky",  # 粘性定位
    # float 属性相关
    "左浮动": "left",  # 左浮动
    "右浮动": "right",  # 右浮动
    "无浮动": "none",  # 清除浮动
    # text-align 属性相关
    "居左": "left",  # 左对齐
    "居右": "right",  # 右对齐
    "居中": "center",  # 居中对齐
    "两端对齐": "justify",  # 两端对齐
    # font-weight 属性相关
    "正常": "normal",  # 正常粗细
    "粗体": "bold",  # 粗体
    "轻体": "lighter",  # 细体
    "超粗": "bolder",  # 特别粗
    # visibility 属性相关
    "可见": "visible",  # 可见
    "不可见": "hidden",  # 不可见
    "折叠": "collapse",  # 折叠（如表格中的列或行）
    # overflow 属性相关
    "隐藏": "hidden",  # 溢出内容隐藏
    "滚动": "scroll",  # 始终显示滚动条
    "自动": "auto",  # 根据需要显示滚动条
    # cursor 属性相关
    "默认": "default",  # 默认指针
    "指针": "pointer",  # 手形指针（常用于超链接）
    "文本": "text",  # 文本输入指针
    "移动": "move",  # 移动指针
    "不可用": "not-allowed",  # 不可用状态
    # text-decoration 属性相关
    "无装饰": "none",  # 无文本装饰
    "下划线": "underline",  # 下划线
    "上划线": "overline",  # 上划线
    "贯穿线": "line-through",  # 删除线
    # white-space 属性相关
    "不换行": "nowrap",  # 不换行
    "预格式": "pre",  # 保留空白和换行
    "预格式包裹": "pre-wrap",  # 保留空白且自动换行
    "预格式行": "pre-line",  # 合并空白符但保留换行
    # list-style 属性相关
    "圆圈": "circle",  # 圆圈
    "实心圆": "disc",  # 实心圆
    "方块": "square",  # 方块
    # flexbox 相关
    "行": "row",  # 主轴为水平方向
    "列": "column",  # 主轴为垂直方向
    "换行": "wrap",  # 容器内的元素换行
    "中心": "center",  # 元素居中对齐
    "左对齐": "flex-start",  # 元素左对齐
    "右对齐": "flex-end",  # 元素右对齐
    "平均分配": "space-between",  # 元素两端对齐
    "平均对齐": "space-around",  # 元素之间平均分配空间
}
样式值表.update(颜色映射表)
参数表 = {
    "链接地址": "href",
    "样式类": "class",
    "资源": "src",
    "标题": "title",
    "禁用": "disabled",
    "类型": "type",
    "名称": "name",
    "链接打开方式": "target",
    "必填": "required",
    "只读": "readonly",
    "值": "value",
    "输入提示": "placeholder",
    "表单提交类型": "method",
    "表单提交地址": "action",
    "表单编码类型": "enctype",
    "图片描述": "alt",
    "选中": "checked",
    "下拉选中项": "selected",
    "隐藏": "hidden",
}
参数值表 = {
    "新窗口": "_blank",
    "当前窗口": "_self",
    "密码": "password",
    "文本": "text",
    "勾选框": "checkbox",
    "邮箱": "email",
    "链接": "url",
    "电话号码": "tel",
    "数字": "number",
    "范围选中": "range",
    "单选": "radio",
    "文件": "file",
    "提交": "submit",
    "重置": "reset",
    "按钮": "button",
    "隐藏": "hidden",
}

资源类型表 = {
    "manifest.json": dict(rel="manifest"),
    "css": dict(rel="stylesheet"),
    "png": dict(rel="icon", type="image/png"),
    "svg": dict(rel="icon", type="image/svg+xml"),
    "ico": dict(rel="icon", type="image/x-icon"),
    "webp": dict(rel="icon", type="image/webp"),
    "avif": dict(rel="icon", type="image/avif"),
}
无需转换的属性值 = ["name"]
