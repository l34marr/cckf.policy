from plone.indexer.decorator import indexer
from cckf.content.interfaces import IGrant
from cckf.content.interfaces import ISinology


@indexer(IGrant)
def category(obj):
    return obj.category

@indexer(IGrant)
def region(obj):
    return obj.region

@indexer(ISinology)
def classify(obj):
    return obj.classify

