import boto3
import datetime

rds = boto3.client('rds', region_name='us-east-1')
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
snapshot_id = f"snapshot-do-rds-monitoramento-{timestamp}"
# se atentar ao nome do snapshot: nomes com espaçamento ou símbolos diferentes de hífen me geraram problema:
#   File "/root/aws-monitoramento/venv/lib/python3.12/site-packages/botocore/client.py", line 1074, in _make_api_call
    # raise error_class(parsed_response, operation_name)
    # botocore.exceptions.ClientError: An error occurred (InvalidParameterValue) when calling the CreateDBSnapshot operation: Invalid snapshot identifier:
#Também, se atentar às permissões do usuário: 
# botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the CreateDBSnapshot operation: User: arn:aws:iam::XXXXXXXXXX:user/monitoramento is not authorized to perform: rds:CreateDBSnapshot on...

response = rds.create_db_snapshot(
        DBInstanceIdentifier='monitoramento-db',
        DBSnapshotIdentifier=snapshot_id
)

print(f"Snapshot criado: {snapshot_id}")
