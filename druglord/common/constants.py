import os

# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

ITEM_TYPES = set(["media_docs",
                  "courses",
                  "datasets",
                  "hardware",
                  "software",
                  "events",
                  "research_projects",
                  "orgs",
                  "patents"])
