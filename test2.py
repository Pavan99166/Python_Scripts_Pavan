awsdata={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudtrail:GetTrail",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:GetServiceLastAccessedDetails",
                "iam:GenerateServiceLastAccessedDetails"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ]
        }
    ]
}

print(awsdata["Version"])
print(awsdata["Statement"])
print(awsdata["Statement"][0])
print(awsdata["Statement"][1]["Action"])
print(awsdata["Statement"][1]["Action"][1])
print(awsdata["Statement"][2]["Resource"][1])
print(awsdata["Statement"][2]["Action","Resource"])
