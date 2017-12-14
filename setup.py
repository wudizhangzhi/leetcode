# coding=utf8
import os
# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='LeetCodeCrawler',
    packages=find_packages(exclude=('easy', 'medium', 'hard')),
    # packages=['LeetCodeCrawler'],
    # packages = os.listdir('tools'),
    version='0.1.5',  # Ideally should be same as your GitHub release tag varsion
    description='A LeetCode Crawler',
    author='wudizhangzhi',
    author_email='554330595@qq.com',
    url='https://github.com/wudizhangzhi/leetcode',
    download_url='https://github.com/wudizhangzhi/leetcode/archive/0.1.5.tar.gz',
    entry_points={
        "console_scripts": ["LeetCodeCrawler = LeetCodeCrawler.LeetCodeCrawler:main", ]
    },
    keywords='leetcode crawler',
    python_requires='>=2.6,',
    install_requires=['requests>=2.18.4',
                      'lxml>=3.7.3',
                      'user-agent>=0.1.9'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="BSD",
)
