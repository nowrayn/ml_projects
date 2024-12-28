## "In this file we mainly create self made 'packages'."
## which we use to install using pip install.
## if you check on google like "python pipy" there you all the packeage
## which has been developed and deployed which we use by installing it
## similarly we can create and deploy on 'python pipy' then any one can use it similarly...



#####  "here i will build my ML applicatin as package and deploy in 'pipy' so that I can use it any where, even others can use.."


from setuptools import find_packages, setup
from typing import List 

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
	with open(file_path) as file_obj:
		requirements = file_obj.readlines()
		requirements=[req.replace("\n","")for req in requirements]
		if HYPEN_E_DOT in requirements:
			requirements.remove(HYPEN_E_DOT)
	return requirements


setup(

	name='MLproject',
	version='0.0.1',
	author='Nischal Nowray',
	author_email='nowrany99@gmail.com',
	packages=find_packages(),
	inatall_requires=get_requirements('requirements.txt')
)