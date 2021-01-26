# -*- coding:utf-8 -*-
# @Author: wanghe
# @Time: 2021/1/22 21:51
# @Filename: File.py
# @Software: PyCharm


import os
from Enity import Disease


class FileHelper(object):
    """
    Class:
        FileHelper: Try to help us do some file operations

    Author:
        Wang He

    Attributes.txt:
        read_file_to_list: Read file and put the contents into a list
        read_file_to_diseases: Read file and put the contents into a diseases-list
        get_same_means: Get the same means fron the lines
    """

    def __init__(self, in_file_path: str):
        """Init the source file_path

        :param in_file_path: The source file's path-->only to be readed
        """
        self.in_file_path = in_file_path

    def read_file_to_list(self):
        lines = []
        try:
            with open(self.in_file_path, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    lines[i] = lines[i].strip("\n")
        except IOError:
            print("Error: File not exists")
        finally:
            if file:
                file.close()
        return lines

    def read_file_to_diseases(self):
        diseases = []
        try:
            with open(self.in_file_path, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    line = lines[i].strip("\n")
                    same_means = self.get_same_means(line)
                    if len(same_means) <= 1:
                        disease = Disease(line)
                    else:
                        disease = Disease(line)
                        n = 0
                        for k in range(len(same_means)):
                            if same_means[k] == '':
                                continue
                            if n == 0:
                                disease.name = same_means[k]
                                n += 1
                            else:
                                disease.put_item_in_sames(same_means[k])
                    diseases.append(disease)
        except IOError:
            print("Error: File not exists")
        finally:
            if file:
                file.close()
        return diseases

    def write_links_to_file(self, out_file_path, lists, attr, filename):
        """
        Write the links data into the local file

        :param out_file_path: Output file path
        :param lists: Output data lists
        :param attr: Output attr
        :return:
        """
        path = '../Output/' + attr + '/' + out_file_path
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + '/' + filename, mode='a', encoding='utf-8') as file:
            for link in lists:
                file.write(link + '\n')
        if file:
            file.close()

    def write_exec_to_file(self, execute):
        with open(self.in_file_path, mode='w', encoding='utf-8') as file:
            file.write(str(execute + 1))
            execute += 1
        if file:
            file.close()

    def get_same_means(self, line):
        """
        Get the word with the same meanings from the line

        :param line: The source line need to be split into words
        :return: The word list, if the line has no same meaning words, the list is empty
        """
        if '][' in line:
            words = line.split('[')
            for i in range(len(words)):
                words[i] = words[i].strip(']')
        else:
            words = []
        return words
