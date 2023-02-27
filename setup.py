from setuptools import setup

package_name = 'chatsystem'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='icduser',
    maintainer_email='icduser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'chat1 = chatsystem.chatter1:main',
            'chat2 = chatsystem.chatter2:main',
            'bunsetsu = chatsystem.bunsetsu:main',
        ],
    },
)
