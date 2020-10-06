import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='getarticle',
      description="A package based on SciHub and Google \
            Scholar that can download articles given DOI, \
            website address or keywords.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.0.9',
      url='https://github.com/HTian1997/getarticle',
      author='Hao Tian',
      author_email='htian1997@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
            "requests", \
            'appscript; platform_system=="Darwin"',\
            "argparse"],
      entry_points={'console_scripts':\
            'getarticle = getarticle.cli:entry_point'},
      zip_safe=False
)