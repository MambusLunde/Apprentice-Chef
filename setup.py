from setuptools import setup, find_packages

setup(name="Apprentice-Chef",
      version="0.1.0",
      description="Predicting revenue and cross-sell success",
      author="Mats Lunde",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="immambus@gmail.com",
      )