from models.tags import TagIn, Tag

tags = {}


def create(tag: Tag):
    tags[tag.tag] = tag
    return


def get(tag_str: str):
    return tags.get(tag_str)

