#!/usr/bin/env python3
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        approved_jobs = [
        "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
        ]
        if value in approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
