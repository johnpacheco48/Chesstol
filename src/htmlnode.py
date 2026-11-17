from asyncio.taskgroups import TaskGroup


class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("sowwy, this function is still under constwuction")

    def props_to_html(self) -> str:
        if self.props is None or {}: return ""
        else:
            final = ""
            for i in self.props:
                final += f' {i}="{self.props[i]}"'
            return final

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):

    def __init__(self, tag: str | None, value: str, props: str | dict | None = None):
        super().__init__(tag, value, props)
        super().props_to_html()
        self.props = props


    def to_html(self) -> str:
        if self.value is None: raise ValueError("LeafNode's value cannot be None")
        if self.tag is None: return self.value
        if self.tag == "img":
            return f'<{self.tag} src="{self.props}" alt="{self.value}" />'
        elif self.tag == "a":
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.tag}, {self.value}, {self.props}'

class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list, props: str | dict | None = None):
        super().__init__(tag, children, props)
        self.children = children

    def to_html(self) -> str:
        if self.tag == None or "": raise ValueError("Tag cannot be None")
        if self.children == None or "": raise ValueError("Children cannot be None")
        child_nodes = ""
        for child in self.children:
            child_nodes += child.to_html()
        return f'<{self.tag}>{child_nodes}</{self.tag}>'
