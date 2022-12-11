# Copyright (c) 2022, Accurate Systems and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import boto3
from botocore.exceptions import ClientError
from frappe.utils.password import get_decrypted_password
from frappe.model.document import Document

def listToString(s):
	str1 = ""
	for ele in s:
		str1 += ele		
	return str1

class EC2(Document):

	@frappe.whitelist()
	def activate(self, doc):
		settings = frappe.get_doc("AWS Settings")
		access_key_id = settings.access_key_id
		access_key_secret = settings.access_key_secret
		region = settings.region
		secret = listToString(access_key_secret)

		ec2_client = boto3.client(
			'ec2',
			aws_access_key_id = access_key_id,
			aws_secret_access_key = secret,
			region_name = region
		)

		ec2_client.start_instances(InstanceIds=[self.instance_id], DryRun=False)

	@frappe.whitelist()
	def deactivate(self, doc):
		settings = frappe.get_doc("AWS Settings")
		access_key_id = settings.access_key_id
		access_key_secret = settings.access_key_secret,
		region = settings.region
		secret = listToString(access_key_secret)

		ec2_client = boto3.client(
			'ec2',
			aws_access_key_id = access_key_id,
			aws_secret_access_key = secret,
			region_name = region
		)

		ec2_client.stop_instances(InstanceIds=[self.instance_id], DryRun=False)

