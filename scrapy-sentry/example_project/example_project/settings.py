# Scrapy settings for example_project project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'example_project'

SPIDER_MODULES = ['example_project.spiders']
NEWSPIDER_MODULE = 'example_project.spiders'

# import os
# if os.environ.get("SENTRY_DSN", None) is None:
#     import sys
#     print >> sys.stderr, "Please define SENTRY_DSN in your environment to run this example_project"
#     exit(1)

# log into sentry
SENTRY_DSN = "http://5eb77277202f41b19582b49b398d0479:9e812799df964c7f92d57b5478f9c2b9@0.0.0.0:9000/3"  # << set your sentry_dsn here >>

EXTENSIONS = {
    'scrapy_sentry.extensions.Errors':10,
}

