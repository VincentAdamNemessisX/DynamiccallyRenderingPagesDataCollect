"""
# File       : testReplace.py
# Time       : 12:14 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
string = """
# ![Metrics](https://metrics.lecoq.io/
VincentAdamNemessisX?
template=classic&
base.header=1&
base.activity=1&
base.community=1&
base.repositories=1&
base.metadata=1&
isocalendar=1&
followup=1&
code=1&
lines=2&
base.indepth=true&
base.hireable=true&
isocalendar.duration=half-year&
followup.sections=repositories&
followup.indepth=true&
followup.archived=true&
code.lines=12&code.load=400&
code.days=30&
code.visibility=public&
config.timezone=Asia%2FShanghai)
"""
str = string.replace('\n', '')
print(str)