**Hosting a Static Website in an AWS S3 Bucket**

In this lab you will use AWS to host a static website hosted in an S3 bucket, and the best part is that you’ll do it programmatically! You may recall that the lesson in module 2 indicated the benefit of having a static website when your primary website is unavailable. However, there are other scenarios where a static website is useful. In this first lab, you will explore the process of setting up a static website.

AWS allows you to provision services using the AWS Management Console, AWS CLI and AWS SDK. In this lab you will use the python SDK, which requires zero setup using our lab environment. However, if you work on this assignment using your laptops you will need to configure your development environment.

Requirements:
Identify a static website of your preference and use python to perform the following:

    Import boto and any required libraries
    Download the static website directly from its url and extract it (if archived)
    Create an S3 bucket and upload the files into the S3 bucket
    Configure the bucket settings to ensure that:
        its enabled for static website hosting,
        its accessible via the internet, and
        it has a bucket policy to allow access to objects in the S3 bucket.
    Display/print the url to your website i.e. the website endpoint
