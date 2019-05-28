# Databricks notebook source
PRUEBA 5:30

# COMMAND ----------

import os
os.chdir('/opt/gams/gams27.1_linux_x64_64_sfx/apifiles/Python/api')
os.environ['LD_LIBRARY_PATH'] = '/opt/gams/gams27.1_linux_x64_64_sfx/'

# COMMAND ----------

# MAGIC %%bash
# MAGIC python setup.py install

# COMMAND ----------

# MAGIC %%bash
# MAGIC python /opt/gams/gams27.1_linux_x64_64_sfx/apifiles/Python/transport1.py