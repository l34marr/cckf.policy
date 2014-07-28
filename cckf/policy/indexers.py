from plone.indexer.decorator import indexer
from cckf.content.interfaces import IGrant


@indexer(IGrant)
def category(obj):
    return obj.category

@indexer(IGrant)
def region(obj):
    return obj.region

