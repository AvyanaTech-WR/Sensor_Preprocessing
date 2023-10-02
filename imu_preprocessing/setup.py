from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'imu_preprocessing'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "config"), glob("config/*.yaml")),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[px]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ashok_a380@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = imu_preprocessing.main:main'
        ],
    },
)
