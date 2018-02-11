#!/usr/bin/env python

"""
budgetbytes.py

This module inherits from RecipeParser, and provides an implementation
for parsing recipes from the budgetbytes.com site.

"""

from lxml import etree
import re

from ..parser import RecipeParser

class BudgetBytes(RecipeParser):

    @staticmethod
    def getBaseURL():
        return 'www.budgetbytes.com'

    def getTitle(self):
        """The title format is:

        <title>[Recipe] recipe | Epicurious.com</title>

        we want just 'Recipe'
        """
        return ''.join(self.tree.xpath('//title')[0].text.split('-')[0].strip())

    def getIngredients(self):
        """Return a list or a map of the recipe ingredients"""
        data = []
        for node in self.tree.xpath('//li[@class="wprm-recipe-ingredient"]'):
            ingred_string = ''
            for subnode in node.xpath('.//*'):
                if subnode.text is None or subnode.text[0] == '$':
                    continue
                ingred_string += subnode.text
                if subnode.text[-1] != ' ':
                    ingred_string += ' '
            data.append(ingred_string[:-1])
        return data

    def getDirections(self):
        """Return a list or a map of the preparation instructions"""
        data = []
        for node in self.tree.xpath('//div[@class="wprm-recipe-instruction-text"]'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return data

    def getNotes(self):
        """Return notes for this recipe"""
        data = []
        for node in self.tree.xpath('//div[@class="wprm-recipe-notes-container"]/p'):
            data.append( ''.join(node.xpath('descendant-or-self::text()')).strip() )
        return data

    def getTags(self):
        return []

    def getTime(self):
        data = ""
        node = self.tree.xpath('//div[@class="wprm-recipe-total-time-container"]')[0]
        for subnode in node[2:]:
            data += ''.join(subnode.xpath('descendant-or-self::text()')).strip()+' '
        return data[:-1]

