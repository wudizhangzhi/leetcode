# coding=utf8
import os
from distutils.core import setup

setup(
    name='LeetCodeCrawler',
    packages=['LeetCodeCrawler'],
    # packages = os.listdir('tools'),
    version='0.1.2',  # Ideally should be same as your GitHub release tag varsion
    description='A LeetCode Crawler',
    author='wudizhangzhi',
    author_email='554330595@qq.com',
    url='https://github.com/wudizhangzhi/leetcode',
    download_url='https://github.com/wudizhangzhi/leetcode/archive/0.1.2.tar.gz',
    keywords=['leetcode', 'crawler'],
    install_requires=['requests>=2.18.4',
                      'lxml>=3.7.3',
                      'user-agent>=0.1.9'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="BSD",
)
