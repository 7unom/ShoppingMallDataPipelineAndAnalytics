import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="retail-database",
    table_name="retail_bucket_1",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node SQL Query 1
SqlQuery0 = """
select * from myDataSource
"""
SQLQuery1_node1697538261400 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"myDataSource": S3bucket_node1},
    transformation_ctx="SQLQuery1_node1697538261400",
)

# Script generated for node SQL Query 2
SqlQuery1 = """
select * from myDataSource
"""
SQLQuery2_node1697538271379 = sparkSqlQuery(
    glueContext,
    query=SqlQuery1,
    mapping={"myDataSource": SQLQuery1_node1697538261400, "dim_date": S3bucket_node1},
    transformation_ctx="SQLQuery2_node1697538271379",
)

# Script generated for node Amazon Redshift
AmazonRedshift_node1697538367571 = glueContext.write_dynamic_frame.from_options(
    frame=SQLQuery1_node1697538261400,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-908444515924-eu-west-3/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.dimdate",
        "connectionName": "retailETL-redshift-connector",
        "preactions": "CREATE TABLE IF NOT EXISTS public.dimdate (sale_id BIGINT, customer_id BIGINT, product_id BIGINT, quantity BIGINT, amount_paid DOUBLE PRECISION, payment_method VARCHAR, timestamp VARCHAR, partition_0 VARCHAR);",
    },
    transformation_ctx="AmazonRedshift_node1697538367571",
)

# Script generated for node Amazon Redshift
AmazonRedshift_node1697538467670 = glueContext.write_dynamic_frame.from_options(
    frame=SQLQuery2_node1697538271379,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-908444515924-eu-west-3/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.factsales",
        "connectionName": "retailETL-redshift-connector",
        "preactions": "CREATE TABLE IF NOT EXISTS public.factsales (sale_id BIGINT, customer_id BIGINT, product_id BIGINT, quantity BIGINT, amount_paid DOUBLE PRECISION, payment_method VARCHAR, timestamp VARCHAR, partition_0 VARCHAR);",
    },
    transformation_ctx="AmazonRedshift_node1697538467670",
)

job.commit()
