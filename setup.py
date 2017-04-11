try:
    import setuptools
    from setuptools import setup
except ImportError:
    print("Please install setuptools.")

setup_options = dict(
    name="slack_notification",
    description="slack webhook",
    author="judetan",
    author_email="judetan@gmail.com",
    license="MIT License",
    url="https://github.com/aethersg/slack_notifications.git",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: MIT License"
    ]
)
setup_options["version"] = "1.0.0"
setup_options.update(dict(
    packages=['slack_notification'],
))

setup(**setup_options)
