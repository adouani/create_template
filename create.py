# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import shutil
import traceback
import fileinput



class ProjectManager(object):
    def __init__(self,project_name,project_path):
        self.project_name=project_name
        self.project_path=project_path
        self.module_path=os.path.join(self.project_path,self.project_name)

    def create_project(self):
        if(os.path.isdir(self.module_path) ==True):
            response=raw_input("The project already exists, would you like to replace it (yes/No)?")
            if(response.strip().lower()=='yes'):
                shutil.rmtree(self.module_path)
            else:
                return;
        shutil.copytree(template,self.module_path)
        shutil.move(os.path.join(self.module_path,'__sample_project__'),
                    os.path.join(self.module_path,self.project_name))
        self.update()

    def update(self):
        files=['setup.py',]
        files=[os.path.join(self.module_path,file) for file in files]
        for file_path in files:
            file=fileinput.FileInput(file_path,
                                 inplace=1)
            for line in file:
                print(line.replace('__sample_project__', self.project_name),end='')



if __name__=="__main__":
    try:
        assert(len(sys.argv) ==3)

        here = os.path.abspath(os.path.dirname(__file__))
        template = os.path.abspath(os.path.join(here, '__sample_project__'))

        p=ProjectManager(sys.argv[1],sys.argv[2])
        p.create_project()
    except OSError as err:
        print("I/O Exception raised, either %s doesn't exist or locked for writing"%(sys.argv[2]))
        traceback.print_exc()
    except AssertionError as err:
        print("3 Arguments are expected, %s given.\nSyntaxe : python create 'project path' 'project_name' "%(len(sys.argv)))
        traceback.print_exc()


