import json
import boto3
import os
import yara

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE')
if not table_name:
    raise RuntimeError("Missing DYNAMODB_TABLE environment variable")
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        key = event.get('key')
        bucket = event.get('bucket')
        if not key or not bucket:
            raise ValueError("Missing 'bucket' or 'key' in event")

        case_id = key.split('/')[0]
        filename = key.split('/')[-1]
        analysis_file_path = f'/tmp/{filename}'
        yara_rules_path = '/opt/rules.yar'

        # Download file from S3
        s3 = boto3.client('s3')
        s3.download_file(bucket, key, analysis_file_path)

        # Load YARA rules
        rules = yara.compile(filepath=yara_rules_path)
        matches = rules.match(analysis_file_path)

        table.update_item(
            Key={'case_id': case_id, 'filename': filename},
            UpdateExpression="SET #s = :s, yara_result = :y",
            ExpressionAttributeNames={'#s': 'status'},
            ExpressionAttributeValues={':s': 'Analyzed', ':y': [m.rule for m in matches]}
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Analysis complete', 'yara_results': [m.rule for m in matches]})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }