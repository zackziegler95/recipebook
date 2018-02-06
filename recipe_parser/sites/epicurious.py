#!/usr/bin/env python

"""
epicurious.py

This module inherits from RecipeParser, and provides an implementation
for parsing recipes from the epicurious.com site.

"""

from lxml import etree
import re

from ..parser import RecipeParser

class Epicurious(RecipeParser):

    # define some patterns to match/filter
    badTag = re.compile(r'Bon App\u00e9tit', re.I)

    @staticmethod
    def getBaseURL():
        return 'www.epicurious.com'

    def getTitle(self):
        """The title format is:

        <title>[Recipe] recipe | Epicurious.com</title>

        we want just 'Recipe'
        """
        return ' '.join(self.tree.xpath('//title')[0].text.split('|')[0].strip().split()[:-1])

    def getIngredients(self):
        """Return a list or a map of the recipe ingredients"""
        data = []
        for node in self.tree.xpath('//li[@itemprop="ingredients"]'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return data

    def getDirections(self):
        """Return a list or a map of the preparation instructions"""
        data = []
        for node in self.tree.xpath('//li[@class="preparation-step"]'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return data

    def getTags(self):
        """Return a list of tags for this recipe"""
        data = []
        for node in self.tree.xpath('//*[@itemprop="recipeCategory"]'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return list(filter(lambda x: self.badTag.search(x) is None, data))

