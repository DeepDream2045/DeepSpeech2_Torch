from distutils.core import setup

setup(
    name='deepspeech2',
    version='latest',
    author='DeepDream2045',
    author_email='DeepDream0426@gmail.com',
    url='https://github.com/sooftware/conformer',
    install_requires=[
        'torch>=1.4.0',
        'numpy',
    ],
    keywords=['asr', 'speech_recognition', 'conformer', 'end-to-end'],
    python_requires='>=3.7'
)
