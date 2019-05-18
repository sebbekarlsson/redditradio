from setuptools import setup, find_packages


setup(
    name='redditradio',
    version='1.0.0',
    install_requires=[
        'google_speech',
        'pyttsx',
        'requests',
        'user_agent',
        'pickledb'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'redditradio = redditradio.bin:run'
        ]
    }
)
