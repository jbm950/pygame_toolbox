from setuptools import setup, find_packages

setup(name='pygame_toolbox',
      version='0.1.2',
      license='MIT',
      description='Tools to help with game development using pygame\nFor' +
                  ' complete details please reference the github page',
      author='James Milam',
      author_email='jmilam343@gmail.com',
      url='https://github.com/jbm950/pygame_toolbox',
      packages=find_packages(),
      classifers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Games/Entertainment',
          'Topic :: Software Development :: Libraries :: pygame'
      ],
      keywords='pygame'
      )
