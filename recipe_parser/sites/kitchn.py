#!/usr/bin/env python

"""
This module inherits from RecipeParser, and provides an implementation
for parsing recipes from the thekitchn.com site.

"""

from lxml import etree
import re

from ..parser import RecipeParser

class Kitchn(RecipeParser):

    @staticmethod
    def getBaseURL():
        return 'www.thekitchn.com'

    def getTitle(self):
        """The title format is:

        <title>[Recipe] recipe | Epicurious.com</title>

        we want just 'Recipe'
        """
        return ''.join(self.tree.xpath('//title')[0].text.split('-')[0].strip())

    def getIngredients(self):
        """Return a list or a map of the recipe ingredients"""
        data = []
        for node in self.tree.xpath('//li[@itemprop="recipeIngredient"]'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return data

    def getDirections(self):
        """Return a list or a map of the preparation instructions"""
        data = []
        for node in self.tree.xpath('//li[@itemprop="recipeInstructions"]'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return data

    def getNotes(self):
        """Return notes for this recipe"""
        return []

    def getTags(self):
        return []

    def getTime(self):
        return "Not listed"

