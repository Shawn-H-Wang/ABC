# -*- coding:utf-8 -*-
# @Author: wanghe
# @Time: 2021/1/23 00:23
# @Filename: Enity.py
# @Software: PyCharm


class Disease(object):
    """
    Description:
        Disease with name and the same means

    Author:
        Wang He

    Attributes.txt:
        name: disease's name
        same_means: disease's same means or description
    """

    def __init__(self, name):
        """
        Init the disease class

        :param name: set the name of the disease
        """
        self.name = name
        self.same_means = []

    def is_in(self, mean):
        """
        Judge whether the means is in the same means

        :param mean: judge if the mean is in the same_means list
        :return: None
        """
        return mean in self.same_means

    def put_item_in_sames(self, same_mean):
        """
        Put the same means in to the list.
        Before push in to the list, we need to de the judge first

        :param same_mean: same_mean: item ready to be pushed
        :return: None
        """

        if not self.is_in(same_mean):
            self.same_means.append(same_mean)
