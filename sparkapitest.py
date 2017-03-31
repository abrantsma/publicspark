import ciscosparkapi
from ciscosparkapi import CiscoSparkAPI
import json
import sys
import requests

SPARK_ACCESS_TOKEN="ZTlkYzU2MGQtNWZlOC00MTA5LWE5MzYtMjdiYjMyNzA5NTYzNjBlYjU3NWMtYjg4"
spark = CiscoSparkAPI(access_token=SPARK_ACCESS_TOKEN)
# roominfo = list(spark.memberships.list(roomId="Y2lzY29zcGFyazovL3VzL1JPT00vZGVmZWQ5ZDAtMTA4OC0xMWU3LWJhYWEtMTc0M2QzNWZjZTFh"))
# print(roominfo[0].personEmail)
roominfo = spark.memberships.list(roomId="Y2lzY29zcGFyazovL3VzL1JPT00vZGVmZWQ5ZDAtMTA4OC0xMWU3LWJhYWEtMTc0M2QzNWZjZTFh")
userEmail = []
for Membership in roominfo:
	userEmail.append(Membership.personEmail)
print(str(userEmail))
newRooms = spark.rooms.create("BrainSpark")
print(newRooms.id)