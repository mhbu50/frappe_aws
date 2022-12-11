# Copyright (c) 2022, Accurate Systems and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import boto3
from botocore.exceptions import ClientError
from frappe.model.document import Document

class AWSSettings(Document):

	def validate(self):
		ec2_client = boto3.client(
			'ec2',
			aws_access_key_id = self.access_key_id,
			aws_secret_access_key = self.access_key_secret,
			region_name=self.region
		)

		try:
			response = ec2_client.describe_instances()
			for i in response['Reservations']:
				for j in i['Instances']:
					# frappe.msgprint(frappe.as_json(j))
					frappe.msgprint('state of the instance "' + j['InstanceId'] + '" is: "' + j['State']['Name'] + '"')

		except ClientError:
			frappe.throw(_("Invalid Access Key ID or Secret Access Key."))
	
	@frappe.whitelist()
	def sync_ec2(self, doc):
		ec2_client = boto3.client(
			'ec2',
			aws_access_key_id = self.access_key_id,
			aws_secret_access_key = self.access_key_secret,
			region_name=self.region
		)
		status =""

		response = ec2_client.describe_instances()
		for i in response['Reservations']:
			for j in i['Instances']:
				if(j['State']['Name'] == 'running'):
						status = 'Active'
				else:
					status = 'Inactive'
				
				if not frappe.db.exists("EC2", j['InstanceId']):					
					doc = frappe.get_doc({
						"doctype": "EC2",
						"instance_id": j['InstanceId'],
						"instant_name": j["Tags"][0]['Value'],
						"status":status
					})
					doc.insert(ignore_permissions=True)
				else:
					doc = frappe.get_doc("EC2", j['InstanceId'])
					doc.status = status
					doc.save()


