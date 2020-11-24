# team6-infra
#Test
**Team Info**

```
Akshay Murgod
email: murgod.a@husky.neu.edu
NUID: 001635872

Akash Balani
Balani.a@husky.neu.edu
001476895

Pankaj Sahani 
sahani.p@husky.neu.edu
001821986

Sunil Yadav
yadav.su@husky.neu.edu
001492711

```

**Pre-requisites**

1. Create DEV and PROD org accounts. Setup Route 53.

2. Host respective zones on DEV and PRO org accounts.
```
       DEV: dev.csye6225-spring2019-murgoda.me
       PROD: prod.csye6225-spring2019-murgoda.me
       
       NOTE : Main account should include NS record for these to subdomains.
```

3. Install Following
```
    kops
    kubectl
```
**Configuration params**

Export AWS credentials
```
export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXXXXXXX
export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXX
```

Export KOPS env variables:
```
export NAME=myfirstcluster.example.com
export KOPS_STATE_STORE=s3://prefix-example-com-state-store
```

**Create S3 bucket**
```
aws s3api create-bucket --bucket <bucket-name>  --region us-east-1
aws s3api put-bucket-versioning --bucket <bucket-name>  --versioning-configuration Status=Enabled
```

**Steps to create cluster via Ansible Plays**

Create cluster:
```
ansible-playbook -vvvv setup-k8s-cluster.yaml --extra-vars "cluster_name=dev.csye6225-spring2019-murgoda.me"

```
Delete Cluster:
```
ansible-playbook -vvvv delete-k8s-cluster.yaml --extra-vars "cluster_name=dev.csye6225-spring2019-murgoda.me"

```

**Kops create, Delete, validate**

Cluster Delete with KOPS:
```
kops delete cluster --name <cluster-name> --state <s3-bucket-name> --yes

```

Cluster validate with KOPS:
```
kops validate cluster <cluster-name> --state <s3-bucket-name>
```


**Steps to SSH into Bastion Host**

```
 ssh -i <Private-Key-Location> admin@<bastion_elb_A_Record>

 ssh -i ~/Documents/csye7374/id_rsa admin@bastion-dev-csye6225-fall-6elu42-510934669.us-east-1.elb.amazonaws.com

```

**Steps to create helm**

```
 ansible-playbook -vvvv setup-k8s-cluster.yaml --extra-vars --tags "create-cluster,create-helm"


```
