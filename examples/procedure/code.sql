create or replace procedure hello()
    returns string
    language python 
    runtime_version= '3.8'
    packages=('snowflake-snowpark-python')
    imports=('@tutorial/branches/main/examples/procedure/hello.py')
    handler='hello.main';

call hello();