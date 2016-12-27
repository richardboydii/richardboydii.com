from invoke import task
import os
import shutil
from subprocess import call
import boto3
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
"""Shovel file used to deploy code to S3."""

OUTPUTDIR = "build"
THEME = "hugo-sustain"
BUCKET = "richardboydii.com"
S3 = boto3.resource("s3")


@task
def build(ctx):
    """Cleans the output directory and compile the site."""
    if os.path.exists(OUTPUTDIR):
        shutil.rmtree(OUTPUTDIR)
    os.makedirs(OUTPUTDIR)
    print("Output directory cleaned.")
    call(["hugo", "-t", THEME, "-d", OUTPUTDIR])
    print("Site has be built.")


def upload_file(src_dest):
    """Use boto3 to upload a file to S3."""
    S3.meta.client.upload_file(src_dest[0], BUCKET, src_dest[1])


@task
def publish(ctx):
    """Clear the S3 bucket, uploads files."""
    S3.Bucket(BUCKET).objects.delete()
    files = []
    for root, directories, filenames in os.walk(OUTPUTDIR):
        for filename in filenames:
            source = os.path.join(root, filename)
            dest = source.replace(OUTPUTDIR + "/", "")
            files.append([source, dest])
    pool = ThreadPool()
    results = pool.map(upload_file, files)
    pool.close()
    pool.join()
