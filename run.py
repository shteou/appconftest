#!/usr/bin/env python

import os

def find(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return os.path.join(root, name)
	return None

def run_policy(policy_path, target_file):
	print(f"Attempting to run policies from {policy_path} against {target_file}")

	target_file_path = find(target_file, '.')
	if target_file_path == None:
		print(f"Warning: Unable to find target file {target_file}")
		exit(1)

	print(f"Located candidate target file: {target_file_path}")	

	os.system(f"conftest test --policy policy/{policy_path} {target_file_path}")

def run_chart_policy():
	# Detect the correct chart folder by looking for a deployment.yaml file
	deployment_path = find('deployment.yaml', '.')
	if deployment_path == None:
		print("Warning: Failed to detect deployment.yaml file, aborting")
		exit(1)

	chart_path = deployment_path.replace('/templates/deployment.yaml', '')
	print(f"Located candidate chart path: {chart_path}")

	orig_dir = os.getcwd()
	os.chdir(deployment_path.replace('/templates/deployment.yaml', ''))
	os.system(f"helm template . | conftest test --policy {orig_dir}/policy/charts -")
	os.chdir(orig_dir)

run_policy('dockerfile', 'Dockerfile')
run_chart_policy()
